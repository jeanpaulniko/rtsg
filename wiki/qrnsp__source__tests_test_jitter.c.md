---
title: "tests/test_jitter.c"
nav_title: "test_jitter.c"
---

# `tests/test_jitter.c`

```c
/*
 * QR-NSP Volcanic Edition — Module 4 Test: Temporal Jitter Channel
 * Simulates TX → network (with added noise) → RX round-trip.
 *
 * Build:
 *   gcc -O2 -march=native -I include -o test_jitter \
 *       tests/test_jitter.c src/jitter/jitter.c src/crypto/symmetric.c \
 *       -lm
 *
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include "qrnsp_jitter.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

/* ─────────────────────────────────────────────
 * Simulated Network Jitter
 *
 * Adds realistic network noise on top of the TX-controlled delays.
 * Models: Gaussian base + occasional spikes (Pareto tail).
 * ───────────────────────────────────────────── */

static uint64_t sim_rng_state[2] = {0xDEADBEEF, 0xCAFEBABE};

static uint64_t
sim_xorshift(void)
{
    uint64_t s1 = sim_rng_state[0];
    uint64_t s0 = sim_rng_state[1];
    sim_rng_state[0] = s0;
    s1 ^= s1 << 23;
    s1 ^= s1 >> 17;
    s1 ^= s0 ^ (s0 >> 26);
    sim_rng_state[1] = s1;
    return s0 + s1;
}

static double
sim_uniform(void)
{
    return (double)(sim_xorshift() >> 11) / (double)(1ULL << 53);
}

static double
sim_gaussian(void)
{
    /* Box-Muller */
    double u1 = sim_uniform();
    double u2 = sim_uniform();
    if (u1 < 1e-10) u1 = 1e-10;
    return sqrt(-2.0 * log(u1)) * cos(2.0 * M_PI * u2);
}

/*
 * Simulate network delay distortion.
 * Adds Gaussian noise + occasional spike (5% chance of 2× jitter).
 *
 * network_noise_us: standard deviation of base network jitter (microseconds)
 */
static int64_t
simulate_network_noise(double noise_sigma_us)
{
    double base = sim_gaussian() * noise_sigma_us;

    /* 5% chance of a spike (models queue delays, retransmissions) */
    if (sim_uniform() < 0.05) {
        base += fabs(sim_gaussian()) * noise_sigma_us * 3.0;
    }

    return (int64_t)(base * 1000.0); /* Convert to nanoseconds */
}

/* ─────────────────────────────────────────────
 * Test 1: Encoding pipeline round-trip (no noise)
 * ───────────────────────────────────────────── */

static int
test_encode_decode_clean(void)
{
    printf("[test] Jitter encode/decode (clean, no noise)... ");

    uint8_t seed[32];
    for (int i = 0; i < 32; i++) seed[i] = (uint8_t)(i + 0x42);

    jitter_tx_t tx;
    jitter_rx_t rx;
    jitter_tx_init(&tx, seed);
    jitter_rx_init(&rx, seed);

    const char *msg = "SOS";
    if (jitter_tx_load(&tx, (const uint8_t *)msg, strlen(msg)) != 0) {
        printf("FAIL (tx_load)\n");
        return -1;
    }

    printf("\n    chips: %u, est. time: %.1fs\n    ",
           tx.chip_count,
           tx.chip_count * JITTER_T_BASE_US / 1e6);

    /* Simulate: TX produces delays, RX receives timestamps */
    uint64_t clock_ns = 1000000000ULL; /* Start at t=1s */
    int rx_status = 0;
    uint32_t packets = 0;

    while (1) {
        uint64_t delay = jitter_tx_next_delay(&tx);
        if (delay == 0) break;

        clock_ns += delay; /* Perfect clock — no network noise */
        jitter_tx_packet_sent(&tx, clock_ns);

        rx_status = jitter_rx_feed(&rx, clock_ns);
        packets++;

        if (rx_status == 2) break; /* Message decoded */
    }

    if (rx_status != 2) {
        printf("FAIL (rx incomplete after %u packets, state=%d)\n",
               packets, rx.state);
        jitter_tx_destroy(&tx);
        jitter_rx_destroy(&rx);
        return -1;
    }

    uint8_t out[256];
    size_t out_len;
    if (jitter_rx_get_data(&rx, out, sizeof(out), &out_len) != 0) {
        printf("FAIL (rx_get_data)\n");
        jitter_tx_destroy(&tx);
        jitter_rx_destroy(&rx);
        return -1;
    }

    if (out_len != strlen(msg) || memcmp(out, msg, out_len) != 0) {
        printf("FAIL (mismatch: got '%.*s', expected '%s')\n",
               (int)out_len, out, msg);
        jitter_tx_destroy(&tx);
        jitter_rx_destroy(&rx);
        return -1;
    }

    printf("OK (%u packets, decoded '%.*s')\n", packets, (int)out_len, out);
    jitter_tx_destroy(&tx);
    jitter_rx_destroy(&rx);
    return 0;
}

/* ─────────────────────────────────────────────
 * Test 2: With simulated network noise
 * ───────────────────────────────────────────── */

static int
test_with_network_noise(double noise_sigma_us)
{
    printf("[test] Jitter channel (network noise σ=%.0fμs)... ", noise_sigma_us);

    uint8_t seed[32];
    for (int i = 0; i < 32; i++) seed[i] = (uint8_t)(i + 0x77);

    jitter_tx_t tx;
    jitter_rx_t rx;
    jitter_tx_init(&tx, seed);
    jitter_rx_init(&rx, seed);

    const char *msg = "HELP";
    jitter_tx_load(&tx, (const uint8_t *)msg, strlen(msg));

    uint64_t clock_ns = 1000000000ULL;
    int rx_status = 0;
    uint32_t packets = 0;

    while (1) {
        uint64_t delay = jitter_tx_next_delay(&tx);
        if (delay == 0) break;

        /* Add network noise */
        int64_t noise = simulate_network_noise(noise_sigma_us);
        int64_t actual_delay = (int64_t)delay + noise;
        if (actual_delay < 500000) actual_delay = 500000; /* Min 0.5ms */

        clock_ns += (uint64_t)actual_delay;
        jitter_tx_packet_sent(&tx, clock_ns);

        rx_status = jitter_rx_feed(&rx, clock_ns);
        packets++;

        if (rx_status == 2) break;
    }

    if (rx_status != 2) {
        printf("FAIL (not decoded after %u packets)\n", packets);
        jitter_tx_destroy(&tx);
        jitter_rx_destroy(&rx);
        return -1;
    }

    uint8_t out[256];
    size_t out_len;
    jitter_rx_get_data(&rx, out, sizeof(out), &out_len);

    if (out_len != strlen(msg) || memcmp(out, msg, out_len) != 0) {
        printf("FAIL (decoded '%.*s', expected '%s')\n",
               (int)out_len, out, msg);
        jitter_tx_destroy(&tx);
        jitter_rx_destroy(&rx);
        return -1;
    }

    printf("OK (%u pkts, '%.*s')\n", packets, (int)out_len, out);
    jitter_tx_destroy(&tx);
    jitter_rx_destroy(&rx);
    return 0;
}

/* ─────────────────────────────────────────────
 * Test 3: Longer message
 * ───────────────────────────────────────────── */

static int
test_longer_message(void)
{
    printf("[test] Jitter longer message (16 bytes)... ");

    uint8_t seed[32] = {0};
    seed[0] = 0xAA;

    jitter_tx_t tx;
    jitter_rx_t rx;
    jitter_tx_init(&tx, seed);
    jitter_rx_init(&rx, seed);

    const char *msg = "Freedom awaits!"; /* 15 chars + null = 16 with length */
    jitter_tx_load(&tx, (const uint8_t *)msg, strlen(msg));

    printf("\n    chips: %u, est. time: %.1fs\n    ",
           tx.chip_count,
           tx.chip_count * JITTER_T_BASE_US / 1e6);

    uint64_t clock_ns = 1000000000ULL;
    int rx_status = 0;
    uint32_t packets = 0;

    while (1) {
        uint64_t delay = jitter_tx_next_delay(&tx);
        if (delay == 0) break;

        /* Moderate noise */
        int64_t noise = simulate_network_noise(300.0);
        clock_ns += (uint64_t)((int64_t)delay + noise);
        jitter_tx_packet_sent(&tx, clock_ns);

        rx_status = jitter_rx_feed(&rx, clock_ns);
        packets++;

        if (rx_status == 2) break;
    }

    if (rx_status != 2) {
        printf("FAIL (not decoded after %u packets)\n", packets);
        jitter_tx_destroy(&tx);
        jitter_rx_destroy(&rx);
        return -1;
    }

    uint8_t out[256];
    size_t out_len;
    jitter_rx_get_data(&rx, out, sizeof(out), &out_len);

    if (out_len != strlen(msg) || memcmp(out, msg, out_len) != 0) {
        printf("FAIL (decoded '%.*s')\n", (int)out_len, out);
        jitter_tx_destroy(&tx);
        jitter_rx_destroy(&rx);
        return -1;
    }

    printf("OK (%u pkts, '%.*s')\n", packets, (int)out_len, out);
    jitter_tx_destroy(&tx);
    jitter_rx_destroy(&rx);
    return 0;
}

/* ─────────────────────────────────────────────
 * Test 4: Bandwidth estimation
 * ───────────────────────────────────────────── */

static int
test_bandwidth(void)
{
    printf("[bench] Jitter channel bandwidth estimate:\n");

    uint8_t seed[32] = {0x55};
    jitter_tx_t tx;
    jitter_tx_init(&tx, seed);

    /* 1-byte message */
    uint8_t msg1[1] = {0x42};
    jitter_tx_load(&tx, msg1, 1);
    double time_1b = tx.chip_count * (double)JITTER_T_BASE_US / 1e6;
    printf("    1 byte:  %u chips, %.2fs, %.1f bps\n",
           tx.chip_count, time_1b, 8.0 / time_1b);

    /* 8-byte message */
    uint8_t msg8[8] = {0};
    jitter_tx_load(&tx, msg8, 8);
    double time_8b = tx.chip_count * (double)JITTER_T_BASE_US / 1e6;
    printf("    8 bytes: %u chips, %.2fs, %.1f bps\n",
           tx.chip_count, time_8b, 64.0 / time_8b);

    /* 32-byte message (256 bits — enough for a key) */
    uint8_t msg32[32] = {0};
    jitter_tx_load(&tx, msg32, 32);
    double time_32b = tx.chip_count * (double)JITTER_T_BASE_US / 1e6;
    printf("    32 bytes: %u chips, %.2fs, %.1f bps\n",
           tx.chip_count, time_32b, 256.0 / time_32b);

    /* 64-byte message (max) */
    uint8_t msg64[64] = {0};
    jitter_tx_load(&tx, msg64, 64);
    double time_64b = tx.chip_count * (double)JITTER_T_BASE_US / 1e6;
    printf("    64 bytes: %u chips, %.2fs, %.1f bps\n",
           tx.chip_count, time_64b, 512.0 / time_64b);

    jitter_tx_destroy(&tx);
    return 0;
}

/* ─────────────────────────────────────────────
 * Main
 * ───────────────────────────────────────────── */

int
main(void)
{
    printf("╔══════════════════════════════════════════════╗\n");
    printf("║  QR-NSP Module 4: Temporal Jitter Test      ║\n");
    printf("║  Spread-Spectrum Timing Channel              ║\n");
    printf("╚══════════════════════════════════════════════╝\n\n");

    /* Seed simulation PRNG */
    sim_rng_state[0] = (uint64_t)time(NULL);
    sim_rng_state[1] = sim_rng_state[0] ^ 0xBEEFCAFEDEAD1234ULL;

    int failures = 0;

    failures += (test_encode_decode_clean() != 0);
    failures += (test_with_network_noise(200.0) != 0);   /* Light noise */
    failures += (test_with_network_noise(500.0) != 0);   /* Moderate noise */
    failures += (test_longer_message() != 0);
    test_bandwidth();

    printf("\n%s: %d test(s) failed\n",
           failures ? "FAILED" : "ALL PASSED", failures);

    return failures;
}

```
