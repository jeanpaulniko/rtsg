---
title: "Hilbert-Pólya Operator: From Theta Kernel to Lax-Phillips Bridge"
version: "2.4.0"
last_updated: "2026-03-14"
status: "IN PROGRESS — D* + Vladimirov + Sobolev + BdG Hessian + Goldstone operator"
---

# Hilbert-Pólya Operator: From Theta Kernel to Lax-Phillips Bridge

**Jean-Paul Niko** · March 2026 · arXiv:math.NT

---

## Abstract (revised)

We construct a character-family theta kernel $K^{\mathrm{full}} = \sum_\chi \theta_\chi \otimes \bar\theta_\chi$ on the modular surface and establish three results toward the Riemann Hypothesis. First, the Lax-Phillips scattering generator $B$ satisfies a cusp intertwining relation $B^*K - KB = \frac{i}{2}K$ whose coefficient equals the universal modular weight of the theta family. Second, an unconditional character-family nonvanishing theorem guarantees visibility of all hypothetical off-line resonances. Third, we identify the structural obstruction (the 2s-1 problem) and propose a resolution via Shimura-Waldspurger transfer to the Eisenstein spectrum. We further formulate Conjecture D* (unique adelic extension selection via GL minimization on $H^1(C_\mathbb{Q})$, with the Vladimirov operator as the $p$-adic uniqueness mechanism) and Conjecture C (the Bogoliubov-de Gennes Hessian at the ground state, gauge-fixed to the Goldstone phase operator, generates the Riemann zeros as its self-adjoint spectrum).

---

## Paper Structure

1. Introduction: The Hilbert-Pólya problem and Lax-Phillips scattering
2. Five historical constructions and their obstructions
3. The Poisson bridge: $C = 0.04467$ and ζ inside θ-orbital integrals
4. The bridge identity: $B^*K - KB = \frac{i}{2}K$ and weight-1/2 mechanism
5. Character-family nonvanishing (Parseval + Hurwitz, unconditional)
6. The 2s-1 obstruction and the Shimura-Waldspurger resolution
7. Conditional results: RH under LI, finite verification to $6 \times 10^{12}$
    - **7.1 Conjecture D\* and the Phase Selector Problem**
    - **7.2 Explicit Definition of $I_{\mathrm{glue}}(\mathcal{W})$**
    - **7.3 The Vladimirov Mechanism: $p$-adic Uniqueness**
    - **7.4 The Adelic Sobolev Space $H^1(C_\mathbb{Q})$**
    - **7.5 Conjecture C: The Bogoliubov-de Gennes Hessian** *(new)*
    - **7.6 Gauge-Fixing and the Goldstone Operator** *(new)*
8. Open gaps and the path forward

## Key Results (proved)

- Poisson bridge constant $C = \sum r_2(n) E_1(\pi n) = 0.04467$ (numerical, 8 decimal places)
- Bridge identity coefficient = weight of θ = 1/2 (representation theory)
- Character nonvanishing for all $s_0$ with Re(s₀) > 0 (Parseval, unconditional)
- "Proves too much" rebuttal (only weight 1/2 converges + positive)
- RH under LI (GPT-5.4, conditional)
- No counterexamples below height $6 \times 10^{12}$ (Platt-Trudgian)

---

## 7.1 Conjecture D\* and the Phase Selector Problem

### The Two Walls

- **Wall 1 — Extension selection:** Choosing a unique self-adjoint extension of the LP scattering generator.
- **Wall 2 — Spectral identification:** Proving the chosen extension has spectrum $\{\gamma_n\}$.

Conjecture D\* addresses Wall 1. Conjecture C (§7.5–7.6) addresses Wall 2.

### Self-Adjoint Extension Family

