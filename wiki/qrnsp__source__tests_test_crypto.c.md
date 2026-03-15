---
title: "tests/test_crypto.c"
nav_title: "test_crypto.c"
---

# `tests/test_crypto.c`

```c
/*
 * QR-NSP Volcanic Edition — Crypto Test Harness
 * SPDX-License-Identifier: AGPL-3.0-or-later
 * Verifies ML-KEM-1024 and Hybrid KEM correctness.
 *
 * Build: gcc -O2 -march=native -I include -o test_crypto \
 *        tests/test_crypto.c src/crypto/ntt.c src/crypto/poly.c \
 *        src/crypto/symmetric.c src/crypto/kem.c src/crypto/hybrid_kem.c
 */

#include "mlkem_params.h"
#include "qrnsp_crypto.h"
#include <stdio.h>
#include <string.h>
#include <time.h>

/* ─────────────────────────────────────────────
 * Timing helper
 * ───────────────────────────────────────────── */

static inline uint64_t
rdtsc(void)
{
#if defined(__x86_64__)
    uint32_t lo, hi;
    __asm__ volatile ("rdtsc" : "=a"(lo), "=d"(hi));
    return ((uint64_t)hi << 32) | lo;
#else
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (uint64_t)ts.tv_sec * 1000000000ULL + ts.tv_nsec;
#endif
}

/* ─────────────────────────────────────────────
 * Test 1: ML-KEM-1024 round-trip
 * ───────────────────────────────────────────── */

static int
test_mlkem_roundtrip(void)
{
    printf("[test] ML-KEM-1024 round-trip... ");

    mlkem_keypair kp;
    uint8_t ct[MLKEM_CIPHERTEXTBYTES];
    uint8_t ss_enc[MLKEM_SSBYTES];
    uint8_t ss_dec[MLKEM_SSBYTES];

    /* KeyGen */
    uint64_t t0 = rdtsc();
    if (mlkem_keypair_generate(&kp) != 0) {
        printf("FAIL (keygen)\n");
        return -1;
    }
    uint64_t t1 = rdtsc();

    /* Encapsulate */
    uint64_t t2 = rdtsc();
    if (mlkem_encapsulate(ct, ss_enc, kp.pk) != 0) {
        printf("FAIL (encaps)\n");
        return -1;
    }
    uint64_t t3 = rdtsc();

    /* Decapsulate */
    uint64_t t4 = rdtsc();
    if (mlkem_decapsulate(ss_dec, ct, kp.sk) != 0) {
        printf("FAIL (decaps)\n");
        return -1;
    }
    uint64_t t5 = rdtsc();

    /* Verify shared secrets match */
    if (memcmp(ss_enc, ss_dec, MLKEM_SSBYTES) != 0) {
        printf("FAIL (ss mismatch)\n");
        printf("  ss_enc: ");
        for (int i = 0; i < 16; i++) printf("%02x", ss_enc[i]);
        printf("...\n  ss_dec: ");
        for (int i = 0; i < 16; i++) printf("%02x", ss_dec[i]);
        printf("...\n");
        return -1;
    }

    printf("OK\n");
    printf("  keygen:  %lu cycles\n", t1 - t0);
    printf("  encaps:  %lu cycles\n", t3 - t2);
    printf("  decaps:  %lu cycles\n", t5 - t4);
    printf("  pk size: %d bytes\n", MLKEM_PUBLICKEYBYTES);
    printf("  sk size: %d bytes\n", MLKEM_SECRETKEYBYTES);
    printf("  ct size: %d bytes\n", MLKEM_CIPHERTEXTBYTES);
    printf("  ss size: %d bytes\n", MLKEM_SSBYTES);

    return 0;
}

/* ─────────────────────────────────────────────
 * Test 2: ML-KEM implicit rejection
 *
 * Tamper with ciphertext → shared secrets must differ
 * ───────────────────────────────────────────── */

static int
test_mlkem_implicit_rejection(void)
{
    printf("[test] ML-KEM-1024 implicit rejection... ");

    mlkem_keypair kp;
    uint8_t ct[MLKEM_CIPHERTEXTBYTES];
    uint8_t ss_enc[MLKEM_SSBYTES];
    uint8_t ss_dec[MLKEM_SSBYTES];

    mlkem_keypair_generate(&kp);
    mlkem_encapsulate(ct, ss_enc, kp.pk);

    /* Tamper with ciphertext */
    ct[0] ^= 0xFF;
    ct[100] ^= 0x42;

    mlkem_decapsulate(ss_dec, ct, kp.sk);

    /* Shared secrets MUST differ (implicit rejection) */
    if (memcmp(ss_enc, ss_dec, MLKEM_SSBYTES) == 0) {
        printf("FAIL (no rejection — tampered ct produced same ss!)\n");
        return -1;
    }

    printf("OK (tampered ct → different ss)\n");
    return 0;
}

/* ─────────────────────────────────────────────
 * Test 3: Hybrid KEM round-trip
 * ───────────────────────────────────────────── */

static int
test_hybrid_roundtrip(void)
{
    printf("[test] Hybrid KEM (ML-KEM-1024 + X25519) round-trip... ");

    uint8_t pk[QRNSP_CRYPTO_PUBLICKEYBYTES];
    uint8_t sk[QRNSP_CRYPTO_SECRETKEYBYTES];
    uint8_t ct[QRNSP_CRYPTO_CIPHERTEXTBYTES];
    uint8_t ss_enc[QRNSP_CRYPTO_SSBYTES];
    uint8_t ss_dec[QRNSP_CRYPTO_SSBYTES];

    uint64_t t0 = rdtsc();
    if (hybrid_keypair_generate(pk, sk) != 0) {
        printf("FAIL (keygen)\n");
        return -1;
    }
    uint64_t t1 = rdtsc();

    uint64_t t2 = rdtsc();
    if (hybrid_encapsulate(ct, ss_enc, pk) != 0) {
        printf("FAIL (encaps)\n");
        return -1;
    }
    uint64_t t3 = rdtsc();

    uint64_t t4 = rdtsc();
    if (hybrid_decapsulate(ss_dec, ct, sk, pk) != 0) {
        printf("FAIL (decaps)\n");
        return -1;
    }
    uint64_t t5 = rdtsc();

    if (memcmp(ss_enc, ss_dec, QRNSP_CRYPTO_SSBYTES) != 0) {
        printf("FAIL (ss mismatch)\n");
        printf("  ss_enc: ");
        for (int i = 0; i < 32; i++) printf("%02x", ss_enc[i]);
        printf("\n  ss_dec: ");
        for (int i = 0; i < 32; i++) printf("%02x", ss_dec[i]);
        printf("\n");
        return -1;
    }

    printf("OK\n");
    printf("  keygen:  %lu cycles\n", t1 - t0);
    printf("  encaps:  %lu cycles\n", t3 - t2);
    printf("  decaps:  %lu cycles\n", t5 - t4);
    printf("  pk size: %d bytes\n", QRNSP_CRYPTO_PUBLICKEYBYTES);
    printf("  sk size: %d bytes\n", QRNSP_CRYPTO_SECRETKEYBYTES);
    printf("  ct size: %d bytes\n", QRNSP_CRYPTO_CIPHERTEXTBYTES);
    printf("  ss size: %d bytes\n", QRNSP_CRYPTO_SSBYTES);

    return 0;
}

/* ─────────────────────────────────────────────
 * Test 4: NTT correctness (forward → inverse = identity)
 * ───────────────────────────────────────────── */

static int
test_ntt_roundtrip(void)
{
    printf("[test] NTT forward/inverse round-trip... ");

    mlkem_poly p, p_orig;

    /* Fill with small known values */
    for (int i = 0; i < MLKEM_N; i++) {
        p.coeffs[i] = (int16_t)(i % 100);
        p_orig.coeffs[i] = p.coeffs[i];
    }

    mlkem_ntt(&p);
    mlkem_invntt(&p);

    /* Check coefficients match (within Montgomery reduction) */
    int mismatches = 0;
    for (int i = 0; i < MLKEM_N; i++) {
        int16_t a = p.coeffs[i] % MLKEM_Q;
        int16_t b = p_orig.coeffs[i] % MLKEM_Q;
        if (a < 0) a += MLKEM_Q;
        if (b < 0) b += MLKEM_Q;
        if (a != b) mismatches++;
    }

    if (mismatches > 0) {
        printf("FAIL (%d mismatches)\n", mismatches);
        return -1;
    }

    printf("OK\n");
    return 0;
}

/* ─────────────────────────────────────────────
 * Test 5: Throughput benchmark
 * ───────────────────────────────────────────── */

static int
test_throughput(void)
{
    printf("[bench] ML-KEM-1024 throughput (100 iterations)...\n");

    mlkem_keypair kp;
    uint8_t ct[MLKEM_CIPHERTEXTBYTES];
    uint8_t ss_e[MLKEM_SSBYTES], ss_d[MLKEM_SSBYTES];
    int iters = 100;

    mlkem_keypair_generate(&kp);

    uint64_t t0 = rdtsc();
    for (int i = 0; i < iters; i++) {
        mlkem_encapsulate(ct, ss_e, kp.pk);
        mlkem_decapsulate(ss_d, ct, kp.sk);
    }
    uint64_t t1 = rdtsc();

    uint64_t total = t1 - t0;
    printf("  %d encaps+decaps in %lu cycles\n", iters, total);
    printf("  avg: %lu cycles per round-trip\n", total / iters);

    return 0;
}

/* ─────────────────────────────────────────────
 * Main
 * ───────────────────────────────────────────── */

int
main(void)
{
    printf("╔══════════════════════════════════════════════╗\n");
    printf("║  QR-NSP Module 2: Crypto Test Suite         ║\n");
    printf("║  ML-KEM-1024 (FIPS 203) + X25519 Hybrid     ║\n");
    printf("╚══════════════════════════════════════════════╝\n\n");

    int failures = 0;

    failures += (test_ntt_roundtrip() != 0);
    failures += (test_mlkem_roundtrip() != 0);
    failures += (test_mlkem_implicit_rejection() != 0);
    failures += (test_hybrid_roundtrip() != 0);
    test_throughput(); /* Bench, not a pass/fail test */

    printf("\n%s: %d test(s) failed\n",
           failures ? "FAILED" : "ALL PASSED", failures);

    return failures;
}

```
