---
title: "src/jitter/jitter.c"
nav_title: "jitter.c"
---

# `src/jitter/jitter.c`

```c
/*
 * QR-NSP Volcanic Edition — Temporal Jitter Shaping
 * Module 4: Timing-based covert channel implementation
 *
 * Signal chain (TX):
 *   payload → FEC(1/3) → Manchester → spread(Gold code) → delay schedule
 *
 * Signal chain (RX):
 *   timestamps → IPAT → preamble correlate → despread → Manchester → FEC → payload
 *
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include "qrnsp_jitter.h"
#include "mlkem_params.h"  /* mlkem_hash_h for seeded PRNG */
#include <string.h>
#include <math.h>

/* ═════════════════════════════════════════════
 * PRNG: xorshift128+ (fast, deterministic from seed)
 * ═════════════════════════════════════════════ */

static inline uint64_t
xorshift128p(uint64_t state[2])
{
    uint64_t s1 = state[0];
    uint64_t s0 = state[1];
    state[0] = s0;
    s1 ^= s1 << 23;
    s1 ^= s1 >> 17;
    s1 ^= s0;
    s1 ^= s0 >> 26;
    state[1] = s1;
    return s0 + s1;
}

static void
prng_seed(uint64_t state[2], const uint8_t seed[32], const char *domain)
{
    /* Derive PRNG seed: SHA3-256(seed || domain) */
    uint8_t buf[64];
    size_t dlen = strlen(domain);
    memcpy(buf, seed, 32);
    memcpy(buf + 32, domain, dlen < 32 ? dlen : 32);
    uint8_t h[32];
    mlkem_hash_h(h, buf, 32 + (dlen < 32 ? dlen : 32));
    memcpy(&state[0], h, 8);
    memcpy(&state[1], h + 8, 8);
    /* Ensure non-zero */
    if (state[0] == 0) state[0] = 1;
    if (state[1] == 0) state[1] = 1;
    memset(buf, 0, sizeof(buf));
    memset(h, 0, sizeof(h));
}

/* ═════════════════════════════════════════════
 * Gaussian Random (Box-Muller transform)
 *
 * Returns samples from N(0, 1).
 * Multiply by σ and add μ for N(μ, σ²).
 * ═════════════════════════════════════════════ */

static double
gaussian_sample(jitter_tx_t *tx)
{
    if (tx->has_spare) {
        tx->has_spare = 0;
        return tx->spare_val;
    }

    double u, v, s;
    do {
        u = ((double)(xorshift128p(tx->rng_state) >> 11) / (double)(1ULL << 53)) * 2.0 - 1.0;
        v = ((double)(xorshift128p(tx->rng_state) >> 11) / (double)(1ULL << 53)) * 2.0 - 1.0;
        s = u * u + v * v;
    } while (s >= 1.0 || s == 0.0);

    double mul = sqrt(-2.0 * log(s) / s);
    tx->spare_val = v * mul;
    tx->has_spare = 1;
    return u * mul;
}

/* ═════════════════════════════════════════════
 * Gold Code Generation
 *
 * Gold codes are preferred sequences for CDMA — low cross-correlation.
 * Generate from two m-sequences (LFSR) of length 2^7 - 1 = 127.
 *
 * LFSR polynomials for degree 7:
 *   G1: x^7 + x^3 + 1           (taps: 7, 3)
 *   G2: x^7 + x^3 + x^2 + x + 1 (taps: 7, 3, 2, 1)
 *
 * Gold code = G1 ⊕ G2 (with relative shift derived from seed)
 * ═════════════════════════════════════════════ */

static void
generate_gold_code(uint8_t code[JITTER_CHIP_SEQ_LEN], const uint8_t seed[32])
{
    /* Derive shift from seed */
    uint8_t h[32];
    mlkem_hash_h(h, seed, 32);
    uint32_t shift = (h[0] | ((uint32_t)h[1] << 8)) % JITTER_CHIP_SEQ_LEN;

    /* Generate m-sequence G1: x^7 + x^3 + 1 */
    uint8_t g1[JITTER_CHIP_SEQ_LEN];
    uint8_t lfsr1 = 0x7F; /* All ones initial state */
    for (int i = 0; i < JITTER_CHIP_SEQ_LEN; i++) {
        g1[i] = lfsr1 & 1;
        uint8_t fb = ((lfsr1 >> 6) ^ (lfsr1 >> 2)) & 1;
        lfsr1 = (lfsr1 >> 1) | (fb << 6);
    }

    /* Generate m-sequence G2: x^7 + x^3 + x^2 + x + 1 */
    uint8_t g2[JITTER_CHIP_SEQ_LEN];
    uint8_t lfsr2 = 0x7F;
    for (int i = 0; i < JITTER_CHIP_SEQ_LEN; i++) {
        g2[i] = lfsr2 & 1;
        uint8_t fb = ((lfsr2 >> 6) ^ (lfsr2 >> 2) ^ (lfsr2 >> 1) ^ lfsr2) & 1;
        lfsr2 = (lfsr2 >> 1) | (fb << 6);
    }

    /* Gold code = G1 ⊕ G2(shifted) */
    for (int i = 0; i < JITTER_CHIP_SEQ_LEN; i++) {
        code[i] = g1[i] ^ g2[(i + shift) % JITTER_CHIP_SEQ_LEN];
    }

    memset(h, 0, sizeof(h));
}

/* ═════════════════════════════════════════════
 * Barker-13 Preamble
 *
 * Barker codes have optimal autocorrelation properties —
 * sharp peak at zero lag, low sidelobes. Barker-13 is the
 * longest known Barker code.
 *
 * Pattern: +1 +1 +1 +1 +1 −1 −1 +1 +1 −1 +1 −1 +1
 * (as bits: 1 1 1 1 1 0 0 1 1 0 1 0 1)
 * ═════════════════════════════════════════════ */

static const uint8_t barker13[13] = {1,1,1,1,1,0,0,1,1,0,1,0,1};

/* Extended preamble: Barker-13 + 3 guard bits (0,0,0) */
static const uint8_t preamble_bits[JITTER_PREAMBLE_BITS] = {
    1,1,1,1,1,0,0,1,1,0,1,0,1, 0,0,0
};

/* ═════════════════════════════════════════════
 * Manchester Encoding
 *
 * bit 0 → 01
 * bit 1 → 10
 *
 * Guarantees transitions for clock recovery.
 * Doubles the bit rate but eliminates baseline wander.
 * ═════════════════════════════════════════════ */

static uint32_t
manchester_encode(uint8_t *out, const uint8_t *bits, uint32_t nbits)
{
    uint32_t j = 0;
    for (uint32_t i = 0; i < nbits; i++) {
        if (bits[i]) {
            out[j++] = 1;
            out[j++] = 0;
        } else {
            out[j++] = 0;
            out[j++] = 1;
        }
    }
    return j;
}

static uint32_t
manchester_decode(uint8_t *out, const uint8_t *encoded, uint32_t nencoded)
{
    uint32_t j = 0;
    for (uint32_t i = 0; i + 1 < nencoded; i += 2) {
        /* 10 → 1, 01 → 0, else → error (use majority) */
        if (encoded[i] == 1 && encoded[i+1] == 0)
            out[j++] = 1;
        else if (encoded[i] == 0 && encoded[i+1] == 1)
            out[j++] = 0;
        else
            out[j++] = encoded[i]; /* Best guess on error */
    }
    return j;
}

/* ═════════════════════════════════════════════
 * FEC: Rate 1/3 Repetition Code
 *
 * Simple but effective for timing channels where BER is high.
 * Each bit is repeated 3 times; majority vote on decode.
 * ═════════════════════════════════════════════ */

static uint32_t
fec_encode(uint8_t *out, const uint8_t *bits, uint32_t nbits)
{
    uint32_t j = 0;
    for (uint32_t i = 0; i < nbits; i++) {
        for (int r = 0; r < JITTER_FEC_RATE_DEN; r++)
            out[j++] = bits[i];
    }
    return j;
}

static uint32_t
fec_decode(uint8_t *out, const uint8_t *encoded, uint32_t nencoded)
{
    uint32_t j = 0;
    for (uint32_t i = 0; i + 2 < nencoded; i += JITTER_FEC_RATE_DEN) {
        /* Majority vote */
        int sum = 0;
        for (int r = 0; r < JITTER_FEC_RATE_DEN; r++)
            sum += encoded[i + r];
        out[j++] = (sum > JITTER_FEC_RATE_DEN / 2) ? 1 : 0;
    }
    return j;
}

/* ═════════════════════════════════════════════
 * Spread Spectrum: chip a bit stream with Gold code
 *
 * Each data bit is XOR'd with CHIPS_PER_BIT chips from the
 * Gold code. Receiver correlates to despread.
 * ═════════════════════════════════════════════ */

static uint32_t
spread(uint8_t *out, const uint8_t *bits, uint32_t nbits,
       const uint8_t gold[JITTER_CHIP_SEQ_LEN])
{
    uint32_t j = 0;
    uint32_t gold_idx = 0;

    for (uint32_t i = 0; i < nbits; i++) {
        for (int c = 0; c < JITTER_CHIPS_PER_BIT; c++) {
            out[j++] = bits[i] ^ gold[gold_idx % JITTER_CHIP_SEQ_LEN];
            gold_idx++;
        }
    }
    return j;
}

/*
 * Despread: correlate received chips against Gold code,
 * recover original bits via majority decision per chip group.
 */
static uint32_t
despread(uint8_t *out, const uint8_t *chips, uint32_t nchips,
         const uint8_t gold[JITTER_CHIP_SEQ_LEN])
{
    uint32_t j = 0;
    uint32_t gold_idx = 0;

    for (uint32_t i = 0; i + JITTER_CHIPS_PER_BIT <= nchips;
         i += JITTER_CHIPS_PER_BIT) {
        int sum = 0;
        for (int c = 0; c < JITTER_CHIPS_PER_BIT; c++) {
            /* XOR with Gold code to despread, then count */
            uint8_t despread_chip = chips[i + c] ^ gold[gold_idx % JITTER_CHIP_SEQ_LEN];
            sum += despread_chip;
            gold_idx++;
        }
        out[j++] = (sum > JITTER_CHIPS_PER_BIT / 2) ? 1 : 0;
    }
    return j;
}

/* ═════════════════════════════════════════════
 * Bytes ↔ Bits conversion
 * ═════════════════════════════════════════════ */

static uint32_t
bytes_to_bits(uint8_t *bits, const uint8_t *bytes, size_t nbytes)
{
    uint32_t j = 0;
    for (size_t i = 0; i < nbytes; i++) {
        for (int b = 7; b >= 0; b--)
            bits[j++] = (bytes[i] >> b) & 1;
    }
    return j;
}

static size_t
bits_to_bytes(uint8_t *bytes, const uint8_t *bits, uint32_t nbits)
{
    size_t nbytes = nbits / 8;
    memset(bytes, 0, nbytes);
    for (uint32_t i = 0; i < nbytes * 8; i++) {
        bytes[i / 8] |= (bits[i] & 1) << (7 - (i % 8));
    }
    return nbytes;
}

/* ═════════════════════════════════════════════
 * TX Implementation
 * ═════════════════════════════════════════════ */

int
jitter_tx_init(jitter_tx_t *tx, const uint8_t seed[32])
{
    memset(tx, 0, sizeof(*tx));
    tx->state = JITTER_STATE_IDLE;

    generate_gold_code(tx->gold_code, seed);
    prng_seed(tx->rng_state, seed, "jitter_tx_noise");

    return 0;
}

int
jitter_tx_load(jitter_tx_t *tx, const uint8_t *payload, size_t len)
{
    if (len > JITTER_MAX_PAYLOAD || len == 0)
        return -1;

    /*
     * Encoding pipeline:
     *   1. Add length prefix (1 byte)
     *   2. Convert to bits
     *   3. FEC encode (×3)
     *   4. Manchester encode (×2)
     *   5. Spread with Gold code (×CHIPS_PER_BIT)
     *   6. Prepend preamble chips
     */

    /* Step 1: length prefix + payload */
    uint8_t framed[JITTER_MAX_PAYLOAD + 1];
    framed[0] = (uint8_t)len;
    memcpy(framed + 1, payload, len);
    size_t framed_len = len + 1;

    /* Step 2: bytes → bits */
    uint8_t data_bits[8 * (JITTER_MAX_PAYLOAD + 1)];
    uint32_t ndata_bits = bytes_to_bits(data_bits, framed, framed_len);

    /* Step 3: FEC encode */
    uint8_t fec_bits[8 * (JITTER_MAX_PAYLOAD + 1) * JITTER_FEC_RATE_DEN];
    uint32_t nfec = fec_encode(fec_bits, data_bits, ndata_bits);

    /* Step 4: Manchester encode */
    uint8_t manc_bits[8 * (JITTER_MAX_PAYLOAD + 1) * JITTER_FEC_RATE_DEN * 2];
    uint32_t nmanc = manchester_encode(manc_bits, fec_bits, nfec);

    /* Step 5: Spread spectrum */
    uint8_t data_chips[65536]; /* Generous buffer */
    uint32_t ndata_chips = spread(data_chips, manc_bits, nmanc, tx->gold_code);

    /* Step 6: Preamble chips */
    uint8_t preamble_manc[JITTER_PREAMBLE_BITS * 2];
    uint32_t npre_manc = manchester_encode(preamble_manc, preamble_bits,
                                           JITTER_PREAMBLE_BITS);
    uint8_t preamble_chips[JITTER_PREAMBLE_BITS * 2 * JITTER_CHIPS_PER_BIT];
    uint32_t npre_chips = spread(preamble_chips, preamble_manc, npre_manc,
                                 tx->gold_code);

    /* Assemble: preamble || data */
    if (npre_chips + ndata_chips > sizeof(tx->chip_stream))
        return -1;

    memcpy(tx->chip_stream, preamble_chips, npre_chips);
    memcpy(tx->chip_stream + npre_chips, data_chips, ndata_chips);
    tx->chip_count = npre_chips + ndata_chips;
    tx->chip_index = 0;
    tx->gold_phase = 0;
    tx->state = JITTER_STATE_PREAMBLE;

    return 0;
}

uint64_t
jitter_tx_next_delay(jitter_tx_t *tx)
{
    if (tx->state == JITTER_STATE_COMPLETE || tx->state == JITTER_STATE_IDLE)
        return 0;

    if (tx->chip_index >= tx->chip_count) {
        tx->state = JITTER_STATE_COMPLETE;
        return 0;
    }

    /* Determine base delay based on current chip value */
    uint8_t chip = tx->chip_stream[tx->chip_index];

    double base_us = (double)JITTER_T_BASE_US;
    if (chip) {
        base_us += (double)JITTER_T_DELTA_US;
    }

    /* Add Gaussian jitter for stealth */
    double noise_us = gaussian_sample(tx) * (double)JITTER_SIGMA_US;
    double delay_us = base_us + noise_us;

    /* Clamp to prevent negative or excessively large delays */
    if (delay_us < (double)(JITTER_T_BASE_US / 2))
        delay_us = (double)(JITTER_T_BASE_US / 2);
    if (delay_us > (double)(JITTER_T_BASE_US + JITTER_T_DELTA_US) * 3.0)
        delay_us = (double)(JITTER_T_BASE_US + JITTER_T_DELTA_US) * 3.0;

    tx->chip_index++;

    /* Update state transition */
    if (tx->chip_index >= JITTER_PREAMBLE_CHIPS &&
        tx->state == JITTER_STATE_PREAMBLE) {
        tx->state = JITTER_STATE_DATA;
    }

    /* Convert to nanoseconds */
    return (uint64_t)(delay_us * 1000.0);
}

void
jitter_tx_packet_sent(jitter_tx_t *tx, uint64_t timestamp_ns)
{
    tx->last_tx_ns = timestamp_ns;
    tx->packets_sent++;
}

double
jitter_tx_progress(const jitter_tx_t *tx)
{
    if (tx->chip_count == 0) return 0.0;
    return (double)tx->chip_index / (double)tx->chip_count;
}

void
jitter_tx_destroy(jitter_tx_t *tx)
{
    memset(tx, 0, sizeof(*tx));
}

/* ═════════════════════════════════════════════
 * RX Implementation
 * ═════════════════════════════════════════════ */

int
jitter_rx_init(jitter_rx_t *rx, const uint8_t seed[32])
{
    memset(rx, 0, sizeof(*rx));
    rx->state = JITTER_STATE_IDLE;
    generate_gold_code(rx->gold_code, seed);

    /* Initialize timing estimates */
    rx->estimated_t_base  = (double)JITTER_T_BASE_US * 1000.0;  /* ns */
    rx->estimated_t_delta = (double)JITTER_T_DELTA_US * 1000.0;
    rx->estimated_sigma   = (double)JITTER_SIGMA_US * 1000.0;

    return 0;
}

/*
 * Classify an IPAT sample as chip 0 or chip 1.
 *
 * Decision boundary: T_base + T_delta/2
 * Below → chip 0, Above → chip 1
 */
static uint8_t
classify_ipat(int64_t ipat_ns, double t_base_ns, double t_delta_ns)
{
    double threshold = t_base_ns + t_delta_ns / 2.0;
    return (ipat_ns > (int64_t)threshold) ? 1 : 0;
}

/*
 * Preamble correlation detector.
 *
 * Cross-correlate the received chip stream with the known
 * preamble pattern. A strong peak indicates synchronization.
 *
 * Returns the offset of the peak, or -1 if no strong peak found.
 */
static int
detect_preamble(const uint8_t *chips, uint32_t nchips,
                const uint8_t gold[JITTER_CHIP_SEQ_LEN])
{
    /* Generate expected preamble chip pattern */
    uint8_t preamble_manc[JITTER_PREAMBLE_BITS * 2];
    uint32_t npre_manc = manchester_encode(preamble_manc, preamble_bits,
                                           JITTER_PREAMBLE_BITS);
    uint8_t expected[JITTER_PREAMBLE_BITS * 2 * JITTER_CHIPS_PER_BIT];
    uint32_t nexpected = spread(expected, preamble_manc, npre_manc, gold);

    if (nchips < nexpected)
        return -1;

    /* Sliding correlation */
    int best_offset = -1;
    double best_corr = 0.0;
    double threshold = 0.7 * (double)nexpected; /* 70% match required */

    uint32_t search_range = nchips - nexpected;
    if (search_range > 1000) search_range = 1000; /* Limit search */

    for (uint32_t off = 0; off < search_range; off++) {
        double corr = 0.0;
        for (uint32_t i = 0; i < nexpected; i++) {
            /* +1 for match, -1 for mismatch */
            corr += (chips[off + i] == expected[i]) ? 1.0 : -1.0;
        }
        if (corr > best_corr) {
            best_corr = corr;
            best_offset = (int)off;
        }
    }

    if (best_corr >= threshold)
        return best_offset;

    return -1;
}

int
jitter_rx_feed(jitter_rx_t *rx, uint64_t timestamp_ns)
{
    /* Store arrival time */
    uint32_t idx = rx->arrival_head;
    rx->arrival_times[idx % 32768] = timestamp_ns;
    rx->arrival_head++;
    rx->arrival_count++;
    rx->packets_received++;

    /* Need at least 2 arrivals to compute IPAT */
    if (rx->arrival_count < 2)
        return 0;

    /* Compute IPAT from last two arrivals */
    uint64_t prev = rx->arrival_times[(idx - 1) % 32768];
    int64_t ipat = (int64_t)(timestamp_ns - prev);

    /* Filter: ignore unreasonable IPATs (< 1ms or > 100ms) */
    if (ipat < 1000000 || ipat > 100000000)
        return 0;

    /* Store IPAT */
    if (rx->ipat_count < 16384) {
        rx->ipat_samples[rx->ipat_count] = ipat;

        /* Classify chip */
        rx->raw_chips[rx->ipat_count] = classify_ipat(
            ipat, rx->estimated_t_base, rx->estimated_t_delta);
        rx->ipat_count++;
        rx->raw_chip_count = rx->ipat_count;
    }

    /* ── Preamble detection phase ── */
    if (!rx->preamble_detected && rx->raw_chip_count >= JITTER_PREAMBLE_CHIPS + 32) {
        int pre_off = detect_preamble(rx->raw_chips, rx->raw_chip_count,
                                      rx->gold_code);
        if (pre_off >= 0) {
            rx->preamble_detected = 1;
            rx->preamble_offset = (uint32_t)pre_off;
            rx->state = JITTER_STATE_DATA;

            /* Refine timing estimates from preamble region */
            /* (Adaptive: compute mean IPAT for known 0s and 1s) */
            return 1;
        }
        return 0;
    }

    /* ── Data reception phase ── */
    if (rx->preamble_detected && rx->state == JITTER_STATE_DATA) {
        /* Data chips start after preamble */
        uint32_t data_start = rx->preamble_offset + JITTER_PREAMBLE_CHIPS;
        if (rx->raw_chip_count <= data_start)
            return 0; /* Still in preamble region */

        uint32_t data_chips_available = rx->raw_chip_count - data_start;

        /* Try to decode what we have so far */
        /* Need at minimum: 1 byte (length prefix) =
         *   8 bits × 3 (FEC) × 2 (Manchester) × 8 (chips) = 384 chips */
        if (data_chips_available < 384)
            return 0;

        /* Despread */
        uint8_t despread_bits[4096];
        uint32_t ndespread = despread(despread_bits,
                                      rx->raw_chips + data_start,
                                      data_chips_available,
                                      rx->gold_code);

        /* Manchester decode */
        uint8_t manc_decoded[2048];
        uint32_t nmanc = manchester_decode(manc_decoded, despread_bits, ndespread);

        /* FEC decode */
        uint8_t fec_decoded[1024];
        uint32_t nfec = fec_decode(fec_decoded, manc_decoded, nmanc);

        /* Convert bits → bytes */
        if (nfec < 8)
            return 0; /* Not enough for length byte */

        uint8_t decoded_bytes[JITTER_MAX_PAYLOAD + 1];
        size_t nbytes = bits_to_bytes(decoded_bytes, fec_decoded, nfec);

        if (nbytes < 1)
            return 0;

        /* First byte is length */
        uint8_t claimed_len = decoded_bytes[0];
        if (claimed_len == 0 || claimed_len > JITTER_MAX_PAYLOAD)
            return 0; /* Keep waiting — probably incomplete */

        /* Check if we have enough chips for the full message */
        uint32_t needed_data_bits = (claimed_len + 1) * 8; /* +1 for length prefix */
        uint32_t needed_chips = needed_data_bits * JITTER_FEC_RATE_DEN * 2 *
                                JITTER_CHIPS_PER_BIT;

        if (data_chips_available < needed_chips)
            return 0; /* Still receiving */

        /* We have enough — final decode */
        if (nbytes >= (size_t)(claimed_len + 1)) {
            memcpy(rx->decoded_data, decoded_bytes + 1, claimed_len);
            rx->decoded_len = claimed_len;
            rx->state = JITTER_STATE_COMPLETE;
            return 2; /* Message complete */
        }

        return 0; /* Keep collecting */
    }

    return 0;
}

int
jitter_rx_get_data(const jitter_rx_t *rx,
                   uint8_t *out, size_t out_cap,
                   size_t *out_len)
{
    if (rx->state != JITTER_STATE_COMPLETE)
        return -1;

    if (rx->decoded_len > out_cap)
        return -1;

    memcpy(out, rx->decoded_data, rx->decoded_len);
    *out_len = rx->decoded_len;
    return 0;
}

void
jitter_rx_reset(jitter_rx_t *rx)
{
    uint8_t gold_save[JITTER_CHIP_SEQ_LEN];
    memcpy(gold_save, rx->gold_code, sizeof(gold_save));
    double t_base = rx->estimated_t_base;
    double t_delta = rx->estimated_t_delta;
    double t_sigma = rx->estimated_sigma;

    memset(rx, 0, sizeof(*rx));
    memcpy(rx->gold_code, gold_save, sizeof(gold_save));
    rx->estimated_t_base = t_base;
    rx->estimated_t_delta = t_delta;
    rx->estimated_sigma = t_sigma;
    rx->state = JITTER_STATE_IDLE;
}

void
jitter_rx_destroy(jitter_rx_t *rx)
{
    memset(rx, 0, sizeof(*rx));
}

```
