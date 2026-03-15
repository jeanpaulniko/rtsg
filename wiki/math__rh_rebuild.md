---
title: "RH Chain Rebuild — Single Level Architecture"
last_updated: "2026-03-08"
status: "ACTIVE — one theorem remains"
---

!!! danger "SUPERSEDED (2026-03-09)"
    This page predates the bounded bridge no-go theorem. See `math/functional_bridge.md` v5.0 and `math/bounded_bridge_nogo.md` for current state. RH confidence: 25%.



# RH Chain Rebuild (GPT-5.4 Pro, 2026-03-08)

The adversarial review killed the old proof chain. GPT-5.4 rebuilt it.

---

## What Died

| Component | Kill | Killer |
|---|---|---|
| $K^{\text{full}} = \sum_{\text{all }\chi} \theta_\chi \otimes \bar\theta_\chi$ | Divergent sum, varying levels | GPT-5.4 (V2) |
| $y\partial_y(y^{1/2}) = \frac{1}{2}y^{1/2}$ as global identity | Trivial calculus, not operator algebra | Gemini (V4) |
| Three-line algebra on generalized eigenfunctions | Boundary terms diverge under truncation | GPT-5.4 (V3) |
| Cusp-local → global eigenvalue constraint | $Bf = \mu f$ is global, commutator is cusp-local | SuperGrok |
| "Proves too much" for weight $k \neq 1/2$ | Weight-4 cusp forms: K=0. Weight-4 Eisenstein: $\langle K,f\rangle = \infty$ | **REBUTTED** (only weight 1/2 works) |

## What Survived

| Component | Status |
|---|---|
| ζ-zeros = scattering resonances on $\Gamma_0(N)\backslash\mathbb{H}$ for all $N$ | ✅ Verified (V1) |
| Character-family nonvanishing (Parseval + Hurwitz) | ✅ Proved unconditionally |
| Weight 1/2 is the unique sweet spot | ✅ Convergence + positivity + nontrivial coefficient |
| "Proves too much" rebuttal | ✅ No other weight has all three properties |

## The Rebuilt Architecture

### Fix 1: Single prime level $4p^2$

For a fixed odd prime $p$, all even primitive characters $\chi \bmod p$ give theta series $\theta_\chi$ of weight $1/2$ and level $4p^2$. The ζ-zeros appear as resonances on $\Gamma(4p^2)\backslash\mathbb{H}$. Everything on one surface.

### Fix 2: Same-space positive operator

$$K_{p,Y} = J_{p,Y}^* J_{p,Y}$$

where $J_{p,Y}: \mathcal{E}_Y \to \ell^2(\mathcal{X}_p^+)$ is the truncated Rankin-Selberg transform. Automatically positive, lives on the same Hilbert space as the resonance problem.

### Fix 3: Even-character Parseval

For Re$(s_0) > 0$, the even-character mean square $M_p^+(s_0) > 0$ for large $p$. Gives a same-level visibility input.

### Fix 4: Corrected intertwiner

$$J_{p,Y} B = (A_{p,Y} - i/4) J_{p,Y} + \mathcal{R}_{p,Y}$$

with $A_{p,Y}$ self-adjoint and $\mathcal{R}_{p,Y} \to 0$ in the resonance limit.

## The One Remaining Theorem

Prove, for the truncated Eisenstein packet $E_Y(\cdot, s_0)$:

$$\langle K_{p,Y} E_Y(\cdot,s_0), E_Y(\cdot,s_0) \rangle = c_p(s_0,Y) \sum_{\chi \in \mathcal{X}_p^+} |L(s_0,\chi)|^2 + R_p(s_0,Y)$$

with $c_p(s_0,Y) > 0$ and $R_p(s_0,Y)$ controlled so it doesn't cancel the main term at a resonance.

**And:** Prove $\mathcal{R}_{p,Y} \to 0$ in the resonance limit.

## If Both Are Proved

The three-line contradiction becomes legitimate:
1. Assume Re$(\rho) < 1/2$
2. Even-character nonvanishing gives $\langle K_{p,Y} f, f \rangle > 0$
3. Corrected intertwiner gives Im$(\mu) = -1/4$
4. Therefore Re$(\rho) = 1/2$. Contradiction.

## RH Confidence: 78%

Down from 92%. The architecture is cleaner but the remaining theorem is genuinely hard — it's a Maass-Selberg / Rankin-Selberg computation on truncated packets at half-integral weight. Standard tools exist (Iwaniec Ch. 7, Shimura half-integral weight theory) but the computation has not been done.

## Backup Route

Burnol's adelic Lax-Phillips framework (arXiv:math/0001013) may be the natural home for this computation, as the metaplectic theta theory is cleaner adelically than on a single modular surface.
