---
title: "include/qrnsp_orchestrator.h"
nav_title: "qrnsp_orchestrator.h"
---

# `include/qrnsp_orchestrator.h`

```c
/*
 * QR-NSP Volcanic Edition — Unified Orchestrator
 * Module 8: Pipeline controller tying all modules together
 *
 * Data flow (TX):
 *   Application data
 *     → Deniable encryption (Module 5)
 *     → Stego payload chunking
 *     → IF QUIC available:
 *         → QUIC PADDING injection (Module 3)
 *         → Temporal jitter shaping (Module 4)
 *       ELSE IF TCP available:
 *         → TCP fallback (Module 6: chaff/timestamp/H2 padding)
 *     → Traffic morphing (Module 7)
 *     → XDP packet send (Module 1)
 *
 * Data flow (RX):
 *   XDP packet receive (Module 1)
 *     → Traffic demorph
 *     → IF QUIC: extract from PADDING (Module 3)
 *       ELSE: winnow/extract from TCP (Module 6)
 *     → Reassemble payload chunks
 *     → Deniable decryption (Module 5)
 *     → Application data
 *
 * Orchestrator manages:
 *   - Hybrid KEM session establishment
 *   - Automatic transport selection and fallback
 *   - Flow control and chunking
 *   - Cover traffic generation
 *   - Session lifecycle
 *
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#ifndef QRNSP_ORCHESTRATOR_H
#define QRNSP_ORCHESTRATOR_H

#include <stdint.h>
#include <stddef.h>
#include "qrnsp_stego.h"
#include "qrnsp_jitter.h"
#include "qrnsp_fallback.h"
#include "qrnsp_morph.h"
#include "qrnsp_deniable.h"
#include "qrnsp_crypto.h"

/* ─────────────────────────────────────────────
 * Pipeline states
 * ───────────────────────────────────────────── */

typedef enum {
    ORCH_STATE_INIT,            /* Pre-handshake                       */
    ORCH_STATE_HANDSHAKE,       /* KEM exchange in progress            */
    ORCH_STATE_ACTIVE,          /* Fully operational                   */
    ORCH_STATE_FALLBACK,        /* Running on TCP fallback             */
    ORCH_STATE_JITTER_ONLY,     /* Only timing channel available       */
    ORCH_STATE_BLOCKED,         /* All channels blocked                */
    ORCH_STATE_CLOSED,          /* Session terminated                  */
} orch_state_t;

/* ─────────────────────────────────────────────
 * Channel capabilities (bitfield)
 * ───────────────────────────────────────────── */

#define ORCH_CAP_QUIC_PADDING  0x01  /* Module 3: PADDING injection    */
#define ORCH_CAP_JITTER        0x02  /* Module 4: Timing channel       */
#define ORCH_CAP_TCP_CHAFF     0x04  /* Module 6: Chaffing             */
#define ORCH_CAP_TCP_TIMESTAMP 0x08  /* Module 6: TCP timestamp LSBs   */
#define ORCH_CAP_H2_PADDING    0x10  /* Module 6: HTTP/2 padding       */

/* ─────────────────────────────────────────────
 * Chunking: split large messages across packets
 * ───────────────────────────────────────────── */

#define ORCH_CHUNK_HEADER  8    /* [MSG_ID:4][CHUNK:2][TOTAL:2]        */
#define ORCH_MAX_MSG_SIZE  (1 << 20)  /* 1 MiB max message             */

typedef struct {
    uint32_t msg_id;
    uint16_t chunk_index;
    uint16_t total_chunks;
    uint8_t  data[1400];        /* Chunk payload                       */
    uint16_t data_len;
} orch_chunk_t;

/* Reassembly buffer (RX side) */
typedef struct {
    uint32_t msg_id;
    uint16_t total_chunks;
    uint16_t received_mask[64]; /* Bit mask: chunks received (max 1024)*/
    uint8_t *buffer;            /* Reassembly buffer (allocated)       */
    size_t   buffer_size;
    uint16_t chunks_received;
    uint64_t first_chunk_ns;    /* Timestamp of first chunk            */
} orch_reassembly_t;

/* ─────────────────────────────────────────────
 * Orchestrator session
 * ───────────────────────────────────────────── */

typedef struct {
    orch_state_t state;
    uint32_t     capabilities;   /* Active channels bitfield           */

    /* Identity */
    int role;                    /* 0 = initiator, 1 = responder       */

    /* Cryptographic state */
    uint8_t pk[QRNSP_CRYPTO_PUBLICKEYBYTES];
    uint8_t sk[QRNSP_CRYPTO_SECRETKEYBYTES];
    uint8_t peer_pk[QRNSP_CRYPTO_PUBLICKEYBYTES];
    uint8_t shared_secret[32];
    int     kem_complete;

    /* Sub-module sessions */
    stego_session_t    stego;    /* Module 3: QUIC PADDING             */
    jitter_tx_t        jitter_tx;/* Module 4: Timing TX                */
    jitter_rx_t        jitter_rx;/* Module 4: Timing RX                */
    fallback_session_t fallback; /* Module 6: TCP fallback             */
    morph_session_t    morph;    /* Module 7: Traffic morphing          */

    /* Message chunking (TX) */
    uint32_t next_msg_id;

    /* Reassembly (RX) */
    orch_reassembly_t reassembly[4]; /* Up to 4 concurrent messages    */
    int               reassembly_count;

    /* Cover traffic timer */
    uint64_t last_cover_ns;
    uint64_t cover_interval_ns;

    /* Stats */
    uint64_t msgs_sent;
    uint64_t msgs_received;
    uint64_t bytes_sent;
    uint64_t bytes_received;
    uint64_t chunks_sent;
    uint64_t chunks_received;
    uint64_t cover_packets_sent;
} orch_session_t;

/* ─────────────────────────────────────────────
 * API
 * ───────────────────────────────────────────── */

/*
 * Initialize orchestrator. Generates keypair.
 * role: 0 = initiator, 1 = responder
 * cover: traffic morphing profile
 */
int orch_init(orch_session_t *sess, int role, morph_cover_t cover);

/*
 * Get our public key (send to peer via out-of-band or trigger SNI).
 */
int orch_get_pubkey(const orch_session_t *sess,
                    uint8_t pk[QRNSP_CRYPTO_PUBLICKEYBYTES]);

/*
 * Set peer's public key and complete KEM handshake.
 * Initiator: encapsulates → generates ciphertext
 * Responder: provide ciphertext from initiator
 */
int orch_handshake(orch_session_t *sess,
                   const uint8_t peer_pk[QRNSP_CRYPTO_PUBLICKEYBYTES],
                   uint8_t ct[QRNSP_CRYPTO_CIPHERTEXTBYTES],
                   int is_ciphertext);

/*
 * Send a message through the covert channel.
 * Handles chunking, encryption, channel selection, and morphing.
 *
 * packets:   output buffer for ready-to-send packets
 * pkt_sizes: output array of packet sizes
 * pkt_delays: output array of delays (ns) before each packet
 * max_pkts:  capacity of output arrays
 * n_pkts:    actual number of packets produced
 */
int orch_send(orch_session_t *sess,
              const uint8_t *msg, size_t msg_len,
              uint8_t packets[][2048], size_t *pkt_sizes,
              uint64_t *pkt_delays, int max_pkts, int *n_pkts);

/*
 * Process a received packet. May or may not contain covert data.
 *
 * Returns:
 *   0 — packet processed, no complete message yet
 *   1 — complete message reassembled (read with orch_recv_msg)
 *  -1 — not a QR-NSP packet (normal traffic, ignore)
 */
int orch_receive(orch_session_t *sess,
                 const uint8_t *pkt, size_t pkt_len,
                 uint64_t timestamp_ns);

/*
 * Retrieve a fully reassembled message.
 */
int orch_recv_msg(orch_session_t *sess,
                  uint8_t *out, size_t out_cap, size_t *out_len);

/*
 * Periodic tick: manage cover traffic, transport fallback, cleanup.
 * Call every ~100ms.
 */
int orch_tick(orch_session_t *sess, uint64_t now_ns);

/*
 * Destroy session and zeroize all state.
 */
void orch_destroy(orch_session_t *sess);

/*
 * Get session statistics.
 */
typedef struct {
    orch_state_t state;
    uint32_t     capabilities;
    uint64_t     msgs_sent;
    uint64_t     msgs_received;
    uint64_t     bytes_sent;
    uint64_t     bytes_received;
    uint64_t     cover_packets;
    double       morph_quality;
    uint64_t     fallback_count;
    uint64_t     recovery_count;
} orch_stats_t;

void orch_get_stats(const orch_session_t *sess, orch_stats_t *stats);

#endif /* QRNSP_ORCHESTRATOR_H */

```
