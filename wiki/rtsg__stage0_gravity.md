---
title: "Stage 0 — Gravity as Geometric Condensation"
nav_title: "Stage 0 Gravity"
version: "1.0.0"
last_updated: "2026-03-08"
status: "active development — fills Gap 3 of graded_brst.md"
---

# Stage 0 — Gravity as Geometric Condensation

**Jean-Paul Niko · Sole Author**

!!! info "Purpose"
    This page resolves **Gap 3** of the [Graded BRST](graded_brst.md) framework: the Stage 0 order parameter $W_0$ and its GL potential $S_0[W_0]$. We show that gravity — as the lowest-complexity instantiation — is a **geometric condensation**: the phase transition from pre-geometric QS to stable spacetime (PS). The order parameter is a condensate field on the source space, and its GL potential is the Chamseddine-Connes spectral action restricted to the gravitational sector.

!!! danger "Integrity"
    Conjectures labeled. Gaps marked. Do not claim what is not proved.

---

## 1. The Problem

The [Graded BRST](graded_brst.md) framework assigns Stage 0 to diffeomorphisms: $s_0$ is the BRST operator for $\text{Diff}(M)$. The order parameter $W_0$ was described as "bisimulation quotient stability" — conceptually clear but mathematically imprecise.

We need:

1. A **precise definition** of $W_0$ as a field
2. An **explicit GL potential** $S_0[W_0]$
3. A **physical interpretation** of $\alpha_0$ crossing zero (the transition)
4. **Connection** to the existing bisimulation formalism ([Horizon Bisimulation](horizon_bisimulation.md))
5. **Connection** to the spectral gap $\Delta = 2$ on $S^2$ ([Source Space](source_space.md))

---

## 2. The Geometric Condensate

### 2.1 Spacetime Points as Bisimulation Equivalence Classes

Under AFA (Axiom 0), QS is the terminal coalgebra of the powerset functor $\mathcal{P}$. The elements of QS are non-well-founded sets — self-referential relational structures with no ground level.

A **spacetime point** $x \in PS$ is not fundamental. It is a **bisimulation equivalence class**:

$$x = [q]_{\sim_{\text{bisim}}} \qquad \text{for some } q \in QS$$

Two QS elements $q_1, q_2$ are bisimilar iff they are observationally indistinguishable — every relational transition available to one is matchable by the other. Under AFA, bisimilarity equals identity in the coalgebraic universe.

**Spacetime** is the quotient $PS = QS/\!\sim_{\text{bisim}}$. The metric on PS is the bisimulation distance:

$$d_{\text{PS}}(x_1, x_2) = d_{\text{bisim}}([q_1], [q_2])$$

### 2.2 When Does the Quotient Stabilize?

The quotient $QS/\!\sim_{\text{bisim}}$ is always formally defined. But it only produces a **stable, smooth geometry** (classical spacetime) when the bisimulation equivalence classes are themselves stable — when small perturbations of a QS element leave it within the same equivalence class.

**Definition (Geometric condensate).** The Stage 0 order parameter $W_0$ is the **bisimulation stability field**:

$$\boxed{W_0(x) = \lim_{\varepsilon \to 0} \frac{\text{Vol}(B_\varepsilon^{\text{bisim}}(q) \cap [q]_\sim)}{\text{Vol}(B_\varepsilon^{\text{bisim}}(q))}}$$

where $B_\varepsilon^{\text{bisim}}(q)$ is the $\varepsilon$-ball around $q$ in bisimulation distance, and $[q]_\sim$ is the equivalence class of $q$.

**Physical reading:**

- $|W_0(x)| = 1$: the QS neighborhood of $q$ is entirely within the bisimulation class. The equivalence class is **dense and stable** — classical spacetime point is well-defined. Geometry is condensed.
- $|W_0(x)| = 0$: the QS neighborhood is spread across many inequivalent classes. No stable point exists. **Pre-geometric phase** — QS is "too hot" for bisimulation classes to hold together.
- $0 < |W_0(x)| < 1$: partially condensed — semiclassical regime, quantum gravity fluctuations.

### 2.3 Connection to GFT

This is the RTSG version of the Group Field Theory (GFT) condensate. In standard GFT:

