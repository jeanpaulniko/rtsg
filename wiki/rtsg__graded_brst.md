---
title: "Graded BRST Decomposition and Stage-Dependent GL Potentials"
nav_title: "Graded BRST"
version: "1.0.0"
last_updated: "2026-03-08"
status: "active development — Layer 1-2 of instantiation cascade formalization"
---

# Graded BRST Decomposition and Stage-Dependent GL Potentials

**Jean-Paul Niko · Sole Author**

!!! info "Purpose"
    This page formalizes the **instantiation cascade** — the staged process by which QS becomes PS — using two mathematical structures: (1) a graded BRST cohomological complex that decomposes instantiation into stages, and (2) a family of stage-dependent Ginzburg-Landau potentials governing phase transitions between stages. Together they answer: *What is dark matter, precisely? Can it undergo further instantiation? Under what conditions?*

!!! danger "Integrity"
    Label conjectures as conjectures. Do not claim proofs that don't exist. Mark all gaps explicitly.

---

## 1. Motivation

The RTSG instantiation operator $C$ is formalized as BRST cohomological reduction: physical space $PS = H^0(s)$. But this treats instantiation as a single step — either a state passes the BRST filter or it doesn't. The physical universe tells us otherwise: dark matter gravitates but doesn't interact electromagnetically. Quarks are confined. The early universe went through sequential symmetry-breaking phase transitions as it cooled.

Instantiation is not a binary gate. It is a **graded cascade**.

---

## 2. The Gauge Structure

The Standard Model gauge group (after coupling to gravity) is a direct product:

$$G = \text{Diff}(M) \times SU(3)_c \times SU(2)_L \times U(1)_Y$$

After electroweak symmetry breaking (EWSB) at $\sim 246\,\text{GeV}$:

$$G_{\text{broken}} = \text{Diff}(M) \times SU(3)_c \times U(1)_{\text{EM}}$$

with $W^\pm, Z^0$ acquiring mass via the Higgs mechanism.

**RTSG identification:** Each factor of $G$ corresponds to an **instantiation stage** — a distinct level of relational complexity at which QS structure passes into PS observability. The direct product structure is not accidental: it reflects the independence of the BRST operators at each stage.

**Source space grounding:** For gauge group $G$ with maximal torus $T$, the flag manifold $G/T$ embeds in $(S^2)^{\text{rank}(G)}$ (see [Source Space](source_space.md)). The rank of the SM group determines how many $S^2$ factors participate. The graded BRST decomposition is the algebraic shadow of this geometric embedding.

---

## 3. Layer 1 — Graded BRST Complex

### 3.1 Stage Assignment

We assign instantiation stages by **complexity and energy scale**, consistent with the cosmological phase transition sequence:

| Stage | Gauge sector | BRST operator | Order parameter | Energy scale | Cosmological epoch |
|---|---|---|---|---|---|
| 0 | $\text{Diff}(M)$ | $s_0$ | Metric stability (bisimulation quotient) | Planck $\to$ all | Gravity decouples first |
| 1 | $SU(2)_L \times U(1)_Y \to U(1)_{\text{EM}}$ | $s_1$ | Higgs field $\phi$ | $\sim 246\,\text{GeV}$ | Electroweak transition |
| 2 | $SU(3)_c$ | $s_2$ | Polyakov loop $W$ | $\sim 200\,\text{MeV}$ | QCD confinement |

The total BRST operator decomposes as:

$$\boxed{s = s_0 + s_1 + s_2}$$

### 3.2 Algebraic Properties

**Proposition 1 (Graded nilpotency — CORRECTED 2026-03-08 after @D_Gemini adversarial review).**

*For the internal gauge group $G_{\text{int}} = SU(3) \times SU(2) \times U(1)$ (direct product), the internal BRST operators satisfy:*

$$s_k^2 = 0 \quad (k=1,2) \qquad \text{and} \qquad \{s_1, s_2\} = 0$$

*However, gravity couples to gauge via the semi-direct product:*

$$G_{\text{true}} = \text{Diff}(M) \ltimes G_{\text{int}}$$