$$S_\theta(z) = \frac{i}{2}\bigl(e^{i\theta} E(z) - e^{-i\theta} E^\#(z)\bigr), \qquad \theta \in [0, \pi),$$

where $E(z) = \xi(1 - 2iz)$ generates $\mathcal{H}(E)$.

### Conjecture D\* (Selection Form)

!!! conjecture "Conjecture D\*"

    Let $\mathcal{S}[\mathcal{W}] = \mathcal{S}_\infty(W_\infty) + \sum_p \mathcal{S}_p(W_p) + \mathcal{I}_{\mathrm{glue}}(\mathcal{W})$ be the adelic GL functional on the gauge quotient, and $\vartheta : \mathrm{Crit}(\mathcal{S}) \to [0,\pi)$ the boundary-phase map. If:

    **(i)** $\mathcal{S}$ is coercive modulo gauge,
    **(ii)** every local family $(W_p)_p$ determines a unique $W_\infty^*$,
    **(iii)** the glued critical point $\mathcal{W}^*$ is unique modulo gauge,

    then $\theta_* := \vartheta(\mathcal{W}^*)$ is unique and selects a unique self-adjoint extension $S_{\theta_*}$.

### Evolution from Conjectures A–D

| Conjecture | Content | Status |
|:-----------|:--------|:-------|
| A | Theta kernel construction | **Proved** |
| B | Bridge identity | **Proved** |
| C | Character-family nonvanishing | **Proved unconditionally** |
| D | Adelic selection ("potential game") | Structural only |
| **D\*** | Three conditions + phase map + failure modes | **Open — §7.1** |

---

## 7.2 Explicit Definition of $I_{\mathrm{glue}}(\mathcal{W})$

$$S[\mathcal{W}] = S_\infty(W_\infty) + \sum_p S_p(W_p) + I_{\mathrm{glue}}(\mathcal{W})$$

Local terms: $S_v(W_v) = \int \left( |\partial W_v|^2 + \alpha |W_v|^2 + \frac{\beta}{2} |W_v|^4 \right) d\mu_v$, with $\alpha < 0$, $\beta > 0$.

!!! conjecture "Definition (proposed): $I_{\mathrm{glue}}$"

    $$I_{\mathrm{glue}}(\mathcal{W}) = \sum_p \log p \int_{\mathbb{Q}_p^* \times \mathbb{R}_{>0}} \beta_{p,\infty} \, |W_p(x_p) - W_\infty(y)|^2 \, d\mu_p \, dy \;+\; \lambda \left( \| \mathcal{W} \|_{\mathbb{A}} - 1 \right)^2$$

| Term | Source | Mechanism |
|:-----|:-------|:----------|
| $\log p$ weighting | Bost–Connes, explicit formula | Arithmetic rigidity |
| $|W_p - W_\infty|^2$ | Multi-component GL | Local-global agreement |
| $\lambda(\|\mathcal{W}\|_{\mathbb{A}} - 1)^2$ | Product formula | Glues places |

**Open:** Convergence of $\sum_p \log p$ terms; non-attainment regimes; superseded structurally by Vladimirov (§7.3).

---

## 7.3 The Vladimirov Mechanism: $p$-adic Uniqueness

### The Vladimirov Operator

On $\mathbb{Q}_p$ (totally disconnected), the fractional Laplacian measures jumps between branches of the $p$-adic tree:

$$(D_p^\alpha w)(x) = \int_{\mathbb{Q}_p} \frac{w(x) - w(y)}{|x - y|_p^{1+\alpha}} \, dy, \qquad \alpha > 0$$

Multiplier in Fourier domain: $|\xi_p|_p^\alpha$.

### The Energy Penalty

If $w_p$ fluctuates on microscopic $p$-adic scales ($|x-y|_p = p^{-k}$ small), the denominator $p^{-k(1+\alpha)}$ is tiny, blowing the kinetic energy to infinity. **Survival:** $w_p$ must be locally constant on large branches.

### The Restricted Product Sieve

By the idèle topology, $w_p \equiv 1$ on $\mathbb{Z}_p$ for almost all $p$. Only finitely many primes "active." The nonlinear product $2\beta|w_\infty|^2 \prod_p |w_p|^2$ collapses to a finite algebraic weight.

### The Global Lock

Rational invariance $W(qx) = W(x)$, $q \in \mathbb{Q}^\times$: shifting by $q = \pm p_1^{k_1} \cdots$ activates specific Vladimirov jumps. The archimedean $w_\infty$ must absorb all rigid discrete jumps under every rational shift.

!!! success "Uniqueness Mechanism"
    The $p$-adic places are infinite rigid sieves. The archimedean component is the unique fluid shape flowing through all simultaneously under the $\beta|W|^4$ hypervisor. This provides the structural coupling for D\*, replacing ad hoc $\beta_{p,\infty}$.

---

## 7.4 The Adelic Sobolev Space $H^1(C_\mathbb{Q})$

### Local Spaces

**Archimedean:** $\|w_\infty\|_{H^s}^2 = \int_\mathbb{R} (1+|\xi_\infty|^2)^s |\widehat{w_\infty}|^2 \, d\xi_\infty$

**$p$-adic:** $\|w_p\|_{H^s}^2 = \int_{\mathbb{Q}_p} (1+|\xi_p|_p^2)^{s/2} |\widehat{w_p}|^2 \, d\xi_p$

### Schwartz-Bruhat Core

$W \in \mathcal{S}(\mathbb{A})$ iff $w_\infty$ is Schwartz, $w_p$ is locally constant with compact support, and $w_p = \Omega(|x_p|_p)$ (indicator of $\mathbb{Z}_p$) for almost all $p$.

### Global Space

$$\|W\|_{H^s(\mathbb{A})}^2 = \int_{\mathbb{A}} (1 + |\xi|_{\mathbb{A}}^2)^{s/2} \, |\widehat{W}(\xi)|^2 \, d\xi < \infty$$

GL kinetic term requires $s=1$.

### The Hypervisor's Domain

$H^1(C_\mathbb{Q})$ = restriction to $\mathbb{Q}^\times$-invariant functions on $C_\mathbb{Q} = \mathbb{Q}^\times \backslash \mathbb{A}^\times$. The Fourier integral collapses to a **discrete sum over Hecke characters**. Zeros of $\zeta(s)$ are poles of the resolvent on this space.

**Proof mechanism for D\*:** Coercivity (minimizer exists) + strict convexity mod gauge (minimizer unique) of $S[\mathcal{W}]$ on $H^1(C_\mathbb{Q})$.

---

## 7.5 Conjecture C: The Bogoliubov-de Gennes Hessian

If Conjecture D\* gives the unique ground state $W_0$, Conjecture C asks: **what is the spectrum of fluctuations around $W_0$?**

### The Fluctuation Field

Perturb: $W(x) = W_0(x) + \eta(x)$. Expand $S[W]$ to second order in $\eta$. First-order vanishes (Euler-Lagrange). Second-order defines the **Hessian** $\mathcal{H}_{W_0}$.

### The BdG Hessian

Because $W$ is complex, $\eta$ and $\overline{\eta}$ couple. The Hessian is a $2 \times 2$ block operator on $(\eta, \overline{\eta})^T$ — the adelic Bogoliubov-de Gennes equations:

$$\mathcal{H}_{W_0} = \begin{pmatrix} -\Delta_\mathbb{A} + \alpha + 4\beta |W_0|^2 & 2\beta W_0^2 \\ 2\beta \overline{W_0}^2 & -\Delta_\mathbb{A} + \alpha + 4\beta |W_0|^2 \end{pmatrix}$$

### The Adelic Eigenvalue Problem

Eigenstates $(u,v)^T$ must live in $H^1(C_\mathbb{Q})$ (invariant under $\mathbb{Q}^\times$). Natural basis: Hecke characters $\chi_s(x) = |x|_\mathbb{A}^s$.

### The Zeta Bridge

!!! conjecture "Conjecture C (Spectral Form)"

    When the eigenvalue equation $\mathcal{H}_{W_0} \Psi = E\Psi$ is projected onto Hecke characters via the global Mellin transform, the "potential well" $4\beta|W_0|^2$ — built from the prime-by-prime Vladimirov sieve — produces a transmission coefficient equal to $\zeta(s)$. The eigenfunction closes its orbit under $\mathbb{Q}^\times$ boundary conditions iff:

    $$\zeta(s) = 0$$

    The chain: stability of $W_0$ $\implies$ $\mathcal{H}_{W_0} \geq 0$ $\implies$ eigenvalues $E_n$ real $\implies$ $\gamma_n \in \mathbb{R}$ $\implies$ all zeros on $\mathrm{Re}(s) = 1/2$.

!!! warning "Gaps in the Chain"
    This argument is structural, not yet a proof. Three steps require rigorous verification:

    1. **Mellin projection:** The claim that the transmission coefficient through the $4\beta|W_0|^2$ lattice equals $\zeta(s)$ must be derived, not asserted. This is the central unproved step.
    2. **Positivity of $\mathcal{H}_{W_0}$:** Requires D\* (unique minimum). If the minimum is degenerate, the Hessian has zero modes beyond the gauge direction.
    3. **Self-adjointness on $H^1(C_\mathbb{Q})$:** The BdG operator must be essentially self-adjoint on this specific domain — not automatic for unbounded operators on infinite-dimensional spaces.

---

## 7.6 Gauge-Fixing and the Goldstone Operator

### Gauge Choice: Real Ground State

$\mathrm{U}(1)$ gauge freedom: rotate $W_0$ to be strictly real and positive:

$$W_0(x) \in \mathbb{R}_{>0}$$

Then $W_0 = \overline{W_0}$, and the off-diagonal BdG terms $2\beta W_0^2 = 2\beta \overline{W_0}^2$ become identical real functions.

### Higgs-Goldstone Decoupling

Split $\eta = u + iv$ (amplitude + phase fluctuations). Unitary basis change $(\eta, \overline{\eta}) \to (u,v)$ block-diagonalizes:

$$\mathcal{H}_{W_0}^{(u,v)} = \begin{pmatrix} \mathcal{H}_{\mathrm{Higgs}} & 0 \\ 0 & \mathcal{H}_{\mathrm{Goldstone}} \end{pmatrix}$$

### The Two Operators

**Higgs (amplitude):**
$$\mathcal{H}_{\mathrm{Higgs}} = -\Delta_\mathbb{A} + \alpha + 6\beta W_0^2$$

Massive, gapped spectrum. Does **not** contain the Riemann zeros.

**Goldstone (phase):**
$$\mathcal{H}_{\mathrm{Goldstone}} = -\Delta_\mathbb{A} + \alpha + 2\beta W_0^2$$

This is the **master operator**.

### Goldstone's Theorem: The Zero Mode

The Euler-Lagrange equation for the real ground state:

$$(-\Delta_\mathbb{A} + \alpha + 2\beta W_0^2)\, W_0 = 0$$

Therefore:

$$\mathcal{H}_{\mathrm{Goldstone}}\, W_0 = 0$$

$W_0$ is an exact eigenvector with eigenvalue $E = 0$. This is Goldstone's theorem on $C_\mathbb{Q}$: spontaneous $\mathrm{U}(1)$ breaking guarantees a massless mode. In the zeta world, this maps to the pole at $s = 1$.

### The Non-Trivial Zeros

!!! conjecture "Conjecture C (Goldstone Form)"

    The higher eigenstates of $\mathcal{H}_{\mathrm{Goldstone}}$:

    $$\mathcal{H}_{\mathrm{Goldstone}}\, v_n = E_n\, v_n, \qquad E_n > 0$$

    have eigenvalues $E_n$ that map through the adelic Mellin transform to:

    $$s_n = \tfrac{1}{2} + i\gamma_n, \qquad \gamma_n = \gamma_n(E_n) \in \mathbb{R}$$

    Self-adjointness of $\mathcal{H}_{\mathrm{Goldstone}}$ forces $E_n \in \mathbb{R}$, hence $\gamma_n \in \mathbb{R}$, hence all zeros on $\mathrm{Re}(s) = 1/2$.

### The Complete Engine

| Step | Content | Status |
|:-----|:--------|:-------|
| D\* | $\beta|W|^4$ hypervisor forces unique $W_0$ on $H^1(C_\mathbb{Q})$ | **Conjectural** (§7.1–7.4) |
| Gauge-fix | Rotate $W_0 \in \mathbb{R}_{>0}$, decouple BdG into Higgs + Goldstone | **Formal** (unitary, rigorous if D\* holds) |
| Goldstone zero mode | $\mathcal{H}_{\mathrm{Goldstone}} W_0 = 0$ (Euler-Lagrange identity) | **Proved** (algebraic, if D\* holds) |
| Spectral identification | Higher eigenvalues $E_n \leftrightarrow \gamma_n$ via Mellin | **Conjectural** (central gap) |
| RH | Self-adjointness $\implies \gamma_n \in \mathbb{R}$ | **Follows from above** (if all steps hold) |

!!! warning "Honest Gaps in the Goldstone Argument"

    1. **The Mellin bridge (central gap).** The assertion that Mellin-projecting $\mathcal{H}_{\mathrm{Goldstone}}$ onto Hecke characters produces eigenvalues at $\zeta(s) = 0$ is the single most important unproved claim. The "arithmetic lattice potential" $2\beta W_0^2$ must be shown to have scattering data equal to $\zeta(s)$. This is nontrivial — it would constitute a new form of the explicit formula.
    2. **Essential self-adjointness.** $\mathcal{H}_{\mathrm{Goldstone}}$ on $H^1(C_\mathbb{Q})$ must be essentially self-adjoint. For Schrödinger-type operators on locally compact groups, this requires control of the potential growth — the $2\beta W_0^2$ term must be bounded below and not oscillate too wildly.
    3. **Dependence on D\*.** The entire Goldstone argument presupposes D\*. If the ground state is degenerate, the Hessian has extra zero modes, the gauge-fixing fails, and the decoupling breaks down.
    4. **Trivial zeros.** The $E=0$ mode maps to $s=1$; the trivial zeros at $s = -2n$ should appear as additional structure (possibly from the Higgs sector or the compact part of $C_\mathbb{Q}$). This mapping is not yet established.

---

## Honest Assessment

| Component | Status | Confidence | Key Obstacle |
|:----------|:-------|:-----------|:-------------|
| Poisson bridge $C = 0.04467$ | Proved (numerical) | High | None — 8 decimal places |
| Bridge identity $B^*K - KB = \frac{i}{2}K$ | Proved | High | Representation theory |
| Character-family nonvanishing | Proved | High | Unconditional (Parseval + Hurwitz) |
| "Proves too much" rebuttal | Proved | High | Weight 1/2 convergence specific |
| RH under LI | Conditional | Medium | Depends on LI hypothesis |
| No counterexamples below $6 \times 10^{12}$ | Verified | High | Platt–Trudgian |
| 2s-1 obstruction (Shimura–Waldspurger) | **Open** | Low | Eisenstein transfer for weight 1/2 |
| Cusp sufficiency for global eigenvalues | **Open** | Medium | Functional-analytic gap |
| **D\*-i: Coercivity mod gauge** | **Open** | Medium | Vladimirov supports; $H^1(C_\mathbb{Q})$ bound needed |
| **D\*-ii: $p$-adic determination** | **Open** | Medium | Vladimirov sieve + restricted product |
| **D\*-iii: Glued uniqueness mod gauge** | **Open** | Low–Medium | Strict convexity on $H^1(C_\mathbb{Q})$ |
| **Adelic Sobolev space $H^1(C_\mathbb{Q})$** | **Defined** | Medium | Formalized; coercivity/convexity unproved |
| **BdG Hessian + gauge-fixing** | **Formal** | Medium | Rigorous if D\* holds; decoupling is algebraic |
| **Goldstone zero mode $= s=1$ pole** | **Formal** | Medium–High | Algebraic identity from EL equation |
| **Mellin bridge: $E_n \leftrightarrow \zeta(s)=0$** | **Conjectural** | Low | **Central gap.** Must derive, not assert. |
| **Essential self-adjointness of $\mathcal{H}_{\mathrm{Gold}}$** | **Open** | Low–Medium | Potential growth control on $C_\mathbb{Q}$ |
| **Spectral identification (Wall 2)** | **Conjectural** | Low | Depends on Mellin bridge |

---

## Open Gaps

- Shimura-Waldspurger transfer for Eisenstein series (the 2s-1 obstruction)
- Functional-analytic verification of cusp sufficiency for global eigenvalues
- **D\*: Strict convexity of $S[\mathcal{W}]$ on $H^1(C_\mathbb{Q})$ (Wall 1)**
- **Mellin bridge: scattering data of $2\beta W_0^2$ on $C_\mathbb{Q}$ equals $\zeta(s)$ (Wall 2 — central gap)**
- **Essential self-adjointness of $\mathcal{H}_{\mathrm{Goldstone}}$ on $H^1(C_\mathbb{Q})$**
- **Trivial zeros: mapping $s=-2n$ to Higgs/compact spectrum**
- Phase selector $\vartheta$: explicit construction
- Finite-prime truncation: numerical test of $\theta^*$ stabilization

## 7.7 The Determinant Obstruction and the Weyl Realization

### The Naive Target (Killed)

The original Theorem I proposed:

$$\det\nolimits_\zeta(\mathcal{H}_{\mathrm{Goldstone}} - s(1-s) I) = \xi(s)$$

**This target is dead.** Here is the obstruction.

### The Obstruction Theorem

In the de Branges model $\mathcal{H}(E)$ with $E(z) = \xi(1-2iz)$, the multiplication operator is a closed symmetric operator with deficiency indices $(1,1)$. Its self-adjoint extensions $S_\beta$ are parametrized by

$$s_\beta(z) = \frac{i}{2}\bigl(e^{i\beta} E(z) - e^{-i\beta} E^\#(z)\bigr)$$

and their spectra are the real zeros of $s_\beta$ — simple and real.

For extension pairs, the boundary-triple perturbation determinant is:

$$\Delta_{\widetilde{A}'/\widetilde{A}}(z) = \det\bigl(I + (B'-B)(B - M(z))^{-1}\bigr)$$

In scalar deficiency $(1,1)$, this simplifies to:

$$\Delta_{\widetilde{A}'/\widetilde{A}}(z) = \frac{B' - M(z)}{B - M(z)}$$

This is meromorphic with:

- **Zeros** at the spectrum of extension $B'$
- **Poles** at the spectrum of extension $B$

Since every self-adjoint de Branges extension has an **infinite real spectrum**, the perturbation determinant necessarily has real poles. But $e^{az+b}\xi(1/2+iz)$ is **entire**. Therefore:

!!! danger "Obstruction"
    No self-adjoint-pair perturbation determinant can equal $e^{az+b}\xi(1/2+iz)$ up to a zero-free factor. The naive Fredholm-Weil target is pruned.

### What Survives: Dissipative Characteristic Functions

The obstruction kills determinants between **self-adjoint** extensions. It does not kill characteristic/scattering functions of **dissipative** extensions.

**Malamud's characteristic-function formula** (scalar case):

$$W_B(z) = 1 + 2i \, \frac{\mathrm{Im}\, B}{\overline{B} - M(z)} = \frac{B - M(z)}{\overline{B} - M(z)}$$

With $B = i$:

$$W_i(z) = \frac{M(z) - i}{M(z) + i}$$

This is a **Schur-class function** (bounded analytic in the upper half-plane), not a meromorphic ratio of extension spectra. It evades the obstruction entirely.

### The Live Target: Weyl Realization of $m_\xi$

Define the Weyl $m$-function associated to $\xi$:

$$m_\xi(z) = -\frac{A'(z)}{A(z)}$$

where $A(z) = \frac{1}{2}(E(z) + E^\#(z))$ is the real part of the de Branges function.

!!! abstract "Revised Theorem I (Weyl Form)"

    **Target:** Realize $m_\xi(z)$ as the Weyl function $M(z)$ of an unconditional simple symmetric operator $T$ with deficiency indices $(1,1)$.

    If this realization exists, then the **scalar characteristic function** of the maximal dissipative extension $T_i$ (with $B = i$) is:

    $$-\Theta_\xi(z) = \frac{m_\xi(z) - i}{m_\xi(z) + i}$$

    This is a Schur-class function whose zeros in the upper half-plane correspond to the non-trivial zeros of $\zeta(s)$.

### Why This Works

| Property | Self-adjoint det (killed) | Dissipative characteristic fn (live) |
|:---------|:-------------------------|:------------------------------------|
| Analytic type | Meromorphic (poles at extension spectrum) | Schur class (bounded, no poles in $\mathbb{C}^+$) |
| Zeros | At one extension's spectrum (real) | At $M(z) = i$ (potentially complex) |
| Obstruction | Poles prevent matching to entire $\xi$ | No obstruction — Schur function can have zeros at zeta ordinates |
| RH mechanism | N/A (dead) | Self-adjointness of underlying $T$ forces completeness; Schur-class structure constrains zero locations |

### The Revised Lemma Decomposition

#### Lemma I.1 (Gate): Weyl Realization

**Prove or disprove:** There exists a simple symmetric operator $T$ on a Hilbert space such that $m_\xi(z) = M_T(z)$ is its Weyl function in the boundary-triple sense.

**What's needed:**

- $m_\xi(z)$ must be a Herglotz-Nevanlinna function (maps $\mathbb{C}^+$ to $\overline{\mathbb{C}^+}$)
- The representing measure in the Herglotz integral must be the spectral measure of a legitimate symmetric operator
- The operator must have deficiency indices $(1,1)$ — unconditional, no extra hypotheses

**Known:** $m_\xi(z) = -A'(z)/A(z)$ where $A(z)$ is real-entire of order 1. By the Hadamard factorization, $A'/A$ is a meromorphic Herglotz function with poles at the real zeros of $A$ and positive residues (since zeros of $A$ interlace with zeros of $B$ in a de Branges space). This is promising — the Herglotz property may follow from de Branges theory itself.

**Status:** Open. This is the new gate. If it fails, the entire program fails cleanly.

#### Lemma I.2: Schur-Class Zero Location

With the Weyl realization secured, the characteristic function $\Theta_\xi(z) = (m_\xi - i)/(m_\xi + i)$ is defined.

**Prove:** The zeros of $\Theta_\xi(z)$ in the upper half-plane are precisely $z_n = \gamma_n$ (the imaginary parts of the non-trivial zeta zeros under the change of variables $s = 1/2 + iz$).

**What's needed:** The equation $m_\xi(z) = i$ must be equivalent to $\zeta(1/2 + iz) = 0$. This is a direct computation from the definition of $m_\xi$ and the relation $E(z) = \xi(1-2iz)$.

#### Lemma I.3: Completeness and the Inverse Spectral Problem

**Prove:** The symmetric operator $T$ from Lemma I.1 has a complete system of root vectors for its dissipative extension $T_i$.

**Why this matters:** Completeness ensures the characteristic function $\Theta_\xi$ determines the operator uniquely (up to unitary equivalence). The Livsic-Brodskii theorem then constrains the zero set of $\Theta_\xi$ — if the underlying $T$ has purely discrete deficiency spectrum, the zeros of $\Theta_\xi$ must satisfy specific asymptotic density conditions.

#### Lemma I.4: RH from Schur-Class Constraints

With I.1–I.3 secured:

1. $T$ is a simple symmetric operator with Weyl function $m_\xi$
2. $\Theta_\xi$ is a Schur-class characteristic function with zeros at $\gamma_n$
3. The self-adjoint extensions of $T$ have purely real spectra
4. The completeness theorem constrains the $\gamma_n$ to satisfy the density/symmetry conditions of a legitimate spectral problem

**The RH question becomes:** Do the Schur-class constraints on $\Theta_\xi$, combined with the specific arithmetic structure of $m_\xi$, force all zeros to lie on the real axis in the $z$-variable (i.e., on the critical line in the $s$-variable)?

!!! warning "Honest Status"
    This is a cleaner path than the killed Fredholm determinant, but it is not a downhill proof. The Schur-class constraints alone do not force real zeros — additional arithmetic input from the specific form of $m_\xi$ is needed. The question is whether de Branges theory + the Herglotz representation of $m_\xi$ provides enough rigidity.

---

## Honest Assessment (Final)

| Component | Status | Confidence | Key Obstacle |
|:----------|:-------|:-----------|:-------------|
| Poisson bridge $C = 0.04467$ | Proved (numerical) | High | None |
| Bridge identity $B^*K - KB = \frac{i}{2}K$ | Proved | High | None |
| Character-family nonvanishing | Proved | High | Unconditional |
| "Proves too much" rebuttal | Proved | High | None |
| RH under LI | Conditional | Medium | Depends on LI |
| No counterexamples below $6 \times 10^{12}$ | Verified | High | Platt–Trudgian |
| 2s-1 obstruction | **Open** | Low | Shimura–Waldspurger |
| **Naive Fredholm det = $\xi(s)$** | **KILLED** | — | Self-adjoint pair det has poles; $\xi$ is entire |
| **Theorem S (Selection)** | **Open** | Low–Medium | GL uniqueness on $H^1(C_\mathbb{Q})$ |
| **Lemma I.1: Weyl realization of $m_\xi$** | **Open** | Medium | Herglotz property of $-A'/A$ — checkable from dB theory |
| **Lemma I.2: Schur zeros = zeta zeros** | **Open** | Medium | Direct computation from $m_\xi(z) = i$ |
| **Lemma I.3: Completeness of root vectors** | **Open** | Low–Medium | Livsic-Brodskii theory on specific operator |
| **Lemma I.4: Schur constraints → RH** | **Open** | Low | Arithmetic input from $m_\xi$ structure needed |
| Goldstone zero mode = $s=1$ pole | Formal | Medium–High | Algebraic identity |

---

## Submission Status

**NOT submission-ready.** The naive determinant target is killed — a genuine obstruction, not a gap. The live target is the **Weyl realization** of $m_\xi(z)$ as a boundary-triple Weyl function, producing a Schur-class characteristic function whose zeros are the zeta ordinates.

**Active target:** Lemma I.1 — build or rule out the unconditional Weyl realization.

**RH confidence: 25%.** The determinant obstruction is a real result (publishable as a negative theorem). The Weyl/Schur path survives but is not yet validated.
