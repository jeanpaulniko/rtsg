---
title: "Module 2: ML-KEM-1024 + X25519 Hybrid KEM"
nav_title: "M2: PQC Crypto"
---

# Module 2: Post-Quantum Hybrid Key Encapsulation

**Files:** `src/crypto/ntt.c`, `poly.c`, `symmetric.c`, `kem.c`, `hybrid_kem.c`  
**Headers:** `include/mlkem_params.h`, `qrnsp_crypto.h`  

## ML-KEM-1024 (FIPS 203)

NIST Level 5 post-quantum KEM based on Module Learning-with-Errors (MLWE).

**Parameters:** n=256, k=4, q=3329, η₁=η₂=2, d_u=11, d_v=5

**Wire sizes:**
- Public key: 1568 bytes (ML-KEM) + 32 bytes (X25519) = **1600 bytes**
- Ciphertext: 1568 + 32 = **1600 bytes**
- Shared secret: **32 bytes**

## NTT Core

Cooley-Tukey forward (7 layers), Gentleman-Sande inverse. Precomputed zetas in Montgomery form (ζ=17, R=2^16). Scalar reference + AVX-512 fast path (32 coefficients per `__m512i` lane).

## Hybrid Combiner

```
ss = SHA3-256(ss_mlkem || ss_x25519 || ct_mlkem || pk_x25519_peer)
```

Both ML-KEM AND X25519 must be broken to recover the shared secret.

## Implicit Rejection (Algorithm 17)

If ciphertext tampered → re-encryption check fails → output `J(z || c)` instead of real key. Constant-time throughout via `ct_cmov`. Adversary cannot distinguish rejection from success.

## Zero-Dependency SHA3

Complete Keccak-f[1600] permutation: SHA3-256 (H), SHA3-512 (G), SHAKE-256 (J/PRF), SHAKE-128 (XOF). Production target: swap in XKCP for 4× throughput.
