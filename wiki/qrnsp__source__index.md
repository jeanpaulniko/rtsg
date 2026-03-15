---
title: "QR-NSP Source Code"
nav_title: "Source Code"
---

# QR-NSP Source Code

**9,593 lines of pure C** — zero external dependencies (except libbpf for XDP).

## Headers (`include/`)

| File | Module | Description |
|------|--------|-------------|
| `qrnsp.h` | M1 | XDP ring buffer, slot structures |
| `mlkem_params.h` | M2 | ML-KEM-1024 FIPS 203 parameters |
| `qrnsp_crypto.h` | M2 | Hybrid KEM public API |
| `qrnsp_aead.h` | M3 | AES-256-GCM interface |
| `qrnsp_stego.h` | M3 | PADDING injection API |
| `qrnsp_jitter.h` | M4 | Timing channel API |
| `qrnsp_deniable.h` | M5 | Deniable encryption API |
| `qrnsp_fallback.h` | M6 | TCP fallback + chaffing API |
| `qrnsp_morph.h` | M7 | Traffic morphing API |
| `qrnsp_orchestrator.h` | M8 | Unified pipeline API |

## Source (`src/`)

| File | Lines | Description |
|------|-------|-------------|
| `xdp/qrnsp_xdp.c` | 297 | eBPF QUIC packet classifier |
| `daemon/daemon.c` | 455 | Userspace ring buffer consumer |
| `crypto/ntt.c` | 416 | NTT (scalar + AVX-512) |
| `crypto/poly.c` | 347 | Polynomial ops, CBD, compression |
| `crypto/symmetric.c` | 269 | Keccak-f[1600], SHA3, SHAKE |
| `crypto/kem.c` | 441 | ML-KEM-1024 KeyGen/Encaps/Decaps |
| `crypto/hybrid_kem.c` | 377 | X25519 + ML-KEM combiner |
| `aead/aes256gcm.c` | 509 | AES-256-GCM (scalar + AES-NI) |
| `stego/inject.c` | 430 | QUIC PADDING injection engine |
| `jitter/jitter.c` | 667 | Spread-spectrum timing channel |
| `deniable/deniable.c` | 627 | Multi-password hidden volumes |
| `fallback/fallback.c` | 503 | TCP stego + state machine |
| `morph/morph.c` | 380 | Statistical traffic morphing |
| `orchestrator/orchestrator.c` | 408 | Pipeline controller |

## Tests (`tests/`)

| File | Tests | Coverage |
|------|-------|----------|
| `test_crypto.c` | 5 | NTT, ML-KEM round-trip, implicit rejection, hybrid KEM, throughput |
| `test_stego.c` | 5 | AEAD, full pipeline, multi-message, clean packet, tamper detection |
| `test_jitter.c` | 5 | Clean decode, noisy decode (2 levels), long message, bandwidth |
| `test_deniable.c` | 6 | Single volume, dual volume, honey-enc, χ² randomness, diversity, KDF perf |
| `test_pipeline.c` | 7 | Chaff/winnow, TCP timestamps, state machine, morphing, profiles, H2 padding, orchestrator |

## Build

```bash
make all        # Build everything
make test       # Run all 28 tests
make clean      # Remove build artifacts
```
