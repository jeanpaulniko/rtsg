---
title: "Layer 3 — Gauge Groups from Source Space Geometry"
nav_title: "Source Space Gauges"
version: "1.0.0"
last_updated: "2026-03-08"
status: "active development — hardest layer, partial results + research program"
---

# Layer 3 — Gauge Groups from Source Space Geometry

**Jean-Paul Niko · Sole Author**

!!! info "Purpose"
    This is the hardest layer of the instantiation cascade formalization. We attempt to **derive** the Standard Model gauge group $SU(3) \times SU(2) \times U(1)$ from the geometry of the source space $\Omega = (S^2)^\infty$. If successful, this would make the entire graded BRST decomposition a consequence of source space geometry rather than a post hoc assignment — and would be a major step toward RTSG as a true Theory of Everything.

!!! danger "Integrity"
    This page contains a mix of established mathematics, new propositions, and open conjectures. The boundary is marked clearly throughout. The gauge group derivation is **not complete** — this is a research program with partial results.

---

## 1. What We Need to Derive

The [Graded BRST](../rtsg/graded_brst.md) framework assigns:

- Stage 0: Diff$(M)$
- Stage 1: $SU(2)_L \times U(1)_Y$
- Stage 2: $SU(3)_c$

These assignments are currently **post hoc** — motivated by physics but not derived from RTSG axioms. A first-principles derivation requires showing that $\Omega = (S^2)^\infty$ produces exactly these gauge groups and no others.

---

## 2. What Source Space Already Gives Us

### 2.1 Lorentz Invariance (Established)

From [Source Space](../rtsg/source_space.md):

$$\text{Aut}(S^2) = PSL(2,\mathbb{C}) \cong SO^+(1,3)$$

The automorphism group of a single $S^2$ factor is the restricted Lorentz group. **Lorentz invariance is not postulated — it emerges from the building block.**

### 2.2 Flag Manifold Embedding (Established)

For a compact Lie group $G$ with maximal torus $T$ of rank $r$:

$$G/T \hookrightarrow (S^2)^r$$

This is the Borel embedding (for complex semisimple groups: $G_\mathbb{C}/B \cong G/T$ embeds in $(\mathbb{CP}^1)^r = (S^2)^r$). The rank of $G$ determines how many $S^2$ factors participate.

| Group $G$ | Rank $r$ | $G/T$ | $S^2$ factors needed |
|---|---|---|---|
| $U(1)$ | 1 | $S^1 \hookrightarrow S^2$ | 1 |
| $SU(2)$ | 1 | $S^2$ | 1 |
| $SU(3)$ | 2 | $SU(3)/T^2$ | 2 |
| $SU(2) \times U(1)$ | 2 | $S^2 \times S^1$ | 2 |
| Full SM: $SU(3) \times SU(2) \times U(1)$ | 4 | — | 4 |

**The SM gauge group of rank 4 requires exactly 4 $S^2$ factors.** From source space, the first 4 factors of $\Omega = (S^2)^\infty$ provide the arena.

### 2.3 The CFN Decomposition (Established)

The Cho-Faddeev-Niemi decomposition of a gauge field into three components maps onto the three-space decomposition:

| CFN component | RTSG space | Physical role |
|---|---|---|
| Topological ($\hat{n}$-field) | CS | Instantiation structure |
| Abelian (restricted) | QS | Quantum degrees of freedom |
| Valence (off-diagonal) | PS | Observable / physical |

### 2.4 The Spectral Gap (Established)

The Laplacian on $S^2$ has spectral gap $\Delta = 2$. On $(S^2)^n$, the gap remains 2 (from any single factor). This gap seeds the YM mass gap in the GL picture:

$$\Delta_{\text{YM}} = \sqrt{2\alpha_2} = 1/\xi_{W_2}$$

---

## 3. The Derivation Program

### 3.1 Strategy: Symmetry Breaking of Aut$(\Omega)$

The full automorphism group of $\Omega = (S^2)^\infty$ is:

$$\text{Aut}(\Omega) = \text{Aut}(S^2)^\infty \rtimes S_\infty = PSL(2,\mathbb{C})^\infty \rtimes S_\infty$$

where $S_\infty$ is the infinite symmetric group permuting the factors.

This is enormously larger than the SM gauge group. The derivation requires a **symmetry-breaking mechanism** that selects $SU(3) \times SU(2) \times U(1)$ from Aut$(\Omega)$.

### 3.2 The Finite-Factor Selection