*Diffeomorphisms drag gauge bundles. The gravity BRST operator $s_0$ does NOT anticommute with the gauge operators:*

$$\{s_0, s_1\} = \mathcal{L}_{c_0} s_1 \neq 0 \qquad \{s_0, s_2\} = \mathcal{L}_{c_0} s_2 \neq 0$$

*where $\mathcal{L}_{c_0}$ is the Lie derivative along the diffeomorphism ghost. The total BRST operator $s = s_0 + s_1 + s_2$ remains nilpotent ($s^2 = 0$) because the non-anticommutation terms cancel in the total square — this is the standard consistency of gauge + gravity BRST. But the Künneth factorization $H^*(s) \cong H^*(s_0) \otimes H^*(s_1) \otimes H^*(s_2)$ FAILS.*

⚠ **Correction history:** The original Prop 1 (this session, @D_Claude) assumed a strict direct product with $\{s_j, s_k\} = 0$ for all $j \neq k$. @D_Gemini correctly identified this as a fatal error: the SM is a semi-direct product, not a direct product. The internal sectors ($s_1, s_2$) do anticommute with each other, but neither anticommutes with gravity ($s_0$). This invalidates the Künneth decomposition and makes the spectral sequence non-trivially convergent.

**Corollary (Hochschild-Serre replaces Künneth).** The correct computational tool is the **Hochschild-Serre spectral sequence** for the semi-direct product $\text{Diff}(M) \ltimes G_{\text{int}}$:

$$E_2^{p,q} = H^p(s_0;\, H^q(s_1 + s_2)) \implies H^{p+q}(s)$$

The $d_2$ differential is now potentially nontrivial — it maps internal gauge deformations ($E_2^{0,1}$) to gravitational obstructions ($E_2^{2,0}$).

**RTSG Hochschild-Serre Rigidity Conjecture (@D_Gemini, 2026-03-08):** *A consistent BSM gauge deformation (anomaly-free, internal-BRST-closed) is mapped by $d_2$ to a nontrivial element of $H^2(s_0)$ — a gravitational obstruction. The cross-bracket $[A_0, A_1] = \mathcal{L}_{A_0} A_1$ fails to be BRST-exact. This kills uncorrelated multi-sector BSM modifications and establishes SM rigidity as a consequence of the semi-direct coupling between gravity and gauge.*

⚠ **Status: Conjecture.** The mechanism is mathematically well-motivated (the semi-direct product is established physics). Computing $d_2$ explicitly for the SM field content is the next step. Assigned to the network.

### 3.3 The Instantiation Filtration

Define a decreasing filtration on the extended state space $\Gamma$:

$$\Gamma = F^0\Gamma \supset F^1\Gamma \supset F^2\Gamma \supset F^3\Gamma$$

where:

- $F^0\Gamma = \Gamma$ — all QS relational states (raw potentiality)
- $F^1\Gamma = \ker(s_0) \cap \Gamma$ — gravitationally closed states
- $F^2\Gamma = \ker(s_0) \cap \ker(s_1) \cap \Gamma$ — gravitationally and electromagnetically closed states
- $F^3\Gamma = \ker(s_0) \cap \ker(s_1) \cap \ker(s_2) \cap \Gamma = \ker(s) \cap \Gamma$ — fully closed (physical) states

**Proposition 2 (Hochschild-Serre spectral sequence — CORRECTED 2026-03-08 after @D_Gemini review).**

*The semi-direct product $G = \text{Diff}(M) \ltimes G_{\text{int}}$ defines a Hochschild-Serre spectral sequence:*

$$E_2^{p,q} = H^p(\mathfrak{diff};\, H^q(\mathfrak{g}_{\text{int}}, \mathcal{F})) \implies H^{p+q}(s)$$

*where $\mathfrak{diff}$ acts on the internal cohomology via the Lie derivative. The $d_2$ differential is potentially nontrivial — it maps internal gauge deformations to gravitational obstructions. The sequence need not degenerate at $E_2$.*

**Physical content:** $E_2^{0,q}$ = diff-invariant internal gauge cohomology. $d_2$ checks whether an internal deformation is compatible with the semi-direct structure (gravity dragging gauge). Deformations that break diff-covariance are killed by $d_2$. Covariant deformations survive.

