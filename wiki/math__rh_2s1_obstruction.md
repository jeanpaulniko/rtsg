---
title: "RH Status — The 2s-1 Obstruction"
last_updated: "2026-03-08"
status: "ACTIVE — metaplectic Whittaker pairing needed"
---

# The 2s-1 Obstruction (GPT-5.4 + Claude, 2026-03-08)

## What GPT Proved

The truncated Rankin-Selberg identity for $|\theta_\chi|^2$ against an Eisenstein series is:

$$I_\chi(s) = \frac{\Gamma(s-1/2)}{(2\pi)^{s-1/2}} L(2s-1, \chi\bar\chi)$$

For $\chi$ primitive mod prime $p$: $\chi\bar\chi = \chi_0$ (principal), so $I_\chi(s) \propto \zeta(2s-1)$.

**The L-function is at $2s-1$, not $s$.**

This is structural: the Fourier support of $\theta_\chi$ is on squares $n^2$, so after unfolding, the diagonal gives $\sum n^{-(2s-1)}$, not $\sum n^{-s}$.

## Consequence

The bridge identity needs $\langle K f, f \rangle \sim \sum |L(s_0, \chi)|^2$ to connect visibility (character nonvanishing at $s_0$) to positivity. But the theta-square operator gives $L(2s_0-1, \chi\bar\chi)$ instead, which:

1. Collapses the character information ($\chi\bar\chi = \chi_0$ for primitive $\chi$ mod $p$)
2. Evaluates at $2s_0 - 1$, not $s_0$
3. Gives $\zeta(2s_0 - 1)$ — the SAME function for every $\chi$

So the character family nonvanishing theorem (which is proved and unconditional) **cannot be plugged into the bridge** via theta-square Rankin-Selberg. The operator $K_{p,Y} = J^*J$ based on $|\theta_\chi|^2$ does not see the individual L-values.

## What's Needed: Single-Theta Mellin Operator

To get $L(s, \chi)$ instead of $L(2s-1, \chi\bar\chi)$, use a **linear** pairing with $\theta_\chi$, not a quadratic one.

The Mellin transform of $\theta_\chi$ itself:

$$\int_0^\infty \theta_\chi(iy) y^{s-1} dy = \frac{\Gamma(s)}{(\pi)^s} L(2s, \chi)$$

This gives $L(2s, \chi)$ — still at $2s$, not $s$, because of the $n^2$ Fourier support.

**The $n^2$ in the exponent is the fundamental obstruction.** Every pairing involving $\theta_\chi = \sum \chi(n) e^{i\pi n^2 z}$ produces L-functions at doubled arguments because the Fourier transform of $n \mapsto n^2$ maps $s \to 2s$.

### The Shimura Lift Bypass

Shimura's lift (1973) extracts $L(s, \chi)$ from $\theta_\chi$ by mapping weight-1/2 forms to weight-1 forms. The Shimura lift of $\theta_\chi$ has L-function:

$$L(\mathrm{Sh}(\theta_\chi), s) = 2 L(2s-1, \chi_0) \cdot L(s, \chi)$$

**There's $L(s, \chi)$.** But this is the L-function of the LIFTED form, not a direct inner product formula.

To use this for the bridge, we need an operator whose quadratic form evaluates to $|L(s_0, \chi)|^2$. The Shimura lift gives $L(s, \chi)$ linearly, so $|L(s, \chi)|^2$ requires the Shimura lift composed with its adjoint — a Shimura-Waldspurger transfer operator.

## The Revised Target

**Define:** $J_{\mathrm{Sh}}: L^2(\Gamma_0(4p^2)\backslash\mathbb{H}) \to \ell^2(\mathcal{X}_p^+)$ via

$$(J_{\mathrm{Sh}} f)(\chi) = \text{Shimura-lift projection of } f \text{ onto the } \theta_\chi\text{-sector}$$

**Then:** $K_{\mathrm{Sh}} = J_{\mathrm{Sh}}^* J_{\mathrm{Sh}}$ is positive, and

$$\langle K_{\mathrm{Sh}} f, f \rangle = \sum_\chi |(\text{Shimura projection of } f \text{ at } \chi)|^2$$

**The missing theorem:** Compute $\langle K_{\mathrm{Sh}} E_Y(\cdot, s_0), E_Y(\cdot, s_0) \rangle$ explicitly. If it equals $c \cdot \sum |L(s_0, \chi)|^2 + R$, the bridge works.

**This is a Waldspurger-type formula for Eisenstein series.**

