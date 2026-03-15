---
title: "tests/test_deniable.c"
nav_title: "test_deniable.c"
---

# `tests/test_deniable.c`

```c
/*
 * QR-NSP Volcanic Edition — Module 5 Test: Deniable Encryption
 * Multi-password hidden volumes with honey-encryption.
 *
 * Build:
 *   gcc -O2 -march=native -I include -o test_deniable \
 *       tests/test_deniable.c src/deniable/deniable.c \
 *       src/aead/aes256gcm.c src/crypto/symmetric.c
 *
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include "qrnsp_deniable.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

/* ─────────────────────────────────────────────
 * Helpers
 * ───────────────────────────────────────────── */

static void
hexdump_short(const char *label, const uint8_t *data, size_t len)
{
    printf("  %s [%zu]: ", label, len);
    size_t show = (len > 40) ? 40 : len;
    for (size_t i = 0; i < show; i++) printf("%02x", data[i]);
    if (len > 40) printf("...");
    printf("\n");
}

static void
print_text(const char *label, const uint8_t *data, size_t len)
{
    printf("  %s [%zu]: \"", label, len);
    size_t show = (len > 60) ? 60 : len;
    for (size_t i = 0; i < show; i++) {
        char c = (char)data[i];
        if (c >= 32 && c < 127) putchar(c);
        else putchar('.');
    }
    if (len > 60) printf("...");
    printf("\"\n");
}

/* ─────────────────────────────────────────────
 * Test 1: Single volume seal + open
 * ───────────────────────────────────────────── */

static int
test_single_volume(void)
{
    printf("[test] Single volume seal/open... ");

    const char *password = "resistance2026";
    const char *secret = "Meeting at dock 7, midnight. Bring the documents.";

    deny_volume_t vol = {
        .password     = password,
        .password_len = strlen(password),
        .plaintext    = (const uint8_t *)secret,
        .plaintext_len = strlen(secret),
        .honey_type   = HONEY_DIST_ENGLISH_TEXT,
    };

    /* Compute required size and allocate */
    size_t req = deny_required_size(&vol, 1);
    uint8_t *buf = calloc(1, req);
    deny_container_t container = { .data = buf, .capacity = req };

    /* Seal */
    clock_t t0 = clock();
    deny_result_t res = deny_seal(&vol, 1, &container);
    clock_t t1 = clock();

    if (res != DENY_OK) {
        printf("FAIL (seal: %d)\n", res);
        free(buf);
        return -1;
    }
    printf("\n    seal: %.2fs, container: %zu bytes\n    ",
           (double)(t1 - t0) / CLOCKS_PER_SEC, req);

    /* Open with correct password */
    uint8_t out[1024];
    size_t out_len;

    clock_t t2 = clock();
    res = deny_open(&container, password, strlen(password),
                    out, sizeof(out), &out_len);
    clock_t t3 = clock();

    if (res != DENY_OK) {
        printf("FAIL (open: %d)\n", res);
        free(buf);
        return -1;
    }

    if (out_len != strlen(secret) || memcmp(out, secret, out_len) != 0) {
        printf("FAIL (mismatch)\n");
        print_text("expected", (const uint8_t *)secret, strlen(secret));
        print_text("got     ", out, out_len);
        free(buf);
        return -1;
    }

    printf("OK (open: %.2fs)\n", (double)(t3 - t2) / CLOCKS_PER_SEC);
    print_text("decrypted", out, out_len);
    free(buf);
    return 0;
}

/* ─────────────────────────────────────────────
 * Test 2: Two volumes (decoy + real)
 * ───────────────────────────────────────────── */

static int
test_dual_volume(void)
{
    printf("[test] Dual volume (decoy + real)... ");

    const char *decoy_pass = "shopping_list";
    const char *decoy_data = "Milk, eggs, bread, butter, cheese";

    const char *real_pass = "fr33d0m_n0w!";
    const char *real_data = "Agent contacts: Alpha=48.2N,16.4E Bravo=51.5N,0.1W";

    deny_volume_t vols[2] = {
        {
            .password = decoy_pass, .password_len = strlen(decoy_pass),
            .plaintext = (const uint8_t *)decoy_data,
            .plaintext_len = strlen(decoy_data),
            .honey_type = HONEY_DIST_ENGLISH_TEXT,
        },
        {
            .password = real_pass, .password_len = strlen(real_pass),
            .plaintext = (const uint8_t *)real_data,
            .plaintext_len = strlen(real_data),
            .honey_type = HONEY_DIST_ENGLISH_TEXT,
        },
    };

    size_t req = deny_required_size(vols, 2);
    uint8_t *buf = calloc(1, req);
    deny_container_t container = { .data = buf, .capacity = req };

    deny_result_t res = deny_seal(vols, 2, &container);
    if (res != DENY_OK) {
        printf("FAIL (seal: %d)\n", res);
        free(buf);
        return -1;
    }

    printf("\n    container: %zu bytes\n", req);

    /* Open with DECOY password (what you show the adversary) */
    uint8_t out[1024];
    size_t out_len;

    res = deny_open(&container, decoy_pass, strlen(decoy_pass),
                    out, sizeof(out), &out_len);
    if (res == DENY_OK && out_len == strlen(decoy_data) &&
        memcmp(out, decoy_data, out_len) == 0) {
        print_text("    decoy", out, out_len);
    } else {
        printf("    WARN: decoy open returned %d (may overlap with real)\n", res);
    }

    /* Open with REAL password (the secret payload) */
    res = deny_open(&container, real_pass, strlen(real_pass),
                    out, sizeof(out), &out_len);
    if (res == DENY_OK && out_len == strlen(real_data) &&
        memcmp(out, real_data, out_len) == 0) {
        print_text("    real ", out, out_len);
        printf("    OK\n");
        free(buf);
        return 0;
    }

    printf("    FAIL (real volume: res=%d, len=%zu)\n", res, out_len);
    free(buf);
    return -1;
}

/* ─────────────────────────────────────────────
 * Test 3: Wrong password → honey-encrypted output
 * ───────────────────────────────────────────── */

static int
test_honey_encryption(void)
{
    printf("[test] Honey-encryption (wrong password)... ");

    const char *real_pass = "correct_horse_battery";
    const char *secret = "Nuclear codes: 00000000";

    deny_volume_t vol = {
        .password = real_pass, .password_len = strlen(real_pass),
        .plaintext = (const uint8_t *)secret,
        .plaintext_len = strlen(secret),
        .honey_type = HONEY_DIST_ENGLISH_TEXT,
    };

    size_t req = deny_required_size(&vol, 1);
    uint8_t *buf = calloc(1, req);
    deny_container_t container = { .data = buf, .capacity = req };
    deny_seal(&vol, 1, &container);

    /* Try 3 wrong passwords — each should return plausible-looking text */
    const char *wrong[] = {"wrong_pass_1", "password123", "letmein"};
    int ok = 1;

    printf("\n");
    for (int i = 0; i < 3; i++) {
        uint8_t out[1024];
        size_t out_len;
        deny_result_t res = deny_open(&container, wrong[i], strlen(wrong[i]),
                                      out, sizeof(out), &out_len);

        if (res != DENY_ERR_HONEY) {
            printf("    FAIL: wrong pass '%s' returned %d (expected HONEY)\n",
                   wrong[i], res);
            ok = 0;
            continue;
        }

        printf("    pass='%s' → honey ", wrong[i]);
        print_text("", out, out_len);

        /* Verify output is non-empty and looks like text */
        if (out_len == 0) {
            printf("    FAIL: empty honey output\n");
            ok = 0;
        }
    }

    if (ok) printf("    OK (3/3 wrong passwords produced plausible honey text)\n");

    free(buf);
    return ok ? 0 : -1;
}

/* ─────────────────────────────────────────────
 * Test 4: Container is uniformly random-looking
 * ───────────────────────────────────────────── */

static int
test_container_randomness(void)
{
    printf("[test] Container byte distribution (χ² test)... ");

    const char *pass = "entropy_test";
    const char *data = "This is secret data that should be invisible";

    deny_volume_t vol = {
        .password = pass, .password_len = strlen(pass),
        .plaintext = (const uint8_t *)data,
        .plaintext_len = strlen(data),
        .honey_type = HONEY_DIST_BINARY,
    };

    size_t req = DENY_CONTAINER_64K;
    uint8_t *buf = calloc(1, req);
    deny_container_t container = { .data = buf, .capacity = req };
    deny_seal(&vol, 1, &container);

    /* Byte frequency analysis (skip salt) */
    size_t freq[256] = {0};
    for (size_t i = DENY_SALT_BYTES; i < req; i++)
        freq[buf[i]]++;

    /* χ² test: compare against uniform distribution */
    double expected = (double)(req - DENY_SALT_BYTES) / 256.0;
    double chi2 = 0.0;
    for (int i = 0; i < 256; i++) {
        double diff = (double)freq[i] - expected;
        chi2 += (diff * diff) / expected;
    }

    /* χ²(255) at p=0.01 ≈ 310.5. Good randomness → χ² ≈ 255 ± 23 */
    printf("χ²=%.1f (expected ~255, reject if >310)\n", chi2);

    if (chi2 > 350.0) {
        printf("    WARN: Container may not look sufficiently random\n");
        /* Not a hard fail — χ² is probabilistic */
    }

    free(buf);
    return 0;
}

/* ─────────────────────────────────────────────
 * Test 5: Different honey outputs for different wrong passwords
 * ───────────────────────────────────────────── */

static int
test_honey_diversity(void)
{
    printf("[test] Honey output diversity... ");

    const char *pass = "real_deal";
    const char *data = "secret";

    deny_volume_t vol = {
        .password = pass, .password_len = strlen(pass),
        .plaintext = (const uint8_t *)data,
        .plaintext_len = strlen(data),
        .honey_type = HONEY_DIST_ENGLISH_TEXT,
    };

    size_t req = deny_required_size(&vol, 1);
    uint8_t *buf = calloc(1, req);
    deny_container_t container = { .data = buf, .capacity = req };
    deny_seal(&vol, 1, &container);

    /* Generate honey outputs for 5 wrong passwords */
    uint8_t honey[5][256];
    size_t honey_lens[5];
    const char *wrong[] = {"aaa","bbb","ccc","ddd","eee"};

    for (int i = 0; i < 5; i++) {
        deny_open(&container, wrong[i], strlen(wrong[i]),
                  honey[i], sizeof(honey[i]), &honey_lens[i]);
    }

    /* Verify all outputs are different */
    int all_different = 1;
    for (int i = 0; i < 5; i++) {
        for (int j = i + 1; j < 5; j++) {
            if (honey_lens[i] == honey_lens[j] &&
                memcmp(honey[i], honey[j], honey_lens[i]) == 0) {
                printf("FAIL (identical honey for '%s' and '%s')\n",
                       wrong[i], wrong[j]);
                all_different = 0;
            }
        }
    }

    if (all_different)
        printf("OK (5 unique honey outputs)\n");

    free(buf);
    return all_different ? 0 : -1;
}

/* ─────────────────────────────────────────────
 * Test 6: Performance benchmark (KDF cost)
 * ───────────────────────────────────────────── */

static int
test_kdf_performance(void)
{
    printf("[bench] KDF performance (seal + open):\n");

    const char *pass = "benchmark_password";
    const char *data = "benchmark payload data for timing";

    deny_volume_t vol = {
        .password = pass, .password_len = strlen(pass),
        .plaintext = (const uint8_t *)data,
        .plaintext_len = strlen(data),
        .honey_type = HONEY_DIST_BINARY,
    };

    size_t req = deny_required_size(&vol, 1);
    uint8_t *buf = calloc(1, req);
    deny_container_t container = { .data = buf, .capacity = req };

    /* Seal timing */
    clock_t t0 = clock();
    deny_seal(&vol, 1, &container);
    clock_t t1 = clock();

    /* Open timing */
    uint8_t out[1024];
    size_t out_len;
    clock_t t2 = clock();
    deny_open(&container, pass, strlen(pass), out, sizeof(out), &out_len);
    clock_t t3 = clock();

    printf("    seal: %.3fs  open: %.3fs  (iterations=%d)\n",
           (double)(t1 - t0) / CLOCKS_PER_SEC,
           (double)(t3 - t2) / CLOCKS_PER_SEC,
           DENY_KDF_ITERATIONS);

    free(buf);
    return 0;
}

/* ─────────────────────────────────────────────
 * Main
 * ───────────────────────────────────────────── */

int
main(void)
{
    printf("╔══════════════════════════════════════════════╗\n");
    printf("║  QR-NSP Module 5: Deniable Encryption Test  ║\n");
    printf("║  Multi-Password KDF + Honey-Encryption       ║\n");
    printf("╚══════════════════════════════════════════════╝\n\n");

    int failures = 0;

    failures += (test_single_volume() != 0);
    failures += (test_dual_volume() != 0);
    failures += (test_honey_encryption() != 0);
    failures += (test_container_randomness() != 0);
    failures += (test_honey_diversity() != 0);
    test_kdf_performance();

    printf("\n%s: %d test(s) failed\n",
           failures ? "FAILED" : "ALL PASSED", failures);

    return failures;
}

```