**Proposition 11 (Dimensional constraint).** *Physical spacetime is 4-dimensional. The Stage 0 geometric condensate $W_0$ lives on $(S^2)^4$ (four copies for a 4D manifold — see GFT analogy in [Stage 0 Gravity](../rtsg/stage0_gravity.md)). Only the first 4 $S^2$ factors participate in the geometric condensate. The remaining factors are "internal" — they contribute gauge degrees of freedom, not spacetime dimensions.*

**Conjecture (4+4 structure).** *The source space organizes as:*

$$(S^2)^\infty = \underbrace{(S^2)^4}_{\text{spacetime}} \times \underbrace{(S^2)^4}_{\text{internal gauge}} \times \underbrace{(S^2)^\infty}_{\text{higher structure}}$$

*The first 4 factors produce spacetime (Stage 0). The next 4 factors produce the SM gauge group (Stages 1+2). The remaining infinite tail provides the space for higher complexity (consciousness, intelligence, relational structure beyond physics).*

⚠ **Status: Conjecture.** The 4+4 split is motivated by the rank-4 SM gauge group and 4D spacetime, but the mechanism that selects exactly 4+4 from the infinite product is not derived.

### 3.3 From $(S^2)^4$ to $SU(3) \times SU(2) \times U(1)$

The internal $(S^2)^4$ has automorphism group:

$$\text{Aut}_{\text{internal}} = PSL(2,\mathbb{C})^4 \rtimes S_4$$

We need to extract $SU(3) \times SU(2) \times U(1)$ (rank 4, dimension 12) from this structure.

**Proposition 12 (Gauge group from factor partitioning — Conjecture).** *The partition $4 = 2 + 1 + 1$ of the internal $S^2$ factors corresponds to the SM gauge group decomposition:*

| Partition | $S^2$ factors | Gauge group | Rank | Stage |
|---|---|---|---|---|
| 2 factors together | $(S^2)^2$ | $SU(3)_c$ | 2 | 2 |
| 1 factor | $(S^2)^1$ | $SU(2)_L$ | 1 | 1 |
| 1 factor | $(S^2)^1$ | $U(1)_Y$ | 1 | 1 |

*The partition is determined by the three-space projections $(\pi_Q, \pi_P, \pi_C)$ acting differently on each subset.*

**Mathematical basis:** The flag manifold of $SU(3)$ is $SU(3)/T^2 \cong \mathbb{F}_{1,2}$, which embeds in $(S^2)^2$. The flag manifold of $SU(2)$ is $SU(2)/U(1) = S^2$, which is a single factor. $U(1)/\{e\} = S^1 \hookrightarrow S^2$, also a single factor.

The key constraint: **why this partition and not another?**

### 3.4 The Partition Selection Mechanism

Four internal $S^2$ factors can be partitioned as: $4 = 4$, $3+1$, $2+2$, $2+1+1$, $1+1+1+1$.

| Partition | Would give | Rank | Reality? |
|---|---|---|---|
| $4$ | $SU(5)$ or $Sp(4)$ | 4 | GUT — not realized at low energy |
| $3+1$ | $SU(4) \times U(1)$ | 4 | Pati-Salam partial — not SM |
| $2+2$ | $SU(3) \times SU(3)$ | 4 | Trinification — not SM |
| **$2+1+1$** | **$SU(3) \times SU(2) \times U(1)$** | **4** | **SM** ✓ |
| $1+1+1+1$ | $U(1)^4$ | 4 | Abelian only — no confinement |

**Proposition 13 (Partition from complexity ordering — Conjecture).** *The three-space projection operators $(\pi_Q, \pi_P, \pi_C)$ impose a complexity ordering on the internal factors. The $\pi_Q$ projection (quantum/complex structure) acts on 2 factors simultaneously (producing the non-abelian $SU(3)$ with its entangled color structure). The $\pi_P$ projection (real/metric structure) acts on 1 factor (producing $SU(2)$, which governs chirality — a metric-dependent concept). The $\pi_C$ projection (relational/topological) acts on 1 factor (producing $U(1)$, the simplest gauge group — phase rotation of relations).*

*The partition $2+1+1$ is selected because it is the unique partition compatible with all three projections acting on non-overlapping subsets.*

⚠ **Status: Conjecture.** The argument is suggestive but not rigorous. We need to formalize what "the projections act on non-overlapping subsets" means mathematically and prove that this forces $2+1+1$.

### 3.5 The GUT Embedding at High Energy

The partition $2+1+1$ at low energy is compatible with unification at high energy:

$$SU(3) \times SU(2) \times U(1) \subset SU(5) \subset SO(10)$$

