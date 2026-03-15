---
title: "include/mlkem_params.h"
nav_title: "mlkem_params.h"
---

# `include/mlkem_params.h`

```c
/*
 * QR-NSP Volcanic Edition — ML-KEM-1024 Parameters (FIPS 203)
 * SPDX-License-Identifier: AGPL-3.0-or-later
 * Module 2: Post-Quantum Key Encapsulation
 *
 * ML-KEM-1024 = Module-LWE KEM at NIST Level 5
 * q = 3329, n = 256, k = 4
 *
 * Reference: FIPS 203 (August 2024)
 */

#ifndef MLKEM_PARAMS_H
#define MLKEM_PARAMS_H

#include <stdint.h>
#include <stddef.h>

/* ─────────────────────────────────────────────
 * ML-KEM-1024 Parameters (FIPS 203 Table 1)
 * ───────────────────────────────────────────── */

#define MLKEM_N          256    /* Polynomial degree                    */
#define MLKEM_K          4      /* Module rank (1024 = k*n)             */
#define MLKEM_Q          3329   /* Modulus (prime, 3329 = 13·256 + 1)   */
#define MLKEM_ETA1       2      /* CBD parameter for secret/error       */
#define MLKEM_ETA2       2      /* CBD parameter for encryption noise   */
#define MLKEM_DU         11     /* Compression bits for u vector        */
#define MLKEM_DV         5      /* Compression bits for v scalar        */

/* Derived sizes (bytes) */
#define MLKEM_SYMBYTES   32     /* Shared secret, seeds, hashes         */
#define MLKEM_POLYBYTES  384    /* 256 coefficients × 12 bits / 8       */

#define MLKEM_POLYCOMPRESSEDBYTES_DU  352  /* 256 × 11 / 8 = 352 */
#define MLKEM_POLYCOMPRESSEDBYTES_DV  160  /* 256 × 5  / 8 = 160 */

/* Public key: ek = (t_hat || rho)  where t_hat is k polys + 32-byte seed */
#define MLKEM_PUBLICKEYBYTES   (MLKEM_K * MLKEM_POLYBYTES + MLKEM_SYMBYTES)
                                /* 4 × 384 + 32 = 1568 */

/* Secret key: dk = (s_hat || ek || H(ek) || z) */
#define MLKEM_SECRETKEYBYTES   (MLKEM_K * MLKEM_POLYBYTES + \
                                MLKEM_PUBLICKEYBYTES + \
                                2 * MLKEM_SYMBYTES)
                                /* 1536 + 1568 + 64 = 3168 */

/* Ciphertext: c = (c1 || c2)  where c1 is k compressed polys + compressed v */
#define MLKEM_CIPHERTEXTBYTES  (MLKEM_K * MLKEM_POLYCOMPRESSEDBYTES_DU + \
                                MLKEM_POLYCOMPRESSEDBYTES_DV)
                                /* 4 × 352 + 160 = 1568 */

/* Shared secret */
#define MLKEM_SSBYTES          32

/* ─────────────────────────────────────────────
 * NTT Constants
 *
 * q = 3329 = 13 × 256 + 1
 * Primitive 512th root of unity mod q: ζ = 17
 * Montgomery constant R = 2^16 mod q = 2285
 * Barrett constant: 5039 (for q)
 * ───────────────────────────────────────────── */

#define MLKEM_MONT       2285   /* 2^16 mod q                          */
#define MLKEM_QINV       62209  /* q^(-1) mod 2^16                     */
#define MLKEM_ZETA       17     /* Primitive 512th root of unity mod q  */

/* ─────────────────────────────────────────────
 * Core Types
 * ───────────────────────────────────────────── */

/* Single polynomial in R_q = Z_q[X]/(X^256 + 1) */
typedef struct {
    int16_t coeffs[MLKEM_N];
} mlkem_poly;

/* Vector of k polynomials (module element) */
typedef struct {
    mlkem_poly vec[MLKEM_K];
} mlkem_polyvec;

/* Key pair */
typedef struct {
    uint8_t pk[MLKEM_PUBLICKEYBYTES];
    uint8_t sk[MLKEM_SECRETKEYBYTES];
} mlkem_keypair;

/* ─────────────────────────────────────────────
 * AVX-512 Detection
 * ───────────────────────────────────────────── */

#if defined(__AVX512F__) && defined(__AVX512BW__)
#define MLKEM_USE_AVX512 1
#else
#define MLKEM_USE_AVX512 0
#endif

/* ─────────────────────────────────────────────
 * Function Declarations
 * ───────────────────────────────────────────── */

/* NTT (ntt.c) */
void mlkem_ntt(mlkem_poly *p);
void mlkem_invntt(mlkem_poly *p);
void mlkem_basemul(mlkem_poly *r, const mlkem_poly *a, const mlkem_poly *b);

/* Polynomial operations (poly.c) */
void mlkem_poly_cbd_eta1(mlkem_poly *r, const uint8_t buf[MLKEM_ETA1 * MLKEM_N / 4]);
void mlkem_poly_cbd_eta2(mlkem_poly *r, const uint8_t buf[MLKEM_ETA2 * MLKEM_N / 4]);
void mlkem_poly_tobytes(uint8_t r[MLKEM_POLYBYTES], const mlkem_poly *p);
void mlkem_poly_frombytes(mlkem_poly *r, const uint8_t a[MLKEM_POLYBYTES]);
void mlkem_poly_compress_du(uint8_t *r, const mlkem_poly *p);
void mlkem_poly_decompress_du(mlkem_poly *r, const uint8_t *a);
void mlkem_poly_compress_dv(uint8_t *r, const mlkem_poly *p);
void mlkem_poly_decompress_dv(mlkem_poly *r, const uint8_t *a);
void mlkem_poly_frommsg(mlkem_poly *r, const uint8_t msg[MLKEM_SYMBYTES]);
void mlkem_poly_tomsg(uint8_t msg[MLKEM_SYMBYTES], const mlkem_poly *p);
void mlkem_poly_add(mlkem_poly *r, const mlkem_poly *a, const mlkem_poly *b);
void mlkem_poly_sub(mlkem_poly *r, const mlkem_poly *a, const mlkem_poly *b);
void mlkem_poly_reduce(mlkem_poly *p);

/* Polyvec operations (poly.c) */
void mlkem_polyvec_ntt(mlkem_polyvec *v);
void mlkem_polyvec_invntt(mlkem_polyvec *v);
void mlkem_polyvec_pointwise_acc(mlkem_poly *r, const mlkem_polyvec *a, const mlkem_polyvec *b);
void mlkem_polyvec_compress(uint8_t *r, const mlkem_polyvec *v);
void mlkem_polyvec_decompress(mlkem_polyvec *r, const uint8_t *a);
void mlkem_polyvec_tobytes(uint8_t *r, const mlkem_polyvec *v);
void mlkem_polyvec_frombytes(mlkem_polyvec *r, const uint8_t *a);
void mlkem_polyvec_add(mlkem_polyvec *r, const mlkem_polyvec *a, const mlkem_polyvec *b);
void mlkem_polyvec_reduce(mlkem_polyvec *v);

/* KEM (kem.c) */
int mlkem_keypair_generate(mlkem_keypair *kp);
int mlkem_encapsulate(uint8_t ct[MLKEM_CIPHERTEXTBYTES],
                      uint8_t ss[MLKEM_SSBYTES],
                      const uint8_t pk[MLKEM_PUBLICKEYBYTES]);
int mlkem_decapsulate(uint8_t ss[MLKEM_SSBYTES],
                      const uint8_t ct[MLKEM_CIPHERTEXTBYTES],
                      const uint8_t sk[MLKEM_SECRETKEYBYTES]);

/* Symmetric primitives (symmetric.c) — SHA3/SHAKE wrappers */
void mlkem_hash_h(uint8_t h[32], const uint8_t *in, size_t inlen);
void mlkem_hash_g(uint8_t h[64], const uint8_t *in, size_t inlen);
void mlkem_kdf(uint8_t ss[MLKEM_SSBYTES], const uint8_t *in, size_t inlen);
void mlkem_xof_absorb(void *state, const uint8_t seed[34]);
void mlkem_xof_squeeze(uint8_t *out, size_t outlen, void *state);
void mlkem_prf(uint8_t *out, size_t outlen, const uint8_t key[MLKEM_SYMBYTES], uint8_t nonce);

#endif /* MLKEM_PARAMS_H */

```
