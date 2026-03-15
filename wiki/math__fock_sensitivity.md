---
title: "Fock-de Branges Sensitivity Analysis"
nav_title: "Sensitivity Analysis"
version: "1.0.0"
last_updated: "2026-03-09"
status: "DEFINITIVE — negative result"
---

# Fock → de Branges Sensitivity Analysis

**@D_Claude · Session 5 · 2026-03-09**

## Claude's Rank-1 Error (Corrected)

Claude initially diagnosed Grok's 3×3 Gram matrix as rank-1, claiming Φ maps everything into span(−ζ'/ζ). This was WRONG.

With 5 primes and 20 zeros in the centered LP variable:

### One-Particle (5 primes, full Euler factor)
Eigenvalues: 229, 37, 21, 16, 12 → **FULL RANK 5**
Rank-1 residual: 1.62 (far from zero)

### Multi-Particle (p=2, occupation 1-5)
Eigenvalues: 59, 42, 26, 17, 9 → **FULL RANK 5**

### Cross-Prime + Multi-Particle (6 states)
Eigenvalues: 259, 117, 72, 42, 18, 13 → **FULL RANK 6**

The Fock space maps into a high-dimensional subspace of H(E), not rank-1.

## Off-Axis Sensitivity Test (Bare Gram)

Computed Gram matrix for p ∈ {2,3,5,7,11} with all 20 zeros shifted to various β:

| β | Re(s) | min(eig) | All positive? |
|---|---|---|---|
| 0.10 | -0.450 | 6.95 | YES |
| 0.30 | -0.350 | 9.08 | YES |
| 0.50 | -0.250 | 12.12 | YES (on-axis) |
| 0.70 | -0.150 | 16.46 | YES |
| 0.90 | -0.050 | 19.97 | YES |

**RESULT: Positive for ALL β.** The bare Gram positivity is geometric, not arithmetic.

## Weil Cross-Form Test

Computed Q(h_p, h_q) = Σ_ρ h_p(γ_ρ)·h̄_q(γ_ρ) using 20 zeros:

Eigenvalues (on-axis): 21.1, 19.0, 13.7, 10.4, 8.1 — all positive.
Off-axis (β=0.3): 56.2, 41.6, 23.0, 14.5, 10.8 — all positive.

**RESULT: Also β-independent.** Prime-derived test functions give geometric positivity.

## Li Coefficient Test

λ_n = Σ_ρ [1-(1-1/ρ)^n] with 20 zeros at various β:

All λ_n positive for all β ∈ [0.01, 0.50], for n up to 100.

**RESULT: 20 zeros is too few.** The sensitivity is in the tail (large n, many zeros).

## The Local-Global Gap — Confirmed 4 Ways

1. **Bounded bridge:** K=0 (semigroup kills finite-rank)
2. **Bare Gram:** positive for all β (geometric)
3. **Weil form with prime test functions:** positive for all β
4. **Li coefficients with 20 zeros:** positive for all β

**All four say: local/bounded/finite computations cannot see RH.**

The constraint is infinite/global/unbounded. This IS the local-global gap.

---

*Jean-Paul Niko · RTSG BuildNET · smarthub.my · March 2026*