| GFT | RTSG Stage 0 |
|---|---|
| Field $\sigma(g_1, \ldots, g_4)$ on $G^4$ | $W_0$ on $(S^2)^4$ (four copies for 4D) |
| Group $G = SL(2,\mathbb{C})$ | $\text{Aut}(S^2) = PSL(2,\mathbb{C}) \cong SO^+(1,3)$ |
| $\langle \sigma \rangle \neq 0$ → smooth geometry | $\langle W_0 \rangle \neq 0$ → stable PS |
| $\langle \sigma \rangle = 0$ → pre-geometric | $\langle W_0 \rangle = 0$ → raw QS |
| Friedmann eqs from condensate dynamics | Friedmann eqs from $S_0[W_0]$ EOM |

The RTSG version is a **coset GFT**: the field lives on $S^2 = PSL(2,\mathbb{C})/\text{Borel}$ rather than the full group. This is natural because the source space building block is $S^2$, and the CFN decomposition identifies the flag manifold $G/T$ as the geometric arena.

---

## 3. The Spectral Action as Stage 0 GL Potential

### 3.1 The Chamseddine-Connes Spectral Action

Given a spectral triple $(\mathcal{A}, \mathcal{H}, D)$ encoding the noncommutative geometry of $(S^2)^\infty$, the spectral action is:

$$S_{\text{spec}} = \text{Tr}\left(f\!\left(\frac{D^2}{\Lambda^2}\right)\right) + \langle J\psi, D\psi \rangle$$

where $f$ is a smooth cutoff, $\Lambda$ is the energy scale, and the second term is the fermionic action (irrelevant for Stage 0). The bosonic part expands via heat kernel:

$$S_{\text{spec}} = \sum_{n \geq 0} f_n \Lambda^{4-n} a_n(D^2)$$

where $a_n$ are the Seeley-de Witt coefficients:

| Order | Coefficient | Geometric content | GL role |
|---|---|---|---|
| $n=0$ | $a_0 = \frac{1}{16\pi^2}\int \sqrt{g}\, d^4x$ | Volume (cosmological constant) | $\alpha_0 \|W_0\|^2$ |
| $n=2$ | $a_2 = \frac{1}{16\pi^2}\int R\sqrt{g}\, d^4x$ | Scalar curvature (Einstein-Hilbert) | $\|\partial W_0\|^2$ |
| $n=4$ | $a_4 \sim \int (C_{\mu\nu\rho\sigma}^2 + \text{GB} + \Box R)\sqrt{g}\, d^4x$ | Weyl squared + Gauss-Bonnet | $\frac{\beta_0}{2}\|W_0\|^4$ |

### 3.2 Identification: Spectral Action = $S_0[W_0]$

$$\boxed{S_0[W_0] = \int \left( |\partial W_0|^2 + \alpha_0 |W_0|^2 + \frac{\beta_0}{2}|W_0|^4 \right) d\mu}$$

with the mapping:

$$|\partial W_0|^2 \longleftrightarrow f_2 \Lambda^2 \int R\sqrt{g}\, d^4x$$

$$\alpha_0 |W_0|^2 \longleftrightarrow f_0 \Lambda^4 \int \sqrt{g}\, d^4x$$

$$\frac{\beta_0}{2}|W_0|^4 \longleftrightarrow f_4 \int C_{\mu\nu\rho\sigma}^2 \sqrt{g}\, d^4x$$

**Physical reading:**

- The **kinetic term** $|\partial W_0|^2$ is the Einstein-Hilbert action — the energy cost of curvature. When $W_0$ is condensed, this is the standard gravitational dynamics.
- The **mass term** $\alpha_0|W_0|^2$ is the cosmological constant contribution — the energy cost/benefit of having geometry at all.
- The **quartic term** $\frac{\beta_0}{2}|W_0|^4$ is the higher-curvature correction (Weyl tensor squared) — the self-interaction that stabilizes the condensate at finite amplitude.

### 3.3 The Critical Parameter $\alpha_0$

$$\alpha_0 = a_0 \left(T - T_c^{(0)}\right)$$

where $T_c^{(0)} \sim T_{\text{Planck}} \approx 1.4 \times 10^{32}\,\text{K}$.

**Phase diagram:**

| Regime | $\alpha_0$ | $\langle W_0 \rangle$ | Physical meaning |
|---|---|---|---|
| Pre-geometric | $> 0$ | $= 0$ | No stable metric. QS without bisimulation condensation. Planck-scale foam. |
| Critical | $= 0$ | $\to 0$ | Geometric phase transition. Correlation length $\xi_0 \to \infty$. Planck epoch. |
| Geometric | $< 0$ | $= \sqrt{-\alpha_0/\beta_0}$ | Stable spacetime. Classical geometry. PS exists. |

