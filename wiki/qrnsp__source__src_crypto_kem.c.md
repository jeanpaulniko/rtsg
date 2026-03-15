---
title: "src/crypto/kem.c"
nav_title: "kem.c"
---

# `src/crypto/kem.c`

```c
/*
 * QR-NSP Volcanic Edition — ML-KEM-1024 KEM
 * SPDX-License-Identifier: AGPL-3.0-or-later
 * Key Generation, Encapsulation, Decapsulation
 *
 * FIPS 203 Algorithms 15 (KeyGen), 16 (Encaps), 17 (Decaps)
 * With implicit rejection (Algorithm 17 line 8)
 *
 * Security: IND-CCA2 under Module-LWE assumption
 */

#include "mlkem_params.h"
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#if defined(__linux__)
#include <sys/random.h>
#endif

/* Forward declaration for XOF state size */
extern size_t mlkem_xof_state_size(void);

/* ─────────────────────────────────────────────
 * OS Random (entropy source)
 * ───────────────────────────────────────────── */

int
randombytes(uint8_t *out, size_t len)
{
#if defined(__linux__)
    ssize_t ret = getrandom(out, len, 0);
    return (ret == (ssize_t)len) ? 0 : -1;
#else
    FILE *f = fopen("/dev/urandom", "rb");
    if (!f) return -1;
    size_t n = fread(out, 1, len, f);
    fclose(f);
    return (n == len) ? 0 : -1;
#endif
}

/* ─────────────────────────────────────────────
 * Constant-time comparison (timing-safe)
 * ───────────────────────────────────────────── */

static int
ct_memcmp(const uint8_t *a, const uint8_t *b, size_t len)
{
    uint8_t r = 0;
    for (size_t i = 0; i < len; i++)
        r |= a[i] ^ b[i];
    return (int)r;
}

/* Constant-time conditional move: if b != 0, copy src → dst */
static void
ct_cmov(uint8_t *dst, const uint8_t *src, size_t len, uint8_t b)
{
    uint8_t mask = -(uint8_t)(b != 0);
    for (size_t i = 0; i < len; i++)
        dst[i] ^= mask & (dst[i] ^ src[i]);
}

/* ─────────────────────────────────────────────
 * Matrix sampling: A ∈ R_q^{k×k} from seed ρ
 *
 * A[i][j] sampled via XOF = SHAKE-128(ρ || j || i)
 * Rejection sampling: parse 3 bytes → 2 coefficients
 * ───────────────────────────────────────────── */

static void
sample_ntt_poly(mlkem_poly *p, const uint8_t seed[MLKEM_SYMBYTES],
                uint8_t x, uint8_t y)
{
    uint8_t xof_seed[34];
    memcpy(xof_seed, seed, MLKEM_SYMBYTES);
    xof_seed[32] = x;
    xof_seed[33] = y;

    /* Allocate XOF state on stack */
    uint8_t xof_buf[sizeof(uint64_t) * 25 + 16]; /* keccak_state sized */
    void *state = xof_buf;

    mlkem_xof_absorb(state, xof_seed);

    unsigned int ctr = 0;
    uint8_t buf[168]; /* One SHAKE-128 block */

    while (ctr < MLKEM_N) {
        mlkem_xof_squeeze(buf, sizeof(buf), state);

        for (unsigned int i = 0; i + 3 <= sizeof(buf) && ctr < MLKEM_N; i += 3) {
            uint16_t d1 = ((uint16_t)buf[i]     | ((uint16_t)buf[i + 1] << 8)) & 0xFFF;
            uint16_t d2 = ((uint16_t)buf[i + 1] >> 4 | ((uint16_t)buf[i + 2] << 4)) & 0xFFF;

            if (d1 < MLKEM_Q) p->coeffs[ctr++] = (int16_t)d1;
            if (ctr < MLKEM_N && d2 < MLKEM_Q) p->coeffs[ctr++] = (int16_t)d2;
        }
    }
}

/* ─────────────────────────────────────────────
 * K-PKE.KeyGen (FIPS 203 Algorithm 13)
 *
 * Internal deterministic keygen from seed d
 * Returns (ek, dk_pke)
 * ───────────────────────────────────────────── */

static void
kpke_keygen(uint8_t *ek, uint8_t *dk_pke, const uint8_t d[MLKEM_SYMBYTES])
{
    uint8_t buf[64];
    mlkem_hash_g(buf, d, MLKEM_SYMBYTES);
    uint8_t *rho   = buf;       /* 32 bytes: seed for A */
    uint8_t *sigma = buf + 32;  /* 32 bytes: seed for s, e */

    /* ── Sample matrix A (in NTT domain) ── */
    mlkem_poly a_hat[MLKEM_K][MLKEM_K];
    for (unsigned int i = 0; i < MLKEM_K; i++)
        for (unsigned int j = 0; j < MLKEM_K; j++)
            sample_ntt_poly(&a_hat[i][j], rho, (uint8_t)j, (uint8_t)i);

    /* ── Sample secret vector s ── */
    mlkem_polyvec s;
    uint8_t prf_buf[MLKEM_ETA1 * MLKEM_N / 4];
    uint8_t nonce = 0;

    for (unsigned int i = 0; i < MLKEM_K; i++) {
        mlkem_prf(prf_buf, sizeof(prf_buf), sigma, nonce++);
        mlkem_poly_cbd_eta1(&s.vec[i], prf_buf);
    }

    /* ── Sample error vector e ── */
    mlkem_polyvec e;
    for (unsigned int i = 0; i < MLKEM_K; i++) {
        mlkem_prf(prf_buf, sizeof(prf_buf), sigma, nonce++);
        mlkem_poly_cbd_eta1(&e.vec[i], prf_buf);
    }

    /* ── NTT(s), NTT(e) ── */
    mlkem_polyvec_ntt(&s);
    mlkem_polyvec_ntt(&e);

    /* ── t_hat = A_hat · s_hat + e_hat ── */
    mlkem_polyvec t_hat;
    for (unsigned int i = 0; i < MLKEM_K; i++) {
        /* Build row i of A as polyvec for pointwise_acc */
        mlkem_polyvec a_row;
        for (unsigned int j = 0; j < MLKEM_K; j++)
            a_row.vec[j] = a_hat[i][j];
        mlkem_polyvec_pointwise_acc(&t_hat.vec[i], &a_row, &s);
    }
    mlkem_polyvec_add(&t_hat, &t_hat, &e);
    mlkem_polyvec_reduce(&t_hat);

    /* ── Serialize: ek = (t_hat || rho), dk_pke = s_hat ── */
    mlkem_polyvec_tobytes(ek, &t_hat);
    memcpy(ek + MLKEM_K * MLKEM_POLYBYTES, rho, MLKEM_SYMBYTES);

    mlkem_polyvec_tobytes(dk_pke, &s);

    /* Zeroize secrets */
    memset(buf, 0, sizeof(buf));
    memset(prf_buf, 0, sizeof(prf_buf));
    memset(&s, 0, sizeof(s));
    memset(&e, 0, sizeof(e));
}

/* ─────────────────────────────────────────────
 * K-PKE.Encrypt (FIPS 203 Algorithm 14)
 *
 * Deterministic encryption: (ek, m, r) → c
 * ───────────────────────────────────────────── */

static void
kpke_encrypt(uint8_t *ct,
             const uint8_t *ek,
             const uint8_t m[MLKEM_SYMBYTES],
             const uint8_t r[MLKEM_SYMBYTES])
{
    /* Parse ek = (t_hat || rho) */
    mlkem_polyvec t_hat;
    mlkem_polyvec_frombytes(&t_hat, ek);
    const uint8_t *rho = ek + MLKEM_K * MLKEM_POLYBYTES;

    /* Sample matrix A^T (transposed: swap i,j indices) */
    mlkem_poly at_hat[MLKEM_K][MLKEM_K];
    for (unsigned int i = 0; i < MLKEM_K; i++)
        for (unsigned int j = 0; j < MLKEM_K; j++)
            sample_ntt_poly(&at_hat[i][j], rho, (uint8_t)i, (uint8_t)j);

    /* Sample r vector, e1, e2 */
    mlkem_polyvec r_vec, e1;
    mlkem_poly e2;
    uint8_t prf_buf[MLKEM_ETA2 * MLKEM_N / 4];
    uint8_t nonce = 0;

    for (unsigned int i = 0; i < MLKEM_K; i++) {
        mlkem_prf(prf_buf, sizeof(prf_buf), r, nonce++);
        mlkem_poly_cbd_eta1(&r_vec.vec[i], prf_buf);
    }
    for (unsigned int i = 0; i < MLKEM_K; i++) {
        mlkem_prf(prf_buf, sizeof(prf_buf), r, nonce++);
        mlkem_poly_cbd_eta2(&e1.vec[i], prf_buf);
    }
    mlkem_prf(prf_buf, sizeof(prf_buf), r, nonce++);
    mlkem_poly_cbd_eta2(&e2, prf_buf);

    /* NTT(r) */
    mlkem_polyvec_ntt(&r_vec);

    /* u = A^T · r + e1 */
    mlkem_polyvec u;
    for (unsigned int i = 0; i < MLKEM_K; i++) {
        mlkem_polyvec at_row;
        for (unsigned int j = 0; j < MLKEM_K; j++)
            at_row.vec[j] = at_hat[i][j];
        mlkem_polyvec_pointwise_acc(&u.vec[i], &at_row, &r_vec);
    }
    mlkem_polyvec_invntt(&u);
    mlkem_polyvec_add(&u, &u, &e1);
    mlkem_polyvec_reduce(&u);

    /* v = t^T · r + e2 + Decompress_1(m) */
    mlkem_poly v;
    mlkem_polyvec_pointwise_acc(&v, &t_hat, &r_vec);
    mlkem_invntt(&v);

    mlkem_poly mp;
    mlkem_poly_frommsg(&mp, m);
    mlkem_poly_add(&v, &v, &e2);
    mlkem_poly_add(&v, &v, &mp);
    mlkem_poly_reduce(&v);

    /* Compress and serialize: c = (Compress_du(u) || Compress_dv(v)) */
    mlkem_polyvec_compress(ct, &u);
    mlkem_poly_compress_dv(ct + MLKEM_K * MLKEM_POLYCOMPRESSEDBYTES_DU, &v);

    /* Zeroize */
    memset(prf_buf, 0, sizeof(prf_buf));
    memset(&r_vec, 0, sizeof(r_vec));
}

/* ─────────────────────────────────────────────
 * K-PKE.Decrypt (FIPS 203 Algorithm 14 inverse)
 * ───────────────────────────────────────────── */

static void
kpke_decrypt(uint8_t m[MLKEM_SYMBYTES],
             const uint8_t *ct,
             const uint8_t *dk_pke)
{
    /* Parse ciphertext */
    mlkem_polyvec u;
    mlkem_poly v;
    mlkem_polyvec_decompress(&u, ct);
    mlkem_poly_decompress_dv(&v, ct + MLKEM_K * MLKEM_POLYCOMPRESSEDBYTES_DU);

    /* Parse secret key */
    mlkem_polyvec s_hat;
    mlkem_polyvec_frombytes(&s_hat, dk_pke);

    /* NTT(u) */
    mlkem_polyvec_ntt(&u);

    /* w = v - s^T · u */
    mlkem_poly w;
    mlkem_polyvec_pointwise_acc(&w, &s_hat, &u);
    mlkem_invntt(&w);
    mlkem_poly_sub(&w, &v, &w);
    mlkem_poly_reduce(&w);

    /* Decode message */
    mlkem_poly_tomsg(m, &w);
}

/* ═════════════════════════════════════════════
 * ML-KEM.KeyGen (FIPS 203 Algorithm 15)
 * ═════════════════════════════════════════════ */

int
mlkem_keypair_generate(mlkem_keypair *kp)
{
    uint8_t d[MLKEM_SYMBYTES], z[MLKEM_SYMBYTES];

    if (randombytes(d, MLKEM_SYMBYTES) != 0) return -1;
    if (randombytes(z, MLKEM_SYMBYTES) != 0) return -1;

    /* Generate PKE keypair */
    uint8_t dk_pke[MLKEM_K * MLKEM_POLYBYTES];
    kpke_keygen(kp->pk, dk_pke, d);

    /* Assemble full secret key: dk = (dk_pke || ek || H(ek) || z) */
    uint8_t *sk = kp->sk;
    memcpy(sk, dk_pke, MLKEM_K * MLKEM_POLYBYTES);
    sk += MLKEM_K * MLKEM_POLYBYTES;

    memcpy(sk, kp->pk, MLKEM_PUBLICKEYBYTES);
    sk += MLKEM_PUBLICKEYBYTES;

    mlkem_hash_h(sk, kp->pk, MLKEM_PUBLICKEYBYTES); /* H(ek) */
    sk += MLKEM_SYMBYTES;

    memcpy(sk, z, MLKEM_SYMBYTES); /* z for implicit rejection */

    /* Zeroize intermediates */
    memset(d, 0, sizeof(d));
    memset(z, 0, sizeof(z));
    memset(dk_pke, 0, sizeof(dk_pke));

    return 0;
}

/* ═════════════════════════════════════════════
 * ML-KEM.Encaps (FIPS 203 Algorithm 16)
 * ═════════════════════════════════════════════ */

int
mlkem_encapsulate(uint8_t ct[MLKEM_CIPHERTEXTBYTES],
                  uint8_t ss[MLKEM_SSBYTES],
                  const uint8_t pk[MLKEM_PUBLICKEYBYTES])
{
    uint8_t m[MLKEM_SYMBYTES];
    if (randombytes(m, MLKEM_SYMBYTES) != 0) return -1;

    /* m ← H(m) — ensures uniform even if RNG is biased */
    mlkem_hash_h(m, m, MLKEM_SYMBYTES);

    /* (K, r) ← G(m || H(pk)) */
    uint8_t h_pk[MLKEM_SYMBYTES];
    mlkem_hash_h(h_pk, pk, MLKEM_PUBLICKEYBYTES);

    uint8_t g_input[2 * MLKEM_SYMBYTES];
    memcpy(g_input, m, MLKEM_SYMBYTES);
    memcpy(g_input + MLKEM_SYMBYTES, h_pk, MLKEM_SYMBYTES);

    uint8_t g_output[64];
    mlkem_hash_g(g_output, g_input, sizeof(g_input));

    uint8_t *K_bar = g_output;       /* First 32 bytes */
    uint8_t *r     = g_output + 32;  /* Second 32 bytes */

    /* c ← Encrypt(ek, m, r) */
    kpke_encrypt(ct, pk, m, r);

    /* K ← H(K_bar || H(c)) */
    uint8_t h_ct[MLKEM_SYMBYTES];
    mlkem_hash_h(h_ct, ct, MLKEM_CIPHERTEXTBYTES);

    uint8_t kdf_input[2 * MLKEM_SYMBYTES];
    memcpy(kdf_input, K_bar, MLKEM_SYMBYTES);
    memcpy(kdf_input + MLKEM_SYMBYTES, h_ct, MLKEM_SYMBYTES);
    mlkem_kdf(ss, kdf_input, sizeof(kdf_input));

    /* Zeroize */
    memset(m, 0, sizeof(m));
    memset(g_input, 0, sizeof(g_input));
    memset(g_output, 0, sizeof(g_output));

    return 0;
}

/* ═════════════════════════════════════════════
 * ML-KEM.Decaps (FIPS 203 Algorithm 17)
 *
 * With implicit rejection: if re-encryption fails,
 * output J(z || c) instead of the real key.
 * Timing-safe throughout.
 * ═════════════════════════════════════════════ */

int
mlkem_decapsulate(uint8_t ss[MLKEM_SSBYTES],
                  const uint8_t ct[MLKEM_CIPHERTEXTBYTES],
                  const uint8_t sk[MLKEM_SECRETKEYBYTES])
{
    /* Parse sk = (dk_pke || ek || h_ek || z) */
    const uint8_t *dk_pke = sk;
    const uint8_t *ek     = sk + MLKEM_K * MLKEM_POLYBYTES;
    const uint8_t *h_ek   = ek + MLKEM_PUBLICKEYBYTES;
    const uint8_t *z      = h_ek + MLKEM_SYMBYTES;

    /* m' ← Decrypt(dk_pke, c) */
    uint8_t m_prime[MLKEM_SYMBYTES];
    kpke_decrypt(m_prime, ct, dk_pke);

    /* (K', r') ← G(m' || h(ek)) */
    uint8_t g_input[2 * MLKEM_SYMBYTES];
    memcpy(g_input, m_prime, MLKEM_SYMBYTES);
    memcpy(g_input + MLKEM_SYMBYTES, h_ek, MLKEM_SYMBYTES);

    uint8_t g_output[64];
    mlkem_hash_g(g_output, g_input, sizeof(g_input));

    uint8_t *K_bar_prime = g_output;
    uint8_t *r_prime     = g_output + 32;

    /* c' ← Encrypt(ek, m', r') */
    uint8_t ct_prime[MLKEM_CIPHERTEXTBYTES];
    kpke_encrypt(ct_prime, ek, m_prime, r_prime);

    /* Constant-time comparison: c == c' ? */
    int fail = ct_memcmp(ct, ct_prime, MLKEM_CIPHERTEXTBYTES);

    /* H(c) for KDF */
    uint8_t h_ct[MLKEM_SYMBYTES];
    mlkem_hash_h(h_ct, ct, MLKEM_CIPHERTEXTBYTES);

    /* ── Implicit rejection path ── */
    /* K_rej = J(z || c) — SHAKE-256 */
    uint8_t rej_input[MLKEM_SYMBYTES + MLKEM_CIPHERTEXTBYTES];
    memcpy(rej_input, z, MLKEM_SYMBYTES);
    memcpy(rej_input + MLKEM_SYMBYTES, ct, MLKEM_CIPHERTEXTBYTES);

    uint8_t K_rej[MLKEM_SSBYTES];
    mlkem_kdf(K_rej, rej_input, sizeof(rej_input));

    /* ── Derive real shared secret ── */
    uint8_t kdf_input[2 * MLKEM_SYMBYTES];
    memcpy(kdf_input, K_bar_prime, MLKEM_SYMBYTES);
    memcpy(kdf_input + MLKEM_SYMBYTES, h_ct, MLKEM_SYMBYTES);

    uint8_t K_real[MLKEM_SSBYTES];
    mlkem_kdf(K_real, kdf_input, sizeof(kdf_input));

    /* ── Constant-time select: fail ? K_rej : K_real ── */
    memcpy(ss, K_real, MLKEM_SSBYTES);
    ct_cmov(ss, K_rej, MLKEM_SSBYTES, (uint8_t)(fail != 0));

    /* Zeroize everything */
    memset(m_prime, 0, sizeof(m_prime));
    memset(g_input, 0, sizeof(g_input));
    memset(g_output, 0, sizeof(g_output));
    memset(ct_prime, 0, sizeof(ct_prime));
    memset(rej_input, 0, sizeof(rej_input));
    memset(K_rej, 0, sizeof(K_rej));
    memset(K_real, 0, sizeof(K_real));
    memset(kdf_input, 0, sizeof(kdf_input));

    return 0; /* Always returns 0 — implicit rejection is silent */
}

```
