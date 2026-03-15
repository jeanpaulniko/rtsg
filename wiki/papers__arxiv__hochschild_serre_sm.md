---
title: "Hochschild-Serre Spectral Sequence for the Standard Model BRST Complex"
nav_title: "HS-SM Paper"
version: "0.1 — outline"
last_updated: "2026-03-08"
status: "DRAFT — computation complete, framing updated after 4-agent adversarial convergence"
---

# Hochschild-Serre Spectral Sequence for the Standard Model BRST Complex

**Jean-Paul Niko** · Draft Outline

---

## Abstract (draft, ~150 words)

We compute the Hochschild-Serre spectral sequence and Chevalley-Eilenberg deformation cohomology for the BRST complex of the Standard Model coupled to gravity, treating the full gauge symmetry as the semi-direct product $\text{Diff}(M) \ltimes (SU(3)_c \times SU(2)_L \times U(1)_Y)$. We prove three results. First, the SM gauge algebra is rigid: $H^2_{CE}(\mathfrak{g}_{SM}; \mathfrak{g}_{SM}) = 0$, following from Whitehead's lemmas on the semisimple factors and the single-abelian constraint. No infinitesimal deformation of the gauge bracket exists on the fixed 12-generator complex. Second, the Hochschild-Serre $d_2$ differential vanishes identically on all generally covariant deformations, by Cartan's magic formula — general covariance geometrically guarantees that gravity cannot algebraically obstruct internal gauge choices. The spectral sequence collapses at $E_2$. Third, BSM extensions (dark photon, GUT embedding) are algebraically permitted but require enlarging the BRST complex, not deforming it — they are extensions, not deformations. To our knowledge, this is the first computation of the full deformation cohomology for the SM gauge structure coupled to gravity. We discuss implications for the classification of consistent BSM extensions and the role of global topological constraints beyond local algebraic BRST cohomology.

---

## 1. Introduction

- The SM gauge group is usually treated as $SU(3) \times SU(2) \times U(1)$, ignoring the coupling to gravity
- BRST deformation theory (Barnich-Brandt-Henneaux 2000) classifies consistent deformations of gauge theories
- BBH compute local BRST cohomology for pure YM — they do NOT extend to the full SM with gravity
- **Gap in the literature:** No computation of $H^1$ or $H^2$ for the complete SM BRST complex with gravity (confirmed by literature search, no results in arXiv/InspireHEP)
- **This paper:** Fill the gap using Hochschild-Serre for the semi-direct product

---

## 2. Preliminaries

### 2.1 BRST for Yang-Mills + Gravity
- Standard BRST construction for $G_{\text{int}} = SU(3) \times SU(2) \times U(1)$
- Standard BRST for diffeomorphisms (BV formalism)
- The combined system: $s = s_0 + s_{\text{int}}$ with $s^2 = 0$

### 2.2 Why the Direct Product Fails
- If $G = \text{Diff} \times G_{\text{int}}$: ghost sectors orthogonal, $\{s_0, s_{\text{int}}\} = 0$
- Künneth: $H^*(s) = H^*(s_0) \otimes H^*(s_{\text{int}})$
- Spectral sequence degenerates at $E_2$, $d_2 \equiv 0$
- **No new structure** — trivially sterile
- But physically: gravity DOES act on gauge fields (Lie transport, gauge bundle dragging)

### 2.3 The Semi-Direct Product
- $G_{\text{true}} = \text{Diff}(M) \ltimes G_{\text{int}}$
- $\{s_0, s_{\text{int}}\} = \mathcal{L}_{c_0} s_{\text{int}} \neq 0$
- Lie derivative couples gravity ghost to gauge ghosts
- Total nilpotency $s^2 = 0$ preserved by equivariance of gauge bundle

---

## 3. The Hochschild-Serre Spectral Sequence

### 3.1 Setup
- Lie algebra extension $0 \to \mathfrak{g}_{\text{int}} \to \mathfrak{g}_{\text{full}} \to \mathfrak{diff} \to 0$
- HS spectral sequence: $E_2^{p,q} = H^p(\mathfrak{diff};\, H^q(\mathfrak{g}_{\text{int}}, \mathcal{F})) \Rightarrow H^{p+q}(s)$
- The $\mathfrak{diff}$ action on $H^q(\mathfrak{g}_{\text{int}})$ is via Lie derivative

### 3.2 $E_2$ Page
- $E_2^{0,0}$: diff-invariant, gauge-invariant observables = physical observables (the Hilbert space)
- $E_2^{0,1}$: diff-invariant internal gauge deformations = BSM candidates
- $E_2^{1,0}$: first diff cohomology with gauge-invariant coefficients
- $E_2^{2,0}$: second diff cohomology = gravitational obstructions

### 3.3 The $d_2$ Differential
- $d_2: E_2^{0,1} \to E_2^{2,0}$: takes a BSM gauge deformation to a gravitational obstruction
- Explicit formula: $d_2(\omega)(\xi_1, \xi_2) = \mathcal{L}_{\xi_1}(\iota_{\xi_2}\omega) - \mathcal{L}_{\xi_2}(\iota_{\xi_1}\omega) - \iota_{[\xi_1,\xi_2]}\omega$
- Physical content: curvature of the lift from internal to full complex
- Vanishes iff the deformation is compatible with general covariance

---

## 4. Explicit Computations

### 4.1 $H^1$ at the SM Point
- Internal: 3 coupling constants + 2 theta angles = 5 continuous directions (from BBH for pure YM)
- The HS spectral sequence preserves these (they are diff-covariant)
- Additional discrete directions: gauge group extensions (adding new factors)

