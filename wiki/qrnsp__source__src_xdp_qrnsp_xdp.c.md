---
title: "src/xdp/qrnsp_xdp.c"
nav_title: "qrnsp_xdp.c"
---

# `src/xdp/qrnsp_xdp.c`

```c
/*
 * QR-NSP Volcanic Edition — XDP Packet Interceptor
 * SPDX-License-Identifier: AGPL-3.0-or-later
 * Kernel-side eBPF program: identifies QUIC traffic, copies to shared ring buffer.
 *
 * Attach to NIC via: ip link set dev <iface> xdp obj qrnsp_xdp.o sec xdp
 *
 * Design constraints:
 *   - eBPF verifier safe (bounded loops, no unbounded memory access)
 *   - All packet access through bounds-checked helpers
 *   - SPSC ring buffer: XDP is sole producer, daemon is sole consumer
 *   - Zero-copy where possible (direct packet data → ring slot)
 */

#include <linux/bpf.h>
#include <linux/if_ether.h>
#include <linux/ip.h>
#include <linux/ipv6.h>
#include <linux/udp.h>
#include <linux/in.h>
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_endian.h>

/* ─────────────────────────────────────────────
 * Constants (mirror qrnsp.h — can't include userspace headers in BPF)
 * ───────────────────────────────────────────── */

#define RING_ORDER       14
#define RING_SIZE        (1U << RING_ORDER)
#define RING_MASK        (RING_SIZE - 1)
#define SLOT_PAYLOAD_MAX 2048
#define SLOT_ALIGNED     2176

/* QUIC detection */
#define QUIC_FIXED_BIT   0x40
#define QUIC_LONG_BIT    0x80

/* Config keys */
#define CFG_ENABLED      0
#define CFG_TARGET_IP    1
#define CFG_TARGET_PORT  2
#define CFG_MODE         3

/* Slot flags */
#define SLOT_F_VALID     0x01
#define SLOT_F_LONG_HDR  0x02

/* ─────────────────────────────────────────────
 * BPF Maps
 * ───────────────────────────────────────────── */

/* Configuration array: indexed by CFG_* keys */
struct {
    __uint(type, BPF_MAP_TYPE_ARRAY);
    __uint(max_entries, 8);
    __type(key, __u32);
    __type(value, __u32);
} qrnsp_config SEC(".maps");

/*
 * Ring buffer control + data.
 * We use a BPF_MAP_TYPE_ARRAY with a single entry pointing to
 * a large per-cpu region. The userspace daemon mmaps this.
 *
 * Alternative approach: BPF_MAP_TYPE_RINGBUF (kernel 5.8+).
 * We use RINGBUF for better semantics — it handles the SPSC
 * head/tail atomics natively and supports variable-length records.
 */
struct {
    __uint(type, BPF_MAP_TYPE_RINGBUF);
    __uint(max_entries, RING_SIZE * SLOT_ALIGNED); /* ~32 MiB */
} qrnsp_ringbuf SEC(".maps");

/* Per-CPU packet counter (lock-free stats) */
struct {
    __uint(type, BPF_MAP_TYPE_PERCPU_ARRAY);
    __uint(max_entries, 4);
    __type(key, __u32);
    __type(value, __u64);
} qrnsp_stats SEC(".maps");

#define STAT_TOTAL_PKT   0
#define STAT_QUIC_PKT    1
#define STAT_QUEUED       2
#define STAT_DROPPED      3

/* ─────────────────────────────────────────────
 * Ring buffer event structure (sent via RINGBUF)
 * ───────────────────────────────────────────── */

struct qrnsp_event {
    __u64  timestamp_ns;
    __u32  pkt_len;
    __u32  payload_len;
    __u32  src_ip;
    __u32  dst_ip;
    __u16  src_port;
    __u16  dst_port;
    __u8   quic_flags;
    __u8   direction;
    __u8   flags;
    __u8   _pad0;
    __u32  quic_version;
    __u32  ifindex;
    __u8   payload[SLOT_PAYLOAD_MAX];
};

/* ─────────────────────────────────────────────
 * Helpers
 * ───────────────────────────────────────────── */

static __always_inline void
stat_inc(__u32 key)
{
    __u64 *val = bpf_map_lookup_elem(&qrnsp_stats, &key);
    if (val)
        __sync_fetch_and_add(val, 1);
}

/*
 * is_quic_packet: inspect first byte of UDP payload.
 * RFC 9000 §17.2: Fixed Bit (0x40) MUST be 1.
 * Long Header: bit 7 set. Short Header: bit 7 clear.
 *
 * Returns: 0 = not QUIC, 1 = short header, 2 = long header
 */
static __always_inline int
classify_quic(const __u8 *udp_payload, const void *data_end)
{
    if ((void *)(udp_payload + 1) > data_end)
        return 0;

    __u8 first = *udp_payload;

    /* Fixed bit must be set for QUIC */
    if (!(first & QUIC_FIXED_BIT))
        return 0;

    return (first & QUIC_LONG_BIT) ? 2 : 1;
}

/*
 * extract_quic_version: for long headers, version is bytes 1-4.
 * Returns 0 for short headers or if bounds check fails.
 */
static __always_inline __u32
extract_quic_version(const __u8 *udp_payload, const void *data_end)
{
    if ((void *)(udp_payload + 5) > data_end)
        return 0;

    return ((__u32)udp_payload[1] << 24) |
           ((__u32)udp_payload[2] << 16) |
           ((__u32)udp_payload[3] <<  8) |
           ((__u32)udp_payload[4]);
}

/* ─────────────────────────────────────────────
 * XDP Main Program
 * ───────────────────────────────────────────── */

SEC("xdp")
int qrnsp_xdp_intercept(struct xdp_md *ctx)
{
    void *data     = (void *)(long)ctx->data;
    void *data_end = (void *)(long)ctx->data_end;

    stat_inc(STAT_TOTAL_PKT);

    /* ── Check if interception is enabled ── */
    __u32 cfg_key = CFG_ENABLED;
    __u32 *enabled = bpf_map_lookup_elem(&qrnsp_config, &cfg_key);
    if (!enabled || *enabled == 0)
        return XDP_PASS;   /* Passthrough mode */

    /* ── Parse Ethernet ── */
    struct ethhdr *eth = data;
    if ((void *)(eth + 1) > data_end)
        return XDP_PASS;

    /* IPv4 only for now (IPv6 path: future module) */
    if (eth->h_proto != bpf_htons(ETH_P_IP))
        return XDP_PASS;

    /* ── Parse IPv4 ── */
    struct iphdr *ip = (void *)(eth + 1);
    if ((void *)(ip + 1) > data_end)
        return XDP_PASS;

    /* Bounds: variable IHL */
    if (ip->ihl < 5)
        return XDP_PASS;

    __u32 ip_hdr_len = ip->ihl * 4;
    void *transport = (void *)ip + ip_hdr_len;

    /* UDP only (QUIC runs over UDP) */
    if (ip->protocol != IPPROTO_UDP)
        return XDP_PASS;

    /* ── Parse UDP ── */
    struct udphdr *udp = transport;
    if ((void *)(udp + 1) > data_end)
        return XDP_PASS;

    __u16 dst_port = bpf_ntohs(udp->dest);
    __u16 src_port = bpf_ntohs(udp->source);

    /* ── Port filter (optional — config-driven) ── */
    cfg_key = CFG_TARGET_PORT;
    __u32 *target_port = bpf_map_lookup_elem(&qrnsp_config, &cfg_key);
    if (target_port && *target_port != 0) {
        if (dst_port != (__u16)*target_port && src_port != (__u16)*target_port)
            return XDP_PASS;
    }

    /* ── IP filter (optional) ── */
    cfg_key = CFG_TARGET_IP;
    __u32 *target_ip = bpf_map_lookup_elem(&qrnsp_config, &cfg_key);
    if (target_ip && *target_ip != 0) {
        if (ip->saddr != *target_ip && ip->daddr != *target_ip)
            return XDP_PASS;
    }

    /* ── QUIC classification ── */
    __u8 *udp_payload = (void *)(udp + 1);
    int quic_type = classify_quic(udp_payload, data_end);
    if (quic_type == 0)
        return XDP_PASS;   /* Not QUIC */

    stat_inc(STAT_QUIC_PKT);

    /* ── Calculate payload size ── */
    __u32 udp_payload_len = bpf_ntohs(udp->len);
    if (udp_payload_len < sizeof(struct udphdr))
        return XDP_PASS;
    udp_payload_len -= sizeof(struct udphdr);

    /* Clamp to slot size */
    __u32 copy_len = udp_payload_len;
    if (copy_len > SLOT_PAYLOAD_MAX)
        copy_len = SLOT_PAYLOAD_MAX;

    /* ── Reserve ring buffer space ── */
    struct qrnsp_event *evt;
    evt = bpf_ringbuf_reserve(&qrnsp_ringbuf, sizeof(*evt), 0);
    if (!evt) {
        stat_inc(STAT_DROPPED);
        return XDP_PASS;   /* Ring full — don't drop the packet */
    }

    /* ── Fill metadata ── */
    evt->timestamp_ns  = bpf_ktime_get_ns();
    evt->pkt_len       = (__u32)(data_end - data);
    evt->payload_len   = copy_len;
    evt->src_ip        = ip->saddr;
    evt->dst_ip        = ip->daddr;
    evt->src_port      = src_port;
    evt->dst_port      = dst_port;
    evt->quic_flags    = (udp_payload < (const __u8 *)data_end) ? *udp_payload : 0;
    evt->direction     = 0; /* ingress */
    evt->flags         = SLOT_F_VALID | ((quic_type == 2) ? SLOT_F_LONG_HDR : 0);
    evt->quic_version  = (quic_type == 2) ?
                         extract_quic_version(udp_payload, data_end) : 0;
    evt->ifindex       = ctx->ingress_ifindex;

    /* ── Copy UDP payload into ring slot ── */
    /*
     * BPF verifier requires bounded access. We use bpf_probe_read_kernel
     * equivalent — but for XDP, direct access with bounds check works.
     * The clamp above ensures copy_len ≤ SLOT_PAYLOAD_MAX.
     */
    if ((void *)(udp_payload + copy_len) <= data_end) {
        /* Direct bounded copy — verifier can prove this is safe */
        __builtin_memcpy(evt->payload, udp_payload,
                         copy_len & (SLOT_PAYLOAD_MAX - 1));
    } else {
        /* Shouldn't happen after bounds check, but satisfy verifier */
        evt->payload_len = 0;
    }

    /* ── Submit to ring ── */
    bpf_ringbuf_submit(evt, 0);
    stat_inc(STAT_QUEUED);

    /*
     * Action: XDP_PASS lets the packet continue through the kernel stack
     * normally. The daemon processes the copy asynchronously.
     *
     * For active injection (Module 3), we'll switch to XDP_TX or
     * XDP_REDIRECT after modifying the packet in-place.
     */
    return XDP_PASS;
}

char _license[] SEC("license") = "GPL";
__u32 _version SEC("version") = 1;

```