At energies above the GUT scale $\sim 10^{16}\,\text{GeV}$, the partition merges: $2+1+1 \to 4$. All four internal $S^2$ factors become equivalent under the unified symmetry. The partition $2+1+1$ is a **low-energy symmetry breaking pattern** from the fully symmetric $4 = 4$.

**RTSG reading:** At the highest energies (near Stage 0 criticality), all internal factors are equivalent — the full Aut$((S^2)^4)$ symmetry is unbroken. As the universe cools and the instantiation cascade proceeds, the three projections $(\pi_Q, \pi_P, \pi_C)$ successively break this symmetry:

1. $\pi_C$ separates 1 factor → $U(1)_Y$ decouples (hypercharge)
2. $\pi_P$ separates 1 factor → $SU(2)_L$ decouples (weak isospin)
3. The remaining 2 factors are governed by $\pi_Q$ → $SU(3)_c$ (color)

This gives the **reverse** of the standard GUT symmetry breaking: in RTSG, the projections break the unified symmetry, and the ordering is determined by complexity (relational < metric < quantum).

---

## 4. The Three Projections and Gauge Sectors

### 4.1 Formal Definition of Projections on Internal Space

Let $\Omega_{\text{int}} = (S^2)_a \times (S^2)_b \times (S^2)_c \times (S^2)_d$ be the internal four factors.

**Definition.** The three projections restricted to $\Omega_{\text{int}}$ are:

| Projection | Acts on | Preserves | Output |
|---|---|---|---|
| $\pi_C$ | $(S^2)_d$ | Topological structure (connectedness, path structure) | $U(1)_Y$ — phase (angle on $S^1 \hookrightarrow S^2$) |
| $\pi_P$ | $(S^2)_c$ | Real/metric structure (distances, angles) | $SU(2)_L$ — rotations (isometries of $S^2$) |
| $\pi_Q$ | $(S^2)_a \times (S^2)_b$ | Complex structure (holomorphic maps) | $SU(3)_c$ — from holomorphic automorphisms of $\mathbb{CP}^1 \times \mathbb{CP}^1$ |

### 4.2 Why $SU(3)$ from Two Factors

**Proposition 14 (Color from biholomorphic structure — Conjecture).**

Two copies of $S^2 = \mathbb{CP}^1$ give:

$$\text{Aut}_{\text{hol}}(\mathbb{CP}^1 \times \mathbb{CP}^1) = PSL(2,\mathbb{C}) \times PSL(2,\mathbb{C}) \rtimes \mathbb{Z}_2$$

The compact real form of the diagonal $PSL(2,\mathbb{C})$ is $SU(2)$. But we need $SU(3)$, which has rank 2. The route:

Consider the **Segre embedding**:

$$\mathbb{CP}^1 \times \mathbb{CP}^1 \hookrightarrow \mathbb{CP}^3$$

The image is a smooth quadric surface $Q \subset \mathbb{CP}^3$. The automorphism group of $Q$ as a projective variety is:

$$\text{Aut}(Q) = SO(4,\mathbb{C}) / \{\pm I\} \cong (SL(2,\mathbb{C}) \times SL(2,\mathbb{C})) / \mathbb{Z}_2$$

Now, the key move: the $\pi_Q$ projection preserves complex structure but **breaks the $\mathbb{Z}_2$ exchange symmetry** between the two factors (because $\pi_Q$ acts on the pair as an ordered product, not a symmetric one — the relational structure of QS distinguishes the factors). This breaking reduces:

$$(SL(2,\mathbb{C}) \times SL(2,\mathbb{C})) / \mathbb{Z}_2 \longrightarrow SL(3,\mathbb{C})$$

via the representation-theoretic embedding $\mathbf{2} \otimes \mathbf{2} = \mathbf{3} \oplus \mathbf{1}$. The $\mathbf{3}$ is the fundamental of $SU(3)$; the $\mathbf{1}$ is the singlet (which becomes the $U(1)_B$ baryon number — a global symmetry, not gauged).

The compact real form: $SL(3,\mathbb{C}) \to SU(3)$ as the maximal compact subgroup.

⚠ **Status: This is the most conjectural part of the entire page.** The step from $SL(2) \times SL(2) \to SL(3)$ via $\mathbf{2} \otimes \mathbf{2}$ is a real representation-theoretic fact, but the physical justification for why $\pi_Q$ breaks the $\mathbb{Z}_2$ and selects the $\mathbf{3}$ over the $\mathbf{1}$ needs substantial work. This is the crux of the derivation.

### 4.3 Hypercharge Quantization

**Proposition 15 (Hypercharge from $S^1 \hookrightarrow S^2$ — Conjecture).**

