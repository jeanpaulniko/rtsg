---
title: "src/fallback/fallback.c"
nav_title: "fallback.c"
---

# `src/fallback/fallback.c`

```c
/*
 * QR-NSP Volcanic Edition — TCP/HTTP2 Fallback Engine
 * Module 6: Transport state machine + TCP steganography
 *
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include "qrnsp_fallback.h"
#include "mlkem_params.h"  /* SHA3 */
#include <string.h>
#include <stdlib.h>

/* ═════════════════════════════════════════════
 * Init / Destroy
 * ═════════════════════════════════════════════ */

int
fallback_init(fallback_session_t *sess, const uint8_t key[32])
{
    memset(sess, 0, sizeof(*sess));
    memcpy(sess->session_key, key, 32);
    sess->state = TRANSPORT_QUIC_OK;
    sess->tcp_mode = TCP_STEGO_CHAFF;
    sess->chaff_ratio = CHAFF_RATIO_DEFAULT;

    /* Default thresholds */
    sess->metrics.quic_loss_threshold = 0.30;   /* 30% loss → fallback */
    sess->metrics.quic_rtt_threshold  = 5000.0;  /* 5s RTT → throttled */
    sess->metrics.quic_silence_ns     = 10ULL * 1000000000ULL; /* 10s silence */

    return 0;
}

void
fallback_destroy(fallback_session_t *sess)
{
    memset(sess, 0, sizeof(*sess));
}

/* ═════════════════════════════════════════════
 * Transport Monitoring
 * ═════════════════════════════════════════════ */

void fallback_quic_tx(fallback_session_t *sess)
{ sess->metrics.quic_pkts_sent++; }

void
fallback_quic_rx(fallback_session_t *sess, uint64_t timestamp_ns)
{
    sess->metrics.quic_pkts_acked++;
    sess->metrics.quic_last_rx_ns = timestamp_ns;
}

void
fallback_quic_loss(fallback_session_t *sess)
{
    sess->metrics.quic_pkts_lost++;
    if (sess->metrics.quic_pkts_sent > 0) {
        sess->metrics.quic_loss_rate =
            (double)sess->metrics.quic_pkts_lost /
            (double)sess->metrics.quic_pkts_sent;
    }
}

void fallback_tcp_tx(fallback_session_t *sess)
{ sess->metrics.tcp_pkts_sent++; }

void
fallback_tcp_rx(fallback_session_t *sess, uint64_t timestamp_ns)
{
    sess->metrics.tcp_pkts_acked++;
    sess->metrics.tcp_last_rx_ns = timestamp_ns;
}

/* ═════════════════════════════════════════════
 * State Machine
 *
 * QUIC_OK ──[loss>thresh]──→ QUIC_DEGRADED
 * QUIC_DEGRADED ──[probe]──→ TCP_PROBE
 * TCP_PROBE ──[tcp_rx]──→ HTTP2_ACTIVE
 * HTTP2_ACTIVE ──[quic_ok]──→ QUIC_OK (prefer QUIC)
 * ═════════════════════════════════════════════ */

transport_state_t
fallback_tick(fallback_session_t *sess, uint64_t now_ns)
{
    transport_metrics_t *m = &sess->metrics;

    switch (sess->state) {
    case TRANSPORT_QUIC_OK:
        /* Check for degradation */
        if (m->quic_loss_rate > m->quic_loss_threshold) {
            sess->state = TRANSPORT_QUIC_DEGRADED;
        }
        /* Check for silence (total block) */
        if (m->quic_pkts_sent > 10 && m->quic_last_rx_ns > 0 &&
            (now_ns - m->quic_last_rx_ns) > m->quic_silence_ns) {
            sess->state = TRANSPORT_QUIC_DEGRADED;
        }
        break;

    case TRANSPORT_QUIC_DEGRADED:
        /* Initiate TCP probe */
        sess->state = TRANSPORT_TCP_PROBE;
        sess->fallback_count++;
        break;

    case TRANSPORT_TCP_PROBE:
        /* Wait for TCP response */
        if (m->tcp_pkts_acked > 0) {
            sess->state = TRANSPORT_HTTP2_ACTIVE;
        }
        /* Timeout: both blocked */
        if (m->tcp_pkts_sent > 5 && m->tcp_pkts_acked == 0) {
            sess->state = TRANSPORT_BLOCKED;
        }
        break;

    case TRANSPORT_HTTP2_ACTIVE:
        /* Check if QUIC has recovered */
        if (m->quic_last_rx_ns > 0 &&
            (now_ns - m->quic_last_rx_ns) < 2000000000ULL && /* Within 2s */
            m->quic_loss_rate < m->quic_loss_threshold / 2.0) {
            sess->state = TRANSPORT_QUIC_OK;
            sess->recovery_count++;
        }
        /* Check if TCP is also degraded */
        if (m->tcp_loss_rate > 0.50) {
            sess->state = TRANSPORT_HTTP2_DEGRADED;
        }
        break;

    case TRANSPORT_HTTP2_DEGRADED:
        /* Try recovery */
        if (m->tcp_loss_rate < 0.20)
            sess->state = TRANSPORT_HTTP2_ACTIVE;
        if (m->quic_loss_rate < m->quic_loss_threshold / 2.0)
            sess->state = TRANSPORT_QUIC_OK;
        break;

    case TRANSPORT_BLOCKED:
        /* Periodically retry */
        if (m->quic_pkts_acked > 0 || m->tcp_pkts_acked > 0) {
            sess->state = (m->quic_pkts_acked > 0) ?
                          TRANSPORT_QUIC_OK : TRANSPORT_HTTP2_ACTIVE;
        }
        break;
    }

    return sess->state;
}

/* ═════════════════════════════════════════════
 * HMAC-SHA3-256 (for chaffing MAC)
 * ═════════════════════════════════════════════ */

static void
hmac_sha3(uint8_t out[32], const uint8_t *key, size_t klen,
          const uint8_t *msg, size_t mlen)
{
    uint8_t k_ipad[136], k_opad[136];
    uint8_t k[32];

    if (klen > 136) { mlkem_hash_h(k, key, klen); key = k; klen = 32; }

    memset(k_ipad, 0x36, 136);
    memset(k_opad, 0x5C, 136);
    for (size_t i = 0; i < klen; i++) {
        k_ipad[i] ^= key[i]; k_opad[i] ^= key[i];
    }

    /* Inner: H(ipad || msg) */
    uint8_t *inner = malloc(136 + mlen);
    if (!inner) { memset(out, 0, 32); return; }
    memcpy(inner, k_ipad, 136);
    memcpy(inner + 136, msg, mlen);
    uint8_t ih[32];
    mlkem_hash_h(ih, inner, 136 + mlen);
    free(inner);

    /* Outer: H(opad || inner_hash) */
    uint8_t outer[136 + 32];
    memcpy(outer, k_opad, 136);
    memcpy(outer + 136, ih, 32);
    mlkem_hash_h(out, outer, sizeof(outer));

    memset(k, 0, sizeof(k));
}

/* ═════════════════════════════════════════════
 * Chaffing-and-Winnowing (Rivest 1998)
 *
 * TX: for each real data chunk, emit 1 real + N chaff packets
 * Real packet: MAC = HMAC(key, seq || data) [valid]
 * Chaff packet: MAC = random [invalid]
 * RX: verify MAC on each packet; discard chaff, keep real
 * ═════════════════════════════════════════════ */

#if defined(__linux__)
#include <sys/random.h>
static int rng_fill(uint8_t *out, size_t len) {
    return (getrandom(out, len, 0) == (ssize_t)len) ? 0 : -1;
}
#else
#include <stdio.h>
static int rng_fill(uint8_t *out, size_t len) {
    FILE *f = fopen("/dev/urandom", "rb");
    if (!f) return -1;
    size_t n = fread(out, 1, len, f); fclose(f);
    return (n == len) ? 0 : -1;
}
#endif

static void
compute_chaff_mac(uint8_t mac[CHAFF_MAC_BYTES],
                  const uint8_t key[32],
                  uint32_t seq, const uint8_t *data, uint16_t dlen)
{
    /* MAC input = seq(4) || data(N) */
    uint8_t *buf = malloc(4 + dlen);
    if (!buf) { memset(mac, 0, CHAFF_MAC_BYTES); return; }
    buf[0] = (uint8_t)(seq >> 24); buf[1] = (uint8_t)(seq >> 16);
    buf[2] = (uint8_t)(seq >> 8);  buf[3] = (uint8_t)(seq);
    memcpy(buf + 4, data, dlen);

    uint8_t full_mac[32];
    hmac_sha3(full_mac, key, 32, buf, 4 + dlen);
    memcpy(mac, full_mac, CHAFF_MAC_BYTES); /* Truncate to 16 bytes */

    free(buf);
    memset(full_mac, 0, sizeof(full_mac));
}

int
chaff_encode(fallback_session_t *sess,
             const uint8_t *payload, size_t len,
             chaff_packet_t *out_packets, int *out_count, int max_packets)
{
    if (len > CHAFF_MAX_DATA) return -1;
    int needed = 1 + sess->chaff_ratio;
    if (needed > max_packets) return -1;

    /* Position for real packet (random within the batch) */
    uint8_t rpos_byte;
    rng_fill(&rpos_byte, 1);
    int real_pos = rpos_byte % needed;

    uint32_t seq = sess->chaff_tx_seq++;

    for (int i = 0; i < needed; i++) {
        chaff_packet_t *pkt = &out_packets[i];
        pkt->seq = seq;
        pkt->data_len = (uint16_t)len;

        if (i == real_pos) {
            /* Real packet */
            memcpy(pkt->data, payload, len);
            compute_chaff_mac(pkt->mac, sess->session_key,
                              seq, payload, (uint16_t)len);
            pkt->is_real = 1;
            sess->chaff_real_sent++;
        } else {
            /* Chaff: random data, random MAC */
            rng_fill(pkt->data, len);
            rng_fill(pkt->mac, CHAFF_MAC_BYTES);
            pkt->is_real = 0;
        }
        sess->chaff_sent++;
    }

    *out_count = needed;
    return 0;
}

int
chaff_winnow(fallback_session_t *sess,
             const chaff_packet_t *packets, int count,
             uint8_t *out, size_t out_cap, size_t *out_len)
{
    *out_len = 0;

    for (int i = 0; i < count; i++) {
        const chaff_packet_t *pkt = &packets[i];

        /* Verify MAC */
        uint8_t expected_mac[CHAFF_MAC_BYTES];
        compute_chaff_mac(expected_mac, sess->session_key,
                          pkt->seq, pkt->data, pkt->data_len);

        /* Constant-time compare */
        uint8_t diff = 0;
        for (int j = 0; j < CHAFF_MAC_BYTES; j++)
            diff |= expected_mac[j] ^ pkt->mac[j];

        if (diff == 0) {
            /* Valid MAC — this is a real packet */
            if (pkt->data_len > out_cap) return -1;
            memcpy(out, pkt->data, pkt->data_len);
            *out_len = pkt->data_len;
            sess->winnowed++;
            return 0;
        }
    }

    return -1; /* No valid packet found */
}

/* ═════════════════════════════════════════════
 * TCP Timestamp Steganography
 *
 * Encode bits into the LSBs of TCP timestamp values.
 * TCP timestamps (RFC 7323) are 32-bit monotonic counters.
 * We replace the lowest N bits with payload data.
 *
 * Capacity: 2-4 bits per packet at ~100 pps = 200-400 bps
 * ═════════════════════════════════════════════ */

uint32_t
tcp_ts_encode_bits(fallback_session_t *sess, uint32_t original_ts, int nbits)
{
    if (nbits < 1 || nbits > 4) nbits = 2;
    if (sess->ts_bit_index >= sess->ts_payload_len * 8)
        return original_ts; /* No more data */

    /* Extract nbits from payload */
    uint32_t bits = 0;
    for (int b = 0; b < nbits; b++) {
        uint32_t idx = sess->ts_bit_index++;
        if (idx < sess->ts_payload_len * 8) {
            uint8_t byte = sess->ts_payload[idx / 8];
            uint8_t bit = (byte >> (7 - (idx % 8))) & 1;
            bits |= (bit << (nbits - 1 - b));
        }
    }

    /* Replace LSBs of timestamp */
    uint32_t mask = (1U << nbits) - 1;
    return (original_ts & ~mask) | (bits & mask);
}

int
tcp_ts_decode_bits(fallback_session_t *sess, uint32_t received_ts, int nbits)
{
    if (nbits < 1 || nbits > 4) nbits = 2;

    uint32_t mask = (1U << nbits) - 1;
    uint32_t bits = received_ts & mask;

    /* Store extracted bits */
    for (int b = 0; b < nbits; b++) {
        uint32_t idx = sess->ts_bit_index++;
        if (idx < sess->ts_payload_cap * 8) {
            uint8_t bit = (bits >> (nbits - 1 - b)) & 1;
            if (bit)
                sess->ts_payload[idx / 8] |= (1 << (7 - (idx % 8)));
            else
                sess->ts_payload[idx / 8] &= ~(1 << (7 - (idx % 8)));
        }
    }

    return 0;
}

/* ═════════════════════════════════════════════
 * HTTP/2 DATA Frame Padding Injection
 *
 * HTTP/2 DATA frames (RFC 9113 §6.1) support a padding field:
 *   [PAD_LEN:1?][DATA:N][PADDING:PAD_LEN?]
 *   Flag 0x08 (PADDED) enables padding.
 *
 * We inject encrypted stego payload into the padding bytes,
 * similar to Module 3's QUIC PADDING injection.
 *
 * Frame format:
 *   [LENGTH:3][TYPE:1][FLAGS:1][R:1][STREAM_ID:31] = 9 byte header
 * ═════════════════════════════════════════════ */

#define H2_FRAME_HEADER_LEN  9
#define H2_TYPE_DATA         0x00
#define H2_FLAG_PADDED       0x08

int
h2_pad_inject(fallback_session_t *sess,
              uint8_t *frame, size_t frame_len, size_t frame_cap,
              const uint8_t *payload, size_t pay_len)
{
    if (frame_len < H2_FRAME_HEADER_LEN) return -1;

    /* Check it's a DATA frame */
    uint8_t frame_type = frame[3];
    if (frame_type != H2_TYPE_DATA) return -1;

    /* Read current frame length */
    uint32_t flen = ((uint32_t)frame[0] << 16) |
                    ((uint32_t)frame[1] << 8) | frame[2];

    /* Set PADDED flag */
    frame[4] |= H2_FLAG_PADDED;

    /* Calculate available padding space */
    size_t data_start = H2_FRAME_HEADER_LEN;
    int already_padded = 0;
    uint8_t existing_pad_len = 0;

    if (frame[4] & H2_FLAG_PADDED) {
        existing_pad_len = frame[data_start];
        data_start += 1;
        already_padded = 1;
    }

    /* Stego header: [MAGIC:2][LEN:2] = 4 bytes overhead in pad area */
    size_t stego_overhead = 4;
    size_t needed_pad = stego_overhead + pay_len;
    if (needed_pad > 255) return -1; /* HTTP/2 pad_len is 1 byte */

    /* Ensure frame fits in buffer */
    size_t new_frame_len = flen + (already_padded ? 0 : 1) + needed_pad - existing_pad_len;
    if (H2_FRAME_HEADER_LEN + new_frame_len > frame_cap) return -1;

    /* Update frame length */
    frame[0] = (uint8_t)(new_frame_len >> 16);
    frame[1] = (uint8_t)(new_frame_len >> 8);
    frame[2] = (uint8_t)(new_frame_len);

    /* Write pad length byte */
    size_t pad_len_pos = H2_FRAME_HEADER_LEN;
    if (!already_padded) {
        /* Shift data right by 1 to insert pad_length byte */
        memmove(frame + pad_len_pos + 1,
                frame + pad_len_pos,
                flen);
    }
    frame[pad_len_pos] = (uint8_t)needed_pad;

    /* Write stego data at end of frame (in padding area) */
    size_t pad_start = H2_FRAME_HEADER_LEN + 1 + (flen - existing_pad_len);

    /* Derive session magic for HTTP/2 channel */
    uint8_t h2_magic[2];
    uint8_t h2_derive[34];
    memcpy(h2_derive, sess->session_key, 32);
    h2_derive[32] = 'H'; h2_derive[33] = '2';
    uint8_t h[32];
    mlkem_hash_h(h, h2_derive, 34);
    h2_magic[0] = h[0]; h2_magic[1] = h[1];

    frame[pad_start]     = h2_magic[0];
    frame[pad_start + 1] = h2_magic[1];
    frame[pad_start + 2] = (uint8_t)(pay_len >> 8);
    frame[pad_start + 3] = (uint8_t)(pay_len);
    memcpy(frame + pad_start + 4, payload, pay_len);

    return 0;
}

int
h2_pad_extract(fallback_session_t *sess,
               const uint8_t *frame, size_t frame_len,
               uint8_t *out, size_t out_cap, size_t *out_len)
{
    *out_len = 0;
    if (frame_len < H2_FRAME_HEADER_LEN) return -1;
    if (frame[3] != H2_TYPE_DATA) return -1;
    if (!(frame[4] & H2_FLAG_PADDED)) return -1;

    uint32_t flen = ((uint32_t)frame[0] << 16) |
                    ((uint32_t)frame[1] << 8) | frame[2];
    uint8_t pad_len = frame[H2_FRAME_HEADER_LEN];

    if (pad_len < 4) return -1; /* Too small for stego header */

    /* Padding starts at end of data payload */
    size_t pad_start = H2_FRAME_HEADER_LEN + 1 + flen - pad_len;
    if (pad_start + 4 > frame_len) return -1;

    /* Check magic */
    uint8_t h2_derive[34];
    memcpy(h2_derive, sess->session_key, 32);
    h2_derive[32] = 'H'; h2_derive[33] = '2';
    uint8_t h[32];
    mlkem_hash_h(h, h2_derive, 34);

    if (frame[pad_start] != h[0] || frame[pad_start + 1] != h[1])
        return -1; /* Not our magic */

    uint16_t pay_len = ((uint16_t)frame[pad_start + 2] << 8) |
                        frame[pad_start + 3];
    if (pay_len > out_cap || pad_start + 4 + pay_len > frame_len)
        return -1;

    memcpy(out, frame + pad_start + 4, pay_len);
    *out_len = pay_len;
    return 0;
}

```