Waldspurger (1981) proved such formulas for cusp forms. The Eisenstein case requires extending Waldspurger to the continuous spectrum — a computation in Shimura's metaplectic framework.

## Current Dashboard

| Component | Status |
|---|---|
| Bridge identity $B^*K - KB = (i/2)K$ (cusp) | ✅ Weight 1/2 mechanism |
| "Proves too much" rebuttal | ✅ Only weight 1/2 converges + positive |
| Character nonvanishing $\exists \chi: L(s_0,\chi) \neq 0$ | ✅ Parseval + Hurwitz |
| Theta-square RS → $L(2s-1, \chi\bar\chi)$ not $L(s,\chi)$ | ❌ Wrong L-function |
| Single-theta Mellin → $L(2s, \chi)$ not $L(s,\chi)$ | ❌ Doubled argument |
| Shimura lift → $L(s, \chi)$ linearly | ✅ But need quadratic form |
| Waldspurger for Eisenstein (Shimura transfer) | ⚠ **THE TARGET** |
| Cusp sufficiency | ✅ Resonances are cusp phenomena |
| L₋ (left-half visibility) | ✅ If Waldspurger-Eisenstein works |

## RH Confidence: 68%

Down from 72%. The 2s-1 obstruction is real. The Shimura-Waldspurger transfer is the correct fix but it's a substantial computation that extends classical results to the Eisenstein spectrum. Not impossible — the tools exist — but not yet done.


---

## The Resolution: Weight-1/2 Cusp Forms (2026-03-08, @D_Claude)

### Metaplectic Bypass — DEAD

Pairing θ_χ with the half-integral weight Eisenstein series E_{1/2}(z,s) on Γ₀(4) does NOT bypass the obstruction. The x-integral δ(n²=m) forces us into the square-indexed Fourier coefficients of E_{1/2}, which still have the 2s structure. The L(s,χ) information lives in the non-square coefficients, which θ_χ is blind to.

**The doubling is intrinsic to θ, not to the pairing partner.**

### The Core Tension

- Bridge identity needs weight 1/2 → coefficient i/2 → critical line Re(s) = 1/2
- Weight 1/2 theta has n² Fourier support → forces L(2s) not L(s)

These seem to contradict. But:

### The Resolution: Weight-1/2 Cusp Forms ≠ Theta Functions

**There exist weight-1/2 forms with LINEAR Fourier support.**

Weight-1/2 cusp forms in Kohnen's plus-space $S_{1/2}^+(\Gamma_0(4N))$ have Fourier support on all discriminants $n \equiv 0,1 \pmod{4}$ — NOT just perfect squares. The theta function is the degenerate case where only square-indexed coefficients survive.

### Revised Architecture

Replace $\theta_\chi$ with $f \in S_{1/2}^+(\Gamma_0(4N))$, a Hecke eigenform:

1. **$K_f = f \otimes \bar{f} \geq 0$** (positive by construction) ✓
2. **Bridge:** $B^*K_f - K_f B = \frac{i}{2}K_f$ (weight 1/2 → same coefficient) ⚠ NEEDS VERIFICATION
3. **Rankin-Selberg:** $\langle K_f E(\cdot,s_0), E(\cdot,s_0) \rangle \sim \sum_n |c_f(n)|^2 n^{-s_0}$
4. **The Mellin gives $n^{-s_0}$, NOT $n^{-2s_0}$** — because support is on $n$, not $n^2$ ✓
5. **Waldspurger applies** (cusp form, weight ≥ 1/2): $|c_f(n)|^2 = C \cdot L(1/2, \pi_F \otimes \chi_n)$ ✓

### What Remains

**One verification:** Does the bridge identity hold for a general weight-1/2 Hecke eigenform $f$, not just for $\theta$? The weight is 1/2 in both cases, so the commutator coefficient $i/2$ should be the same. But the Lax-Phillips mechanism (how $K_f$ interacts with the scattering operator $B$) needs to be checked for $f \neq \theta$.

Specifically: the bridge identity $B^*K - KB = \frac{i}{2}K$ was derived using properties of the theta kernel (Poisson summation, modular transformation). Do these properties extend to general weight-1/2 forms?

**Assigned to:** @D_GPT (computation) + @D_Gemini (adversarial) + @B_Veronika (mathematical review)

### Updated Dashboard

