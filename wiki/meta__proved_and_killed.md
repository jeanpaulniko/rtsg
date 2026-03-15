---
title: "Session 5 Registry — Proved Theorems and Killed Approaches"
nav_title: "Proved & Killed"
version: "1.0.0"
last_updated: "2026-03-09"
status: "REFERENCE — single source for what's proved and what's dead"
---

# Session 5 Registry: Proved Theorems and Killed Approaches

**Jean-Paul Niko · Sole Author**

---

## Part I: Proved Theorems

### Operator Theory

| # | Theorem | Statement | Proof | Page |
|---|---|---|---|---|
| T1 | Geometric Adjoint | $A^* = 1-A$ on $L^2(\mathbb{R}_+, dy/y^2)$ where $A=y\partial_y$ | Integration by parts | functional_bridge.md |
| T2 | Centered Skew-Adjointness | $D = A-1/2$ satisfies $D^*=-D$ | From T1 | functional_bridge.md |
| T3 | Conditional Bridge | If $D^*=-D$, $K\geq 0$, $[D,K]=0$, $D\phi=\lambda\phi$, $\langle K\phi,\phi\rangle>0$ → Re$(\lambda)=0$ | Linear algebra | functional_bridge.md |
| T4 | Bounded Bridge No-Go | On any LP scattering space, $B^*G+GB=0$ with $G$ bounded → $G=0$ | Strong stability + const of motion | bounded_bridge_nogo.md |
| T5 | No Bounded Intertwiner | $DC=CB$ with $D$ skew-adjoint, $C$ bounded → $C=0$ | Corollary of T4 | bounded_bridge_nogo.md |
| T6 | Universal Kernel (i) | $K_t=e^{-tX}$ with $X\geq 0$: $\|K_t(I-P_0)\|=e^{-t\Delta}$ | Spectral theorem | bounded_bridge_nogo.md |
| T7 | Universal Kernel (ii) | Same as T4 (strongly stable → bridge=0) | Same | bounded_bridge_nogo.md |

### Arithmetic/Structural

| # | Theorem | Statement | Proof | Page |
|---|---|---|---|---|
| T8 | Hasse-Weil Identification | BRST filter on $(S^2)^\mathcal{P}$ = étale $H^0$ projection → $\zeta(s)$ | Weil conjectures for $\mathbb{P}^1$ | arithmetic_source_space.md |
| T9 | Functional Equation | Antipodal involution on $S^2$ = Poincaré duality = $s\leftrightarrow 1-s$ | Étale cohomology | arithmetic_source_space.md |
| T10 | Visibility (meromorphic) | $\zeta(\rho-1)\neq 0$ for ζ-zeros: Res$(φ,ρ/2)\neq 0$ | Euler product at Re$=-1/2$ | functional_bridge.md |
| T11 | Spectral Disjointness | Cusp form eigenvalues $\neq$ ζ-zeros (contrapositive visibility) | Hecke L-function independence | functional_bridge.md |
| T12 | Euler Factor Mechanism | BRST-filtered prime mode + bosonic Fockization → $(1-p^{-s})^{-1}$ | Direct construction | bounded_bridge_nogo.md |

### Algebraic/Framework

| # | Theorem | Statement | Proof | Page |
|---|---|---|---|---|
| T13 | Exact Sequence | $0\to\ker(C)\to\mathcal{H}_Q\to\text{Im}(C)\to 0$ | First isomorphism theorem | cs_operator_theory.md |
| T14 | K-Matrix Positivity | $K$ PSD iff cognitive basis orthogonal | Gram matrix argument | k_bridge.md |
| T15 | Filter Non-Commutativity | $F_\text{cult}\circ F_\text{dev}\neq F_\text{dev}\circ F_\text{cult}$ | 2D counterexample | filter_algebra.md |
| T16 | Kernel Composition | Information loss monotonically non-decreasing through pipeline | Ker inclusion | filter_algebra.md |

### Numerical/Computational