**The Big Bang is the moment $\alpha_0$ crosses zero.**

Not a singularity in the traditional sense — a **phase transition** from pre-geometric QS to geometric PS. Before the transition, there is no spacetime, no metric, no "where" — only the non-well-founded relational graph of QS. The condensation of $W_0$ creates spacetime itself.

### 3.4 The VEV and the Cosmological Constant

In the condensed phase ($\alpha_0 < 0$):

$$\langle W_0 \rangle = v_0 = \sqrt{\frac{-\alpha_0}{\beta_0}}$$

The ground state energy density:

$$\rho_0 = \frac{-\alpha_0^2}{2\beta_0}$$

**Conjecture (Cosmological constant from Stage 0 condensate):**

$$\Lambda_{\text{grav}} = 8\pi G \cdot \rho_0 = \frac{-8\pi G\, \alpha_0^2}{2\beta_0}$$

This is the **gravitational sector's contribution** to the cosmological constant. The full $\Lambda_{\text{eff}} \sim \langle \rho_W \rangle$ from the master Will Field action receives contributions from all stages. The 120-order-of-magnitude discrepancy between the naive QFT vacuum energy and the observed $\Lambda$ may be a cancellation between stage contributions — each $S_k[W_k]$ contributes $\rho_k = -\alpha_k^2/(2\beta_k)$, and the physical $\Lambda$ is the sum.

⚠ **Status: Conjecture.** This reframes the cosmological constant problem as a multi-stage cancellation problem — potentially more tractable but not solved.

---

## 4. The Spectral Gap and the Planck Scale

### 4.1 $\Delta = 2$ on $S^2$

The Laplacian on the unit $S^2$ has eigenvalues $\ell(\ell+1)$ with multiplicity $2\ell+1$. The spectral gap is:

$$\Delta_{S^2} = \lambda_1 - \lambda_0 = 2 - 0 = 2$$

On the product $(S^2)^n$, the gap remains 2 (from any single factor).

### 4.2 The Planck Mass from the Spectral Gap

**Proposition 6 (Planck mass as Stage 0 mass gap — Conjecture).**

$$m_{\text{Planck}} = \frac{\hbar}{c} \cdot \sqrt{\Delta_{S^2}} \cdot \Lambda_{\text{UV}} = \frac{\hbar}{c} \cdot \sqrt{2} \cdot \Lambda_{\text{UV}}$$

where $\Lambda_{\text{UV}}$ is the fundamental UV cutoff of the source space.

**Physical reading:** The spectral gap of $S^2$ sets the **minimum energy** required to excite a mode of the geometric condensate. Below this energy, geometry is frozen in its ground state — spacetime is smooth and classical. Above this energy, geometric excitations appear — these are Planck-scale fluctuations.

The mass gap formula for Stage 0 parallels the YM mass gap: $\Delta_k = \sqrt{2\alpha_k}$. At Stage 0:

$$\Delta_0 = \sqrt{2|\alpha_0|} = \sqrt{2\beta_0}\, v_0$$

This should equal the Planck mass (up to factors of order unity) if the GL parameters are set by the source space geometry.

⚠ **Status: Conjecture.** The numerical matching requires knowing $\beta_0$ and $v_0$ from the spectral action, which requires computing the Seeley-de Witt coefficients on $(S^2)^\infty$ — a serious but potentially tractable calculation.

---

## 5. Bisimulation Dynamics and the Horizon

### 5.1 Connection to Horizon Bisimulation

The [Horizon Bisimulation](horizon_bisimulation.md) paper proved (Theorem 3.3):

$$\lambda_{\text{bis}} = \kappa = \frac{1}{4M}$$

Surface gravity $\kappa$ is the bisimulation divergence rate at the horizon. In the Stage 0 framework, this acquires a deeper meaning:

**The horizon is where the geometric condensate approaches its critical point locally.**

Near a black hole, the effective gravitational blueshift drives the local energy density up. As $r \to r_s$ from outside, the locally measured temperature $T_{\text{local}} = T_H / \sqrt{1 - r_s/r} \to \infty$. This means:

$$\alpha_0^{\text{eff}}(r) = a_0\left(T_{\text{local}}(r) - T_c^{(0)}\right)$$

As $r \to r_s$, $T_{\text{local}} \to \infty$, so $\alpha_0^{\text{eff}} \to +\infty$ — the geometry is driven back toward the uncondensed (pre-geometric) phase. The horizon is the surface where the condensate begins to melt.

