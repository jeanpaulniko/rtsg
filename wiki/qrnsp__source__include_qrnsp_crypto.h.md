---
title: "include/qrnsp_crypto.h"
nav_title: "qrnsp_crypto.h"
---

# `include/qrnsp_crypto.h`

```c
/*
 * QR-NSP Volcanic Edition — Public Crypto API
 * SPDX-License-Identifier: AGPL-3.0-or-later
 * Module 2: Hybrid PQC Key Encapsulation
 *
 * Usage:
 *   1. hybrid_keypair_generate() → (pk, sk)
 *   2. Sender: hybrid_encapsulate(ct, ss, pk) → ciphertext + shared secret
 *   3. Receiver: hybrid_decapsulate(ss, ct, sk, pk) → same shared secret
 *   4. Use ss as key for AES-256-GCM (Module 3)
 *
 * Wire sizes:
 *   Public key:   1600 bytes  (ML-KEM-1024: 1568, X25519: 32)
 *   Secret key:   3200 bytes  (ML-KEM-1024: 3168, X25519: 32)
 *   Ciphertext:   1600 bytes  (ML-KEM-1024: 1568, X25519: 32)
 *   Shared secret: 32 bytes
 */

#ifndef QRNSP_CRYPTO_H
#define QRNSP_CRYPTO_H

#include <stdint.h>
#include <stddef.h>

/* ─────────────────────────────────────────────
 * Size constants
 * ───────────────────────────────────────────── */

#define QRNSP_CRYPTO_PUBLICKEYBYTES   1600
#define QRNSP_CRYPTO_SECRETKEYBYTES   3200
#define QRNSP_CRYPTO_CIPHERTEXTBYTES  1600
#define QRNSP_CRYPTO_SSBYTES          32

/* ─────────────────────────────────────────────
 * Key generation
 *
 * Generates ML-KEM-1024 + X25519 hybrid keypair.
 * pk: public key (send to peer)
 * sk: secret key (keep private)
 *
 * Returns 0 on success, -1 on RNG failure.
 * ───────────────────────────────────────────── */

int hybrid_keypair_generate(uint8_t pk[QRNSP_CRYPTO_PUBLICKEYBYTES],
                            uint8_t sk[QRNSP_CRYPTO_SECRETKEYBYTES]);

/* ─────────────────────────────────────────────
 * Encapsulation (sender side)
 *
 * Given peer's public key, produces:
 *   ct: ciphertext (send to peer)
 *   ss: shared secret (use as AES-256-GCM key)
 *
 * Returns 0 on success.
 * ───────────────────────────────────────────── */

int hybrid_encapsulate(uint8_t ct[QRNSP_CRYPTO_CIPHERTEXTBYTES],
                       uint8_t ss[QRNSP_CRYPTO_SSBYTES],
                       const uint8_t pk[QRNSP_CRYPTO_PUBLICKEYBYTES]);

/* ─────────────────────────────────────────────
 * Decapsulation (receiver side)
 *
 * Given ciphertext and own keys, recovers shared secret.
 * With implicit rejection: always produces output (timing-safe).
 *
 * Returns 0 always (implicit rejection is silent).
 * ───────────────────────────────────────────── */

int hybrid_decapsulate(uint8_t ss[QRNSP_CRYPTO_SSBYTES],
                       const uint8_t ct[QRNSP_CRYPTO_CIPHERTEXTBYTES],
                       const uint8_t sk[QRNSP_CRYPTO_SECRETKEYBYTES],
                       const uint8_t pk[QRNSP_CRYPTO_PUBLICKEYBYTES]);

#endif /* QRNSP_CRYPTO_H */

```
