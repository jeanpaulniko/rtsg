---
title: "src/crypto/poly.c"
nav_title: "poly.c"
---

# `src/crypto/poly.c`

```c
/*
 * QR-NSP Volcanic Edition — Polynomial Operations
 * SPDX-License-Identifier: AGPL-3.0-or-later
 * CBD sampling, compression/decompression, serialization
 *
 * Reference: FIPS 203 §4.2 (compression), §4.1 (CBD)
 */

#include "mlkem_params.h"
#include <string.h>

/* ─────────────────────────────────────────────
 * Centered Binomial Distribution (CBD)
 *
 * Sample polynomial with coefficients from CBD_η
 * Each coefficient = Σ(a_i) - Σ(b_i) for η random bits each
 * ───────────────────────────────────────────── */

/*
 * Load 32 bits from byte array
 */
static inline uint32_t
load32_le(const uint8_t x[4])
{
    return (uint32_t)x[0]       | ((uint32_t)x[1] << 8) |
           ((uint32_t)x[2] << 16) | ((uint32_t)x[3] << 24);
}

/*
 * CBD with η = 2
 * Requires 2 × 2 = 4 bits per coefficient → 128 bytes input for 256 coefficients
 */
void
mlkem_poly_cbd_eta1(mlkem_poly *r, const uint8_t buf[MLKEM_ETA1 * MLKEM_N / 4])
{
    /* η1 = 2 for ML-KEM-1024 */
    unsigned int i, j;
    uint32_t t, d;
    int16_t a, b;

    for (i = 0; i < MLKEM_N / 8; i++) {
        t = load32_le(&buf[4 * i]);
        d = t & 0x55555555;
        d += (t >> 1) & 0x55555555;

        for (j = 0; j < 8; j++) {
            a = (d >> (4 * j)) & 0x3;
            b = (d >> (4 * j + 2)) & 0x3;
            r->coeffs[8 * i + j] = a - b;
        }
    }
}

void
mlkem_poly_cbd_eta2(mlkem_poly *r, const uint8_t buf[MLKEM_ETA2 * MLKEM_N / 4])
{
    /* η2 = 2, same as η1 for ML-KEM-1024 */
    mlkem_poly_cbd_eta1(r, buf);
}

/* ─────────────────────────────────────────────
 * Serialization: polynomial ↔ byte array
 *
 * Each coefficient is 12 bits (for q = 3329 < 2^12)
 * 256 × 12 / 8 = 384 bytes
 * ───────────────────────────────────────────── */

void
mlkem_poly_tobytes(uint8_t r[MLKEM_POLYBYTES], const mlkem_poly *p)
{
    unsigned int i;
    uint16_t t0, t1;

    for (i = 0; i < MLKEM_N / 2; i++) {
        /* Ensure positive representative */
        t0 = (uint16_t)p->coeffs[2 * i];
        t0 += ((int16_t)t0 >> 15) & MLKEM_Q;
        t1 = (uint16_t)p->coeffs[2 * i + 1];
        t1 += ((int16_t)t1 >> 15) & MLKEM_Q;

        r[3 * i + 0] = (uint8_t)(t0 >> 0);
        r[3 * i + 1] = (uint8_t)((t0 >> 8) | (t1 << 4));
        r[3 * i + 2] = (uint8_t)(t1 >> 4);
    }
}

void
mlkem_poly_frombytes(mlkem_poly *r, const uint8_t a[MLKEM_POLYBYTES])
{
    unsigned int i;
    for (i = 0; i < MLKEM_N / 2; i++) {
        r->coeffs[2 * i]     = ((a[3 * i + 0] >> 0) | ((uint16_t)a[3 * i + 1] << 8)) & 0xFFF;
        r->coeffs[2 * i + 1] = ((a[3 * i + 1] >> 4) | ((uint16_t)a[3 * i + 2] << 4)) & 0xFFF;
    }
}

/* ─────────────────────────────────────────────
 * Compression / Decompression
 *
 * Compress_d(x) = ⌈(2^d / q) · x⌋ mod 2^d
 * Decompress_d(x) = ⌈(q / 2^d) · x⌋
 * ───────────────────────────────────────────── */

/* Compress polynomial coefficients to d_u = 11 bits */
void
mlkem_poly_compress_du(uint8_t *r, const mlkem_poly *p)
{
    unsigned int i, j;
    int16_t u;
    uint16_t t[8];

    for (i = 0; i < MLKEM_N / 8; i++) {
        for (j = 0; j < 8; j++) {
            u = p->coeffs[8 * i + j];
            u += (u >> 15) & MLKEM_Q;
            t[j] = ((((uint32_t)u << 11) + MLKEM_Q / 2) / MLKEM_Q) & 0x7FF;
        }

        /* Pack 8 × 11-bit values into 11 bytes */
        r[0]  = (uint8_t)(t[0] >> 0);
        r[1]  = (uint8_t)((t[0] >> 8) | (t[1] << 3));
        r[2]  = (uint8_t)((t[1] >> 5) | (t[2] << 6));
        r[3]  = (uint8_t)(t[2] >> 2);
        r[4]  = (uint8_t)((t[2] >> 10) | (t[3] << 1));
        r[5]  = (uint8_t)((t[3] >> 7) | (t[4] << 4));
        r[6]  = (uint8_t)((t[4] >> 4) | (t[5] << 7));
        r[7]  = (uint8_t)(t[5] >> 1);
        r[8]  = (uint8_t)((t[5] >> 9) | (t[6] << 2));
        r[9]  = (uint8_t)((t[6] >> 6) | (t[7] << 5));
        r[10] = (uint8_t)(t[7] >> 3);
        r += 11;
    }
}

/* Decompress from d_u = 11 bits */
void
mlkem_poly_decompress_du(mlkem_poly *r, const uint8_t *a)
{
    unsigned int i;
    uint16_t t[8];

    for (i = 0; i < MLKEM_N / 8; i++) {
        t[0]  = (a[0]  >> 0) | ((uint16_t)a[1]  << 8);
        t[1]  = (a[1]  >> 3) | ((uint16_t)a[2]  << 5);
        t[2]  = (a[2]  >> 6) | ((uint16_t)a[3]  << 2) | ((uint16_t)a[4] << 10);
        t[3]  = (a[4]  >> 1) | ((uint16_t)a[5]  << 7);
        t[4]  = (a[5]  >> 4) | ((uint16_t)a[6]  << 4);
        t[5]  = (a[6]  >> 7) | ((uint16_t)a[7]  << 1) | ((uint16_t)a[8] << 9);
        t[6]  = (a[8]  >> 2) | ((uint16_t)a[9]  << 6);
        t[7]  = (a[9]  >> 5) | ((uint16_t)a[10] << 3);
        a += 11;

        for (unsigned int j = 0; j < 8; j++) {
            t[j] &= 0x7FF;
            r->coeffs[8 * i + j] = (int16_t)(((uint32_t)t[j] * MLKEM_Q + 1024) >> 11);
        }
    }
}

/* Compress polynomial coefficients to d_v = 5 bits */
void
mlkem_poly_compress_dv(uint8_t *r, const mlkem_poly *p)
{
    unsigned int i, j;
    int16_t u;
    uint8_t t[8];

    for (i = 0; i < MLKEM_N / 8; i++) {
        for (j = 0; j < 8; j++) {
            u = p->coeffs[8 * i + j];
            u += (u >> 15) & MLKEM_Q;
            t[j] = (uint8_t)((((uint32_t)u << 5) + MLKEM_Q / 2) / MLKEM_Q) & 0x1F;
        }

        /* Pack 8 × 5-bit values into 5 bytes */
        r[0] = (t[0] >> 0) | (t[1] << 5);
        r[1] = (t[1] >> 3) | (t[2] << 2) | (t[3] << 7);
        r[2] = (t[3] >> 1) | (t[4] << 4);
        r[3] = (t[4] >> 4) | (t[5] << 1) | (t[6] << 6);
        r[4] = (t[6] >> 2) | (t[7] << 3);
        r += 5;
    }
}

/* Decompress from d_v = 5 bits */
void
mlkem_poly_decompress_dv(mlkem_poly *r, const uint8_t *a)
{
    unsigned int i;
    uint8_t t[8];

    for (i = 0; i < MLKEM_N / 8; i++) {
        t[0] =  a[0]       & 0x1F;
        t[1] = (a[0] >> 5) | ((a[1] << 3) & 0x1F);
        t[2] = (a[1] >> 2) & 0x1F;
        t[3] = (a[1] >> 7) | ((a[2] << 1) & 0x1F);
        t[4] = (a[2] >> 4) | ((a[3] << 4) & 0x1F);
        t[5] = (a[3] >> 1) & 0x1F;
        t[6] = (a[3] >> 6) | ((a[4] << 2) & 0x1F);
        t[7] = (a[4] >> 3);
        a += 5;

        for (unsigned int j = 0; j < 8; j++) {
            r->coeffs[8 * i + j] = (int16_t)(((uint32_t)t[j] * MLKEM_Q + 16) >> 5);
        }
    }
}

/* ─────────────────────────────────────────────
 * Message encoding / decoding
 *
 * Encode 32-byte message as polynomial:
 *   coefficient i = ⌈q/2⌋ × bit i
 * ───────────────────────────────────────────── */

void
mlkem_poly_frommsg(mlkem_poly *r, const uint8_t msg[MLKEM_SYMBYTES])
{
    unsigned int i, j;
    for (i = 0; i < MLKEM_N / 8; i++) {
        for (j = 0; j < 8; j++) {
            int16_t bit = (msg[i] >> j) & 1;
            r->coeffs[8 * i + j] = bit * ((MLKEM_Q + 1) / 2);
        }
    }
}

void
mlkem_poly_tomsg(uint8_t msg[MLKEM_SYMBYTES], const mlkem_poly *p)
{
    unsigned int i, j;
    uint16_t t;

    memset(msg, 0, MLKEM_SYMBYTES);
    for (i = 0; i < MLKEM_N / 8; i++) {
        for (j = 0; j < 8; j++) {
            t = (uint16_t)p->coeffs[8 * i + j];
            t += ((int16_t)t >> 15) & MLKEM_Q;
            /* Compress to 1 bit: round(2t/q) mod 2 */
            t = (((t << 1) + MLKEM_Q / 2) / MLKEM_Q) & 1;
            msg[i] |= (uint8_t)(t << j);
        }
    }
}

/* ─────────────────────────────────────────────
 * Arithmetic helpers
 * ───────────────────────────────────────────── */

void
mlkem_poly_add(mlkem_poly *r, const mlkem_poly *a, const mlkem_poly *b)
{
    for (unsigned int i = 0; i < MLKEM_N; i++)
        r->coeffs[i] = a->coeffs[i] + b->coeffs[i];
}

void
mlkem_poly_sub(mlkem_poly *r, const mlkem_poly *a, const mlkem_poly *b)
{
    for (unsigned int i = 0; i < MLKEM_N; i++)
        r->coeffs[i] = a->coeffs[i] - b->coeffs[i];
}

void
mlkem_poly_reduce(mlkem_poly *p)
{
    for (unsigned int i = 0; i < MLKEM_N; i++) {
        /* Barrett reduction to [0, q) */
        int16_t t = p->coeffs[i];
        t += (t >> 15) & MLKEM_Q;
        int16_t v = ((int32_t)20159 * t + (1 << 25)) >> 26;
        t -= v * MLKEM_Q;
        p->coeffs[i] = t;
    }
}

/* ─────────────────────────────────────────────
 * Polyvec operations (vector of k polynomials)
 * ───────────────────────────────────────────── */

void
mlkem_polyvec_ntt(mlkem_polyvec *v)
{
    for (unsigned int i = 0; i < MLKEM_K; i++)
        mlkem_ntt(&v->vec[i]);
}

void
mlkem_polyvec_invntt(mlkem_polyvec *v)
{
    for (unsigned int i = 0; i < MLKEM_K; i++)
        mlkem_invntt(&v->vec[i]);
}

void
mlkem_polyvec_pointwise_acc(mlkem_poly *r, const mlkem_polyvec *a, const mlkem_polyvec *b)
{
    mlkem_poly t;
    mlkem_basemul(r, &a->vec[0], &b->vec[0]);
    for (unsigned int i = 1; i < MLKEM_K; i++) {
        mlkem_basemul(&t, &a->vec[i], &b->vec[i]);
        mlkem_poly_add(r, r, &t);
    }
    mlkem_poly_reduce(r);
}

void
mlkem_polyvec_compress(uint8_t *r, const mlkem_polyvec *v)
{
    for (unsigned int i = 0; i < MLKEM_K; i++)
        mlkem_poly_compress_du(r + i * MLKEM_POLYCOMPRESSEDBYTES_DU, &v->vec[i]);
}

void
mlkem_polyvec_decompress(mlkem_polyvec *r, const uint8_t *a)
{
    for (unsigned int i = 0; i < MLKEM_K; i++)
        mlkem_poly_decompress_du(&r->vec[i], a + i * MLKEM_POLYCOMPRESSEDBYTES_DU);
}

void
mlkem_polyvec_tobytes(uint8_t *r, const mlkem_polyvec *v)
{
    for (unsigned int i = 0; i < MLKEM_K; i++)
        mlkem_poly_tobytes(r + i * MLKEM_POLYBYTES, &v->vec[i]);
}

void
mlkem_polyvec_frombytes(mlkem_polyvec *r, const uint8_t *a)
{
    for (unsigned int i = 0; i < MLKEM_K; i++)
        mlkem_poly_frombytes(&r->vec[i], a + i * MLKEM_POLYBYTES);
}

void
mlkem_polyvec_add(mlkem_polyvec *r, const mlkem_polyvec *a, const mlkem_polyvec *b)
{
    for (unsigned int i = 0; i < MLKEM_K; i++)
        mlkem_poly_add(&r->vec[i], &a->vec[i], &b->vec[i]);
}

void
mlkem_polyvec_reduce(mlkem_polyvec *v)
{
    for (unsigned int i = 0; i < MLKEM_K; i++)
        mlkem_poly_reduce(&v->vec[i]);
}

```
