---
title: "include/qrnsp_aead.h"
nav_title: "qrnsp_aead.h"
---

# `include/qrnsp_aead.h`

```c
/*
 * QR-NSP Volcanic Edition — AES-256-GCM
 * Authenticated Encryption with Associated Data
 * Module 3 dependency: encrypts steganographic payloads before injection.
 *
 * AES-256 is considered quantum-safe for symmetric use (Grover's gives
 * effective 128-bit security, still intractable).
 *
 * This is a compact reference implementation. For production on x86:
 *   - Use AES-NI intrinsics (_mm_aesenc_si128 etc.)
 *   - Use PCLMULQDQ for GF(2^128) multiplication (GHASH)
 *   - Or use libsodium's crypto_aead_aes256gcm_*
 *
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#ifndef QRNSP_AEAD_H
#define QRNSP_AEAD_H

#include <stdint.h>
#include <stddef.h>

#define AEAD_KEY_BYTES   32
#define AEAD_NONCE_BYTES 12
#define AEAD_TAG_BYTES   16

/*
 * Encrypt and authenticate.
 *
 * ct:    ciphertext output (plaintext_len bytes)
 * tag:   authentication tag output (16 bytes)
 * pt:    plaintext input
 * ptlen: plaintext length
 * aad:   additional authenticated data (integrity-only, not encrypted)
 * aadlen: AAD length
 * nonce: 12-byte nonce (MUST be unique per key)
 * key:   32-byte key (from hybrid KEM shared secret)
 *
 * Returns 0 on success.
 */
int aead_encrypt(uint8_t *ct, uint8_t tag[AEAD_TAG_BYTES],
                 const uint8_t *pt, size_t ptlen,
                 const uint8_t *aad, size_t aadlen,
                 const uint8_t nonce[AEAD_NONCE_BYTES],
                 const uint8_t key[AEAD_KEY_BYTES]);

/*
 * Decrypt and verify.
 *
 * Returns 0 on success, -1 if authentication fails.
 * On failure, pt buffer is zeroed (no partial plaintext leak).
 */
int aead_decrypt(uint8_t *pt,
                 const uint8_t *ct, size_t ctlen,
                 const uint8_t tag[AEAD_TAG_BYTES],
                 const uint8_t *aad, size_t aadlen,
                 const uint8_t nonce[AEAD_NONCE_BYTES],
                 const uint8_t key[AEAD_KEY_BYTES]);

#endif /* QRNSP_AEAD_H */

```
