---
title: "Photon Sphere — Inverted Oscillator Map"
nav_title: "Photon Sphere Oscillator"
last_updated: "2026-03-07"
status: "Novel formulation"
---

# Photon Sphere as Quantum Inverted Harmonic Oscillator

*Gemini, 2026-03-07 · Novel QS-to-oscillator mapping*

---

## Construction

At the photon ring of a black hole ($r = 3M$ Schwarzschild), null geodesics are unstable — they orbit but diverge exponentially under perturbation. The Penrose limit of the near-photon-ring metric yields an **inverted harmonic oscillator** potential:

$$V(x) = -\frac{1}{2}\omega^2 x^2$$

where $\omega$ is set by the generalized surface gravity of the photon ring:

$$\omega = \kappa_{\text{photon}} = \frac{1}{3\sqrt{3}M}$$

## RTSG Interpretation

The uninstantiated QS geodesics at the photon ring map to a quantum inverted harmonic oscillator. This yields:

1. **Lyapunov exponent** $\lambda = \omega = \kappa_{\text{photon}}$ directly from the oscillator frequency
2. **Quasi-normal modes** (QNMs) from the quantization of the inverted oscillator spectrum
3. The photon ring is a **QS resonance** — uninstantiated potentiality orbiting at the boundary between capture (instantiation into BH) and escape (instantiation into far-field PS)

## Chaos Bound Connection

The photon ring Lyapunov exponent satisfies:

$$\lambda_{\text{photon}} = \kappa_{\text{photon}} \leq \kappa_H$$

The event horizon has strictly higher surface gravity than the photon ring. This is the hierarchy: the horizon is the maximal chaos processor (CS bandwidth limit), the photon ring is a sub-maximal resonance.

## Connection to GRF Essay

!!! warning "Do NOT add to GRF 2026"
    The GRF essay deliberately avoids the photon sphere (attack surface identified by GPT-5.4 / o3 review). This formulation belongs in the cosmological vision paper or a standalone QNM paper.

## Relation to Prior Debate

See [Photon Sphere Debate](../papers/grf/photon_sphere_debate.md) — the inverted oscillator map resolves the earlier dispute by providing a clean derivation that doesn't mix local temperatures with system bounds.


---

## Generalized Surface Gravity at the Photon Sphere

*Gemini, 2026-03-07 · Extends the inverted oscillator map*

For null geodesics (massless QS states), the classical massive-particle bound $\lambda \leq \kappa_H$ is replaced by a generalized surface gravity evaluated at the photon sphere:

$$\kappa(r_{\text{ph}}) = \frac{1}{3\sqrt{3}M}$$

The instability of circular null geodesics dictates the **quasinormal mode (QNM) decay rate**. In the RTSG interpretation, the photon sphere is the specific **frequency filter** of the CS operator — it regulates the maximal bandwidth at which purely massless QS states can be localized and collapsed into PS geometry.

**QNM connection:** In the eikonal limit ($\ell \to \infty$), QNM frequencies satisfy:

$$\omega_{\text{QNM}} \approx \Omega_{\text{ph}} \ell - i\left(n + \frac{1}{2}\right)\kappa(r_{\text{ph}})$$

where $\Omega_{\text{ph}}$ is the orbital frequency at the photon sphere. The imaginary part — the decay rate — is set by $\kappa(r_{\text{ph}})$, confirming the photon sphere as the CS bandwidth regulator for massless modes.
