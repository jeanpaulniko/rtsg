---
title: "include/qrnsp_stego.h"
nav_title: "qrnsp_stego.h"
---

# `include/qrnsp_stego.h`

```c
/*
 * QR-NSP Volcanic Edition — Steganographic Injection Engine
 * Module 3: QUIC PADDING frame replacement
 *
 * Hides encrypted payloads inside QUIC PADDING frames.
 * PADDING frames (RFC 9000 §19.1) are 0x00 bytes that QUIC endpoints
 * add to meet minimum packet sizes. They're the perfect carrier:
 *   - Already present in most QUIC packets
 *   - Variable length (tens to hundreds of bytes)
 *   - Receivers discard them — our injection is invisible to the QUIC stack
 *   - Statistical profile: random after encryption ≈ random padding
 *
 * Wire format of an injected PADDING region:
 *   [MAGIC:2][LEN:2][NONCE:12][CIPHERTEXT:N][TAG:16][REMAINING_PAD:M]
 *
 *   MAGIC  = 2 bytes: session-derived marker (not static — derived from ss)
 *   LEN    = 2 bytes: payload length (big-endian)
 *   NONCE  = 12 bytes: AES-GCM nonce (counter-based)
 *   CT     = N bytes: encrypted payload
 *   TAG    = 16 bytes: AES-GCM authentication tag
 *   PAD    = remaining 0x00 bytes to fill original PADDING region
 *
 * Overhead per injection: 32 bytes (2+2+12+16)
 * Minimum PADDING region: 64 bytes → 32 bytes usable payload
 *
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#ifndef QRNSP_STEGO_H
#define QRNSP_STEGO_H

#include <stdint.h>
#include <stddef.h>

/* ─────────────────────────────────────────────
 * Constants
 * ───────────────────────────────────────────── */

#define STEGO_MAGIC_BYTES    2
#define STEGO_LEN_BYTES      2
#define STEGO_NONCE_BYTES    12
#define STEGO_TAG_BYTES      16
#define STEGO_OVERHEAD       (STEGO_MAGIC_BYTES + STEGO_LEN_BYTES + \
                              STEGO_NONCE_BYTES + STEGO_TAG_BYTES)  /* 32 */
#define STEGO_MIN_PAD_REGION 64   /* Minimum padding to attempt injection */
#define STEGO_MAX_PAYLOAD    1400 /* Maximum single-packet payload        */

/* Session states */
typedef enum {
    STEGO_STATE_IDLE,        /* No active session                    */
    STEGO_STATE_HANDSHAKE,   /* Hybrid KEM exchange in progress      */
    STEGO_STATE_READY,       /* Shared secret established, can inject*/
    STEGO_STATE_ERROR        /* Unrecoverable error                  */
} stego_state_t;

/* Direction */
typedef enum {
    STEGO_DIR_INJECT,        /* Writing payloads into PADDING        */
    STEGO_DIR_EXTRACT        /* Reading payloads from PADDING        */
} stego_dir_t;

/* ─────────────────────────────────────────────
 * Session Context
 *
 * One context per active covert channel.
 * Thread-safe: each session gets its own context.
 * ───────────────────────────────────────────── */

typedef struct {
    /* State */
    stego_state_t state;

    /* Cryptographic material (from hybrid KEM) */
    uint8_t  shared_secret[32]; /* From hybrid_encapsulate/decapsulate */
    uint8_t  tx_key[32];        /* Derived: SHA3-256(ss || "tx")       */
    uint8_t  rx_key[32];        /* Derived: SHA3-256(ss || "rx")       */
    uint8_t  magic[2];          /* Derived: SHA3-256(ss || "magic")[0:2]*/

    /* Nonce counters (monotonic, never reuse) */
    uint64_t tx_nonce_ctr;
    uint64_t rx_nonce_ctr;

    /* Statistics */
    uint64_t tx_bytes;           /* Total payload bytes injected       */
    uint64_t rx_bytes;           /* Total payload bytes extracted      */
    uint64_t tx_packets;         /* Packets with injected payload      */
    uint64_t rx_packets;         /* Packets with extracted payload     */
    uint64_t padding_regions_seen;
    uint64_t padding_too_small;  /* Regions too small to use           */
} stego_session_t;

/* ─────────────────────────────────────────────
 * Result codes
 * ───────────────────────────────────────────── */

typedef enum {
    STEGO_OK = 0,
    STEGO_ERR_NO_SESSION,     /* Session not initialized              */
    STEGO_ERR_NO_PADDING,     /* No padding region found in packet    */
    STEGO_ERR_PAD_TOO_SMALL,  /* Padding region too small for payload */
    STEGO_ERR_PAYLOAD_TOO_BIG,/* Payload exceeds available space      */
    STEGO_ERR_MAGIC_MISMATCH, /* Not a QR-NSP packet (wrong magic)    */
    STEGO_ERR_AUTH_FAIL,      /* AEAD authentication failed           */
    STEGO_ERR_NONCE_REUSE,    /* Nonce counter regression detected    */
    STEGO_ERR_CRYPTO,         /* Generic crypto error                 */
} stego_result_t;

/* ─────────────────────────────────────────────
 * API
 * ───────────────────────────────────────────── */

/*
 * Initialize session from hybrid KEM shared secret.
 * Derives tx_key, rx_key, and magic marker.
 * role: 0 = initiator (tx_key from "init_tx"), 1 = responder (keys swapped)
 */
int stego_session_init(stego_session_t *sess,
                       const uint8_t shared_secret[32],
                       int role);

/*
 * Inject payload into a QUIC packet's PADDING region.
 *
 * pkt:     mutable packet buffer (UDP payload from XDP ring)
 * pkt_len: packet length
 * payload: data to hide
 * pay_len: payload length
 *
 * Returns STEGO_OK on success. Packet is modified in-place.
 * The function finds the first PADDING region ≥ STEGO_MIN_PAD_REGION,
 * encrypts the payload, and writes the stego frame in place of the padding.
 */
stego_result_t stego_inject(stego_session_t *sess,
                            uint8_t *pkt, size_t pkt_len,
                            const uint8_t *payload, size_t pay_len);

/*
 * Extract payload from a QUIC packet's PADDING region.
 *
 * pkt:     packet buffer (read-only)
 * pkt_len: packet length
 * out:     output buffer for extracted payload
 * out_cap: output buffer capacity
 * out_len: actual extracted length (set on success)
 *
 * Returns STEGO_OK if a valid stego frame was found and decrypted.
 * Returns STEGO_ERR_MAGIC_MISMATCH if this isn't a QR-NSP packet (normal).
 */
stego_result_t stego_extract(stego_session_t *sess,
                             const uint8_t *pkt, size_t pkt_len,
                             uint8_t *out, size_t out_cap,
                             size_t *out_len);

/*
 * Probe: check if a packet contains QR-NSP steganographic data
 * without attempting full decryption. Fast path for filtering.
 *
 * Returns 1 if magic matches, 0 otherwise.
 */
int stego_probe(const stego_session_t *sess,
                const uint8_t *pkt, size_t pkt_len);

/*
 * Destroy session and zeroize all key material.
 */
void stego_session_destroy(stego_session_t *sess);

/*
 * Query maximum injectable payload for a given packet.
 * Returns 0 if no suitable padding region exists.
 */
size_t stego_max_payload(const uint8_t *pkt, size_t pkt_len);

#endif /* QRNSP_STEGO_H */

```