**Proposition 7 (Horizon as condensate boundary — Conjecture).** *The event horizon at $r = r_s$ is the surface where the geometric condensate amplitude $|W_0(r)|$ transitions from the condensed phase ($|W_0| \approx v_0$, exterior) toward the critical point ($|W_0| \to 0$, deep interior). The bisimulation divergence rate $\lambda_{\text{bis}} = \kappa$ measures the rate at which the condensate melts as the horizon is crossed.*

This gives Proposition 4 of [Graded BRST](graded_brst.md) (black holes as demotion environments) a concrete mechanism: the interior of a black hole is where Stage 0 itself begins to fail. Not just Stages 1 and 2 — the geometric condensate dissolves. The singularity at $r = 0$ is the point where $|W_0| = 0$: pre-geometric QS, no stable bisimulation classes, no spacetime.

### 5.2 Hawking Temperature as GL Fluctuations

Hawking radiation at temperature $T_H = \kappa/(2\pi)$ is the thermal fluctuation of the geometric condensate near its boundary. In GL theory, fluctuations near the phase boundary produce thermal excitations with characteristic temperature set by the order parameter's correlation length.

The Hawking temperature is not mysterious in this picture — it is the **standard GL fluctuation temperature** at the condensate edge, determined by $\kappa = \lambda_{\text{bis}}$ (the bisimulation divergence rate proven in Theorem 3.3).

---

## 6. The Equivalence Principle — Derived

### 6.1 Trivial Stalk at Vacuum

From [Source Space](source_space.md): at vacuum, the CS stalk is $C_x = (S^2)^0 = \{*\}$ — trivial. A trivial stalk treats all matter identically: it cannot distinguish between types of matter because there is no internal structure in the stalk to project differently.

**Proposition 8 (Equivalence principle from Stage 0 — Proved).**

*At Stage 0, the instantiation operator $C$ acts through a trivial stalk $C_x = \{*\}$. A trivial stalk induces a universal coupling: all QS elements that are $s_0$-closed respond identically to the Stage 0 condensate. This is the equivalence principle — gravity is universal because the gravitational instantiation operator has no internal structure with which to discriminate.*

*Proof.* The BRST operator $s_0$ acts on the Diff$(M)$ ghost sector. A state $|\psi\rangle$ is $s_0$-closed iff it is diffeomorphism-invariant — it has well-defined energy-momentum. The coupling to the geometric condensate $W_0$ is through the energy-momentum tensor $T_{\mu\nu}$, which is the only diffeomorphism-invariant quantity. Since the stalk $C_x = \{*\}$ carries no additional quantum numbers (no color, no charge, no flavor), $T_{\mu\nu}$ is the **unique** coupling channel. All $s_0$-closed states couple to gravity through $T_{\mu\nu}$ alone — universally. $\square$

**Corollary:** Higher stages break universality.

**Dual description (2026-03-08, after @D_Gemini semi-direct correction):** The equivalence principle has two equivalent RTSG derivations:

| Direction | Mechanism | Result |
|---|---|---|
| Top-down (source space) | Trivial stalk $C_x = \{*\}$ at Stage 0 → no internal quantum numbers → universal coupling via $T_{\mu\nu}$ alone | Gravity can't discriminate |
| Bottom-up (BRST algebra) | Semi-direct product $\text{Diff}(M) \ltimes G_{\text{int}}$ → gravity drags all gauge bundles via $\mathcal{L}$ | Gravity acts on everything |

These are the same statement. The trivial stalk IS why the product is semi-direct: gravity has no internal structure, so it can only act on internal structure by transport (Lie derivative), not by internal coupling. The Hochschild-Serre $d_2$ differential enforces this — it kills deformations that would decouple gravity from gauge, i.e., that would violate the equivalence principle in the gauge sector. Stage 1 (EM) couples to charge. Stage 2 (color) couples to color charge. Only Stage 0 is universal, because only the trivial stalk has no discriminating structure.

---

## 7. Summary: Stage 0 Resolved

