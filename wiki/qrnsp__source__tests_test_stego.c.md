---
title: "tests/test_stego.c"
nav_title: "test_stego.c"
---

# `tests/test_stego.c`

```c
/*
 * QR-NSP Volcanic Edition — Module 3 Integration Test
 * Full pipeline: KEM handshake → session → inject → extract
 *
 * Build:
 *   gcc -O2 -march=native -I include -o test_stego \
 *       tests/test_stego.c src/crypto/ntt.c src/crypto/poly.c \
 *       src/crypto/symmetric.c src/crypto/kem.c src/crypto/hybrid_kem.c \
 *       src/aead/aes256gcm.c src/stego/inject.c
 *
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include "qrnsp_stego.h"
#include "qrnsp_crypto.h"
#include "qrnsp_aead.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

/* ─────────────────────────────────────────────
 * Helpers
 * ───────────────────────────────────────────── */

static void
hexdump(const char *label, const uint8_t *data, size_t len)
{
    printf("  %s [%zu]: ", label, len);
    size_t show = (len > 32) ? 32 : len;
    for (size_t i = 0; i < show; i++) printf("%02x", data[i]);
    if (len > 32) printf("...");
    printf("\n");
}

/*
 * Build a fake QUIC Initial packet with PADDING.
 *
 * Layout (simplified):
 *   [Long header: 1+4+1+8+1+8 = 23 bytes]
 *   [CRYPTO frame: ~30 bytes of fake data]
 *   [PADDING: remaining to 1200 bytes]
 *
 * Real QUIC Initial packets pad to ≥1200 bytes (RFC 9000 §14.1).
 */
static size_t
build_fake_quic_initial(uint8_t *pkt, size_t bufsize)
{
    if (bufsize < 1200) return 0;

    size_t pos = 0;

    /* ── Long header ── */
    pkt[pos++] = 0xC0; /* Long header + Initial type */

    /* Version (QUIC v1) */
    pkt[pos++] = 0x00; pkt[pos++] = 0x00;
    pkt[pos++] = 0x00; pkt[pos++] = 0x01;

    /* DCID length + DCID (8 bytes) */
    pkt[pos++] = 0x08;
    for (int i = 0; i < 8; i++) pkt[pos++] = (uint8_t)(0xA0 + i);

    /* SCID length + SCID (8 bytes) */
    pkt[pos++] = 0x08;
    for (int i = 0; i < 8; i++) pkt[pos++] = (uint8_t)(0xB0 + i);

    /* Token length (0) */
    pkt[pos++] = 0x00;

    /* Payload length (2 bytes, simplified) */
    uint16_t payload_len = 1200 - (uint16_t)pos - 2;
    pkt[pos++] = (uint8_t)(0x40 | (payload_len >> 8)); /* 2-byte var-int */
    pkt[pos++] = (uint8_t)(payload_len & 0xFF);

    /* Packet number (4 bytes) */
    pkt[pos++] = 0x00; pkt[pos++] = 0x00;
    pkt[pos++] = 0x00; pkt[pos++] = 0x01;

    /* ── CRYPTO frame (fake) ── */
    pkt[pos++] = 0x06; /* CRYPTO frame type */
    pkt[pos++] = 0x00; /* Offset = 0 */
    pkt[pos++] = 0x1A; /* Length = 26 bytes */
    for (int i = 0; i < 26; i++) pkt[pos++] = (uint8_t)(0xCC + i); /* Fake crypto data */

    /* ── PADDING to 1200 bytes ── */
    while (pos < 1200) pkt[pos++] = 0x00;

    return 1200;
}

/* ─────────────────────────────────────────────
 * Test 1: AES-256-GCM round-trip
 * ───────────────────────────────────────────── */

static int
test_aead_roundtrip(void)
{
    printf("[test] AES-256-GCM round-trip... ");

    uint8_t key[32] = {0};
    uint8_t nonce[12] = {0};
    const char *msg = "Hello from behind the firewall";
    size_t msglen = strlen(msg);

    for (int i = 0; i < 32; i++) key[i] = (uint8_t)(i + 1);
    nonce[11] = 1;

    uint8_t ct[256], pt[256];
    uint8_t tag[16];
    uint8_t aad[] = "QR-NSP";

    if (aead_encrypt(ct, tag, (const uint8_t *)msg, msglen,
                     aad, sizeof(aad) - 1, nonce, key) != 0) {
        printf("FAIL (encrypt)\n");
        return -1;
    }

    if (aead_decrypt(pt, ct, msglen, tag, aad, sizeof(aad) - 1,
                     nonce, key) != 0) {
        printf("FAIL (decrypt)\n");
        return -1;
    }

    if (memcmp(pt, msg, msglen) != 0) {
        printf("FAIL (mismatch)\n");
        return -1;
    }

    /* Test tamper detection */
    ct[0] ^= 0x01;
    int ret = aead_decrypt(pt, ct, msglen, tag, aad, sizeof(aad) - 1,
                           nonce, key);
    if (ret == 0) {
        printf("FAIL (accepted tampered ct!)\n");
        return -1;
    }

    printf("OK\n");
    return 0;
}

/* ─────────────────────────────────────────────
 * Test 2: Full pipeline — KEM → session → inject → extract
 * ───────────────────────────────────────────── */

static int
test_full_pipeline(void)
{
    printf("[test] Full pipeline (KEM → inject → extract)... ");

    /* ── Step 1: Hybrid KEM handshake ── */
    uint8_t pk_init[QRNSP_CRYPTO_PUBLICKEYBYTES];
    uint8_t sk_init[QRNSP_CRYPTO_SECRETKEYBYTES];
    uint8_t pk_resp[QRNSP_CRYPTO_PUBLICKEYBYTES];
    uint8_t sk_resp[QRNSP_CRYPTO_SECRETKEYBYTES];

    if (hybrid_keypair_generate(pk_init, sk_init) != 0) {
        printf("FAIL (init keygen)\n"); return -1;
    }
    if (hybrid_keypair_generate(pk_resp, sk_resp) != 0) {
        printf("FAIL (resp keygen)\n"); return -1;
    }

    /* Initiator encapsulates to responder's public key */
    uint8_t ct[QRNSP_CRYPTO_CIPHERTEXTBYTES];
    uint8_t ss_init[32], ss_resp[32];

    if (hybrid_encapsulate(ct, ss_init, pk_resp) != 0) {
        printf("FAIL (encaps)\n"); return -1;
    }
    if (hybrid_decapsulate(ss_resp, ct, sk_resp, pk_resp) != 0) {
        printf("FAIL (decaps)\n"); return -1;
    }

    if (memcmp(ss_init, ss_resp, 32) != 0) {
        printf("FAIL (KEM ss mismatch)\n"); return -1;
    }

    /* ── Step 2: Initialize stego sessions ── */
    stego_session_t sess_init, sess_resp;
    stego_session_init(&sess_init, ss_init, 0); /* Initiator */
    stego_session_init(&sess_resp, ss_resp, 1); /* Responder */

    /* Verify magic markers match */
    if (memcmp(sess_init.magic, sess_resp.magic, 2) != 0) {
        printf("FAIL (magic mismatch)\n"); return -1;
    }

    /* ── Step 3: Build fake QUIC packet with PADDING ── */
    uint8_t pkt[2048];
    size_t pkt_len = build_fake_quic_initial(pkt, sizeof(pkt));

    /* Check available capacity */
    size_t capacity = stego_max_payload(pkt, pkt_len);
    printf("\n    padding capacity: %zu bytes\n    ", capacity);

    /* ── Step 4: Inject payload ── */
    const char *secret_msg = "Freedom is the oxygen of the soul. - Moshe Dayan";
    size_t msg_len = strlen(secret_msg);

    stego_result_t res = stego_inject(&sess_init, pkt, pkt_len,
                                      (const uint8_t *)secret_msg, msg_len);
    if (res != STEGO_OK) {
        printf("FAIL (inject: %d)\n", res); return -1;
    }

    /* ── Step 5: Probe (fast check without decryption) ── */
    if (!stego_probe(&sess_resp, pkt, pkt_len)) {
        printf("FAIL (probe missed injected packet)\n"); return -1;
    }

    /* ── Step 6: Extract payload ── */
    uint8_t extracted[2048];
    size_t extracted_len = 0;

    res = stego_extract(&sess_resp, pkt, pkt_len,
                        extracted, sizeof(extracted), &extracted_len);
    if (res != STEGO_OK) {
        printf("FAIL (extract: %d)\n", res); return -1;
    }

    if (extracted_len != msg_len || memcmp(extracted, secret_msg, msg_len) != 0) {
        printf("FAIL (payload mismatch)\n");
        hexdump("expected", (const uint8_t *)secret_msg, msg_len);
        hexdump("got     ", extracted, extracted_len);
        return -1;
    }

    printf("OK\n");
    printf("    injected: \"%.*s\" (%zu bytes)\n", (int)msg_len, secret_msg, msg_len);
    printf("    extracted: \"%.*s\" (%zu bytes)\n", (int)extracted_len, extracted, extracted_len);
    printf("    stego overhead: %d bytes\n", STEGO_OVERHEAD);
    printf("    tx_packets: %lu, tx_bytes: %lu\n",
           sess_init.tx_packets, sess_init.tx_bytes);

    stego_session_destroy(&sess_init);
    stego_session_destroy(&sess_resp);

    return 0;
}

/* ─────────────────────────────────────────────
 * Test 3: Multi-message session (nonce advancement)
 * ───────────────────────────────────────────── */

static int
test_multi_message(void)
{
    printf("[test] Multi-message session (10 messages)... ");

    /* Quick KEM handshake */
    uint8_t pk[QRNSP_CRYPTO_PUBLICKEYBYTES], sk[QRNSP_CRYPTO_SECRETKEYBYTES];
    uint8_t ct_kem[QRNSP_CRYPTO_CIPHERTEXTBYTES];
    uint8_t ss_a[32], ss_b[32];

    hybrid_keypair_generate(pk, sk);
    hybrid_encapsulate(ct_kem, ss_a, pk);
    hybrid_decapsulate(ss_b, ct_kem, sk, pk);

    stego_session_t sa, sb;
    stego_session_init(&sa, ss_a, 0);
    stego_session_init(&sb, ss_b, 1);

    int ok = 1;
    for (int i = 0; i < 10; i++) {
        /* Fresh packet each time (PADDING gets consumed) */
        uint8_t pkt[2048];
        size_t pkt_len = build_fake_quic_initial(pkt, sizeof(pkt));

        char msg[64];
        int n = snprintf(msg, sizeof(msg), "Message #%d from inside", i);

        if (stego_inject(&sa, pkt, pkt_len, (const uint8_t *)msg, (size_t)n) != STEGO_OK) {
            printf("FAIL (inject #%d)\n", i);
            ok = 0; break;
        }

        uint8_t out[256];
        size_t out_len;
        if (stego_extract(&sb, pkt, pkt_len, out, sizeof(out), &out_len) != STEGO_OK) {
            printf("FAIL (extract #%d)\n", i);
            ok = 0; break;
        }

        if (out_len != (size_t)n || memcmp(out, msg, n) != 0) {
            printf("FAIL (mismatch #%d)\n", i);
            ok = 0; break;
        }
    }

    if (ok) {
        printf("OK (10/10 round-trips)\n");
        printf("    nonce_ctr: tx=%lu rx=%lu\n", sa.tx_nonce_ctr, sb.rx_nonce_ctr);
    }

    stego_session_destroy(&sa);
    stego_session_destroy(&sb);
    return ok ? 0 : -1;
}

/* ─────────────────────────────────────────────
 * Test 4: Uninjected packet returns MAGIC_MISMATCH (not error)
 * ───────────────────────────────────────────── */

static int
test_clean_packet(void)
{
    printf("[test] Clean packet probe returns no match... ");

    uint8_t ss[32] = {0x42};
    stego_session_t sess;
    stego_session_init(&sess, ss, 0);

    uint8_t pkt[2048];
    size_t pkt_len = build_fake_quic_initial(pkt, sizeof(pkt));

    /* Should not find any stego data */
    if (stego_probe(&sess, pkt, pkt_len)) {
        printf("FAIL (false positive on clean packet)\n");
        stego_session_destroy(&sess);
        return -1;
    }

    uint8_t out[256];
    size_t out_len;
    stego_result_t res = stego_extract(&sess, pkt, pkt_len,
                                       out, sizeof(out), &out_len);
    if (res != STEGO_ERR_MAGIC_MISMATCH) {
        printf("FAIL (expected MAGIC_MISMATCH, got %d)\n", res);
        stego_session_destroy(&sess);
        return -1;
    }

    printf("OK\n");
    stego_session_destroy(&sess);
    return 0;
}

/* ─────────────────────────────────────────────
 * Test 5: Tamper detection
 * ───────────────────────────────────────────── */

static int
test_tamper_detection(void)
{
    printf("[test] Tamper detection (bit flip in payload)... ");

    uint8_t ss[32];
    for (int i = 0; i < 32; i++) ss[i] = (uint8_t)(i * 7);

    stego_session_t sa, sb;
    stego_session_init(&sa, ss, 0);
    stego_session_init(&sb, ss, 1);

    uint8_t pkt[2048];
    size_t pkt_len = build_fake_quic_initial(pkt, sizeof(pkt));

    const char *msg = "sensitive data";
    stego_inject(&sa, pkt, pkt_len, (const uint8_t *)msg, strlen(msg));

    /* Flip a bit somewhere in the payload area */
    pkt[200] ^= 0x01;

    uint8_t out[256];
    size_t out_len;
    stego_result_t res = stego_extract(&sb, pkt, pkt_len,
                                       out, sizeof(out), &out_len);

    /* Should fail auth OR fail magic (depending on where the flip landed) */
    if (res == STEGO_OK) {
        printf("FAIL (accepted tampered packet!)\n");
        stego_session_destroy(&sa);
        stego_session_destroy(&sb);
        return -1;
    }

    printf("OK (rejected with code %d)\n", res);
    stego_session_destroy(&sa);
    stego_session_destroy(&sb);
    return 0;
}

/* ─────────────────────────────────────────────
 * Main
 * ───────────────────────────────────────────── */

int
main(void)
{
    printf("╔══════════════════════════════════════════════╗\n");
    printf("║  QR-NSP Module 3: Stego Pipeline Test Suite ║\n");
    printf("║  KEM → AES-GCM → PADDING Injection          ║\n");
    printf("╚══════════════════════════════════════════════╝\n\n");

    int failures = 0;

    failures += (test_aead_roundtrip() != 0);
    failures += (test_full_pipeline() != 0);
    failures += (test_multi_message() != 0);
    failures += (test_clean_packet() != 0);
    failures += (test_tamper_detection() != 0);

    printf("\n%s: %d test(s) failed\n",
           failures ? "FAILED" : "ALL PASSED", failures);

    return failures;
}

```
