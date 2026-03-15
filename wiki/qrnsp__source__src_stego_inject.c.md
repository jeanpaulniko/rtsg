---
title: "src/stego/inject.c"
nav_title: "inject.c"
---

# `src/stego/inject.c`

```c
/*
 * QR-NSP Volcanic Edition — Steganographic Injection Engine
 * Module 3: QUIC PADDING frame replacement
 *
 * This is where steganography meets post-quantum crypto.
 * XDP captures the packet → we find PADDING → encrypt payload → write in-place.
 *
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include "qrnsp_stego.h"
#include "qrnsp_aead.h"
#include "mlkem_params.h"   /* For mlkem_hash_h (SHA3-256) */
#include <string.h>

/* ─────────────────────────────────────────────
 * Key Derivation from Shared Secret
 *
 * tx_key = SHA3-256(ss || role || "tx")
 * rx_key = SHA3-256(ss || role || "rx")
 * magic  = SHA3-256(ss || "magic")[0:2]
 *
 * Initiator (role=0): tx uses "init_tx", rx uses "init_rx"
 * Responder (role=1): tx/rx swapped so both sides agree
 * ───────────────────────────────────────────── */

static void
derive_key(uint8_t out[32], const uint8_t ss[32], const char *label)
{
    uint8_t buf[32 + 32]; /* ss || label (label < 32 bytes) */
    size_t llen = strlen(label);
    memcpy(buf, ss, 32);
    memcpy(buf + 32, label, llen);
    mlkem_hash_h(out, buf, 32 + llen);
    memset(buf, 0, sizeof(buf));
}

int
stego_session_init(stego_session_t *sess,
                   const uint8_t shared_secret[32],
                   int role)
{
    memset(sess, 0, sizeof(*sess));
    memcpy(sess->shared_secret, shared_secret, 32);

    if (role == 0) {
        /* Initiator */
        derive_key(sess->tx_key, shared_secret, "init_tx");
        derive_key(sess->rx_key, shared_secret, "init_rx");
    } else {
        /* Responder: swap tx/rx so both sides match */
        derive_key(sess->tx_key, shared_secret, "init_rx");
        derive_key(sess->rx_key, shared_secret, "init_tx");
    }

    /* Magic marker: session-specific, not a static pattern */
    uint8_t magic_full[32];
    derive_key(magic_full, shared_secret, "magic");
    sess->magic[0] = magic_full[0];
    sess->magic[1] = magic_full[1];
    memset(magic_full, 0, sizeof(magic_full));

    sess->tx_nonce_ctr = 0;
    sess->rx_nonce_ctr = 0;
    sess->state = STEGO_STATE_READY;

    return 0;
}

void
stego_session_destroy(stego_session_t *sess)
{
    memset(sess, 0, sizeof(*sess));
    sess->state = STEGO_STATE_IDLE;
}

/* ─────────────────────────────────────────────
 * Nonce Construction
 *
 * 12-byte nonce = [4 bytes: fixed context] [8 bytes: counter]
 * Counter is monotonically increasing, never reused.
 * ───────────────────────────────────────────── */

static void
build_nonce(uint8_t nonce[12], uint64_t counter, int is_tx)
{
    /* First 4 bytes: direction tag to separate tx/rx nonce spaces */
    nonce[0] = is_tx ? 0x01 : 0x02;
    nonce[1] = 0x00;
    nonce[2] = 0x00;
    nonce[3] = 0x00;

    /* Last 8 bytes: big-endian counter */
    for (int i = 0; i < 8; i++)
        nonce[4 + i] = (uint8_t)(counter >> (56 - 8 * i));
}

/* ─────────────────────────────────────────────
 * PADDING Region Scanner
 *
 * Finds contiguous 0x00 byte runs in the QUIC payload.
 *
 * For Initial packets (unencrypted): PADDING follows CRYPTO frames
 * and pads to ≥1200 bytes (RFC 9000 §14.1).
 *
 * For 1-RTT packets (after decryption by QUIC stack): PADDING can
 * appear anywhere in the frame sequence.
 *
 * We scan from the end of the packet backward — PADDING is
 * typically trailing. This also avoids false positives from
 * the QUIC header.
 * ───────────────────────────────────────────── */

typedef struct {
    size_t offset;   /* Byte offset of PADDING region start */
    size_t length;   /* Length of contiguous 0x00 bytes     */
} padding_region_t;

/*
 * Find the largest PADDING region in the packet.
 * Scans for runs of 0x00 bytes, returns the longest one.
 *
 * skip_header: bytes to skip at start (QUIC header estimate)
 */
static int
find_padding_region(const uint8_t *pkt, size_t pkt_len,
                    size_t skip_header, padding_region_t *region)
{
    if (pkt_len <= skip_header)
        return -1;

    size_t best_off = 0, best_len = 0;
    size_t cur_off = 0, cur_len = 0;
    int in_run = 0;

    for (size_t i = skip_header; i < pkt_len; i++) {
        if (pkt[i] == 0x00) {
            if (!in_run) {
                cur_off = i;
                cur_len = 0;
                in_run = 1;
            }
            cur_len++;
        } else {
            if (in_run && cur_len > best_len) {
                best_off = cur_off;
                best_len = cur_len;
            }
            in_run = 0;
        }
    }
    /* Check trailing run */
    if (in_run && cur_len > best_len) {
        best_off = cur_off;
        best_len = cur_len;
    }

    if (best_len < STEGO_MIN_PAD_REGION)
        return -1;

    region->offset = best_off;
    region->length = best_len;
    return 0;
}

/*
 * Estimate QUIC header size for the padding scanner.
 * Long header: ≥7 bytes (1 + 4 version + DCID len + DCID + ...)
 * Short header: ≥1 byte (1 + DCID)
 *
 * We use a conservative minimum to avoid scanning into headers.
 */
static size_t
estimate_quic_header(const uint8_t *pkt, size_t pkt_len)
{
    if (pkt_len < 1) return pkt_len;

    if (pkt[0] & 0x80) {
        /* Long header: 1 + 4(ver) + 1(dcid_len) + dcid + 1(scid_len) + scid + ... */
        if (pkt_len < 7) return pkt_len;
        size_t dcid_len = pkt[5];
        size_t min = 7 + dcid_len;
        if (min + 1 < pkt_len) {
            size_t scid_len = pkt[6 + dcid_len];
            min += 1 + scid_len;
        }
        /* Add token/length fields for Initial packets */
        return (min < pkt_len) ? min + 4 : pkt_len; /* +4 conservative */
    } else {
        /* Short header: 1 byte flags + DCID (typically 0-20 bytes) */
        /* We don't know DCID len without connection state, use conservative 21 */
        return (pkt_len > 21) ? 21 : pkt_len;
    }
}

/* ═════════════════════════════════════════════
 * Injection (TX path)
 *
 * Stego frame layout within PADDING region:
 *   [MAGIC:2][LEN:2][NONCE:12][CIPHERTEXT:N][TAG:16][0x00:remaining]
 * ═════════════════════════════════════════════ */

stego_result_t
stego_inject(stego_session_t *sess,
             uint8_t *pkt, size_t pkt_len,
             const uint8_t *payload, size_t pay_len)
{
    if (sess->state != STEGO_STATE_READY)
        return STEGO_ERR_NO_SESSION;

    if (pay_len == 0 || pay_len > STEGO_MAX_PAYLOAD)
        return STEGO_ERR_PAYLOAD_TOO_BIG;

    /* Find PADDING region */
    padding_region_t pad;
    size_t hdr_skip = estimate_quic_header(pkt, pkt_len);

    if (find_padding_region(pkt, pkt_len, hdr_skip, &pad) != 0) {
        sess->padding_too_small++;
        return STEGO_ERR_NO_PADDING;
    }

    sess->padding_regions_seen++;

    /* Check if payload + overhead fits in PADDING region */
    size_t needed = STEGO_OVERHEAD + pay_len;
    if (needed > pad.length) {
        sess->padding_too_small++;
        return STEGO_ERR_PAD_TOO_SMALL;
    }

    /* Build nonce */
    uint8_t nonce[12];
    build_nonce(nonce, sess->tx_nonce_ctr, 1);

    /* Encrypt payload */
    uint8_t ct[STEGO_MAX_PAYLOAD];
    uint8_t tag[AEAD_TAG_BYTES];

    /*
     * AAD = packet header bytes (integrity-bound to this specific packet).
     * This prevents replay attacks: ciphertext is bound to the carrier.
     */
    const uint8_t *aad = pkt;
    size_t aadlen = hdr_skip;

    if (aead_encrypt(ct, tag, payload, pay_len, aad, aadlen, nonce,
                     sess->tx_key) != 0) {
        return STEGO_ERR_CRYPTO;
    }

    /* ── Write stego frame into PADDING region ── */
    uint8_t *dst = pkt + pad.offset;

    /* Magic (session-derived) */
    dst[0] = sess->magic[0];
    dst[1] = sess->magic[1];
    dst += STEGO_MAGIC_BYTES;

    /* Length (big-endian) */
    dst[0] = (uint8_t)(pay_len >> 8);
    dst[1] = (uint8_t)(pay_len & 0xFF);
    dst += STEGO_LEN_BYTES;

    /* Nonce */
    memcpy(dst, nonce, STEGO_NONCE_BYTES);
    dst += STEGO_NONCE_BYTES;

    /* Ciphertext */
    memcpy(dst, ct, pay_len);
    dst += pay_len;

    /* Authentication tag */
    memcpy(dst, tag, AEAD_TAG_BYTES);
    dst += AEAD_TAG_BYTES;

    /* Zero remaining padding (maintain padding appearance) */
    size_t written = needed;
    if (written < pad.length) {
        memset(pkt + pad.offset + written, 0x00, pad.length - written);
    }

    /* Update state */
    sess->tx_nonce_ctr++;
    sess->tx_bytes += pay_len;
    sess->tx_packets++;

    /* Zeroize intermediates */
    memset(ct, 0, pay_len);
    memset(tag, 0, sizeof(tag));

    return STEGO_OK;
}

/* ═════════════════════════════════════════════
 * Extraction (RX path)
 *
 * Scan for magic marker, then decrypt the stego frame.
 * ═════════════════════════════════════════════ */

/*
 * Scan packet for magic marker at the start of a zero-run.
 * Returns offset of magic, or -1 if not found.
 */
static int
find_magic(const uint8_t *pkt, size_t pkt_len,
           const uint8_t magic[2], size_t skip_header)
{
    if (pkt_len < skip_header + STEGO_OVERHEAD)
        return -1;

    /*
     * Scan for magic bytes. Since magic is session-derived (from ss),
     * false positives are ~1/65536 per position. We verify with AEAD
     * auth tag, so false positives are harmless.
     */
    for (size_t i = skip_header; i + STEGO_OVERHEAD <= pkt_len; i++) {
        if (pkt[i] == magic[0] && pkt[i + 1] == magic[1]) {
            /* Verify this looks like a stego frame: check length field sanity */
            uint16_t claimed_len = ((uint16_t)pkt[i + 2] << 8) | pkt[i + 3];
            if (claimed_len > 0 && claimed_len <= STEGO_MAX_PAYLOAD &&
                i + STEGO_OVERHEAD + claimed_len <= pkt_len) {
                return (int)i;
            }
        }
    }

    return -1;
}

stego_result_t
stego_extract(stego_session_t *sess,
              const uint8_t *pkt, size_t pkt_len,
              uint8_t *out, size_t out_cap,
              size_t *out_len)
{
    if (sess->state != STEGO_STATE_READY)
        return STEGO_ERR_NO_SESSION;

    *out_len = 0;
    size_t hdr_skip = estimate_quic_header(pkt, pkt_len);

    /* Find magic marker */
    int magic_off = find_magic(pkt, pkt_len, sess->magic, hdr_skip);
    if (magic_off < 0)
        return STEGO_ERR_MAGIC_MISMATCH;

    const uint8_t *src = pkt + magic_off;

    /* Parse length */
    uint16_t pay_len = ((uint16_t)src[2] << 8) | src[3];
    if (pay_len > out_cap)
        return STEGO_ERR_PAYLOAD_TOO_BIG;

    src += STEGO_MAGIC_BYTES + STEGO_LEN_BYTES;

    /* Extract nonce */
    uint8_t nonce[12];
    memcpy(nonce, src, STEGO_NONCE_BYTES);
    src += STEGO_NONCE_BYTES;

    /* Extract ciphertext */
    const uint8_t *ct = src;
    src += pay_len;

    /* Extract tag */
    uint8_t tag[AEAD_TAG_BYTES];
    memcpy(tag, src, AEAD_TAG_BYTES);

    /* AAD = packet header (same binding as injection) */
    const uint8_t *aad = pkt;
    size_t aadlen = hdr_skip;

    /* Decrypt and verify */
    if (aead_decrypt(out, ct, pay_len, tag, aad, aadlen, nonce,
                     sess->rx_key) != 0) {
        *out_len = 0;
        return STEGO_ERR_AUTH_FAIL;
    }

    /* Verify nonce monotonicity (prevent replay) */
    uint64_t received_ctr = 0;
    for (int i = 0; i < 8; i++)
        received_ctr |= ((uint64_t)nonce[4 + i]) << (56 - 8 * i);

    if (received_ctr < sess->rx_nonce_ctr) {
        memset(out, 0, pay_len);
        *out_len = 0;
        return STEGO_ERR_NONCE_REUSE;
    }
    sess->rx_nonce_ctr = received_ctr + 1;

    *out_len = pay_len;
    sess->rx_bytes += pay_len;
    sess->rx_packets++;

    return STEGO_OK;
}

/* ═════════════════════════════════════════════
 * Fast Probe (no decryption)
 * ═════════════════════════════════════════════ */

int
stego_probe(const stego_session_t *sess,
            const uint8_t *pkt, size_t pkt_len)
{
    size_t hdr_skip = estimate_quic_header(pkt, pkt_len);
    return find_magic(pkt, pkt_len, sess->magic, hdr_skip) >= 0 ? 1 : 0;
}

/* ═════════════════════════════════════════════
 * Capacity Query
 * ═════════════════════════════════════════════ */

size_t
stego_max_payload(const uint8_t *pkt, size_t pkt_len)
{
    padding_region_t pad;
    size_t hdr_skip = estimate_quic_header(pkt, pkt_len);

    if (find_padding_region(pkt, pkt_len, hdr_skip, &pad) != 0)
        return 0;

    if (pad.length <= STEGO_OVERHEAD)
        return 0;

    size_t max = pad.length - STEGO_OVERHEAD;
    return (max > STEGO_MAX_PAYLOAD) ? STEGO_MAX_PAYLOAD : max;
}

```
