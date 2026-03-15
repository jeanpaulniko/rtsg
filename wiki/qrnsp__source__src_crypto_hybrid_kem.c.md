---
title: "src/crypto/hybrid_kem.c"
nav_title: "hybrid_kem.c"
---

# `src/crypto/hybrid_kem.c`

```c
/*
 * QR-NSP Volcanic Edition — Hybrid KEM
 * SPDX-License-Identifier: AGPL-3.0-or-later
 * ML-KEM-1024 ⊕ X25519 — dual classical/quantum security
 *
 * Combiner: ss = SHA3-256(ss_mlkem || ss_x25519 || ct_mlkem || pk_x25519_peer)
 *
 * This follows the NIST SP 800-227 (draft) hybrid KEM approach:
 * both component KEMs must be broken to recover the shared secret.
 *
 * Wire format:
 *   Public key:  [ML-KEM pk (1568)] [X25519 pk (32)]  = 1600 bytes
 *   Secret key:  [ML-KEM sk (3168)] [X25519 sk (32)]  = 3200 bytes
 *   Ciphertext:  [ML-KEM ct (1568)] [X25519 pk (32)]  = 1600 bytes
 *   Shared secret: 32 bytes
 */

#include "mlkem_params.h"
#include <string.h>

/* ─────────────────────────────────────────────
 * X25519 — Curve25519 Diffie-Hellman
 *
 * Minimal implementation using radix-2^51 representation.
 * For production: use monocypher or libsodium.
 * This is a compact reference for zero-dependency compilation.
 * ───────────────────────────────────────────── */

#define X25519_BYTES 32

typedef int64_t fe25519[5]; /* Radix 2^51 representation */

static const int64_t reduce_mask_51 = (1LL << 51) - 1;

/* a]  = 121665 (constant for curve equation) */
static const int64_t a24 = 121665;

static inline uint64_t
fe_load64(const uint8_t *b)
{
    return (uint64_t)b[0]       | ((uint64_t)b[1] << 8)  | ((uint64_t)b[2] << 16) |
           ((uint64_t)b[3] << 24) | ((uint64_t)b[4] << 32) | ((uint64_t)b[5] << 40) |
           ((uint64_t)b[6] << 48) | ((uint64_t)b[7] << 56);
}

static void
fe_frombytes(fe25519 h, const uint8_t s[32])
{
    uint64_t v0 = fe_load64(s);
    uint64_t v1 = fe_load64(s + 6);
    uint64_t v2 = fe_load64(s + 12);
    uint64_t v3 = fe_load64(s + 19);
    uint64_t v4 = fe_load64(s + 24);

    h[0] = (int64_t)(v0 & (uint64_t)reduce_mask_51);
    h[1] = (int64_t)((v1 >> 3) & (uint64_t)reduce_mask_51);
    h[2] = (int64_t)((v2 >> 6) & (uint64_t)reduce_mask_51);
    h[3] = (int64_t)((v3 >> 1) & (uint64_t)reduce_mask_51);
    h[4] = (int64_t)((v4 >> 12) & (uint64_t)reduce_mask_51);
}

static void
fe_tobytes(uint8_t s[32], const fe25519 h)
{
    int64_t t[5];
    memcpy(t, h, sizeof(t));

    /* Reduce */
    for (int i = 0; i < 5; i++) {
        int64_t c = t[i] >> 51;
        t[i] &= reduce_mask_51;
        t[(i + 1) % 5] += c * (i == 4 ? 19 : 1);
    }
    /* Final reduction */
    int64_t c = t[0] >> 51;
    t[0] &= reduce_mask_51;
    t[1] += c;

    /* Serialize as little-endian 256-bit integer */
    uint64_t u = (uint64_t)t[0] | ((uint64_t)t[1] << 51);
    for (int i = 0; i < 8; i++) s[i] = (uint8_t)(u >> (8 * i));
    u = ((uint64_t)t[1] >> 13) | ((uint64_t)t[2] << 38);
    for (int i = 0; i < 8; i++) s[8 + i] = (uint8_t)(u >> (8 * i));
    u = ((uint64_t)t[2] >> 26) | ((uint64_t)t[3] << 25);
    for (int i = 0; i < 8; i++) s[16 + i] = (uint8_t)(u >> (8 * i));
    u = ((uint64_t)t[3] >> 39) | ((uint64_t)t[4] << 12);
    for (int i = 0; i < 8; i++) s[24 + i] = (uint8_t)(u >> (8 * i));
    s[31] &= 0x7F; /* Clear top bit */
}

static void fe_add(fe25519 h, const fe25519 f, const fe25519 g)
{ for (int i = 0; i < 5; i++) h[i] = f[i] + g[i]; }

static void fe_sub(fe25519 h, const fe25519 f, const fe25519 g)
{ for (int i = 0; i < 5; i++) h[i] = f[i] - g[i]; }

static void
fe_mul(fe25519 h, const fe25519 f, const fe25519 g)
{
    /* Schoolbook multiplication with lazy reduction */
    __int128 r[5] = {0};
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            int idx = i + j;
            __int128 prod = (__int128)f[i] * g[j];
            if (idx >= 5) {
                r[idx - 5] += prod * 19;
            } else {
                r[idx] += prod;
            }
        }
    }
    /* Carry propagation */
    for (int i = 0; i < 5; i++) {
        __int128 c = r[i] >> 51;
        h[i] = (int64_t)(r[i] & reduce_mask_51);
        if (i < 4) r[i + 1] += c;
        else h[0] += (int64_t)c * 19;
    }
}

static void
fe_sq(fe25519 h, const fe25519 f)
{
    fe_mul(h, f, f);
}

static void
fe_mul_scalar(fe25519 h, const fe25519 f, int64_t s)
{
    for (int i = 0; i < 5; i++)
        h[i] = f[i] * s;
    /* Carry */
    for (int i = 0; i < 4; i++) {
        h[i + 1] += h[i] >> 51;
        h[i] &= reduce_mask_51;
    }
    h[0] += (h[4] >> 51) * 19;
    h[4] &= reduce_mask_51;
}

/* Inversion via Fermat: a^(p-2) mod p where p = 2^255 - 19 */
static void
fe_invert(fe25519 out, const fe25519 z)
{
    fe25519 t0, t1, t2, t3;
    int i;

    fe_sq(t0, z);
    fe_sq(t1, t0);
    fe_sq(t1, t1);
    fe_mul(t1, z, t1);
    fe_mul(t0, t0, t1);
    fe_sq(t2, t0);
    fe_mul(t1, t1, t2);
    fe_sq(t2, t1);
    for (i = 1; i < 5; i++) fe_sq(t2, t2);
    fe_mul(t1, t2, t1);
    fe_sq(t2, t1);
    for (i = 1; i < 10; i++) fe_sq(t2, t2);
    fe_mul(t2, t2, t1);
    fe_sq(t3, t2);
    for (i = 1; i < 20; i++) fe_sq(t3, t3);
    fe_mul(t2, t3, t2);
    fe_sq(t2, t2);
    for (i = 1; i < 10; i++) fe_sq(t2, t2);
    fe_mul(t1, t2, t1);
    fe_sq(t2, t1);
    for (i = 1; i < 50; i++) fe_sq(t2, t2);
    fe_mul(t2, t2, t1);
    fe_sq(t3, t2);
    for (i = 1; i < 100; i++) fe_sq(t3, t3);
    fe_mul(t2, t3, t2);
    fe_sq(t2, t2);
    for (i = 1; i < 50; i++) fe_sq(t2, t2);
    fe_mul(t1, t2, t1);
    fe_sq(t1, t1);
    for (i = 1; i < 5; i++) fe_sq(t1, t1);
    fe_mul(out, t1, t0);
}

/*
 * X25519 Montgomery ladder
 * Constant-time scalar multiplication on Curve25519
 */
static void
x25519_scalarmult(uint8_t out[32], const uint8_t scalar[32], const uint8_t point[32])
{
    uint8_t e[32];
    memcpy(e, scalar, 32);
    e[0]  &= 248;
    e[31] &= 127;
    e[31] |= 64;

    fe25519 x1, x2, z2, x3, z3, tmp0, tmp1;
    fe_frombytes(x1, point);

    /* x2 = 1, z2 = 0, x3 = x1, z3 = 1 */
    memset(x2, 0, sizeof(fe25519)); x2[0] = 1;
    memset(z2, 0, sizeof(fe25519));
    memcpy(x3, x1, sizeof(fe25519));
    memset(z3, 0, sizeof(fe25519)); z3[0] = 1;

    int swap = 0;

    for (int pos = 254; pos >= 0; pos--) {
        int b = (e[pos / 8] >> (pos & 7)) & 1;
        swap ^= b;

        /* Constant-time conditional swap */
        for (int i = 0; i < 5; i++) {
            int64_t mask = -(int64_t)swap;
            int64_t d;
            d = mask & (x2[i] ^ x3[i]); x2[i] ^= d; x3[i] ^= d;
            d = mask & (z2[i] ^ z3[i]); z2[i] ^= d; z3[i] ^= d;
        }
        swap = b;

        /* Montgomery ladder step */
        fe25519 A, AA, B, BB, E, C, D, DA, CB;
        fe_add(A, x2, z2);
        fe_sq(AA, A);
        fe_sub(B, x2, z2);
        fe_sq(BB, B);
        fe_sub(E, AA, BB);
        fe_add(C, x3, z3);
        fe_sub(D, x3, z3);
        fe_mul(DA, D, A);
        fe_mul(CB, C, B);

        fe_add(tmp0, DA, CB);
        fe_sq(x3, tmp0);

        fe_sub(tmp0, DA, CB);
        fe_sq(tmp1, tmp0);
        fe_mul(z3, x1, tmp1);

        fe_mul(x2, AA, BB);
        fe_mul_scalar(tmp0, E, a24);
        fe_add(tmp0, tmp0, AA);
        fe_mul(z2, E, tmp0);
    }

    /* Final swap */
    for (int i = 0; i < 5; i++) {
        int64_t mask = -(int64_t)swap;
        int64_t d;
        d = mask & (x2[i] ^ x3[i]); x2[i] ^= d; x3[i] ^= d;
        d = mask & (z2[i] ^ z3[i]); z2[i] ^= d; z3[i] ^= d;
    }

    /* out = x2 / z2 */
    fe_invert(z2, z2);
    fe_mul(x2, x2, z2);
    fe_tobytes(out, x2);
}

/* X25519 base point (9) */
static const uint8_t x25519_basepoint[32] = { 9 };

static void
x25519_keypair(uint8_t pk[32], uint8_t sk[32])
{
    /* sk is random; pk = sk * G */
    x25519_scalarmult(pk, sk, x25519_basepoint);
}

/* ═════════════════════════════════════════════
 * Hybrid KEM: ML-KEM-1024 ⊕ X25519
 * ═════════════════════════════════════════════ */

#define HYBRID_PUBLICKEYBYTES  (MLKEM_PUBLICKEYBYTES + X25519_BYTES)   /* 1600 */
#define HYBRID_SECRETKEYBYTES  (MLKEM_SECRETKEYBYTES + X25519_BYTES)   /* 3200 */
#define HYBRID_CIPHERTEXTBYTES (MLKEM_CIPHERTEXTBYTES + X25519_BYTES)  /* 1600 */
#define HYBRID_SSBYTES         32

/* Defined in kem.c */
extern int randombytes(uint8_t *out, size_t len);

int
hybrid_keypair_generate(uint8_t pk[HYBRID_PUBLICKEYBYTES],
                        uint8_t sk[HYBRID_SECRETKEYBYTES])
{
    /* ML-KEM keypair */
    mlkem_keypair kp;
    if (mlkem_keypair_generate(&kp) != 0) return -1;
    memcpy(pk, kp.pk, MLKEM_PUBLICKEYBYTES);
    memcpy(sk, kp.sk, MLKEM_SECRETKEYBYTES);

    /* X25519 keypair */
    uint8_t x_sk[32];
    if (randombytes(x_sk, 32) != 0) return -1;
    uint8_t x_pk[32];
    x25519_keypair(x_pk, x_sk);

    memcpy(pk + MLKEM_PUBLICKEYBYTES, x_pk, 32);
    memcpy(sk + MLKEM_SECRETKEYBYTES, x_sk, 32);

    memset(&kp, 0, sizeof(kp));
    memset(x_sk, 0, 32);
    return 0;
}

int
hybrid_encapsulate(uint8_t ct[HYBRID_CIPHERTEXTBYTES],
                   uint8_t ss[HYBRID_SSBYTES],
                   const uint8_t pk[HYBRID_PUBLICKEYBYTES])
{
    /* ML-KEM encapsulate */
    uint8_t ss_mlkem[MLKEM_SSBYTES];
    if (mlkem_encapsulate(ct, ss_mlkem, pk) != 0) return -1;

    /* X25519 ephemeral DH */
    uint8_t x_ek[32]; /* ephemeral secret */
    if (randombytes(x_ek, 32) != 0) return -1;

    uint8_t x_epk[32]; /* ephemeral public */
    x25519_keypair(x_epk, x_ek);

    uint8_t ss_x25519[32];
    x25519_scalarmult(ss_x25519, x_ek, pk + MLKEM_PUBLICKEYBYTES);

    /* ct = [mlkem_ct || x25519_epk] */
    memcpy(ct + MLKEM_CIPHERTEXTBYTES, x_epk, 32);

    /* Combine: ss = SHA3-256(ss_mlkem || ss_x25519 || mlkem_ct || x25519_peer_pk) */
    uint8_t combiner_input[MLKEM_SSBYTES + 32 + MLKEM_CIPHERTEXTBYTES + 32];
    uint8_t *p = combiner_input;
    memcpy(p, ss_mlkem, MLKEM_SSBYTES); p += MLKEM_SSBYTES;
    memcpy(p, ss_x25519, 32);           p += 32;
    memcpy(p, ct, MLKEM_CIPHERTEXTBYTES); p += MLKEM_CIPHERTEXTBYTES;
    memcpy(p, pk + MLKEM_PUBLICKEYBYTES, 32);

    mlkem_hash_h(ss, combiner_input, sizeof(combiner_input));

    /* Zeroize */
    memset(x_ek, 0, 32);
    memset(ss_mlkem, 0, sizeof(ss_mlkem));
    memset(ss_x25519, 0, sizeof(ss_x25519));
    memset(combiner_input, 0, sizeof(combiner_input));

    return 0;
}

int
hybrid_decapsulate(uint8_t ss[HYBRID_SSBYTES],
                   const uint8_t ct[HYBRID_CIPHERTEXTBYTES],
                   const uint8_t sk[HYBRID_SECRETKEYBYTES],
                   const uint8_t pk[HYBRID_PUBLICKEYBYTES])
{
    /* ML-KEM decapsulate */
    uint8_t ss_mlkem[MLKEM_SSBYTES];
    mlkem_decapsulate(ss_mlkem, ct, sk);

    /* X25519 DH with ephemeral public key from ct */
    const uint8_t *x_epk = ct + MLKEM_CIPHERTEXTBYTES;
    const uint8_t *x_sk  = sk + MLKEM_SECRETKEYBYTES;

    uint8_t ss_x25519[32];
    x25519_scalarmult(ss_x25519, x_sk, x_epk);

    /* Same combiner as encapsulate */
    uint8_t combiner_input[MLKEM_SSBYTES + 32 + MLKEM_CIPHERTEXTBYTES + 32];
    uint8_t *p = combiner_input;
    memcpy(p, ss_mlkem, MLKEM_SSBYTES); p += MLKEM_SSBYTES;
    memcpy(p, ss_x25519, 32);           p += 32;
    memcpy(p, ct, MLKEM_CIPHERTEXTBYTES); p += MLKEM_CIPHERTEXTBYTES;
    memcpy(p, pk + MLKEM_PUBLICKEYBYTES, 32);

    mlkem_hash_h(ss, combiner_input, sizeof(combiner_input));

    memset(ss_mlkem, 0, sizeof(ss_mlkem));
    memset(ss_x25519, 0, sizeof(ss_x25519));
    memset(combiner_input, 0, sizeof(combiner_input));

    return 0;
}

```