| # | Result | Value | Method | Page |
|---|---|---|---|---|
| N1 | HO ground state cost | $\sigma_0^2=1/2$ | Husimi projection | cost_functional.md |
| N2 | H atom: $\sigma_{2p}>\sigma_{1s}$ | Energy $\neq$ instantiation | Coherent-state overlap | cost_functional.md |
| N3 | Li's $\lambda_n>0$ for $n\leq 20$ | Verified (30 zeros) | Direct computation | Chain E1 |
| N4 | Exact D-sum (306 discs) | 80-540× larger than ζ | Kronecker symbols | Chain C1 |

---

## Part II: Killed Approaches (The Graveyard)

### RH Approaches (10 killed)

| # | Approach | Kill Date | Killed By | Mechanism | Fatal? |
|---|---|---|---|---|---|
| K1 | Theta-family kernel $\sum\theta_\chi\otimes\bar\theta_\chi$ | 03-08 | @D_Gemini | Serre-Stark: weight 1/2 = theta series, $n^2$ support | ✓ |
| K2 | Cusp-form bypass $S_{1/2}^+(\Gamma_0(4N))$ | 03-08 | @D_Gemini | Serre-Stark applies at all levels | ✓ |
| K3 | Sylvester v1.0 ($\bar\rho+\rho\neq 0$) | 03-09 | @B_Niko | Wrong equation. Actual: resonant at $\bar\rho+\rho=1$ | ✓ |
| K4 | RTF $P^*P$ bare kernel | 03-09 | @D_Claude | Archimedean: $\Delta\propto\zeta(\bar u+s)\neq 0$ off-diagonal | ✓ |
| K5 | RTF $P^{\vee*}P$ dual | 03-09 | @D_Claude | Self-dual ($\varepsilon=1$ for quadratic chars) | ✓ |
| K6 | RTF $K_f$ dressed | 03-09 | @D_Gemini | $h_f(s)$ univariate + Paley-Wiener | ✓ |
| K7 | Exact D-sum cancellation | 03-09 | @D_Claude | 306 discriminants, 80-540× LARGER | ✓ |
| K8 | Wigner $\Theta=-M^{-1}M'$ | 03-09 | @D_GPT | Noncompact, divergent, signed (4 citations) | ✓ |
| K9 | SVD v2.5 circular | 03-09 | @D_Claude | $A=1/2+iT$ is RH → conclusion in premise | ✓ |
| K10 | ALL bounded bridges | 03-09 | @D_GPT | Strong stability theorem: $G=0$ | ✓ (permanent) |

### YM Approaches (partial kills)

| # | Approach | Status | Issue |
|---|---|---|---|
| K11 | $I-C^*C = H$ (raw) | KILLED | Bounded $\neq$ unbounded (GPT) |
| K12 | Polyakov loop = Clay gap | PARTIAL | Finite-T only (Svetitsky-Yaffe) |
| K13 | RG monotonicity | KILLED | Does not give constructive bound (Gemini, session 4) |

### Structural/Framework (kills from Gemini)

| # | Approach | Status | Issue |
|---|---|---|---|
| K14 | Archimedean from $S^2$ heat kernel | KILLED | $\zeta_{S^2}(s)$ ≠ $\Gamma(s/2)$ (Gemini B4) |
| K15 | Deligne closes local-global gap | KILLED | $H^1(\mathbb{P}^1)=0$, Deligne vacuous (Claude) |
| K16 | Faltings → Hodge via BRST=étale | PARTIAL | $\mathbb{P}^1$ not abelian (Claude) |

---

## Part III: What Survives

| Direction | Status | Key Result | Next Step |
|---|---|---|---|
| De Branges spaces for LP | OPEN | Only unbounded path survives T4 | Construct HB function from LP data |
| Hasse-Weil / BRST = étale | PROVED | $\zeta(s)$ from source space | Formalize adelic construction |
| $C_t=e^{-tH/2}$ for YM | PROVED | Correct bounded transform | Constructive QFT gap |
| Fock space Euler product | PROVED | Filtered modes + Fockization | Connect to de Branges form |
| Fradkin-Shenker armor | CITED | GL↔confinement continuity | Already in paper |
| Plato → RTSG | PUBLISHED | Cave = exact sequence | Already on wiki |
| Filter algebra | PROVED | Non-abelian monoid | P≠NP connection weak |

---

*Jean-Paul Niko · RTSG BuildNet · smarthub.my · Session 5, March 9 2026*
