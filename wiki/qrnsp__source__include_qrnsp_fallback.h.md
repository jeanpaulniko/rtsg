---
title: "include/qrnsp_fallback.h"
nav_title: "qrnsp_fallback.h"
---

# `include/qrnsp_fallback.h`

```c
/*
 * QR-NSP Volcanic Edition — TCP/HTTP2 Fallback
 * Module 6: Graceful degradation when UDP/QUIC is blocked
 *
 * When authoritarian regimes block UDP entirely or throttle QUIC
 * (deep-packet inspection on port 443/UDP), the system falls back
 * to TCP-based HTTP/2. Steganographic channels shift to:
 *
 *   1. TCP Options fields (timestamps, SACK blocks)
 *   2. HTTP/2 WINDOW_UPDATE / PRIORITY frame manipulation
 *   3. Chaffing-and-Winnowing (Rivest 1998): interleave authentic
 *      and chaff packets; only the holder of the MAC key can winnow
 *
 * State machine:
 *   QUIC_OK → detect_throttle → QUIC_DEGRADED → probe_tcp → TCP_PROBE
 *   TCP_PROBE → handshake_ok → HTTP2_ACTIVE
 *   HTTP2_ACTIVE → quic_recovered → QUIC_OK (always prefer QUIC)
 *
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#ifndef QRNSP_FALLBACK_H
#define QRNSP_FALLBACK_H

#include <stdint.h>
#include <stddef.h>

/* ─────────────────────────────────────────────
 * Transport states
 * ───────────────────────────────────────────── */

typedef enum {
    TRANSPORT_QUIC_OK,          /* Primary: QUIC/UDP operational       */
    TRANSPORT_QUIC_DEGRADED,    /* QUIC loss > threshold               */
    TRANSPORT_TCP_PROBE,        /* Testing TCP/HTTP2 path              */
    TRANSPORT_HTTP2_ACTIVE,     /* Fallback: HTTP2/TCP operational     */
    TRANSPORT_HTTP2_DEGRADED,   /* TCP also impaired                   */
    TRANSPORT_BLOCKED,          /* Both paths blocked                  */
} transport_state_t;

/* ─────────────────────────────────────────────
 * TCP steganographic channel types
 * ───────────────────────────────────────────── */

typedef enum {
    TCP_STEGO_TIMESTAMP,        /* Encode in TCP timestamp LSBs        */
    TCP_STEGO_WINDOW,           /* Encode in window size LSBs          */
    TCP_STEGO_HTTP2_PAD,        /* HTTP/2 DATA frame padding           */
    TCP_STEGO_HTTP2_PRIO,       /* HTTP/2 PRIORITY weight manipulation */
    TCP_STEGO_CHAFF,            /* Chaffing-and-Winnowing              */
} tcp_stego_mode_t;

/* ─────────────────────────────────────────────
 * Quality metrics for transport monitoring
 * ───────────────────────────────────────────── */

typedef struct {
    /* QUIC health */
    double   quic_loss_rate;     /* Packet loss ratio [0,1]            */
    double   quic_rtt_ms;        /* Smoothed RTT in milliseconds       */
    uint64_t quic_pkts_sent;
    uint64_t quic_pkts_acked;
    uint64_t quic_pkts_lost;
    uint64_t quic_last_rx_ns;    /* Last QUIC packet received          */

    /* TCP health */
    double   tcp_loss_rate;
    double   tcp_rtt_ms;
    uint64_t tcp_pkts_sent;
    uint64_t tcp_pkts_acked;
    uint64_t tcp_last_rx_ns;

    /* Thresholds */
    double   quic_loss_threshold; /* Trigger fallback at this loss rate */
    double   quic_rtt_threshold;  /* RTT suggesting throttling (ms)    */
    uint64_t quic_silence_ns;     /* Timeout: no QUIC rx → fallback    */
} transport_metrics_t;

/* ─────────────────────────────────────────────
 * Chaffing-and-Winnowing packet
 *
 * Rivest (1998): Authentication without encryption.
 * Interleave real packets (valid MAC) with chaff packets
 * (invalid MAC). Only the MAC key holder can tell them apart.
 *
 * Layout:
 *   [SEQ:4][DATA:N][MAC:16]
 *   Real:  MAC = HMAC(key, seq || data) — valid
 *   Chaff: MAC = random 16 bytes — invalid
 * ───────────────────────────────────────────── */

#define CHAFF_SEQ_BYTES    4
#define CHAFF_MAC_BYTES    16
#define CHAFF_OVERHEAD     (CHAFF_SEQ_BYTES + CHAFF_MAC_BYTES)
#define CHAFF_MAX_DATA     1024
#define CHAFF_RATIO_DEFAULT 3  /* 3 chaff packets per real packet     */

typedef struct {
    uint32_t seq;
    uint8_t  data[CHAFF_MAX_DATA];
    uint16_t data_len;
    uint8_t  mac[CHAFF_MAC_BYTES];
    int      is_real;            /* For TX bookkeeping only            */
} chaff_packet_t;

/* ─────────────────────────────────────────────
 * Fallback session
 * ───────────────────────────────────────────── */

typedef struct {
    transport_state_t state;
    tcp_stego_mode_t  tcp_mode;

    /* Shared secret (from hybrid KEM) */
    uint8_t  session_key[32];

    /* Chaffing state */
    uint32_t chaff_tx_seq;
    uint32_t chaff_rx_seq;
    int      chaff_ratio;        /* Chaff packets per real packet      */

    /* TCP timestamp steganography */
    uint32_t ts_bit_index;       /* Current bit position in payload    */
    uint8_t  ts_payload[256];    /* Data being embedded in timestamps  */
    uint16_t ts_payload_len;
    uint16_t ts_payload_cap;

    /* HTTP/2 frame steganography */
    uint32_t h2_stream_id;       /* Current HTTP/2 stream              */
    uint8_t  h2_payload[4096];   /* Data for HTTP/2 padding injection  */
    uint16_t h2_payload_len;

    /* Metrics */
    transport_metrics_t metrics;

    /* Stats */
    uint64_t fallback_count;     /* Times we've fallen back            */
    uint64_t recovery_count;     /* Times QUIC recovered               */
    uint64_t chaff_sent;
    uint64_t chaff_real_sent;
    uint64_t winnowed;           /* Successfully winnowed packets      */
} fallback_session_t;

/* ─────────────────────────────────────────────
 * API
 * ───────────────────────────────────────────── */

int  fallback_init(fallback_session_t *sess, const uint8_t key[32]);
void fallback_destroy(fallback_session_t *sess);

/* Transport monitoring — call on every packet event */
void fallback_quic_tx(fallback_session_t *sess);
void fallback_quic_rx(fallback_session_t *sess, uint64_t timestamp_ns);
void fallback_quic_loss(fallback_session_t *sess);
void fallback_tcp_tx(fallback_session_t *sess);
void fallback_tcp_rx(fallback_session_t *sess, uint64_t timestamp_ns);

/* State machine tick — call periodically (e.g., every 100ms) */
transport_state_t fallback_tick(fallback_session_t *sess, uint64_t now_ns);

/* Chaffing-and-Winnowing */
int  chaff_encode(fallback_session_t *sess,
                  const uint8_t *payload, size_t len,
                  chaff_packet_t *out_packets, int *out_count, int max_packets);
int  chaff_winnow(fallback_session_t *sess,
                  const chaff_packet_t *packets, int count,
                  uint8_t *out, size_t out_cap, size_t *out_len);

/* TCP timestamp steganography */
uint32_t tcp_ts_encode_bits(fallback_session_t *sess,
                            uint32_t original_ts, int nbits);
int      tcp_ts_decode_bits(fallback_session_t *sess,
                            uint32_t received_ts, int nbits);

/* HTTP/2 DATA frame padding injection */
int  h2_pad_inject(fallback_session_t *sess,
                   uint8_t *frame, size_t frame_len, size_t frame_cap,
                   const uint8_t *payload, size_t pay_len);
int  h2_pad_extract(fallback_session_t *sess,
                    const uint8_t *frame, size_t frame_len,
                    uint8_t *out, size_t out_cap, size_t *out_len);

#endif /* QRNSP_FALLBACK_H */

```