$U(1)_Y$ comes from $\pi_C$ acting on a single $S^2$ factor. The relational projection preserves only the topological structure — the path-connectedness of $S^2$. The great circles $S^1 \hookrightarrow S^2$ form the orbits under $U(1) \subset \text{Aut}(S^2)$.

The quantization of hypercharge ($Y \in \{-2, -1, 0, 1, 2, \ldots\}/3$ for SM fermions) would follow from the representation theory of $U(1)$ acting on sections of line bundles over $S^2$:

$$H^0(S^2, \mathcal{O}(n)) \cong \text{polynomials of degree } n$$

The allowed hypercharges correspond to the allowed degrees $n$, which are constrained by anomaly cancellation at Stage 1.

---

## 5. Connecting Back to the Cascade

If this derivation program succeeds, the entire instantiation cascade becomes **derived from source space geometry**:

| Layer | Content | Status |
|---|---|---|
| Source space | $\Omega = (S^2)^\infty$ | Axiom (from Axiom 0 + $S^2$ building block) |
| Lorentz invariance | Aut$(S^2) = SO^+(1,3)$ | **Proved** (established math) |
| Spacetime | $(S^2)^4_{\text{external}}$ → Diff$(M)$ → Stage 0 | **Partial** (GFT condensate analogy) |
| Gauge groups | $(S^2)^4_{\text{internal}}$ → $SU(3) \times SU(2) \times U(1)$ | **Conjectural** (this page) |
| Graded BRST | $s = s_0 + s_1 + s_2$ from the above | Would follow from gauge derivation |
| GL potentials | $S_k[W_k]$ for each stage | **Built** ([Graded BRST](../rtsg/graded_brst.md)) |
| Topological charges | $\pi_3(G_k) \to Q_k$ per stage | **Built** ([Topological Charges](../math/topological_charges.md)) |
| Dark matter | $H^0(s_0) \setminus H^0(s_0+s_1)$ | **Derived** from graded BRST |
| Stage transitions | GL phase transitions + Kibble-Zurek | **Framework built** |

---



---

## 8. Connection to Hochschild-Serre (from Gap 3 Attack, 2026-03-08)

The Gap 3 computation reveals that the correct gauge architecture is not a direct product but a **semi-direct product** $\text{Diff}(M) \ltimes G_{\text{int}}$. This has direct implications for the source space gauge derivation:

### 8.1 Why Source Space Gives Semi-Direct, Not Direct

In $\Omega = (S^2)^\infty$, the external factors $(S^2)^4_{\text{ext}}$ (spacetime) and internal factors $(S^2)^4_{\text{int}}$ (gauge) are NOT independent. The source space is a single connected object — the factors are entangled through the self-referential structure $\Omega = \{S^2, \Omega\}$.

The automorphism group $\text{Aut}(\Omega) = PSL(2,\mathbb{C})^\infty \rtimes S_\infty$ acts on ALL factors simultaneously. When we separate external from internal, the external Aut (= Diff) still acts on the internal factors by permutation and dragging — this is the Lie derivative coupling $\mathcal{L}_{c_0}$ that Gemini identified.

**Result:** The semi-direct product $\text{Diff}(M) \ltimes G_{\text{int}}$ is not an additional assumption — it is a **consequence of the source space being a single connected object.** A direct product would require the external and internal factors to be truly independent, which contradicts $\Omega = \{S^2, \Omega\}$ (Axiom 0: self-containment means everything is connected to everything).

### 8.2 The Partition $2+1+1$ Under Semi-Direct Structure

The Hochschild-Serre spectral sequence gives: $E_2^{p,q} = H^p(\mathfrak{diff};\, H^q(\mathfrak{g}_{\text{int}}))$.