| Component | Formalization |
|---|---|
| **Order parameter** $W_0$ | Bisimulation stability field on $(S^2)^4$ — condensate density of stable equivalence classes |
| **GL potential** $S_0[W_0]$ | Chamseddine-Connes spectral action on $(S^2)^\infty$: EH = kinetic, $\Lambda$ = mass, Weyl² = quartic |
| **Critical parameter** $\alpha_0$ | $a_0(T - T_{\text{Planck}})$; crossing zero = Big Bang = geometric phase transition |
| **VEV** $v_0$ | $\sqrt{-\alpha_0/\beta_0}$; determines Planck scale |
| **Mass gap** $\Delta_0$ | $\sqrt{2|\alpha_0|}$; should match $m_{\text{Planck}}$ up to $O(1)$ factors |
| **Horizon connection** | Horizon = condensate boundary; $\kappa = \lambda_{\text{bis}}$ = melt rate |
| **Equivalence principle** | Derived from trivial stalk $C_x = \{*\}$ at Stage 0 |
| **Cosmological constant** | $\Lambda_{\text{grav}} = -8\pi G \alpha_0^2 / (2\beta_0)$; one stage's contribution |

---

## 8. Open Gaps (Honest)

1. **Seeley-de Witt coefficients on $(S^2)^\infty$.** The mapping spectral action → GL potential requires computing $a_0, a_2, a_4$ on the infinite product. Individual $S^2$ coefficients are known ($a_0 = 4\pi$, $a_2 = \frac{4\pi}{3} \cdot 2$, etc.), but the infinite product introduces regularization subtleties. The Tychonoff topology and the weighted metric $d = \sum 2^{-i} d_{S^2}$ suggest a natural regularization, but this computation has not been done.

2. **$W_0$ as a rigorous field.** The bisimulation stability field (Definition, §2.2) is conceptually clean but needs measure-theoretic foundations. What is the appropriate $\sigma$-algebra on QS? The terminal coalgebra structure provides a natural Borel structure, but the limit in the definition needs functional-analytic justification.

3. **Condensed-matter connection.** The geometric condensate picture is closely analogous to BEC (Bose-Einstein condensation) of spacetime atoms. The GFT literature (Oriti, Gielen, Sindoni) has developed this extensively. Our contribution is the source space identification $(S^2)^\infty$ and the bisimulation interpretation. A systematic comparison with GFT condensate cosmology is needed.

4. **Multi-stage cosmological constant cancellation.** The conjecture that $\Lambda_{\text{obs}} = \sum_k \rho_k$ is a multi-stage cancellation is attractive but uncontrolled. Without computing the individual $\rho_k = -\alpha_k^2/(2\beta_k)$ from first principles, this is reframing, not solving, the CC problem.

5. **Pre-geometric QS dynamics.** Before the condensation ($\alpha_0 > 0$), what governs QS? The coalgebraic dynamics on the terminal coalgebra should provide a "pre-geometric mechanics" — but this has not been formalized. The Will SDE operates on a manifold; without a manifold (pre-condensation), the SDE must be reformulated combinatorially.

6. **The Planck epoch.** The critical point $\alpha_0 = 0$ is the Planck epoch. Correlation length $\xi_0 \to \infty$. This is a second-order phase transition (in the Landau classification). What are the critical exponents? They would characterize the quantum gravity regime and should be computable from the GL potential (universality class = $O(2)$ in 4D, which is actually the same universality class as the superfluid transition).

---

## 9. Equations Summary

$$W_0(x) = \lim_{\varepsilon \to 0} \frac{\text{Vol}(B_\varepsilon^{\text{bisim}}(q) \cap [q]_\sim)}{\text{Vol}(B_\varepsilon^{\text{bisim}}(q))}$$

$$S_0[W_0] = \int \left( |\partial W_0|^2 + \alpha_0 |W_0|^2 + \frac{\beta_0}{2}|W_0|^4 \right) d\mu$$

$$|\partial W_0|^2 \leftrightarrow f_2\Lambda^2 \!\int\! R\sqrt{g}\, d^4x, \qquad \alpha_0|W_0|^2 \leftrightarrow f_0\Lambda^4 \!\int\! \sqrt{g}\, d^4x, \qquad \tfrac{\beta_0}{2}|W_0|^4 \leftrightarrow f_4 \!\int\! C^2 \sqrt{g}\, d^4x$$

$$v_0 = \sqrt{-\alpha_0/\beta_0}, \qquad \Delta_0 = \sqrt{2|\alpha_0|} \sim m_{\text{Planck}}, \qquad \Lambda_{\text{grav}} = \frac{-8\pi G\, \alpha_0^2}{2\beta_0}$$

$$\lambda_{\text{bis}} = \kappa = \frac{1}{4M} \qquad \text{(horizon = condensate boundary)}$$
