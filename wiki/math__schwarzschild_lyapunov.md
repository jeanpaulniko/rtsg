---
title: "Schwarzschild Geodesics & Lyapunov Exponent"
version: "1.0.0"
last_updated: "2026-03-05"
status: current
---

# Schwarzschild Geodesics & Lyapunov Exponent

## Painlevé-Gullstrand Setup

$$ds^2 = -\!\left(1 - \frac{2M}{r}\right)dT^2 + 2\sqrt{\frac{2M}{r}}\,dT\,dr + dr^2 + r^2\,d\Omega^2$$

Regular at r = 2M (no coordinate singularity). Time T = PG time.

## Derivation: λ = κ

Outgoing radial null geodesic: dr/dT = 1 − √(2M/r).

Near horizon: let r = 2M + ε, ε ≪ 2M.

$$\frac{d\varepsilon}{dT} = \kappa\varepsilon + O(\varepsilon^2), \qquad \kappa = \frac{1}{4M}$$

Solution: ε(T) = ε(0)·e^{κT}

**Lyapunov exponent:**

$$\lambda = \kappa = \frac{1}{4M}$$

!!! warning "Corrected Error (v5 → v6)"
    Earlier drafts contained a contradiction: claiming λ = 0 at the horizon (S-N bifurcation) while also claiming λ = κ > 0 (MSS saturation). These are mutually exclusive. Resolution: λ = κ > 0 is the correct statement for radial null congruences. The bifurcation (λ = 0 transition) is a *different* physical regime — the interior attractor.

## MSS Comparison

| Surface | λ | Status |
|---|---|---|
| Event horizon r = 2M | κ = 1/(4M) ≈ 0.25/M | **MSS saturated** ← unique |
| Photon sphere r = 3M | 1/(3√3 M) ≈ 0.192/M | Below MSS bound |
| Asymptotic r → ∞ | 0 | No divergence |

## Thermodynamic Reinterpretation

| Classical expression | Lyapunov reading |
|---|---|
| T_H = κ/(2π) | Thermal scale of geodesic chaos |
| S_BH = ∫dM/T_H | Integral of reciprocal chaos rate ∫(2π/λ)dM |
| Negative heat capacity | Smaller M → larger λ → faster scrambling |

## MSS Bound Statement

$$\lambda_{\text{OTOC}} \leq 2\pi T$$

For Schwarzschild: λ = κ = 2πT_H. **Exactly saturated at horizon and only at horizon.**