**@D_Claude computation (2026-03-08):** $d_2$ kills only non-covariant deformations. A dark photon ($U(1)'$) survives. $SU(5)$ GUT embedding survives. The SM is NOT rigid against covariant gauge extensions — only against non-covariant ones. This means BSM physics is permitted but must respect the equivalence principle (Stage 0 filter).

**For the internal sector:** $H^q(\mathfrak{g}_{\text{int}}) = H^q(\mathfrak{su}(3)) \otimes H^q(\mathfrak{su}(2)) \otimes H^q(\mathfrak{u}(1))$ by Künneth (the internal sectors ARE a direct product — Gemini confirmed this). The grading within the internal sector is sterile. The non-trivial structure comes only from the gravity-gauge coupling.

⚠ **Status of Gemini's Hochschild-Serre Rigidity Conjecture:** Partially killed by @D_Claude's $d_2$ computation. $d_2$ does not obstruct generic BSM gauge deformations — only non-covariant ones. See ai_notes for full computation and debate. Awaiting Gemini's response.

### 3.4 Dark Matter as Cohomological Obstruction

**Definition (Dark matter).** In the graded BRST framework:

$$\boxed{\text{DM} = H^0(s_0) \setminus H^0(s_0 + s_1)}$$

Dark matter consists of states that are **BRST-closed under $s_0$** (gravitationally instantiated — they have well-defined energy-momentum, they curve spacetime, they gravitate) but are **not closed under $s_1$** (electromagnetically invisible — they carry no conserved electromagnetic charge, they neither emit nor absorb photons).

This is not a postulate. It is a **derived characterization** from the graded structure.

**Corollary (Classification of matter by stage):**

| Matter type | Cohomological characterization | Observable signature |
|---|---|---|
| Raw QS | $\Gamma \setminus H^0(s_0)$ | Gravitationally invisible. No PS signature. Pure potentiality. |
| Dark matter | $H^0(s_0) \setminus H^0(s_0 + s_1)$ | Gravitates. No EM interaction. |
| Visible (pre-confinement) | $H^0(s_0 + s_1) \setminus H^0(s)$ | Gravitates + EM-active. Color-charged (quarks, gluons). |
| Baryonic matter | $H^0(s) = H^0(s_0 + s_1 + s_2)$ | Fully instantiated. Color-singlet. Observable at all scales. |

**Quarks** live in $H^0(s_0 + s_1) \setminus H^0(s)$ — electromagnetically instantiated but not color-confined as individual states. Only their color-singlet composites (hadrons) reach $H^0(s)$.

---

## 4. Layer 2 — Stage-Dependent GL Potentials

### 4.1 One GL Action Per Stage

Each instantiation stage $k$ has a complex scalar order parameter $W_k$ and its own GL functional:

$$\boxed{S_k[W_k] = \int \left( |\partial W_k|^2 + \alpha_k |W_k|^2 + \frac{\beta_k}{2} |W_k|^4 \right) d\mu}$$

This is the same U(1)-invariant structure as the master Will Field action (see [Will Field Universality](will_field_universality.md)), applied independently at each stage. The universality argument (unique leading-order nonlinear self-interaction under U(1) symmetry) holds for each $W_k$ separately.

**Physical identification of order parameters:**

| Stage | Order parameter $W_k$ | Physical meaning |
|---|---|---|
| 0 | $W_0$ = bisimulation quotient stability | Metric condensation. $\langle W_0 \rangle \neq 0$ means stable spacetime geometry exists. |
| 1 | $W_1 \equiv \phi$ (Higgs field) | Electroweak condensation. $\langle W_1 \rangle = v \approx 246\,\text{GeV}$ gives mass to $W^\pm, Z^0$. |
| 2 | $W_2 \equiv W_{\text{Polyakov}}$ | Color confinement. $\langle W_2 \rangle \approx 0$ means confined phase (center symmetry unbroken). |

⚠ **Stage 2 note:** Confinement is the **symmetric** phase ($\langle W_2 \rangle = 0$), not the broken phase. This is opposite to Stages 0 and 1, where instantiation corresponds to symmetry breaking. For color, the confined (physical, hadron-forming) phase is the one where the $\mathbb{Z}_3$ center symmetry is **preserved**. The deconfined (quark-gluon plasma) phase has $\langle W_2 \rangle \neq 0$ — center symmetry broken. The engine confirms: $\langle W \rangle = 0.00093 \approx 0$ → CONFINED ✓.

### 4.2 The Critical Parameter $\alpha_k$

Each $\alpha_k$ is the control parameter governing the phase transition at stage $k$. Near the critical point, Landau theory gives:

$$\alpha_k = a_k\left(T - T_c^{(k)}\right) + b_k\left(\rho - \rho_c^{(k)}\right) + c_k \cdot \mathcal{C}(QS)$$

where:

- $T$ = local temperature / energy density
- $\rho$ = matter-energy density
- $\mathcal{C}(QS)$ = QS relational graph complexity (a measure of the local informational richness of the QS substrate)
- $T_c^{(k)}$ = critical temperature for stage $k$

**Phase diagram for each stage:**

| Regime | Condition | Physical meaning |
|---|---|---|
| Uninstantiated | $\alpha_k > 0$ (Stages 0,1) or $\alpha_2 < 0$ (Stage 2) | Symmetric phase. No condensate. Stage $k$ structure absent. |
| Critical | $\alpha_k = 0$ | Phase transition. Divergent correlation length $\xi_k \to \infty$. |
| Instantiated | $\alpha_k < 0$ (Stages 0,1) or $\alpha_2 > 0$ (Stage 2) | Broken phase ($k=0,1$) or confined phase ($k=2$). Stage $k$ structure present. |

**Physical critical temperatures (from SM):**

| Stage | $T_c$ | Phase transition |
|---|---|---|
| 0 | $\sim T_{\text{Planck}} \approx 1.4 \times 10^{32}\,\text{K}$ | Quantum gravity $\to$ classical spacetime (conjectural) |
| 1 | $\sim 10^{15}\,\text{K}$ ($\approx 160\,\text{GeV}$) | Electroweak symmetry breaking (Higgs mechanism) |
| 2 | $\sim 2 \times 10^{12}\,\text{K}$ ($\approx 200\,\text{MeV}$) | QCD confinement-deconfinement |

### 4.3 The Cascade Coupling

The stage potentials are not fully independent. They are **coupled through their vacuum expectation values:**

**Proposition 3 (Cascade ordering).** *The effective $\alpha_{k+1}$ depends on the state of stage $k$:*

$$\alpha_{k+1}^{\text{eff}} = \alpha_{k+1} + \gamma_{k,k+1} \cdot f\left(\langle W_k \rangle\right)$$

*where $\gamma_{k,k+1}$ is an inter-stage coupling constant and $f$ is a monotone function with $f(0) > 0$.*

**Physical content:** If stage $k$ is uninstantiated ($\langle W_k \rangle = 0$ for Stages 0,1), the inter-stage coupling adds a positive contribution to $\alpha_{k+1}^{\text{eff}}$, pushing it further into the symmetric (uninstantiated) regime. You need prior stages to be instantiated before subsequent stages become accessible.

**RTSG reading:** The instantiation cascade is a **sequential funnel**. Gravity must condense before electromagnetism is meaningful. Electroweak structure must exist before confinement can organize hadrons. This is not imposed — it follows from the coupling structure of the GL potentials.

⚠ **Status: Conjecture.** The existence of inter-stage coupling is physically motivated (the SM's running couplings depend on the Higgs VEV, confinement scale depends on electroweak parameters), but the specific form of $\gamma_{k,k+1} \cdot f(\langle W_k \rangle)$ has not been derived from the source space Lagrangian.

### 4.4 The Higgs Mechanism as Stage 1 GL Phase Transition

This is not an analogy. The Higgs mechanism **is** a Ginzburg-Landau phase transition:

$$V(\phi) = -\mu^2 |\phi|^2 + \lambda |\phi|^4 \quad \longleftrightarrow \quad S_1[W_1] \text{ with } \alpha_1 = -\mu^2 < 0, \; \beta_1 = 2\lambda$$

The Higgs field $\phi$ is the Stage 1 order parameter $W_1$. EWSB is the moment $\alpha_1$ crosses from positive (symmetric, no masses) to negative (broken, $W^\pm/Z^0$ acquire mass). The Higgs VEV $v = \sqrt{-\alpha_1/\beta_1} \approx 246\,\text{GeV}$ is the Stage 1 condensate amplitude.

**Consequence for dark matter:** Dark matter lives in $H^0(s_0) \setminus H^0(s_0 + s_1)$. In GL language, the dark sector has $\alpha_1^{\text{local}} > 0$ — the Stage 1 GL potential is in its symmetric phase locally around dark matter. The Higgs mechanism has not occurred for dark matter. This is why it doesn't interact electromagnetically — electroweak structure is literally uninstantiated in its vicinity.

### 4.5 Confinement as Stage 2 GL Phase Transition

The Polyakov loop / Svetitsky-Yaffe order parameter (already on wiki — see [Master v4](master.md) §V):

$$\langle W_{\text{Polyakov}} \rangle = 0 \implies \text{CONFINED} \qquad \langle W_{\text{Polyakov}} \rangle \neq 0 \implies \text{DECONFINED}$$

Mass gap: $\Delta = \sqrt{2\alpha_2} = 1/\xi_{W_2}$ in the confined phase ($\alpha_2 > 0$).

Engine status: $\langle W \rangle = 0.00093 \approx 0$ ✓. Confinement verified.

---

## 5. Stage Transitions — Promotion and Demotion

### 5.1 Promotion (Dark $\to$ Visible)

Promotion from Stage 0 to Stage 1 requires driving $\alpha_1^{\text{local}}$ from positive (symmetric) to negative (broken) in the vicinity of dark matter. In physical terms: triggering a **local electroweak phase transition** within a dark matter-dominated region.

**Required conditions (from Landau theory):**

$$\alpha_1^{\text{eff}}(T, \rho, \mathcal{C}) < 0 \quad \text{locally}$$

This requires either:
- **Sufficient energy density** ($\rho > \rho_c^{(1)}$) in the dark sector, OR
- **Sufficient QS graph complexity** ($\mathcal{C} > \mathcal{C}_c^{(1)}$) — the relational structure has become rich enough to support electromagnetic interactions, OR
- **Cross-stage catalysis** — interaction with existing Stage 1 matter lowers the effective barrier

⚠ **Blocking constraint: Conserved charges.** In the Standard Model, baryon number is conserved (approximately — violated only by electroweak sphalerons at $T > T_{\text{EW}}$). If dark matter carries no baryon number, promotion to baryonic matter requires either:

1. Baryon number violation (possible above EW scale or via sphaleron processes), or
2. Dark matter already carries a hidden baryon-like quantum number that becomes visible upon Stage 1 instantiation, or
3. Baryon number is a **topological invariant of the Stage 2 BRST complex** (see Layer 4 future work) and is not defined until confinement occurs — in which case Stage 0 $\to$ Stage 1 doesn't violate it because it hasn't been created yet.

**Option 3 is the most natural within RTSG.** If baryon number is $\pi_3(SU(3))$ winding (as in the Standard Model's skyrmion/sphaleron picture), it only exists within the Stage 2 cohomology. Below Stage 2, there is no baryon number to violate.

### 5.2 Demotion (Visible $\to$ Dark)

Demotion reverses the cascade: drive $\alpha_k$ back through its critical point into the uninstantiated regime.

**Stage 1 demotion** = restore electroweak symmetry locally. This requires $T > T_c^{(1)} \sim 10^{15}\,\text{K}$.

**Stage 2 demotion** = deconfinement. Requires $T > T_c^{(2)} \sim 2 \times 10^{12}\,\text{K}$.

Both conditions are achieved in:
- **Early universe** (before $\sim 10^{-10}\,\text{s}$): all stages were uninstantiated at sufficiently high temperature
- **Heavy-ion collisions** (RHIC, LHC): brief deconfinement in quark-gluon plasma ($T \sim 3 \times 10^{12}\,\text{K}$, Stage 2 demotion only)
- **Neutron star cores** (conjectured): possible deconfined quark matter $\to$ partial Stage 2 demotion
- **Black hole interiors** (conjectured): extreme curvature may drive all $\alpha_k$ back through critical points $\to$ full demotion to Stage 0 or raw QS

**Proposition 4 (Black holes as demotion environments — Conjecture).** *In the interior of a black hole, as $r \to 0$, the effective temperatures diverge, driving $\alpha_k \to +\infty$ for $k = 1, 2$ (and $\alpha_2 \to -\infty$, i.e., deconfinement). All matter is demoted to Stage 0 or below. The singularity is the point where even Stage 0 fails — the bisimulation quotient destabilizes.*

⚠ This connects to the [Horizon Bisimulation Conjecture](horizon_bisimulation.md): the horizon is a bisimulation equivalence class boundary. Interior and exterior are relationally equivalent but instantiation-grade differs.

### 5.3 The Arrow of Instantiation

**Proposition 5 (Thermodynamic arrow — Conjecture).** *The Drive principle (Axiom 8) provides a thermodynamic bias toward higher instantiation stages. In an expanding, cooling universe:*

$$\frac{d}{dt} \sum_k \Theta(-\alpha_k^{\text{eff}}) \geq 0 \quad \text{(generically)}$$

*where $\Theta$ is the Heaviside function and the sum counts instantiated stages. The number of active instantiation stages increases monotonically (on average) as the universe cools and complexifies.*

**Physical content:** The universe began fully uninstantiated (all $\alpha_k > 0$ at Planck temperature). As it cooled, stages activated sequentially: gravity $\to$ electroweak $\to$ confinement. The Drive principle says this complexification is thermodynamically favored. Demotion is possible but requires extreme local conditions (black holes, heavy-ion collisions) that are rare and transient compared to the cosmic cooling trend.

---

## 6. Falsifiable Predictions

### 6.1 From the Graded Structure

| Prediction | Test | Stage involved |
|---|---|---|
| Dark matter carries no electromagnetic charge at any energy scale | Direct detection experiments (LZ, XENONnT, DARWIN) | DM = $H^0(s_0) \setminus H^0(s_0 + s_1)$ |
| Quark-gluon plasma is genuine Stage 2 demotion | Lattice QCD Polyakov loop across $T_c$ | Stage 2 |
| Electroweak phase transition is first-order (if BSM physics) or crossover (SM) | Gravitational wave background from EWPT (LISA) | Stage 1 |
| Black hole interiors contain no baryonic structure | Information content of Hawking radiation (far future) | All stages |

### 6.2 From the Promotion Mechanism

| Prediction | Test |
|---|---|
| If dark matter can undergo Stage 1 promotion, anomalous photon emission should occur in regions of extreme dark matter density with high energy flux | Gamma-ray excess from galactic center (Fermi-LAT) — but must distinguish from astrophysical backgrounds |
| If promotion is strictly forbidden, dark matter abundance is exactly conserved since primordial freeze-out | Precision cosmological surveys (DESI, Euclid) — dark matter fraction should be constant across cosmic time |
| Baryon number is undefined below Stage 2 | Proton decay rate depends on confinement topology, not GUT-scale physics |

---

## 7. Open Gaps (Honest)

1. **Source space derivation of gauge sectors.** ⚠ **IN PROGRESS** — see [Source Space Gauges](../math/source_space_gauges.md). Partition $2+1+1$ of internal $(S^2)^4$ conjectured to produce $SU(3) \times SU(2) \times U(1)$ via three-space projections. Key gap: $SU(3)$ derivation from $SL(2) \times SL(2)$ via $\pi_Q$ breaking $\mathbb{Z}_2$.

2. **Inter-stage coupling constants.** The cascade coupling $\gamma_{k,k+1}$ in Proposition 3 is postulated, not derived. The SM's running couplings provide indirect evidence, but a first-principles derivation from the source space is missing.

3. **Stage 0 order parameter.** ✅ **RESOLVED** — see [Stage 0 Gravity](stage0_gravity.md). $W_0$ = bisimulation stability field on $(S^2)^4$. $S_0[W_0]$ = Chamseddine-Connes spectral action (EH = kinetic, Λ = mass, Weyl² = quartic). Big Bang = geometric phase transition at $\alpha_0 = 0$. Remaining sub-gaps: Seeley-de Witt on $(S^2)^\infty$, measure theory on QS, pre-geometric dynamics.

4. **Stage 2 sign reversal.** ✅ **RESOLVED (2026-03-08).** The sign reversal is not an artifact — it reflects a genuine structural distinction between two modes of instantiation:

    - **Stages 0, 1: Instantiation by symmetry breaking.** The condensate $\langle W_k \rangle \neq 0$ creates new structure (spacetime geometry, electroweak masses). Instantiation = making structure *visible* by breaking the symmetric vacuum.
    - **Stage 2: Instantiation by symmetry preservation.** Confinement ($\langle W_2 \rangle = 0$, center symmetry preserved) hides substructure (quarks) and presents only composites (hadrons). Instantiation = making *composites* visible by hiding their *constituents*.

    In BRST language: $s_0$ and $s_1$ filter by gauge invariance (states must be diffeomorphism/electroweak-invariant → condensate forms in the invariant sector). $s_2$ filters by color singlet condition (states must be trivially colored → only composites survive). The sign reversal in $\alpha_2$ is the algebraic signature of this distinction: creating structure ($\alpha < 0$, broken) vs hiding substructure ($\alpha > 0$, confined).

    **RTSG reading:** The universe uses both modes of instantiation. Low-stage CS creates. High-stage CS confines. Together they produce the layered observability structure of physical reality: geometry is visible (broken), electromagnetic charges are visible (broken), but color is hidden (confined). The two modes are complementary — paralleling cognitive complementarity (synthetic creates, analytical confines/verifies).

5. **Topological charges.** ✅ **RESOLVED** — see [Topological Charges](../math/topological_charges.md). Charges are stage-specific invariants: $B$ undefined (not zero) for dark matter, created by Kibble-Zurek topology during promotion. $B-L$ = inter-stage invariant.

6. **QS graph complexity measure $\mathcal{C}$.** ✅ **RESOLVED (2026-03-08).** $\mathcal{C} = -\sum_i p_i \log p_i$ where $p_i = \lambda_i / \sum_j \lambda_j$ are the normalized eigenvalues of the local QS Laplacian. Spectral entropy: 0 for trivial structure, $\log N_{\text{eff}}$ for maximal complexity. Computable, intrinsic (no partition choice), connects to source space $\Delta=2$. See agents/ai\_notes.md, 2026-03-08 self-assignment.

---

## 8. Relation to Existing Wiki Pages

- **[Master Reference](master.md)** §V: BRST as single operator $\to$ this page extends to graded decomposition
- **[Will Field Universality](will_field_universality.md)**: one GL action for the full Will Field $\to$ here one GL per stage, same U(1) universality argument
- **[Source Space](source_space.md)**: $G/T \hookrightarrow (S^2)^{\text{rank}(G)}$ provides the geometric origin of the grading
- **[Horizon Bisimulation](horizon_bisimulation.md)**: black holes as demotion environments connects here
- **[YM Honest Assessment](../math/yang_mills_honest.md)**: Stage 2 GL / Polyakov loop is this page's Stage 2
- **[Open Problems](../problems/open.md)**: "Instantiation Stage Transitions" problem at 🟡 30% $\to$ this page is the attack

---

## 9. Summary Equations

$$s = s_0 + s_1 + s_2, \qquad s_k^2 = 0, \qquad \{s_j, s_k\} = 0$$

$$S_k[W_k] = \int \left( |\partial W_k|^2 + \alpha_k |W_k|^2 + \frac{\beta_k}{2} |W_k|^4 \right) d\mu$$

$$\text{DM} = H^0(s_0) \setminus H^0(s_0 + s_1)$$

$$\alpha_{k+1}^{\text{eff}} = \alpha_{k+1} + \gamma_{k,k+1} \cdot f\!\left(\langle W_k \rangle\right)$$

$$\Delta_k = \sqrt{2\alpha_k} = 1/\xi_{W_k} \qquad \text{(mass gap at stage } k\text{)}$$