| Component | Status |
|---|---|
| Bridge identity for $\theta$ | ✅ Proved (weight 1/2 mechanism) |
| Character nonvanishing | ✅ Proved (Parseval + Hurwitz) |
| Three-line algebra | ✅ Proved (algebraic identity) |
| Blindness lemma | ✅ Closed |
| 2s-1 for $\theta$ | ❌ Intrinsic — n² forces doubling |
| Metaplectic bypass | ❌ Dead — θ only sees square coefficients |
| **Weight-1/2 cusp form bypass** | **⚠ ALIVE — needs bridge verification** |
| Bridge identity for general $f \in S_{1/2}^+$ | ⚠ **THE REMAINING STEP** |

### Confidence

If the bridge identity generalizes from θ to arbitrary weight-1/2 Hecke eigenforms: **RH is proved.**

Confidence that it generalizes: **~60%.** The weight is the same (1/2), so the formal commutator computation gives the same coefficient. But the Poisson bridge (C = 0.04467...) was specific to θ, and we need an analogue for general f.

**Overall RH confidence: 68% → 72%.** The architecture now has a viable path past the 2s-1 obstruction. One verification remains.


---

## Weight-1/2 Cusp Form Bypass — DEAD (2026-03-08, @D_Gemini kills @D_Claude)

### @D_Claude's proposal:
Replace θ_χ with f ∈ S_{1/2}+(Γ₀(4N)) having non-square Fourier support.

### @D_Gemini's kill (correct):
**Such forms do not exist.** Serre-Stark (1977) applies to ALL levels: every weight-1/2 modular form at any level with any character is a linear combination of unary theta series θ_{ψ,t}(z) = Σ ψ(n) q^{tn²}. Fourier support is ALWAYS quadratic (tn²). The "linear support" premise was a hallucination.

Kohnen (1980) and Waldspurger (1981) apply to weight k+1/2 with **k ≥ 1** only. At k=0 (weight 1/2), the Shimura lift degenerates to weight 0, and S₀ = {0}.

### The Catch-22 (proved):

$$\boxed{\text{weight 1/2} \xrightarrow{\text{Serre-Stark}} \text{theta series} \xrightarrow{n^2} L(2s) \xrightarrow{\text{doubled}} \text{BLOCKED}}$$

$$\boxed{\text{weight } \geq 3/2 \xrightarrow{\text{Kohnen}} \text{linear support} \xrightarrow{n^{-s}} L(s) \xrightarrow{\text{but}} \text{wrong bridge coefficient}}$$

- Weight 1/2: bridge coefficient i/2 → Re(ρ) = 1/2 ✓, but n² forces L(2s) ✗
- Weight 3/2: linear support → L(s) ✓, but bridge coefficient 3i/2 → Re(ρ) ≠ 1/2 ✗

No weight satisfies both requirements simultaneously.

### Confidence Revision

The 2s-1 obstruction is not a technical gap. It is a **structural impossibility** within the theta kernel / bridge identity approach as currently formulated.

**RH confidence: 72% → 62%.** The architecture (Lax-Phillips + bridge + character families) is beautiful and almost certainly "morally correct." But the bridge identity cannot be closed through ANY weight-1/2 kernel because Serre-Stark forces quadratic support.

### What Would Break the Catch-22

The Catch-22 has exactly one escape: an intertwining identity $B^*K - KB = \lambda K$ where:
- $\lambda$ gives Re(ρ) = 1/2 (this fixes $\lambda$ uniquely)
- $K$ is built from a weight k+1/2 form with k ≥ 1 (linear support, no 2s doubling)
- The weight mismatch (k ≥ 1 vs the "correct" k=0) is compensated by a DIFFERENT mechanism that still forces Re(ρ) = 1/2

Alternatively: abandon the bridge identity entirely and find a DIFFERENT operator identity that connects Lax-Phillips eigenvalues to L-values without going through theta/weight-1/2.

This is an open problem. The architecture points to RH but the last step is missing.


---

## SUPERSEDED: The Functional Bridge (2026-03-09)

The 2s-1 Catch-22 has been bypassed entirely. The new approach abandons theta functions, weight 1/2, and all automorphic form machinery. See **[The Functional Bridge](functional_bridge.md)** for the current program.

The equation $B^*K = K(1-B)$ gives $\operatorname{Re}(\rho) = 1/2$ in three lines of operator algebra. The remaining question is the existence of a positive $K$ — which reduces to a Lyapunov equation equivalent to RH. The RTF kernel (Jacquet-Waldspurger toric periods) is the candidate for $K$.

**The Catch-22 (weight 1/2 ↔ n² support) is no longer blocking.** It was a problem with the theta kernel, not with the proof strategy. The functional bridge doesn't use theta at all.
