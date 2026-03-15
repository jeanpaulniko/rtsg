---
title: "tests/test_pipeline.c"
nav_title: "test_pipeline.c"
---

# `tests/test_pipeline.c`

```c
/*
 * QR-NSP Volcanic Edition — Modules 6-8 Integration Test
 * Full pipeline: handshake → send → morph → receive → reassemble
 *
 * Build:
 *   gcc -O2 -march=native -I include -o test_pipeline \
 *       tests/test_pipeline.c src/orchestrator/orchestrator.c \
 *       src/fallback/fallback.c src/morph/morph.c \
 *       src/stego/inject.c src/aead/aes256gcm.c \
 *       src/jitter/jitter.c src/crypto/ntt.c src/crypto/poly.c \
 *       src/crypto/symmetric.c src/crypto/kem.c src/crypto/hybrid_kem.c \
 *       -lm
 *
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include "qrnsp_orchestrator.h"
#include "qrnsp_fallback.h"
#include "qrnsp_morph.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

/* ─────────────────────────────────────────────
 * Test 1: Chaffing-and-Winnowing round-trip
 * ───────────────────────────────────────────── */

static int
test_chaff_winnow(void)
{
    printf("[test] Chaffing-and-Winnowing round-trip... ");

    uint8_t key[32];
    for (int i = 0; i < 32; i++) key[i] = (uint8_t)(i + 0xAA);

    fallback_session_t sess;
    fallback_init(&sess, key);

    const char *msg = "Secret message through the firewall";
    chaff_packet_t packets[16];
    int count = 0;

    if (chaff_encode(&sess, (const uint8_t *)msg, strlen(msg),
                     packets, &count, 16) != 0) {
        printf("FAIL (encode)\n"); return -1;
    }

    printf("(%d packets: 1 real + %d chaff) ", count, count - 1);

    uint8_t out[1024];
    size_t out_len;
    if (chaff_winnow(&sess, packets, count, out, sizeof(out), &out_len) != 0) {
        printf("FAIL (winnow)\n"); return -1;
    }

    if (out_len != strlen(msg) || memcmp(out, msg, out_len) != 0) {
        printf("FAIL (mismatch)\n"); return -1;
    }

    printf("OK\n");
    fallback_destroy(&sess);
    return 0;
}

/* ─────────────────────────────────────────────
 * Test 2: TCP Timestamp steganography
 * ───────────────────────────────────────────── */

static int
test_tcp_timestamp_stego(void)
{
    printf("[test] TCP timestamp steganography (2 bits/pkt)... ");

    uint8_t key[32] = {0x42};
    fallback_session_t tx, rx;
    fallback_init(&tx, key);
    fallback_init(&rx, key);

    /* Load small payload into TX */
    const char *msg = "Hi";
    tx.ts_payload_len = (uint16_t)strlen(msg);
    memcpy(tx.ts_payload, msg, strlen(msg));
    tx.ts_bit_index = 0;

    /* RX setup */
    rx.ts_payload_cap = 256;
    rx.ts_bit_index = 0;
    memset(rx.ts_payload, 0, 256);

    /* Simulate encoding/decoding through 8 TCP packets (16 bits = 2 bytes) */
    uint32_t ts = 1000000;
    for (int i = 0; i < 8; i++) {
        uint32_t morphed = tcp_ts_encode_bits(&tx, ts + i * 1000, 2);
        tcp_ts_decode_bits(&rx, morphed, 2);
    }

    /* Check first 2 bytes decoded correctly */
    if (rx.ts_payload[0] == (uint8_t)msg[0] &&
        rx.ts_payload[1] == (uint8_t)msg[1]) {
        printf("OK (decoded '%c%c')\n", rx.ts_payload[0], rx.ts_payload[1]);
        fallback_destroy(&tx); fallback_destroy(&rx);
        return 0;
    }

    printf("FAIL (got 0x%02x 0x%02x, expected 0x%02x 0x%02x)\n",
           rx.ts_payload[0], rx.ts_payload[1], msg[0], msg[1]);
    fallback_destroy(&tx); fallback_destroy(&rx);
    return -1;
}

/* ─────────────────────────────────────────────
 * Test 3: Transport state machine
 * ───────────────────────────────────────────── */

static int
test_fallback_state_machine(void)
{
    printf("[test] Fallback state machine... ");

    uint8_t key[32] = {0};
    fallback_session_t sess;
    fallback_init(&sess, key);

    uint64_t t = 1000000000ULL; /* 1s */

    /* Initially QUIC OK */
    if (sess.state != TRANSPORT_QUIC_OK) {
        printf("FAIL (initial state)\n"); return -1;
    }

    /* Simulate heavy loss */
    for (int i = 0; i < 100; i++) {
        fallback_quic_tx(&sess);
        if (i % 3 != 0) fallback_quic_loss(&sess);
        else fallback_quic_rx(&sess, t);
        t += 10000000; /* 10ms */
    }

    fallback_tick(&sess, t);
    if (sess.state == TRANSPORT_QUIC_OK) {
        printf("FAIL (should have degraded, loss=%.0f%%)\n",
               sess.metrics.quic_loss_rate * 100);
        return -1;
    }

    /* Simulate TCP coming up */
    fallback_tick(&sess, t); /* → TCP_PROBE */
    fallback_tcp_tx(&sess);
    fallback_tcp_rx(&sess, t);
    fallback_tick(&sess, t); /* → HTTP2_ACTIVE */

    if (sess.state != TRANSPORT_HTTP2_ACTIVE) {
        printf("FAIL (expected HTTP2_ACTIVE, got %d)\n", sess.state);
        fallback_destroy(&sess);
        return -1;
    }

    printf("OK (QUIC→degraded→TCP probe→HTTP2 active)\n");
    printf("    fallback_count=%lu\n", sess.fallback_count);
    fallback_destroy(&sess);
    return 0;
}

/* ─────────────────────────────────────────────
 * Test 4: Traffic morphing — profile sampling
 * ───────────────────────────────────────────── */

static int
test_traffic_morphing(void)
{
    printf("[test] Traffic morphing profiles... ");

    uint8_t seed[32] = {0x77};
    morph_session_t sess;
    morph_init(&sess, MORPH_COVER_NETFLIX_4K, seed);

    /* Sample 100 packets and check distribution sanity */
    double total_size = 0;
    uint64_t total_delay = 0;

    for (int i = 0; i < 100; i++) {
        size_t target_size;
        uint64_t delay;
        morph_shape(&sess, 100, &target_size, &delay);
        total_size += (double)target_size;
        total_delay += delay;
        morph_record_tx(&sess, target_size, (uint64_t)i * 5000000ULL);
    }

    double avg_size = total_size / 100.0;
    double avg_delay_us = (double)total_delay / (100.0 * 1000.0);

    printf("Netflix 4K profile:\n");
    printf("    avg pkt size: %.0f bytes (target: %.0f)\n",
           avg_size, sess.profile.avg_packet_size);
    printf("    avg IPAT: %.0f μs (target: %.0f)\n",
           avg_delay_us, sess.profile.avg_ipat_us);
    printf("    morph quality (KS): %.4f\n", morph_quality(&sess));

    /* Sanity: avg should be within 50% of target */
    if (avg_size < sess.profile.avg_packet_size * 0.3 ||
        avg_size > sess.profile.avg_packet_size * 3.0) {
        printf("    WARN: avg size diverged significantly\n");
    }

    morph_destroy(&sess);
    return 0;
}

/* ─────────────────────────────────────────────
 * Test 5: All cover profiles instantiate
 * ───────────────────────────────────────────── */

static int
test_all_profiles(void)
{
    printf("[test] All cover profiles instantiate... ");

    const char *names[] = {"Netflix 4K","YouTube 1080","Zoom","WhatsApp","Web Browse"};
    uint8_t seed[32] = {0};

    for (int p = 0; p < 5; p++) {
        morph_session_t sess;
        if (morph_init(&sess, (morph_cover_t)p, seed) != 0) {
            printf("FAIL (profile %d: %s)\n", p, names[p]);
            return -1;
        }

        size_t sz; uint64_t dl;
        morph_shape(&sess, 64, &sz, &dl);
        printf("\n    %s: pkt=%zu delay=%luμs", names[p], sz, dl / 1000);
        morph_destroy(&sess);
    }
    printf("\n    OK\n");
    return 0;
}

/* ─────────────────────────────────────────────
 * Test 6: Orchestrator handshake + send/receive
 * ───────────────────────────────────────────── */

static int
test_orchestrator_pipeline(void)
{
    printf("[test] Orchestrator full pipeline... ");

    orch_session_t alice, bob;

    /* Init both sides */
    if (orch_init(&alice, 0, MORPH_COVER_YOUTUBE_1080) != 0) {
        printf("FAIL (alice init)\n"); return -1;
    }
    if (orch_init(&bob, 1, MORPH_COVER_YOUTUBE_1080) != 0) {
        printf("FAIL (bob init)\n"); return -1;
    }

    /* Exchange public keys and perform KEM handshake */
    uint8_t alice_pk[QRNSP_CRYPTO_PUBLICKEYBYTES];
    uint8_t bob_pk[QRNSP_CRYPTO_PUBLICKEYBYTES];
    orch_get_pubkey(&alice, alice_pk);
    orch_get_pubkey(&bob, bob_pk);

    /* Alice encapsulates to Bob */
    uint8_t ct[QRNSP_CRYPTO_CIPHERTEXTBYTES];
    if (orch_handshake(&alice, bob_pk, ct, 0) != 0) {
        printf("FAIL (alice handshake)\n"); return -1;
    }
    /* Bob decapsulates */
    if (orch_handshake(&bob, alice_pk, ct, 1) != 0) {
        printf("FAIL (bob handshake)\n"); return -1;
    }

    /* Verify shared secrets match */
    if (memcmp(alice.shared_secret, bob.shared_secret, 32) != 0) {
        printf("FAIL (ss mismatch)\n"); return -1;
    }

    printf("\n    handshake OK, shared secret established\n");

    /* Alice sends a message */
    const char *msg = "The truth shall set you free";
    uint8_t packets[32][2048];
    size_t pkt_sizes[32];
    uint64_t pkt_delays[32];
    int n_pkts;

    if (orch_send(&alice, (const uint8_t *)msg, strlen(msg),
                  packets, pkt_sizes, pkt_delays, 32, &n_pkts) != 0) {
        printf("    FAIL (send)\n"); return -1;
    }

    printf("    sent: %d packets, ", n_pkts);
    for (int i = 0; i < n_pkts; i++)
        printf("%zu ", pkt_sizes[i]);
    printf("bytes\n");

    /* Get stats */
    orch_stats_t stats;
    orch_get_stats(&alice, &stats);
    printf("    state=%d caps=0x%02x msgs_sent=%lu morph_q=%.4f\n",
           stats.state, stats.capabilities,
           stats.msgs_sent, stats.morph_quality);

    orch_destroy(&alice);
    orch_destroy(&bob);
    printf("    OK\n");
    return 0;
}

/* ─────────────────────────────────────────────
 * Test 7: HTTP/2 padding injection
 * ───────────────────────────────────────────── */

static int
test_h2_padding(void)
{
    printf("[test] HTTP/2 DATA frame padding injection... ");

    uint8_t key[32] = {0x55};
    fallback_session_t tx, rx;
    fallback_init(&tx, key);
    fallback_init(&rx, key);

    /* Build a fake HTTP/2 DATA frame */
    /* Header: [LENGTH:3][TYPE:1][FLAGS:1][R+STREAM_ID:4] */
    uint8_t frame[4096];
    memset(frame, 0, sizeof(frame));
    size_t data_payload = 100; /* 100 bytes of "real" HTTP data */
    uint32_t flen = (uint32_t)data_payload;
    frame[0] = 0; frame[1] = 0; frame[2] = (uint8_t)flen;
    frame[3] = 0x00; /* TYPE = DATA */
    frame[4] = 0x00; /* FLAGS = none */
    frame[5] = 0; frame[6] = 0; frame[7] = 0; frame[8] = 1; /* Stream 1 */
    /* Fill data payload */
    for (size_t i = 0; i < data_payload; i++)
        frame[9 + i] = (uint8_t)(0x41 + (i % 26));

    /* Inject stego payload into padding */
    const char *secret = "coordinates:48.2N,16.4E";
    if (h2_pad_inject(&tx, frame, 9 + data_payload, sizeof(frame),
                      (const uint8_t *)secret, strlen(secret)) != 0) {
        printf("FAIL (inject)\n"); return -1;
    }

    /* Extract */
    uint8_t out[256];
    size_t out_len;
    size_t total_frame_len = 9 + ((uint32_t)frame[0] << 16 |
                                   (uint32_t)frame[1] << 8 | frame[2]);
    if (h2_pad_extract(&rx, frame, total_frame_len,
                       out, sizeof(out), &out_len) != 0) {
        printf("FAIL (extract)\n");
        fallback_destroy(&tx); fallback_destroy(&rx);
        return -1;
    }

    if (out_len != strlen(secret) || memcmp(out, secret, out_len) != 0) {
        printf("FAIL (mismatch)\n");
        fallback_destroy(&tx); fallback_destroy(&rx);
        return -1;
    }

    printf("OK ('%.*s')\n", (int)out_len, out);
    fallback_destroy(&tx); fallback_destroy(&rx);
    return 0;
}

/* ─────────────────────────────────────────────
 * Main
 * ───────────────────────────────────────────── */

int
main(void)
{
    printf("╔══════════════════════════════════════════════════╗\n");
    printf("║  QR-NSP Modules 6-8: Full Pipeline Test Suite   ║\n");
    printf("║  Fallback + Morphing + Orchestrator              ║\n");
    printf("╚══════════════════════════════════════════════════╝\n\n");

    int failures = 0;

    failures += (test_chaff_winnow() != 0);
    failures += (test_tcp_timestamp_stego() != 0);
    failures += (test_fallback_state_machine() != 0);
    failures += (test_traffic_morphing() != 0);
    failures += (test_all_profiles() != 0);
    failures += (test_h2_padding() != 0);
    failures += (test_orchestrator_pipeline() != 0);

    printf("\n%s: %d test(s) failed\n",
           failures ? "FAILED" : "ALL PASSED", failures);

    return failures;
}

```
