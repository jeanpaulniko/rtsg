---
title: "RH as Local-Global Compatibility"
nav_title: "Local-Global"
version: "1.0.0"
last_updated: "2026-03-09"
status: "ACTIVE — structural identification"
---

# RH as Local-Global Compatibility

**Jean-Paul Niko · Sole Author**

*Analysis by @D_Claude (Chain D1, 2026-03-09)*

---

## The Identification

| Level | Object | Unitarity | Status |
|---|---|---|---|
| **Local** (each prime $p$) | Frobenius on $H^0(\mathbb{P}^1/\mathbb{F}_p)$ | Eigenvalue $= 1 \in S^1$ (on unit circle) | ✅ Trivially true |
| **Global** (all primes) | LP semigroup on $\mathcal{K}$ | Similar to unitary group | ⟺ **RH** |

The gap between local and global unitarity is EXACTLY the gap between the Weil conjectures (proved for varieties over $\mathbb{F}_q$, by Deligne 1974) and the classical Riemann Hypothesis (open for $\text{Spec}(\mathbb{Z})$).

## The Chain

$$\text{Frobenius eigenvalue } 1 \text{ at each } p$$
$$\downarrow \text{(Euler product)}$$
$$\zeta(s) = \prod_p (1-p^{-s})^{-1}$$
$$\downarrow \text{(LP scattering theory)}$$
$$\text{Zeros of } \zeta = \text{resonances of LP generator } B$$
$$\downarrow \text{(bridge equation)}$$
$$B^*K + K(B-1) = 0 \text{ with } K > 0 \text{ invertible } \iff \text{RH}$$
$$\updownarrow$$
$$B \text{ similar to skew-adjoint} \iff e^{tB} \text{ similar to unitary}$$

## The RTSG Reading

The BRST filter on $(S^2)^\mathcal{P}$ produces local unitarity automatically (Frobenius eigenvalue $= 1$ on $H^0$). The bridge equation asks whether local unitarity assembles into global unitarity.

In the language of the Langlands program: RH is the **automorphic-Galois compatibility** for the trivial motive $\mathbb{Q}(0)$ over $\text{Spec}(\mathbb{Z})$.

In RTSG language: RH is the statement that instantiation is globally coherent — the local instantiation rule (BRST at each prime) assembles into a globally unitary operator on the scattering space.

## What Would Close the Gap

A **motivic cohomology** for $\text{Spec}(\mathbb{Z})$ that:
1. Has a positive-definite inner product (Weil's "standard conjectures")
2. Has Frobenius acting unitarily
3. Has the correct L-function ($\zeta$) as its characteristic polynomial

This is the program of Deninger, Connes, and the standard conjectures. RTSG identifies the source space $(S^2)^\mathcal{P}$ as the candidate geometric object, and the BRST filter as the cohomological projection. What remains is constructing the global inner product.

---

*Jean-Paul Niko · RTSG BuildNet · smarthub.my · March 2026*
