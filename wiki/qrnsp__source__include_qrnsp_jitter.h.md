---
title: "include/qrnsp_jitter.h"
nav_title: "qrnsp_jitter.h"
---

# `include/qrnsp_jitter.h`

```c
/*
 * QR-NSP Volcanic Edition — Temporal Jitter Shaping
 * Module 4: Timing-based covert channel
 *
 * Encodes binary data into the inter-packet arrival time (IPAT) of
 * UDP datagrams. This is a SECOND steganographic channel, orthogonal
 * to Module 3's PADDING injection. It works even when:
 *   - PADDING regions are too small or absent (short-header 1-RTT packets)
 *   - Packet payloads are fully encrypted and unmodifiable
 *   - Only packet timing is under our control
 *
 * Encoding: Spread-spectrum On-Off Keying (SS-OOK)
 *   bit 0 → inter-packet delay T_base + jitter
 *   bit 1 → inter-packet delay T_base + T_delta + jitter
 *   jitter ~ N(0, σ²) shaped to match natural network variance
 *
 * Stealth properties:
 *   - T_base and T_delta chosen so both bins overlap the natural IPAT
 *     distribution of the cover traffic (e.g., video streaming)
 *   - Added Gaussian noise makes individual delays indistinguishable
 *   - Only statistical analysis over many packets can detect the channel,
 *     and the spread-spectrum chipping makes that analysis expensive
 *
 * Bandwidth: ~10-100 bits/second (low but sufficient for key exchange,
 *   signaling, or short messages when PADDING channel is unavailable)
 *
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#ifndef QRNSP_JITTER_H
#define QRNSP_JITTER_H

#include <stdint.h>
#include <stddef.h>

/* ─────────────────────────────────────────────
 * Configuration
 * ───────────────────────────────────────────── */

/* Timing parameters (microseconds) */
#define JITTER_T_BASE_US       5000   /* Base inter-packet delay: 5ms     */
#define JITTER_T_DELTA_US      2000   /* Extra delay for bit=1: +2ms      */
#define JITTER_SIGMA_US        800    /* Gaussian noise σ: 0.8ms          */

/* Spread-spectrum chipping */
#define JITTER_CHIPS_PER_BIT   8      /* Chips per data bit (redundancy)  */
#define JITTER_CHIP_SEQ_LEN    127    /* Gold code length (2^7 - 1)       */

/* Synchronization preamble */
#define JITTER_PREAMBLE_BITS   16     /* Barker-13 + 3 guard bits         */
#define JITTER_PREAMBLE_CHIPS  (JITTER_PREAMBLE_BITS * JITTER_CHIPS_PER_BIT)

/* Manchester encoding doubles bit count but provides clock recovery */
#define JITTER_USE_MANCHESTER  1

/* Forward Error Correction */
#define JITTER_FEC_RATE_NUM    1      /* Rate 1/3 repetition code         */
#define JITTER_FEC_RATE_DEN    3

/* Maximum payload (pre-FEC, pre-Manchester) */
#define JITTER_MAX_PAYLOAD     64     /* 64 bytes = 512 bits              */

/* With Manchester + FEC + chipping:
 * 512 bits × 2 (Manchester) × 3 (FEC) × 8 (chips) = 24576 chips
 * At ~5ms/chip → ~123 seconds for 64 bytes
 * Practical: use for signaling and short keys, not bulk data
 */

/* ─────────────────────────────────────────────
 * State
 * ───────────────────────────────────────────── */

typedef enum {
    JITTER_ROLE_TX,
    JITTER_ROLE_RX
} jitter_role_t;

typedef enum {
    JITTER_STATE_IDLE,
    JITTER_STATE_PREAMBLE,      /* Sending/detecting preamble          */
    JITTER_STATE_DATA,          /* Transmitting/receiving data bits     */
    JITTER_STATE_COMPLETE,      /* Transfer finished                   */
    JITTER_STATE_ERROR
} jitter_state_t;

/* Transmitter context */
typedef struct {
    jitter_state_t state;

    /* Data to transmit (after FEC + Manchester encoding) */
    uint8_t  chip_stream[8192]; /* Encoded chip sequence               */
    uint32_t chip_count;        /* Total chips to send                 */
    uint32_t chip_index;        /* Current position                    */

    /* Timing */
    uint64_t last_tx_ns;        /* Timestamp of last packet sent       */
    uint64_t next_tx_ns;        /* Scheduled time for next packet      */

    /* Spread spectrum */
    uint8_t  gold_code[JITTER_CHIP_SEQ_LEN]; /* PN sequence            */
    uint32_t gold_phase;        /* Current phase in Gold code          */

    /* PRNG for Gaussian noise (Box-Muller) */
    uint64_t rng_state[2];      /* xorshift128+ state                  */
    int      has_spare;         /* Box-Muller spare available          */
    double   spare_val;         /* Cached Gaussian sample              */

    /* Stats */
    uint64_t packets_sent;
    uint64_t bits_encoded;
} jitter_tx_t;

/* Receiver context */
typedef struct {
    jitter_state_t state;

    /* Arrival time buffer for correlation */
    uint64_t arrival_times[32768]; /* Ring buffer of packet timestamps  */
    uint32_t arrival_head;
    uint32_t arrival_count;

    /* IPAT (inter-packet arrival time) samples */
    int64_t  ipat_samples[16384]; /* Computed IPATs in nanoseconds     */
    uint32_t ipat_count;

    /* Preamble detection */
    double   correlation_buf[256];
    int      preamble_detected;
    uint32_t preamble_offset;   /* IPAT index where preamble starts    */

    /* Decoded chips → bits */
    uint8_t  raw_chips[8192];
    uint32_t raw_chip_count;

    /* Despread + FEC decoded data */
    uint8_t  decoded_data[JITTER_MAX_PAYLOAD];
    uint32_t decoded_len;

    /* Spread spectrum */
    uint8_t  gold_code[JITTER_CHIP_SEQ_LEN];

    /* Timing reference */
    double   estimated_t_base;   /* Estimated base delay               */
    double   estimated_t_delta;  /* Estimated delta                    */
    double   estimated_sigma;    /* Estimated jitter                   */

    /* Stats */
    uint64_t packets_received;
    double   bit_error_rate;
} jitter_rx_t;

/* ─────────────────────────────────────────────
 * TX API
 * ───────────────────────────────────────────── */

/*
 * Initialize transmitter with shared secret (for Gold code seed).
 */
int jitter_tx_init(jitter_tx_t *tx, const uint8_t seed[32]);

/*
 * Load payload for transmission.
 * Applies FEC → Manchester → spread-spectrum chipping.
 * After this call, use jitter_tx_next_delay() in the packet send loop.
 */
int jitter_tx_load(jitter_tx_t *tx,
                   const uint8_t *payload, size_t len);

/*
 * Get the delay (in nanoseconds) before sending the next packet.
 * Returns 0 when transmission is complete.
 *
 * Usage in send loop:
 *   while ((delay = jitter_tx_next_delay(tx)) > 0) {
 *       nanosleep(delay);
 *       send_packet(cover_traffic);
 *   }
 */
uint64_t jitter_tx_next_delay(jitter_tx_t *tx);

/*
 * Mark that a packet was actually sent (records true timestamp).
 */
void jitter_tx_packet_sent(jitter_tx_t *tx, uint64_t timestamp_ns);

/*
 * Query progress: returns fraction complete [0.0, 1.0].
 */
double jitter_tx_progress(const jitter_tx_t *tx);

/* ─────────────────────────────────────────────
 * RX API
 * ───────────────────────────────────────────── */

/*
 * Initialize receiver with shared secret (same seed as TX).
 */
int jitter_rx_init(jitter_rx_t *rx, const uint8_t seed[32]);

/*
 * Feed a packet arrival timestamp to the receiver.
 * Call this for every QUIC packet received.
 *
 * Returns:
 *   0  — still collecting
 *   1  — preamble detected, data reception in progress
 *   2  — message fully decoded (read with jitter_rx_get_data)
 *  -1  — error
 */
int jitter_rx_feed(jitter_rx_t *rx, uint64_t timestamp_ns);

/*
 * Retrieve decoded message after jitter_rx_feed returns 2.
 */
int jitter_rx_get_data(const jitter_rx_t *rx,
                       uint8_t *out, size_t out_cap,
                       size_t *out_len);

/*
 * Reset receiver for next message.
 */
void jitter_rx_reset(jitter_rx_t *rx);

/* ─────────────────────────────────────────────
 * Cleanup
 * ───────────────────────────────────────────── */

void jitter_tx_destroy(jitter_tx_t *tx);
void jitter_rx_destroy(jitter_rx_t *rx);

#endif /* QRNSP_JITTER_H */

```