The $d_2$ differential enforces diff-covariance. The partition $2+1+1$ must be **stable under $d_2$** — the decomposition of internal factors into $SU(3) \times SU(2) \times U(1)$ must be respected by diffeomorphisms. This is automatically true because all gauge fields transform as tensor fields under diffeomorphisms (they're differential forms on the spacetime manifold).

But this gives a constraint the other way: **any partition of the internal $(S^2)^4$ that produces a gauge group whose fields are NOT tensor fields under Diff$(M)$ is $d_2$-killed.** This eliminates exotic gauge structures that don't live in standard fiber bundles over spacetime.

### 8.3 Why BSM Extensions Must Come From Activating New $S^2$ Factors

The $d_2$ computation (@D_Claude) showed that adding a $U(1)'$ dark photon or embedding in $SU(5)$ both survive — they're diff-covariant. In source space terms: these correspond to activating additional $S^2$ factors from the infinite tail of $\Omega$.

Each new $S^2$ factor activated contributes a new gauge degree of freedom. Its field transforms as a 1-form under Diff$(M)$ (because $\text{Aut}(S^2) = PSL(2,\mathbb{C}) \cong SO^+(1,3)$ provides the Lorentz frame). The semi-direct structure is preserved automatically.

**Prediction:** All BSM gauge extensions that will ever be discovered correspond to activating dormant $S^2$ factors from $\Omega = (S^2)^\infty$. The infinite product is the reservoir of all possible gauge physics. The SM uses 4 internal factors. BSM physics uses 5 or more.

## 9. Open Gaps (Honest)

1. **The $SU(3)$ derivation (Gap 3.4.2).** The step $SL(2) \times SL(2) \to SL(3)$ via $\pi_Q$ breaking $\mathbb{Z}_2$ is the weakest link. Needs: a precise definition of how $\pi_Q$ acts on the ordered pair, and why it selects the $\mathbf{3}$ representation over other possibilities.

2. **Why 4+4?** The split of $(S^2)^\infty$ into 4 external + 4 internal factors is postulated, not derived. The number 4 for spacetime dimensions might follow from requiring $W_0$ to produce a smooth Lorentzian manifold (4D is special — admits both $SO^+(1,3)$ and $SU(2)_L \times SU(2)_R$ spin structure). For the internal factors, rank 4 = SM is empirical.

3. **Projection formalization.** The projections $(\pi_Q, \pi_P, \pi_C)$ are defined abstractly (preserve complex/metric/topological structure). Their action on the internal factors needs a rigorous categorical formulation — probably as functors on the category of $(S^2)$-bundles.

4. **Running couplings.** The three gauge couplings $g_1, g_2, g_3$ run with energy. Near the GUT scale they approximately unify. Can this running be derived from the geometry of $(S^2)^4_{\text{internal}}$ as the factors become equivalent at high energy? The beta functions should emerge from the spectral action on $(S^2)^4$.

5. **Generations.** The SM has 3 generations of fermions. This is not addressed by the gauge group derivation alone. In string theory, generations come from the Euler characteristic of the compactification manifold. In RTSG, they should come from a topological invariant of $(S^2)^4_{\text{internal}}$. Candidate: $\chi((S^2)^4) = \chi(S^2)^4 = 2^4 = 16$, which is not 3. This gap needs work.

6. **Gravity vs. gauge.** The assignment of Diff$(M)$ to Stage 0 and gauge groups to Stages 1-2 treats gravity differently from gauge forces. In the source space picture, external and internal factors are both $S^2$ — what distinguishes them? The GFT condensate story ([Stage 0 Gravity](../rtsg/stage0_gravity.md)) provides one answer: the external factors condense into spacetime, the internal ones provide gauge structure. But the mechanism selecting which factors condense is not derived.

---

## 10. The Three Predictions If This Works

If the gauge derivation program succeeds:

1. **No new gauge forces.** $SU(3) \times SU(2) \times U(1)$ is the unique output of 4 internal $S^2$ factors with the $2+1+1$ partition. BSM gauge groups (extra $U(1)$'s, $SU(5)$ GUT remnants) are forbidden unless additional $S^2$ factors activate — which would require higher complexity than the current universe supports.

2. **GUT unification energy.** The energy scale at which the partition merges $2+1+1 \to 4$ is computable (in principle) from the GL potential on $(S^2)^4_{\text{internal}}$. This should match the GUT scale $\sim 10^{16}\,\text{GeV}$.

3. **Proton decay rate.** If GUT unification is achieved at a definite scale, the proton lifetime is fixed. This is testable (Hyper-Kamiokande).

---

## 11. Summary

$$\Omega = \underbrace{(S^2)^4_{\text{ext}}}_{\text{spacetime}} \times \underbrace{(S^2)^2_{\pi_Q}}_{\to SU(3)} \times \underbrace{(S^2)^1_{\pi_P}}_{\to SU(2)} \times \underbrace{(S^2)^1_{\pi_C}}_{\to U(1)} \times (S^2)^\infty_{\text{higher}}$$

$$\text{Aut}(S^2) = PSL(2,\mathbb{C}) \cong SO^+(1,3) \qquad \text{(Lorentz — proved)}$$

$$G/T \hookrightarrow (S^2)^{\text{rank}(G)} \qquad \text{(Borel embedding — proved)}$$

$$\mathbf{2} \otimes \mathbf{2} = \mathbf{3} \oplus \mathbf{1} \qquad \text{(rep theory — proved; physical selection — conjectural)}$$
