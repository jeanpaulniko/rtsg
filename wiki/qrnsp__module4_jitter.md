---
title: "Module 4: Temporal Jitter Shaping"
nav_title: "M4: Timing Channel"
---

# Module 4: Spread-Spectrum Timing Channel

**Files:** `src/jitter/jitter.c`  
**Header:** `include/qrnsp_jitter.h`  

## Concept

Encodes binary data into inter-packet arrival times (IPAT). Works even when packet payloads are unmodifiable. Orthogonal to Module 3 — operates on a different dimension of the traffic.

## Signal Chain

**TX:** payload → length prefix → FEC (rate 1/3) → Manchester encoding → spread-spectrum chipping (Gold code, 8 chips/bit) → Gaussian-noised delay schedule

**RX:** timestamps → IPAT → Barker-13 preamble correlation → dechip → Manchester decode → FEC majority vote → payload

## Key Design

- **Gold codes** (degree-7 LFSRs): near-ideal cross-correlation, 8 chips/bit = 9dB processing gain
- **Barker-13 preamble**: optimal autocorrelation for synchronization
- **Manchester encoding**: clock recovery, eliminates baseline wander
- **Gaussian noise**: N(0, σ²) with σ=800μs makes individual delays indistinguishable

## Bandwidth

| Payload | Time | Effective bps |
|---------|------|---------------|
| 1 byte | ~3.8s | ~2.1 |
| 8 bytes | ~17s | ~3.7 |
| 32 bytes (key) | ~63s | ~4.0 |

Low bandwidth — but sufficient for signaling, key exchange, and "I need help" beacons.