### 4.2 $d_2$ on a Dark Photon ($U(1)'$)
- Deformation: $\omega = (A'_\mu, c', g')$ — new gauge field, ghost, coupling
- $\mathcal{L}_\xi A'_\mu = \xi^\nu \partial_\nu A'_\mu + A'_\nu \partial_\mu \xi^\nu$ — standard 1-form transport
- $d_2(\omega) = 0$: the dark photon is diff-covariant
- **Result: dark photon SURVIVES**

### 4.3 $d_2$ on $SU(5)$ GUT Embedding
- Deformation: adjoint Higgs $\Phi \in \mathbf{24}$ breaking $SU(5) \to SU(3) \times SU(2) \times U(1)$
- $\mathcal{L}_\xi \Phi = \xi^\mu \partial_\mu \Phi$ — standard scalar transport
- $d_2(\Phi) = 0$: GUT Higgs is diff-covariant
- **Result: GUT embedding SURVIVES**

### 4.4 What $d_2$ Kills — Honest Answer
$d_2 \equiv 0$ for ALL generally covariant deformations. By Cartan's magic formula, $s_0 \omega = \int_M \partial_\mu(c_0^\mu \sqrt{-g} \mathcal{L}_{BSM}) d^4x = 0$ for any covariant scalar density integrated over $M$ without boundary.

The compensating parameter $\alpha = 0$ identically, so $d_2[\omega] = s_0(0) = 0$.

**$d_2$ kills nothing physical.** General covariance is too weak a constraint to obstruct BSM gauge choices algebraically. Any consistent, anomaly-free, generally covariant gauge deformation survives the spectral sequence.

This is an honest negative result. It means the semi-direct product $\text{Diff} \ltimes \text{Gauge}$, while physically correct, does not generate the cross-stage obstructions that were initially conjectured.

---

## 5. The Internal Sector (Künneth)

### 5.1 Internal Factorization
- $H^*(s_1 + s_2) = H^*(s_1) \otimes H^*(s_2)$ for $SU(3) \times SU(2) \times U(1)$ (strict direct product)
- Internal grading is sterile — no new obstructions within gauge sector alone
- Anomaly cancellation: cross-sector constraint, but present in BOTH graded and ungraded treatments

### 5.2 The Anomaly Cancellation as $E_2$ Structure
- Mixed anomalies $\text{Tr}(T^{(1)}\{T^{(2)},T^{(2)}\})$ are elements of $H^1(s_{\text{int}})$
- They are NOT new from the grading — they are internal structure visible at $E_2$ but always present monolithically
- The grading provides a natural DECOMPOSITION but not new cohomology

---

## 6. Discussion

### 6.1 The SM is Extensible, Not Rigid
- $H^1 \neq 0$: BSM physics is permitted. The SM admits continuous deformations (couplings, theta angles) and discrete extensions (new gauge groups)
- $d_2 \equiv 0$: general covariance provides NO algebraic obstruction to BSM gauge choices
- $H^2_{CE} = 0$: the gauge bracket cannot be deformed on a fixed complex — only extended
- **Any principle constraining BSM must be global/topological, not local/algebraic** — this is the key result

### 6.2 The Classification of BSM Extensions

Given the permissiveness of local BRST, the physically meaningful question becomes: which extensions are consistent at the GLOBAL level? In RTSG, this is the question of which dormant $S^2$ factors from $\Omega = (S^2)^\infty$ can be activated.

**Proposed selection mechanism (Gemini, 2026-03-08):** The bisimulation quotient $QS/\!\sim_{bisim}$ constrains which $S^2$ factors can successfully instantiate into PS. A new gauge sector must not only be locally anomaly-free but must pass the global bisimulation consistency — its relational structure must be compatible with the existing quotient structure of spacetime.

This is analogous to the difference between local and global anomalies: a theory can be locally consistent (perturbative anomaly cancellation) but globally inconsistent (Witten's $SU(2)$ anomaly). The bisimulation constraint is the RTSG version of a global consistency condition.

### 6.2 Connection to Source Space Geometry
- In RTSG ($\Omega = (S^2)^\infty$): BSM extensions = activating new $S^2$ factors
- Each new $S^2$ contributes an automatically diff-covariant gauge field ($\text{Aut}(S^2) = PSL(2,\mathbb{C})$)
- The semi-direct product is a consequence of the source space self-containment (Axiom 0)
- PREDICTION: all BSM gauge physics = dormant $S^2$ factors

### 6.3 Comparison with BBH
- BBH (2000): pure YM, no gravity, internal cohomology only
- This paper: full SM + gravity, semi-direct product, Hochschild-Serre
- BBH's rigidity result for pure YM is recovered as a special case (internal $E_2$ factors by Künneth)
- The novelty: gravity coupling via $d_2$ provides the missing physical constraint

---

## 7. Conclusion

First computation of BRST deformation cohomology for the complete Standard Model with gravity. The semi-direct product $\text{Diff}(M) \ltimes G_{\text{int}}$ is essential — direct product gives trivially sterile results. The Hochschild-Serre $d_2$ differential enforces the equivalence principle on BSM physics: all extensions must be generally covariant. Dark photon and GUT embedding survive; non-covariant modifications are killed. The SM is extensible within the covariance constraint.

---

## References (to compile)

1. Barnich, Brandt, Henneaux — Phys.Rept. 338 (2000) [hep-th/0002245]
2. Barnich, Henneaux — Phys.Lett.B 311 (1993) [hep-th/9304057] — deformation theory
3. Hochschild, Serre — Trans.AMS 74 (1953) — spectral sequence for group extensions
4. Niko — RTSG Framework (this wiki / arXiv forthcoming)
