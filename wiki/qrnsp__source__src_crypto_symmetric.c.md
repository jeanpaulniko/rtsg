---
title: "src/crypto/symmetric.c"
nav_title: "symmetric.c"
---

# `src/crypto/symmetric.c`

```c
/*
 * QR-NSP Volcanic Edition — Symmetric Primitives (SHA-3 / SHAKE)
 * SPDX-License-Identifier: AGPL-3.0-or-later
 * Wrapper for ML-KEM's hash function requirements (FIPS 203 §4.1)
 *
 * ML-KEM requires:
 *   H  = SHA3-256   (hash H)
 *   G  = SHA3-512   (hash G — key derivation)
 *   J  = SHAKE-256  (implicit rejection KDF)
 *   XOF = SHAKE-128 (matrix sampling)
 *   PRF = SHAKE-256 (pseudorandom function for CBD sampling)
 *
 * This file provides a minimal Keccak-f[1600] implementation.
 * For production: replace with optimized XKCP (Keccak Code Package)
 * or libcrypto. This exists for zero-dependency compilation.
 */

#include "mlkem_params.h"
#include <string.h>

/* ─────────────────────────────────────────────
 * Keccak-f[1600] State
 * ───────────────────────────────────────────── */

typedef struct {
    uint64_t s[25];
    unsigned int pos;
    unsigned int rate;   /* In bytes: 168 for SHAKE-128, 136 for SHAKE-256/SHA3-256, 72 for SHA3-512 */
} keccak_state;

/* ─────────────────────────────────────────────
 * Keccak-f[1600] Round Constants
 * ───────────────────────────────────────────── */

static const uint64_t keccak_rc[24] = {
    0x0000000000000001ULL, 0x0000000000008082ULL,
    0x800000000000808aULL, 0x8000000080008000ULL,
    0x000000000000808bULL, 0x0000000080000001ULL,
    0x8000000080008081ULL, 0x8000000000008009ULL,
    0x000000000000008aULL, 0x0000000000000088ULL,
    0x0000000080008009ULL, 0x000000008000000aULL,
    0x000000008000808bULL, 0x800000000000008bULL,
    0x8000000000008089ULL, 0x8000000000008003ULL,
    0x8000000000008002ULL, 0x8000000000000080ULL,
    0x000000000000800aULL, 0x800000008000000aULL,
    0x8000000080008081ULL, 0x8000000000008080ULL,
    0x0000000080000001ULL, 0x8000000080008008ULL
};

/* Rotation offsets */
static const unsigned int keccak_rotc[24] = {
     1,  3,  6, 10, 15, 21, 28, 36, 45, 55,  2, 14,
    27, 41, 56,  8, 25, 43, 62, 18, 39, 61, 20, 44
};

static const unsigned int keccak_piln[24] = {
    10,  7, 11, 17, 18,  3,  5, 16,  8, 21, 24,  4,
    15, 23, 19, 13, 12,  2, 20, 14, 22,  9,  6,  1
};

static inline uint64_t
rotl64(uint64_t x, unsigned int n)
{
    return (x << n) | (x >> (64 - n));
}

/* ─────────────────────────────────────────────
 * Keccak-f[1600] Permutation (24 rounds)
 * ───────────────────────────────────────────── */

static void
keccak_f1600(uint64_t s[25])
{
    uint64_t t, bc[5];

    for (int round = 0; round < 24; round++) {
        /* θ step */
        for (int i = 0; i < 5; i++)
            bc[i] = s[i] ^ s[i + 5] ^ s[i + 10] ^ s[i + 15] ^ s[i + 20];
        for (int i = 0; i < 5; i++) {
            t = bc[(i + 4) % 5] ^ rotl64(bc[(i + 1) % 5], 1);
            for (int j = 0; j < 25; j += 5)
                s[j + i] ^= t;
        }

        /* ρ and π steps */
        t = s[1];
        for (int i = 0; i < 24; i++) {
            unsigned int j = keccak_piln[i];
            bc[0] = s[j];
            s[j] = rotl64(t, keccak_rotc[i]);
            t = bc[0];
        }

        /* χ step */
        for (int j = 0; j < 25; j += 5) {
            for (int i = 0; i < 5; i++)
                bc[i] = s[j + i];
            for (int i = 0; i < 5; i++)
                s[j + i] ^= (~bc[(i + 1) % 5]) & bc[(i + 2) % 5];
        }

        /* ι step */
        s[0] ^= keccak_rc[round];
    }
}

/* ─────────────────────────────────────────────
 * Sponge Absorb / Squeeze
 * ───────────────────────────────────────────── */

static void
keccak_init(keccak_state *state, unsigned int rate)
{
    memset(state, 0, sizeof(*state));
    state->rate = rate;
}

static void
keccak_absorb(keccak_state *state, const uint8_t *in, size_t inlen)
{
    unsigned int rate = state->rate;
    uint8_t *s = (uint8_t *)state->s;

    while (inlen > 0) {
        size_t chunk = rate - state->pos;
        if (chunk > inlen) chunk = inlen;

        for (size_t i = 0; i < chunk; i++)
            s[state->pos + i] ^= in[i];

        state->pos += (unsigned int)chunk;
        in += chunk;
        inlen -= chunk;

        if (state->pos == rate) {
            keccak_f1600(state->s);
            state->pos = 0;
        }
    }
}

static void
keccak_finalize(keccak_state *state, uint8_t suffix)
{
    uint8_t *s = (uint8_t *)state->s;
    s[state->pos] ^= suffix;
    s[state->rate - 1] ^= 0x80;
    keccak_f1600(state->s);
    state->pos = 0;
}

static void
keccak_squeeze(keccak_state *state, uint8_t *out, size_t outlen)
{
    unsigned int rate = state->rate;
    uint8_t *s = (uint8_t *)state->s;

    while (outlen > 0) {
        if (state->pos == rate) {
            keccak_f1600(state->s);
            state->pos = 0;
        }

        size_t chunk = rate - state->pos;
        if (chunk > outlen) chunk = outlen;

        memcpy(out, s + state->pos, chunk);
        state->pos += (unsigned int)chunk;
        out += chunk;
        outlen -= chunk;
    }
}

/* ─────────────────────────────────────────────
 * SHA3-256: H(m) → 32 bytes
 * ───────────────────────────────────────────── */

static void
sha3_256(uint8_t h[32], const uint8_t *in, size_t inlen)
{
    keccak_state state;
    keccak_init(&state, 136);    /* rate = 1600 - 2×256 = 1088 bits = 136 bytes */
    keccak_absorb(&state, in, inlen);
    keccak_finalize(&state, 0x06); /* SHA-3 domain separator */
    keccak_squeeze(&state, h, 32);
}

/* ─────────────────────────────────────────────
 * SHA3-512: G(m) → 64 bytes
 * ───────────────────────────────────────────── */

static void
sha3_512(uint8_t h[64], const uint8_t *in, size_t inlen)
{
    keccak_state state;
    keccak_init(&state, 72);     /* rate = 1600 - 2×512 = 576 bits = 72 bytes */
    keccak_absorb(&state, in, inlen);
    keccak_finalize(&state, 0x06);
    keccak_squeeze(&state, h, 64);
}

/* ─────────────────────────────────────────────
 * SHAKE-128: XOF for matrix sampling
 * ───────────────────────────────────────────── */

static keccak_state xof_state; /* Thread-local in production */

void
mlkem_xof_absorb(void *state_ptr, const uint8_t seed[34])
{
    keccak_state *st = (keccak_state *)state_ptr;
    keccak_init(st, 168);        /* rate = 1600 - 2×128 = 1344 bits = 168 bytes */
    keccak_absorb(st, seed, 34);
    keccak_finalize(st, 0x1F);   /* SHAKE domain separator */
}

void
mlkem_xof_squeeze(uint8_t *out, size_t outlen, void *state_ptr)
{
    keccak_state *st = (keccak_state *)state_ptr;
    keccak_squeeze(st, out, outlen);
}

/* ─────────────────────────────────────────────
 * SHAKE-256: PRF for CBD sampling
 * PRF(s, b) = SHAKE-256(s || b)
 * ───────────────────────────────────────────── */

void
mlkem_prf(uint8_t *out, size_t outlen, const uint8_t key[MLKEM_SYMBYTES], uint8_t nonce)
{
    keccak_state state;
    keccak_init(&state, 136);    /* SHAKE-256 rate */
    keccak_absorb(&state, key, MLKEM_SYMBYTES);
    keccak_absorb(&state, &nonce, 1);
    keccak_finalize(&state, 0x1F);
    keccak_squeeze(&state, out, outlen);
}

/* ─────────────────────────────────────────────
 * Public API wrappers
 * ───────────────────────────────────────────── */

void
mlkem_hash_h(uint8_t h[32], const uint8_t *in, size_t inlen)
{
    sha3_256(h, in, inlen);
}

void
mlkem_hash_g(uint8_t h[64], const uint8_t *in, size_t inlen)
{
    sha3_512(h, in, inlen);
}

void
mlkem_kdf(uint8_t ss[MLKEM_SSBYTES], const uint8_t *in, size_t inlen)
{
    /* J = SHAKE-256, truncated to 32 bytes */
    keccak_state state;
    keccak_init(&state, 136);
    keccak_absorb(&state, in, inlen);
    keccak_finalize(&state, 0x1F);
    keccak_squeeze(&state, ss, MLKEM_SSBYTES);
}

/* Expose keccak_state size for external callers */
size_t mlkem_xof_state_size(void) { return sizeof(keccak_state); }

```
