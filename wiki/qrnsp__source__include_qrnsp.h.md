---
title: "include/qrnsp.h"
nav_title: "qrnsp.h"
---

# `include/qrnsp.h`

```c
/*
 * QR-NSP Volcanic Edition — Core Header
 * SPDX-License-Identifier: AGPL-3.0-or-later
 * Project: Quantum-Resistant Network Steganography Protocol
 * Mission: Censorship-resistant communication for people under authoritarian regimes
 * Module:  Shared definitions (XDP ↔ Userspace)
 *
 * Author: Jean-Paul Niko / BuildNet
 * License: TBD (recommend AGPLv3 for censorship-resistance tooling)
 */

#ifndef QRNSP_H
#define QRNSP_H

#include <stdint.h>
#include <stdbool.h>

/* ─────────────────────────────────────────────
 * Build-time configuration
 * ───────────────────────────────────────────── */

#define QRNSP_VERSION_MAJOR  0
#define QRNSP_VERSION_MINOR  1
#define QRNSP_VERSION_PATCH  0

/* Ring buffer: 2^RING_ORDER slots. 14 = 16384 slots × 2048 bytes ≈ 32 MiB */
#define QRNSP_RING_ORDER     14
#define QRNSP_RING_SIZE      (1U << QRNSP_RING_ORDER)
#define QRNSP_RING_MASK      (QRNSP_RING_SIZE - 1)

/* Maximum packet payload stored per slot (jumbo-safe) */
#define QRNSP_SLOT_SIZE      2048

/* QUIC detection */
#define QUIC_LONG_HEADER_BIT 0x80   /* Bit 7 set = long header (handshake)   */
#define QUIC_FIXED_BIT       0x40   /* Bit 6 set = QUIC (always 1 per RFC 9000) */
#define QUIC_VERSION_1       0x00000001
#define QUIC_VERSION_2       0x6B3343CF  /* RFC 9369 */

/* UDP port hints — QUIC typically on 443 but regimes may remap */
#define QUIC_PORT_PRIMARY    443
#define QUIC_PORT_ALT_LO     8443
#define QUIC_PORT_ALT_HI     8444

/* ─────────────────────────────────────────────
 * Shared ring-buffer slot (XDP → userspace)
 *
 * Layout chosen for DDR5 cache-line alignment:
 *   metadata (64 bytes) + payload (2048 bytes) = 2112 bytes
 *   Padded to 2176 (34 × 64-byte cache lines)
 * ───────────────────────────────────────────── */

#define QRNSP_SLOT_ALIGNED   2176   /* 34 cache lines */

struct __attribute__((aligned(64))) qrnsp_slot {
    /* ── Metadata (cache line 0) ── */
    uint64_t  timestamp_ns;     /* XDP rx timestamp (bpf_ktime_get_ns)     */
    uint32_t  pkt_len;          /* Original packet length on wire          */
    uint32_t  payload_len;      /* Bytes copied into payload[]             */
    uint32_t  src_ip;           /* Network byte order                      */
    uint32_t  dst_ip;           /* Network byte order                      */
    uint16_t  src_port;         /* Host byte order                         */
    uint16_t  dst_port;         /* Host byte order                         */
    uint8_t   quic_flags;       /* First byte of QUIC header               */
    uint8_t   direction;        /* 0 = ingress, 1 = egress (future)        */
    uint8_t   flags;            /* QRNSP_SLOT_F_* below                    */
    uint8_t   _pad0;
    uint32_t  quic_version;     /* Extracted version (long header only)     */
    uint32_t  ifindex;          /* Interface index                         */
    uint8_t   _reserved[16];    /* Future: DCID hash, flow label           */

    /* ── Payload (cache lines 1–32) ── */
    uint8_t   payload[QRNSP_SLOT_SIZE];

    /* ── Padding to 2176 ── */
    uint8_t   _pad1[QRNSP_SLOT_ALIGNED - 64 - QRNSP_SLOT_SIZE];
};

/* Slot flags */
#define QRNSP_SLOT_F_VALID     0x01  /* Slot contains a valid packet        */
#define QRNSP_SLOT_F_LONG_HDR  0x02  /* QUIC long header detected           */
#define QRNSP_SLOT_F_PADDING   0x04  /* Contains PADDING frames (injectable)*/
#define QRNSP_SLOT_F_INJECTED  0x08  /* Userspace has injected payload      */
#define QRNSP_SLOT_F_TX_READY  0x10  /* Ready for retransmission            */

/* ─────────────────────────────────────────────
 * Shared ring-buffer control block
 *
 * Placed at the start of the mmap'd region.
 * Producer (XDP) writes head; consumer (daemon) writes tail.
 * Both use __atomic builtins for lock-free SPSC.
 * ───────────────────────────────────────────── */

struct __attribute__((aligned(64))) qrnsp_ring_ctl {
    volatile uint64_t  head;          /* Next write position (XDP)           */
    uint8_t            _pad_h[56];    /* Avoid false sharing                 */
    volatile uint64_t  tail;          /* Next read position (daemon)         */
    uint8_t            _pad_t[56];    /* Avoid false sharing                 */
    uint64_t           dropped;       /* Packets dropped (ring full)         */
    uint64_t           total_rx;      /* Total QUIC packets seen             */
    uint64_t           total_injected;/* Payloads injected by daemon         */
    uint32_t           ring_size;     /* Copy of QRNSP_RING_SIZE             */
    uint32_t           slot_size;     /* Copy of QRNSP_SLOT_ALIGNED          */
    uint64_t           start_ns;      /* Daemon start timestamp              */
};

/* Total shared memory size */
#define QRNSP_SHM_SIZE  (sizeof(struct qrnsp_ring_ctl) + \
                         (QRNSP_RING_SIZE * QRNSP_SLOT_ALIGNED))

/* ─────────────────────────────────────────────
 * BPF map keys (shared between XDP and loader)
 * ───────────────────────────────────────────── */

/* BPF_MAP_TYPE_ARRAY for config */
#define QRNSP_CFG_KEY_ENABLED     0   /* uint32: 1=active, 0=passthrough    */
#define QRNSP_CFG_KEY_TARGET_IP   1   /* uint32: target server IP (net order)*/
#define QRNSP_CFG_KEY_TARGET_PORT 2   /* uint32: target port (host order)    */
#define QRNSP_CFG_KEY_MODE        3   /* uint32: 0=monitor, 1=intercept     */

/* ─────────────────────────────────────────────
 * Inline helpers
 * ───────────────────────────────────────────── */

static inline uint64_t
qrnsp_ring_available(const struct qrnsp_ring_ctl *ctl)
{
    uint64_t h = __atomic_load_n(&ctl->head, __ATOMIC_ACQUIRE);
    uint64_t t = __atomic_load_n(&ctl->tail, __ATOMIC_ACQUIRE);
    return h - t;
}

static inline bool
qrnsp_ring_full(const struct qrnsp_ring_ctl *ctl)
{
    return qrnsp_ring_available(ctl) >= QRNSP_RING_SIZE;
}

static inline struct qrnsp_slot *
qrnsp_slot_at(void *ring_base, uint64_t index)
{
    uint8_t *base = (uint8_t *)ring_base + sizeof(struct qrnsp_ring_ctl);
    return (struct qrnsp_slot *)(base + (index & QRNSP_RING_MASK) * QRNSP_SLOT_ALIGNED);
}

#endif /* QRNSP_H */

```
