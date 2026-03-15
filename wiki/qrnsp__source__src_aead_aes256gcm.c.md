---
title: "src/aead/aes256gcm.c"
nav_title: "aes256gcm.c"
---

# `src/aead/aes256gcm.c`

```c
/*
 * QR-NSP Volcanic Edition — AES-256-GCM Implementation
 * Reference scalar + AES-NI hardware-accelerated path
 *
 * GCM = CTR mode encryption + GHASH authentication
 *
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include "qrnsp_aead.h"
#include <string.h>

/* ─────────────────────────────────────────────
 * AES-NI detection
 * ───────────────────────────────────────────── */

#if defined(__AES__) && defined(__PCLMUL__) && defined(__x86_64__)
#define USE_AESNI 1
#include <immintrin.h>
#include <wmmintrin.h>
#else
#define USE_AESNI 0
#endif

/* ═════════════════════════════════════════════
 * AES-256 Core (Scalar Reference)
 * ═════════════════════════════════════════════ */

/* AES S-box */
static const uint8_t sbox[256] = {
    0x63,0x7c,0x77,0x7b,0xf2,0x6b,0x6f,0xc5,0x30,0x01,0x67,0x2b,0xfe,0xd7,0xab,0x76,
    0xca,0x82,0xc9,0x7d,0xfa,0x59,0x47,0xf0,0xad,0xd4,0xa2,0xaf,0x9c,0xa4,0x72,0xc0,
    0xb7,0xfd,0x93,0x26,0x36,0x3f,0xf7,0xcc,0x34,0xa5,0xe5,0xf1,0x71,0xd8,0x31,0x15,
    0x04,0xc7,0x23,0xc3,0x18,0x96,0x05,0x9a,0x07,0x12,0x80,0xe2,0xeb,0x27,0xb2,0x75,
    0x09,0x83,0x2c,0x1a,0x1b,0x6e,0x5a,0xa0,0x52,0x3b,0xd6,0xb3,0x29,0xe3,0x2f,0x84,
    0x53,0xd1,0x00,0xed,0x20,0xfc,0xb1,0x5b,0x6a,0xcb,0xbe,0x39,0x4a,0x4c,0x58,0xcf,
    0xd0,0xef,0xaa,0xfb,0x43,0x4d,0x33,0x85,0x45,0xf9,0x02,0x7f,0x50,0x3c,0x9f,0xa8,
    0x51,0xa3,0x40,0x8f,0x92,0x9d,0x38,0xf5,0xbc,0xb6,0xda,0x21,0x10,0xff,0xf3,0xd2,
    0xcd,0x0c,0x13,0xec,0x5f,0x97,0x44,0x17,0xc4,0xa7,0x7e,0x3d,0x64,0x5d,0x19,0x73,
    0x60,0x81,0x4f,0xdc,0x22,0x2a,0x90,0x88,0x46,0xee,0xb8,0x14,0xde,0x5e,0x0b,0xdb,
    0xe0,0x32,0x3a,0x0a,0x49,0x06,0x24,0x5c,0xc2,0xd3,0xac,0x62,0x91,0x95,0xe4,0x79,
    0xe7,0xc8,0x37,0x6d,0x8d,0xd5,0x4e,0xa9,0x6c,0x56,0xf4,0xea,0x65,0x7a,0xae,0x08,
    0xba,0x78,0x25,0x2e,0x1c,0xa6,0xb4,0xc6,0xe8,0xdd,0x74,0x1f,0x4b,0xbd,0x8b,0x8a,
    0x70,0x3e,0xb5,0x66,0x48,0x03,0xf6,0x0e,0x61,0x35,0x57,0xb9,0x86,0xc1,0x1d,0x9e,
    0xe1,0xf8,0x98,0x11,0x69,0xd9,0x8e,0x94,0x9b,0x1e,0x87,0xe9,0xce,0x55,0x28,0xdf,
    0x8c,0xa1,0x89,0x0d,0xbf,0xe6,0x42,0x68,0x41,0x99,0x2d,0x0f,0xb0,0x54,0xbb,0x16
};

/* Round constants */
static const uint8_t rcon[10] = {
    0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36
};

/* GF(2^8) multiplication tables for MixColumns */
static uint8_t
xtime(uint8_t x)
{
    return (uint8_t)((x << 1) ^ (((x >> 7) & 1) * 0x1b));
}

static uint8_t
gmul(uint8_t a, uint8_t b)
{
    uint8_t p = 0;
    for (int i = 0; i < 8; i++) {
        if (b & 1) p ^= a;
        uint8_t hi = a & 0x80;
        a <<= 1;
        if (hi) a ^= 0x1b;
        b >>= 1;
    }
    return p;
}

/* AES-256 key schedule: 32-byte key → 15 round keys (240 bytes) */
static void
aes256_key_expand(uint8_t rk[240], const uint8_t key[32])
{
    memcpy(rk, key, 32);
    unsigned int i = 8; /* 8 words already in key */
    unsigned int rcon_idx = 0;

    while (i < 60) { /* 60 words for AES-256 */
        uint8_t t[4];
        memcpy(t, &rk[(i - 1) * 4], 4);

        if (i % 8 == 0) {
            /* RotWord + SubWord + Rcon */
            uint8_t tmp = t[0];
            t[0] = sbox[t[1]] ^ rcon[rcon_idx++];
            t[1] = sbox[t[2]];
            t[2] = sbox[t[3]];
            t[3] = sbox[tmp];
        } else if (i % 8 == 4) {
            /* SubWord only */
            t[0] = sbox[t[0]];
            t[1] = sbox[t[1]];
            t[2] = sbox[t[2]];
            t[3] = sbox[t[3]];
        }

        for (int j = 0; j < 4; j++)
            rk[i * 4 + j] = rk[(i - 8) * 4 + j] ^ t[j];
        i++;
    }
}

/* AES single-block encryption (14 rounds for AES-256) */
static void
aes256_encrypt_block(uint8_t out[16], const uint8_t in[16], const uint8_t rk[240])
{
    uint8_t s[16];
    memcpy(s, in, 16);

    /* AddRoundKey (round 0) */
    for (int i = 0; i < 16; i++) s[i] ^= rk[i];

    for (int round = 1; round <= 14; round++) {
        /* SubBytes */
        for (int i = 0; i < 16; i++) s[i] = sbox[s[i]];

        /* ShiftRows */
        uint8_t t;
        t = s[1]; s[1] = s[5]; s[5] = s[9]; s[9] = s[13]; s[13] = t;
        t = s[2]; s[2] = s[10]; s[10] = t; t = s[6]; s[6] = s[14]; s[14] = t;
        t = s[15]; s[15] = s[11]; s[11] = s[7]; s[7] = s[3]; s[3] = t;

        /* MixColumns (skip on last round) */
        if (round < 14) {
            for (int c = 0; c < 4; c++) {
                uint8_t a0 = s[c*4], a1 = s[c*4+1], a2 = s[c*4+2], a3 = s[c*4+3];
                s[c*4]   = xtime(a0) ^ xtime(a1) ^ a1 ^ a2 ^ a3;
                s[c*4+1] = a0 ^ xtime(a1) ^ xtime(a2) ^ a2 ^ a3;
                s[c*4+2] = a0 ^ a1 ^ xtime(a2) ^ xtime(a3) ^ a3;
                s[c*4+3] = xtime(a0) ^ a0 ^ a1 ^ a2 ^ xtime(a3);
            }
        }

        /* AddRoundKey */
        for (int i = 0; i < 16; i++) s[i] ^= rk[round * 16 + i];
    }

    memcpy(out, s, 16);
}

/* ═════════════════════════════════════════════
 * AES-NI Accelerated Path
 * ═════════════════════════════════════════════ */

#if USE_AESNI

/* AES-256 key expansion using AES-NI */
static inline __m128i
aes_keygen_assist(__m128i key, __m128i gen, int rcon_shift)
{
    gen = _mm_shuffle_epi32(gen, 0xFF);
    key = _mm_xor_si128(key, _mm_slli_si128(key, 4));
    key = _mm_xor_si128(key, _mm_slli_si128(key, 4));
    key = _mm_xor_si128(key, _mm_slli_si128(key, 4));
    return _mm_xor_si128(key, gen);
}

static inline __m128i
aes_keygen_assist2(__m128i key, __m128i gen)
{
    gen = _mm_shuffle_epi32(_mm_aeskeygenassist_si128(gen, 0), 0xAA);
    key = _mm_xor_si128(key, _mm_slli_si128(key, 4));
    key = _mm_xor_si128(key, _mm_slli_si128(key, 4));
    key = _mm_xor_si128(key, _mm_slli_si128(key, 4));
    return _mm_xor_si128(key, gen);
}

static void
aesni_key_expand(__m128i rk[15], const uint8_t key[32])
{
    rk[0] = _mm_loadu_si128((const __m128i *)key);
    rk[1] = _mm_loadu_si128((const __m128i *)(key + 16));

    rk[2]  = aes_keygen_assist(rk[0], _mm_aeskeygenassist_si128(rk[1], 0x01), 0);
    rk[3]  = aes_keygen_assist2(rk[1], rk[2]);
    rk[4]  = aes_keygen_assist(rk[2], _mm_aeskeygenassist_si128(rk[3], 0x02), 0);
    rk[5]  = aes_keygen_assist2(rk[3], rk[4]);
    rk[6]  = aes_keygen_assist(rk[4], _mm_aeskeygenassist_si128(rk[5], 0x04), 0);
    rk[7]  = aes_keygen_assist2(rk[5], rk[6]);
    rk[8]  = aes_keygen_assist(rk[6], _mm_aeskeygenassist_si128(rk[7], 0x08), 0);
    rk[9]  = aes_keygen_assist2(rk[7], rk[8]);
    rk[10] = aes_keygen_assist(rk[8], _mm_aeskeygenassist_si128(rk[9], 0x10), 0);
    rk[11] = aes_keygen_assist2(rk[9], rk[10]);
    rk[12] = aes_keygen_assist(rk[10], _mm_aeskeygenassist_si128(rk[11], 0x20), 0);
    rk[13] = aes_keygen_assist2(rk[11], rk[12]);
    rk[14] = aes_keygen_assist(rk[12], _mm_aeskeygenassist_si128(rk[13], 0x40), 0);
}

/* AES-256 single block encrypt via AES-NI */
static inline __m128i
aesni_encrypt_block(__m128i block, const __m128i rk[15])
{
    block = _mm_xor_si128(block, rk[0]);
    block = _mm_aesenc_si128(block, rk[1]);
    block = _mm_aesenc_si128(block, rk[2]);
    block = _mm_aesenc_si128(block, rk[3]);
    block = _mm_aesenc_si128(block, rk[4]);
    block = _mm_aesenc_si128(block, rk[5]);
    block = _mm_aesenc_si128(block, rk[6]);
    block = _mm_aesenc_si128(block, rk[7]);
    block = _mm_aesenc_si128(block, rk[8]);
    block = _mm_aesenc_si128(block, rk[9]);
    block = _mm_aesenc_si128(block, rk[10]);
    block = _mm_aesenc_si128(block, rk[11]);
    block = _mm_aesenc_si128(block, rk[12]);
    block = _mm_aesenc_si128(block, rk[13]);
    return _mm_aesenclast_si128(block, rk[14]);
}

/* GHASH multiply using PCLMULQDQ */
static inline __m128i
ghash_mul_ni(__m128i a, __m128i b)
{
    __m128i t0 = _mm_clmulepi64_si128(a, b, 0x00);
    __m128i t1 = _mm_clmulepi64_si128(a, b, 0x01);
    __m128i t2 = _mm_clmulepi64_si128(a, b, 0x10);
    __m128i t3 = _mm_clmulepi64_si128(a, b, 0x11);

    t1 = _mm_xor_si128(t1, t2);
    t2 = _mm_slli_si128(t1, 8);
    t1 = _mm_srli_si128(t1, 8);
    t0 = _mm_xor_si128(t0, t2);
    t3 = _mm_xor_si128(t3, t1);

    /* Reduce mod x^128 + x^7 + x^2 + x + 1 */
    __m128i poly = _mm_set_epi32(0, 0, 0xC2000000, 0x00000001);
    t1 = _mm_clmulepi64_si128(t0, poly, 0x00);
    t0 = _mm_shuffle_epi32(t0, 78);
    t0 = _mm_xor_si128(t0, t1);
    t1 = _mm_clmulepi64_si128(t0, poly, 0x00);
    t0 = _mm_shuffle_epi32(t0, 78);
    t0 = _mm_xor_si128(t0, t1);

    return _mm_xor_si128(t0, t3);
}

#endif /* USE_AESNI */

/* ═════════════════════════════════════════════
 * GHASH (Scalar Reference)
 * GF(2^128) multiplication for authentication
 * ═════════════════════════════════════════════ */

/* Byte-reverse a 128-bit block (GCM uses big-endian bit ordering) */
static void
block_reverse(uint8_t out[16], const uint8_t in[16])
{
    for (int i = 0; i < 16; i++) out[i] = in[15 - i];
}

/* GF(2^128) multiplication: R = A * B mod P(x) */
static void
ghash_mul_scalar(uint8_t R[16], const uint8_t A[16], const uint8_t B[16])
{
    uint8_t V[16], Z[16];
    memcpy(V, B, 16);
    memset(Z, 0, 16);

    for (int i = 0; i < 128; i++) {
        if ((A[i / 8] >> (7 - (i % 8))) & 1) {
            for (int j = 0; j < 16; j++) Z[j] ^= V[j];
        }
        uint8_t lsb = V[15] & 1;
        /* Right-shift V by 1 */
        for (int j = 15; j > 0; j--)
            V[j] = (V[j] >> 1) | (V[j-1] << 7);
        V[0] >>= 1;
        if (lsb) V[0] ^= 0xE1; /* x^128 + x^7 + x^2 + x + 1 reduction */
    }

    memcpy(R, Z, 16);
}

/* ═════════════════════════════════════════════
 * GCM State
 * ═════════════════════════════════════════════ */

typedef struct {
    uint8_t rk_scalar[240];     /* Scalar round keys                    */
#if USE_AESNI
    __m128i rk_ni[15] __attribute__((aligned(16)));
    __m128i H_ni;               /* Hash subkey for PCLMULQDQ           */
#endif
    uint8_t H[16];              /* Hash subkey: AES_K(0^128)           */
    uint8_t J0[16];             /* Pre-counter block                   */
    uint8_t ghash_state[16];    /* Running GHASH accumulator           */
    uint64_t aad_len;           /* Total AAD bytes processed           */
    uint64_t ct_len;            /* Total ciphertext bytes processed    */
    int use_ni;                 /* AES-NI available                    */
} gcm_ctx;

static void
gcm_init(gcm_ctx *ctx, const uint8_t key[32], const uint8_t nonce[12])
{
    memset(ctx, 0, sizeof(*ctx));

#if USE_AESNI
    ctx->use_ni = 1;
    aesni_key_expand(ctx->rk_ni, key);
    /* H = AES_K(0^128) */
    ctx->H_ni = aesni_encrypt_block(_mm_setzero_si128(), ctx->rk_ni);
    _mm_storeu_si128((__m128i *)ctx->H, ctx->H_ni);
#else
    ctx->use_ni = 0;
    aes256_key_expand(ctx->rk_scalar, key);
    uint8_t zero[16] = {0};
    aes256_encrypt_block(ctx->H, zero, ctx->rk_scalar);
#endif

    /* J0 = nonce || 0x00000001 (for 96-bit nonce) */
    memcpy(ctx->J0, nonce, 12);
    ctx->J0[12] = 0; ctx->J0[13] = 0; ctx->J0[14] = 0; ctx->J0[15] = 1;
}

/* Increment 32-bit counter in block (big-endian, last 4 bytes) */
static void
inc32(uint8_t block[16])
{
    uint32_t c = ((uint32_t)block[12] << 24) | ((uint32_t)block[13] << 16) |
                 ((uint32_t)block[14] << 8)  | block[15];
    c++;
    block[12] = (uint8_t)(c >> 24);
    block[13] = (uint8_t)(c >> 16);
    block[14] = (uint8_t)(c >> 8);
    block[15] = (uint8_t)c;
}

/* Encrypt block (dispatch) */
static void
gcm_encrypt_block(gcm_ctx *ctx, uint8_t out[16], const uint8_t in[16])
{
#if USE_AESNI
    if (ctx->use_ni) {
        __m128i b = _mm_loadu_si128((const __m128i *)in);
        __m128i r = aesni_encrypt_block(b, ctx->rk_ni);
        _mm_storeu_si128((__m128i *)out, r);
        return;
    }
#endif
    aes256_encrypt_block(out, in, ctx->rk_scalar);
}

/* GHASH update: state = (state ⊕ data) · H */
static void
gcm_ghash_update(gcm_ctx *ctx, const uint8_t data[16])
{
#if USE_AESNI
    if (ctx->use_ni) {
        __m128i s = _mm_loadu_si128((const __m128i *)ctx->ghash_state);
        __m128i d = _mm_loadu_si128((const __m128i *)data);
        s = _mm_xor_si128(s, d);
        s = ghash_mul_ni(s, ctx->H_ni);
        _mm_storeu_si128((__m128i *)ctx->ghash_state, s);
        return;
    }
#endif
    uint8_t tmp[16];
    for (int i = 0; i < 16; i++) tmp[i] = ctx->ghash_state[i] ^ data[i];
    ghash_mul_scalar(ctx->ghash_state, tmp, ctx->H);
}

/* ═════════════════════════════════════════════
 * GCM Encrypt / Decrypt
 * ═════════════════════════════════════════════ */

int
aead_encrypt(uint8_t *ct, uint8_t tag[AEAD_TAG_BYTES],
             const uint8_t *pt, size_t ptlen,
             const uint8_t *aad, size_t aadlen,
             const uint8_t nonce[AEAD_NONCE_BYTES],
             const uint8_t key[AEAD_KEY_BYTES])
{
    gcm_ctx ctx;
    gcm_init(&ctx, key, nonce);

    /* GHASH AAD */
    size_t i;
    for (i = 0; i + 16 <= aadlen; i += 16)
        gcm_ghash_update(&ctx, aad + i);
    if (i < aadlen) {
        uint8_t pad[16] = {0};
        memcpy(pad, aad + i, aadlen - i);
        gcm_ghash_update(&ctx, pad);
    }
    ctx.aad_len = aadlen;

    /* CTR encryption + GHASH ciphertext */
    uint8_t ctr[16], keystream[16];
    memcpy(ctr, ctx.J0, 16);
    inc32(ctr); /* First counter is J0+1 */

    for (i = 0; i + 16 <= ptlen; i += 16) {
        gcm_encrypt_block(&ctx, keystream, ctr);
        for (int j = 0; j < 16; j++) ct[i + j] = pt[i + j] ^ keystream[j];
        gcm_ghash_update(&ctx, ct + i);
        inc32(ctr);
    }
    if (i < ptlen) {
        gcm_encrypt_block(&ctx, keystream, ctr);
        uint8_t pad[16] = {0};
        for (size_t j = 0; j < ptlen - i; j++) ct[i + j] = pt[i + j] ^ keystream[j];
        memcpy(pad, ct + i, ptlen - i);
        gcm_ghash_update(&ctx, pad);
    }
    ctx.ct_len = ptlen;

    /* Final GHASH: len(A) || len(C) in bits, big-endian 64-bit */
    uint8_t len_block[16] = {0};
    uint64_t aad_bits = ctx.aad_len * 8;
    uint64_t ct_bits  = ctx.ct_len * 8;
    for (int j = 0; j < 8; j++) {
        len_block[j]     = (uint8_t)(aad_bits >> (56 - 8 * j));
        len_block[8 + j] = (uint8_t)(ct_bits  >> (56 - 8 * j));
    }
    gcm_ghash_update(&ctx, len_block);

    /* Tag = AES_K(J0) ⊕ GHASH */
    uint8_t s[16];
    gcm_encrypt_block(&ctx, s, ctx.J0);
    for (int j = 0; j < 16; j++) tag[j] = s[j] ^ ctx.ghash_state[j];

    /* Zeroize */
    memset(&ctx, 0, sizeof(ctx));
    memset(keystream, 0, sizeof(keystream));

    return 0;
}

int
aead_decrypt(uint8_t *pt,
             const uint8_t *ct, size_t ctlen,
             const uint8_t tag[AEAD_TAG_BYTES],
             const uint8_t *aad, size_t aadlen,
             const uint8_t nonce[AEAD_NONCE_BYTES],
             const uint8_t key[AEAD_KEY_BYTES])
{
    gcm_ctx ctx;
    gcm_init(&ctx, key, nonce);

    /* GHASH AAD */
    size_t i;
    for (i = 0; i + 16 <= aadlen; i += 16)
        gcm_ghash_update(&ctx, aad + i);
    if (i < aadlen) {
        uint8_t pad[16] = {0};
        memcpy(pad, aad + i, aadlen - i);
        gcm_ghash_update(&ctx, pad);
    }
    ctx.aad_len = aadlen;

    /* GHASH ciphertext (before decryption) */
    for (i = 0; i + 16 <= ctlen; i += 16)
        gcm_ghash_update(&ctx, ct + i);
    if (i < ctlen) {
        uint8_t pad[16] = {0};
        memcpy(pad, ct + i, ctlen - i);
        gcm_ghash_update(&ctx, pad);
    }
    ctx.ct_len = ctlen;

    /* Compute expected tag */
    uint8_t len_block[16] = {0};
    uint64_t aad_bits = ctx.aad_len * 8;
    uint64_t ct_bits  = ctx.ct_len * 8;
    for (int j = 0; j < 8; j++) {
        len_block[j]     = (uint8_t)(aad_bits >> (56 - 8 * j));
        len_block[8 + j] = (uint8_t)(ct_bits  >> (56 - 8 * j));
    }
    gcm_ghash_update(&ctx, len_block);

    uint8_t s[16];
    gcm_encrypt_block(&ctx, s, ctx.J0);
    uint8_t expected_tag[16];
    for (int j = 0; j < 16; j++) expected_tag[j] = s[j] ^ ctx.ghash_state[j];

    /* Constant-time tag comparison */
    uint8_t diff = 0;
    for (int j = 0; j < 16; j++) diff |= expected_tag[j] ^ tag[j];

    if (diff != 0) {
        memset(pt, 0, ctlen); /* Zero output on auth failure */
        memset(&ctx, 0, sizeof(ctx));
        return -1;
    }

    /* CTR decrypt */
    uint8_t ctr[16], keystream[16];
    memcpy(ctr, ctx.J0, 16);
    inc32(ctr);

    for (i = 0; i + 16 <= ctlen; i += 16) {
        gcm_encrypt_block(&ctx, keystream, ctr);
        for (int j = 0; j < 16; j++) pt[i + j] = ct[i + j] ^ keystream[j];
        inc32(ctr);
    }
    if (i < ctlen) {
        gcm_encrypt_block(&ctx, keystream, ctr);
        for (size_t j = 0; j < ctlen - i; j++) pt[i + j] = ct[i + j] ^ keystream[j];
    }

    memset(&ctx, 0, sizeof(ctx));
    memset(keystream, 0, sizeof(keystream));
    return 0;
}

```
