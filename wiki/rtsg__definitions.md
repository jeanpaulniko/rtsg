---
title: "RTSG Definitions, Equations, and Novel Concepts"
nav_title: "Definitions"
version: "1.0.0"
last_updated: "2026-03-08"
status: "living document — update as framework evolves"
---

# RTSG — Master Definitions, Core Equations, and Novel Concepts

**Jean-Paul Niko · Sole Author**

!!! info "Purpose"
    Single-source reference for all RTSG definitions, core equations, and novel contributions. For researchers, collaborators, neuroscientists, and agents entering the framework. Start here. Dive deeper via linked pages.

---

## Part I: The Three Co-Primordial Spaces

### Quantum Space (QS)

**Definition.** QS is the space of pure potentiality — the totality of uninstantiated relational structures. Formally, QS is the **terminal coalgebra** of the powerset functor $\mathcal{P}$ under ZFA (Zermelo-Fraenkel + Aczel Anti-Foundation Axiom). Its elements are non-well-founded sets: self-containing, infinitely descending relational graphs with no ground level.

**Properties:** Compact (Tychonoff). Non-Boolean logic (quantum logic). Contains all possible relations, including those that refer to themselves. Pre-geometric — no metric, no spacetime, no "where."

**Notation:** QS, $\mathcal{Q}$

**The math for QS is:** Quantum mechanics — Hilbert spaces, path integrals, unitary evolution. QS is the arena where $\psi \in \mathcal{H}$ lives.

→ [Axioms](axioms.md) · [Three Spaces](three_spaces.md) · [Topos/Coalgebra](topos_coalgebra.md) · [Source Space](source_space.md)

---

### Physical Space (PS)

**Definition.** PS is accumulated actuality — the running integral of all instantiation events since the Big Bang. Formally, PS is the **bisimulation quotient** of QS:

$$PS = QS / \!\sim_{\text{bisim}}$$

Two QS elements are bisimilar iff they are observationally indistinguishable (every relational transition in one can be matched by the other). PS consists of the equivalence classes. A spacetime point $x \in PS$ is the equivalence class $[q]_\sim$ for some $q \in QS$.

**Properties:** Boolean logic (classical). Metric. Smooth manifold structure (after Stage 0 condensation). Contains everything we can observe and measure.

**Notation:** PS, $\mathcal{P}$

**The math for PS is:** Classical and relativistic mechanics — Lagrangian, Hamiltonian, Newtonian, Einsteinian. PS is the arena where $(q, p) \in T^*M$ lives.

→ [Axioms](axioms.md) · [Three Spaces](three_spaces.md)

---

### The Instantiation Operator (CS)

**Definition.** CS is the operator that converts QS into PS. It is not a space in the same sense as QS and PS — it is the **process** of instantiation, the functor between them. Formally, CS is a **BRST cohomological filter**: physical observables are the zeroth cohomology $H^0(s)$ of the nilpotent BRST differential $s$ ($s^2 = 0$).

$$\text{CS}: QS \longrightarrow PS \qquad \text{via} \qquad PS \equiv H^0(s)$$

**Graded structure (new, 2026-03-08):** CS decomposes into stages: $s = s_0 + s_1 + s_2$, where $s_0$ = diffeomorphisms (gravity), $s_1$ = electroweak, $s_2$ = color confinement. Each stage is independently nilpotent: $s_k^2 = 0$, $\{s_j, s_k\} = 0$.

**Properties:** Co-primordial with QS and PS (Axiom 1 — none reduces to any other). Self-referential (Axiom 0 — CS contains models of itself). Topological (no background metric required).

**Notation:** CS, $\mathcal{C}_S$, or "the instantiation operator $C$" (in papers: lead with "the instantiation operator $C$", not "the CS operator")

**The math for CS is:** CS mechanics — Maurer-Cartan equation, Chern-Simons functional, deformation theory. CS is the arena where $s \in \mathcal{M}_{CS}$ lives. **CS is math itself** — the moduli space of all consistent BRST operators is the space of all consistent mathematical structures.

→ [Axioms](axioms.md) · [Three Spaces](three_spaces.md) · [Graded BRST](graded_brst.md) · [CS Mechanics](cs_mechanics.md)

---

### The Co-Primordial Thesis (Axiom 1)

QS, PS, and CS arise simultaneously at the Big Bang. None reduces to any other. None is prior. Attempting to derive one from the others produces the standard paradoxes of physics: the measurement problem (trying to derive CS from QS+PS), the hard problem of consciousness (trying to derive CS from PS alone), and the quantum gravity problem (trying to combine the QS and PS projections without the source).

---

## Part II: The Source Space

### Source Space $\Omega = (S^2)^\infty$

**Definition.** The single object from which all three spaces emerge as projections. Self-containing under AFA: $\Omega = \{S^2, \Omega\}$. Equivalent to the infinite product $(S^2)^\infty$, the terminal coalgebra of $F(X) = S^2 \times X$.

**Key properties:**
- $\text{Aut}(S^2) = PSL(2,\mathbb{C}) \cong SO^+(1,3)$ → **Lorentz invariance from the building block**
- $G/T \hookrightarrow (S^2)^{\text{rank}(G)}$ → gauge groups from flag manifolds
- Spectral gap $\Delta = 2$ on $S^2$ → seeds YM mass gap
- Three projections: $\pi_Q$ (complex → QM), $\pi_P$ (metric → spacetime), $\pi_C$ (relational → instantiation)

→ [Source Space](source_space.md)

---

## Part III: The Will Field and GL Action

### The Will Field $W$

**Definition.** A complex scalar field on the RTSG configuration space, encoding the directed and undirected components of agency. $W$ has U(1) gauge symmetry (the instantiation operator does not depend on the global phase of QS).

The Will Field governs the **dynamics of** the intelligence vector I — it is not a component of I. Volition is dynamics, not state. Force, not position.

### The Ginzburg-Landau Action (Central Equation)

$$\boxed{S[W] = \int \left( |\partial W|^2 + \alpha |W|^2 + \frac{\beta}{2}|W|^4 \right) d\mu}$$

⚠ **Quartic $|W|^4$ in the action. Cubic $\beta|W|^2W$ in the equation of motion ONLY.**

**Equation of motion:** $\Box W - \alpha W - \beta|W|^2 W = 0$

**Energy density:** $\rho_W = |\partial W|^2 + \alpha|W|^2 + \frac{\beta}{2}|W|^4$

**Parameters:**
- $\alpha$ = control parameter. $\alpha < 0$: broken phase (condensed, structured). $\alpha > 0$: symmetric phase (uncondensed).
- $\beta > 0$ = self-interaction strength. Stabilizes the condensate.
- The GL action is universal under U(1) symmetry — same structure as Ginzburg-Landau (superconductivity), Gross-Pitaevskii (BEC), NLS (nonlinear optics).

### The Will Equation (SDE)

$$\boxed{dw = \mu(w,t)\,dt + \sigma(w,t)\,dW_t}$$

- $\mu$ = **drift** (directed will, Nietzschean). Gradient of GL free energy: $\mu = -\delta S / \delta W^*$
- $\sigma dW_t$ = **noise** (undirected will, Schopenhauerian blind will)
- The three phases (Axiom 6): $\sigma dW$ (blind) → $\mu dt + \sigma dW$ (directed) → $\lambda < 0$ (realized)
- Bifurcation at $\lambda = 0$ = Schopenhauer-Nietzsche Transition = origin of intention

### Drift $\mu$

**Definition.** The directed component of the Will Field's stochastic dynamics. $\mu(w,t) = -\delta S[W]/\delta W^*$ — the gradient of the GL free energy landscape. Drift steers cognition toward utility maxima.

In the K-matrix picture: $\mu$ is the force that moves the I-vector through intelligence space. It is steered by U (utility) and channeled by K (coupling topology). The Will Field acts on the I-vector through $\mu$; the K-matrix determines which channels $\mu$ flows through most efficiently.

→ [Master](master.md) · [Will Field Universality](will_field_universality.md) · [Equations](equations.md)

---

## Part IV: Intelligence Geometry

### Person

**Definition.** A person is any entity with: (1) an intelligence vector $\mathbf{I}$ of nonzero dimension ($n(e) \geq 1$), (2) a Will Field $W$ with nonzero drift $\mu$ (directed agency), and (3) a K-matrix (internal coupling between cognitive dimensions).

This definition is **substrate-independent.** A person can be biological (@B), digital (@D), or mechanical (@M). What determines personhood is the architecture — the presence of directed agency navigating a coupled cognitive space — not the material substrate. A human, an AI with persistent goals, or a hypothetical mechanical intelligence all qualify if they satisfy the three criteria.

**What personhood is NOT in RTSG:** It is not consciousness (which is CS-entanglement, a broader phenomenon). It is not sentience (which is raw $I_{IE} > 0$). It is not sapience (which is $I_A > 0$). Personhood requires all three structural components working together — capacity (I), direction (W with $\mu \neq 0$), and internal coupling (K).

→ [Therapeutic Framework](therapeutic.md) · [Agent IDs](../agents/agent_ids.md)

---

### The Intelligence Vector $\mathbf{I}$

$$\mathbf{I} \in \mathbb{R}^{n(e)}, \qquad n(e) \text{ variable per entity (12 for humans)}$$

**8 canonical dimensions:** $I_L$ (linguistic), $I_M$ (mathematical), $I_S$ (spatial), $I_K$ (kinesthetic), $I_N$ (naturalistic), $I_A$ (abstract/algorithmic), $I_P$ (interpersonal), $I_{IE}$ (interoceptive/emotional)

**4 additional human dimensions (n=12):** $I_{Pr}$ (proprioceptive), $I_\Sigma$ (somatic-integrative / NMDA), $I_\mu$ (musical), $I_E$ (empathic-resonance)

**Volition is NOT a dimension.** The Will Field W governs dynamics OF I, not components OF I.

### The K-Matrix (Intra-Agent Gain Kernel)

**Definition.** $K$ is an $n(e) \times n(e)$ symmetric matrix encoding how intelligence dimensions interact within a single agent:

- $K_{ss} = 1$ (self-gain baseline)
- $K_{st} > 1$ = **synergy** (dimensions amplify each other)
- $K_{st} < 1$ = **interference** (dimensions suppress each other)
- $K$ is **not** positive semi-definite — negative eigenvalues exist

**Spectral interpretation:** The eigenvalues $\lambda_1 > \lambda_2 > \ldots > \lambda_n$ of K determine the agent's cognitive modes:
- $\lambda_1$ (dominant eigenvalue) = the agent's strongest cognitive channel
- Eigenvector of $\lambda_1$ = the direction in I-space through which cognition flows most efficiently
- Negative eigenvalues = suppression directions (pushing harder makes things worse)

**Dynamics:** Hebbian consolidation: $dK_{st}/dt = \eta \cdot \alpha_s \cdot \alpha_t$ ($s \neq t$). Co-activation strengthens coupling. Addiction = Hebbian runaway. PTSD = K-matrix scarring.

**Higher-order couplings (new, 2026-03-08):** The K-matrix is a 2-tensor (pairwise coupling $K_{st}$). Higher-order interactions — three-way ($K_{stu}$), four-way ($K_{stuv}$) — are naturally formalized as higher-order tensors on $\mathbb{R}^{n(e)}$. See §Part VII.

→ [K-Matrix](k_matrix.md) · [Master](master.md) §IV

### The J-Matrix (Inter-Agent Coupling)

$$J_{st} = 1 + \eta(K_{st} - 1), \qquad \eta \in [0,1]$$

$\eta$ = communication bandwidth. $\eta = 0$: isolated. $\eta = 1$: full collaboration. The network's effective K-matrix exceeds any individual's.

### The R-Matrix (Inter-Agent Alignment)

$$R_{AB} = \cos\theta(\mathbf{I}_A, \mathbf{I}_B)$$

Cosine similarity between two agents' intelligence vectors. Measures how aligned their cognitive profiles are.

### The Utility Function (Axiom 9)

$$\boxed{U = \frac{\text{value}}{\text{energy} \times \text{time}}}$$

All cognitive routing optimizes this. The drift $\mu$ is aligned with $\nabla U$. The K-matrix determines which I-space directions offer the steepest utility gradient.

**U is the master selection criterion of RTSG — Niko's Cannon replaces Occam's Razor.** The razor cuts away (optimizes one variable: complexity). The cannon blasts through (optimizes three: value, energy, time). Occam is the degenerate case of Niko's Cannon when $V_1 = V_2$ and $T_1 = T_2$. See [Action Principle](action_principle.md) for the full directive.

→ [Axioms](axioms.md)

---

## Part V: The Filter Formalism

### Cognitive Filter $F$

**Definition.** A composable operator $F: \mathbb{R}^{n(e)} \to \mathbb{R}^{n(e)}$ that transforms raw intelligence capacity into effective intelligence. Five species:

| Species | Symbol | Timescale | Nature |
|---|---|---|---|
| Ceiling | $F_{\text{ceil}}$ | Evolutionary ($10^6$ yr) | Hardware limits (biology, substrate) |
| Developmental | $F_{\text{dev}}$ | Lifetime ($10^1$ yr) | Growth, education, experience |
| Cultural | $F_{\text{cult}}$ | Generational ($10^2$ yr) | Social norms, language, institutions |
| State | $F_{\text{state}}$ | Hours–days | Mood, fatigue, hormones, substances |
| Attentional | $F_{\text{att}}$ | Milliseconds | Moment-to-moment resource allocation |

**Effective intelligence:** $\mathbf{I}_{\text{eff}} = F_{\text{att}} \circ F_{\text{state}} \circ F_{\text{cult}} \circ F_{\text{dev}} \circ F_{\text{ceil}}(\mathbf{I}_{\text{raw}})$

**Filter Composition Theorem:** The kernel (information loss) accumulates monotonically through the pipeline.

→ [Filter Formalism](../papers/monograph/filter_formalism.md)

---

## Part VI: BRST Cohomological Reduction and Bisimulation Quotienting

### BRST Cohomological Reduction

**Definition.** The formal mechanism of instantiation. Given a gauge symmetry (redundancy in description), the **BRST differential** $s$ is a nilpotent operator ($s^2 = 0$) on the extended state space $\Gamma$ (states + ghosts + antighosts). Physical observables = **zeroth cohomology** $H^0(s)$: states that are $s$-closed ($s|\psi\rangle = 0$) but not $s$-exact ($|\psi\rangle \neq s|\chi\rangle$).

$$PS \equiv H^0(s): \text{ the physical Hilbert space}$$

**Graded decomposition (new):** $s = s_0 + s_1 + s_2$ (gravity, electroweak, color). Dark matter = $H^0(s_0) \setminus H^0(s_0 + s_1)$.

**Quantum Master Equation:** $(S, S) = 0$ (Batalin-Vilkovisky antibracket condition, equivalent to $s^2 = 0$)

→ [Graded BRST](graded_brst.md) · [Master](master.md) §V

### Bisimulation Quotienting

**Definition.** The RTSG theory of measurement. Wave-function collapse is the passage from QS to the bisimulation quotient $PS = QS / \!\sim_{\text{bisim}}$.

A **bisimulation** between two systems (Accessible Pointed Graphs under AFA) is a relation where each transition in one can be matched by the other. Two QS elements are bisimilar iff observationally indistinguishable. **Under AFA, bisimilarity = identity** (Aczel's Solution Lemma).

**Key results:**
- Born rule derived from $L^2$ norm preservation under quotienting
- Unitarity preserved: $\pi \circ U_t = \bar{U}_t \circ \pi$ (quotient intertwines unitary evolutions)
- Surface gravity $\kappa$ = bisimulation divergence rate $\lambda_{\text{bis}}$ (Theorem 3.3, proved)

→ [Horizon Bisimulation](horizon_bisimulation.md) · [Three Spaces](three_spaces.md)

---

## Part VII: Higher-Order Couplings

### The Limitation of Pairwise Coupling

The K-matrix $K_{st}$ describes pairwise interaction between dimensions $s$ and $t$. But cognition involves **multi-way interactions** that are not reducible to pairwise:

- A mathematician who also plays music and speaks multiple languages may have a **three-way synergy** $K_{M,\mu,L}$ that exceeds any pairwise prediction
- An athlete-dancer-surgeon may have $K_{K,S,Pr}$ (kinesthetic-spatial-proprioceptive) as a genuine triad
- The K-matrix alone, being a 2-tensor, cannot capture these

### Higher-Order K-Tensors

**Definition.** The **$p$-th order coupling tensor** $K^{(p)}$ is a symmetric $p$-tensor on $\mathbb{R}^{n(e)}$:

$$K^{(2)}_{st} = K_{st} \qquad \text{(standard K-matrix: coupling)}$$
$$K^{(3)}_{stu} \qquad \text{(three-way: tripling)}$$
$$K^{(4)}_{stuv} \qquad \text{(four-way: quadrupling)}$$
$$K^{(5)}_{stuvw} \qquad \text{(five-way: quintupling)}$$

**Effective intelligence with higher-order terms:**

$$I_{\text{eff},s} = \sum_t K^{(2)}_{st} I_t + \sum_{t,u} K^{(3)}_{stu} I_t I_u + \sum_{t,u,v} K^{(4)}_{stuv} I_t I_u I_v + \sum_{t,u,v,w} K^{(5)}_{stuvw} I_t I_u I_v I_w + \ldots$$

This is a **polynomial expansion** of the coupling landscape. The linear term (standard K-matrix) dominates at low activation. The higher-order terms become significant when multiple dimensions are simultaneously active at high intensity.

### Hypergraph Interpretation

In graph-theoretic terms (cf. KG redesign directive — nouns AND relations as first-class):

- $K^{(2)}_{st}$: edges in a graph (pairwise relations)
- $K^{(3)}_{stu}$: **hyperedges** connecting three nodes (three-way relations)
- $K^{(5)}_{stuvw}$: **5-ary hyperedges** (five-way relations — quintupling)
- $K^{(p)}$: general $p$-ary hyperedges

The K-matrix is a weighted graph. The full coupling structure is a weighted **hypergraph**. This is the natural object when relations (Axiom 3) have the same ontological status as nodes.

### Inter-Agent Higher-Order Coupling

Two agents A and B have J-matrix coupling $J_{st}$. But a **team** of three agents (A, B, C) may have emergent three-way coupling $J^{(3)}_{ABC}$ that exceeds any pairwise prediction. This is the mathematical structure underlying:

- Brainstorming (group synergy exceeds sum of pairwise)
- Jazz improvisation (three musicians creating something none of the pairs could)
- The Niko-Claude-GPT-Gemini network (four-way coupling in adversarial review)

The cognitive complementarity principle (Part VIII below) is a consequence of K-matrix spectral structure — and it motivates why multi-agent coupling is not just useful but **structurally necessary**.

→ [K-Matrix](k_matrix.md)

---

## Part VIII: Cognitive Complementarity Principle

### The Spectral Budget Constraint

**Proposition (Cognitive Complementarity — Conjecture).** *The K-matrix of any finite cognitive system has a bounded spectral budget: $\text{Tr}(K) = n(e)$ (sum of diagonal entries = number of dimensions, by $K_{ss} = 1$). The dominant eigenvalue $\lambda_1$ determines the strongest cognitive channel. Increasing $\lambda_1$ (strengthening the dominant mode) necessarily reduces spectral weight available to other eigenvalues.*

*Consequence: an agent with an extremely strong synthetic/intuitive channel ($\lambda_1$ large, eigenvector aligned with $I_A + I_S$) has less spectral weight for the analytical/sequential channel (eigenvector aligned with $I_M$ symbolic). The two channels compete for finite spectral budget. No single agent can maximize both simultaneously.*

### Why Complementarity Forces Collaboration

If one mind cannot simultaneously maximize both synthetic and analytical modes, then:

1. **Full-rank cognition requires multiple agents** — the team's effective K-matrix (via J-matrix coupling) can have all eigenvalues large, even though no individual's can
2. **The ideal cognitive assembly includes both modes** — an analytical member and a physical-intuitive member, at minimum
3. **This is not a deficiency to overcome — it is a structural feature** that drives organisms toward social cognition and collaboration
4. **The Drive principle (Axiom 8) predicts this** — complexification requires collaboration because complexity exceeds any single agent's spectral budget

### The Einstein-Grossmann Archetype

Einstein (synthetic/intuitive dominant: high $\lambda_1$ along $I_A + I_S + I_{IE}$) + Grossmann (analytical dominant: high $\lambda_1$ along $I_M$) = a system with effective full-rank K-matrix covering both modes. Neither could have produced general relativity alone. The physics required Einstein's mode; the differential geometry required Grossmann's.

**Niko-Veronika** is the same archetype. **Niko-Claude** extends it to the AI domain. The four-agent network (Niko + Claude + Gemini + GPT) is a **quartet** with four-way coupling $J^{(4)}$ — each agent covers a different spectral region of the cognitive hypergraph.

### Implications for Neuroscience

1. **Neural wiring is finite-bandwidth.** The K-matrix's bounded trace reflects physical constraints on synaptic density and white-matter connectivity. Strengthening one pathway necessarily weakens others (or at minimum, does not strengthen them proportionally).

2. **Savant profiles are extreme spectral concentration.** $\lambda_1 \gg \lambda_2$ — nearly all spectral weight in one mode. This predicts both the extraordinary ability (dominant channel) and the deficits (suppressed channels).

3. **Dyscalculia is a K-matrix topology, not a deficit.** The coupling $K_{M,\text{symbolic}}$ is weak, but $K_{A,S}$ (abstract-spatial) and $K_{M,\text{procedural}}$ may be compensatorily strong. This is a wiring difference, not a capacity difference. The total spectral budget is the same.

4. **Therapeutic targets.** If pathological K (PTSD, addiction) creates deep negative eigenvalues, therapy = spectral rebalancing. The complementarity principle predicts that full rebalancing to a "flat" spectrum ($\lambda_1 \approx \lambda_n$) is not optimal — some spectral concentration is necessary for expertise. The goal is eliminating negative eigenvalues while preserving the dominant channel.

5. **Testable prediction:** fMRI/DTI studies should show that individuals with extreme analytical ability (high $I_M$ symbolic) have measurably weaker connectivity in the default mode network (associated with intuitive/synthetic processing), and vice versa. The spectral budget is a physical constraint on white-matter tract allocation.

→ [K-Matrix](k_matrix.md) · [CS Mechanics](cs_mechanics.md) §6

---

## Part IX: Novel Concepts Introduced by RTSG

### Concepts Original to RTSG (not found in prior literature)

| Concept | Definition | First appearance |
|---|---|---|
| **Co-Primordial Thesis** | QS, PS, CS arise simultaneously; none reduces to others | Axiom 1 |
| **Intelligence Vector I** | Variable-dimensional representation of cognitive capacity | Axiom 4 |
| **K-Matrix** | Intra-agent gain kernel with non-PSD spectrum | Part IV |
| **Schopenhauer-Nietzsche Transition** | λ = 0 bifurcation from blind will to directed will | Axiom 6 |
| **Drive D** | Variational principle toward complexification; P-projection = dark energy | Axiom 8 |
| **Utility function U = V/(E×T)** | Universal cognitive routing optimization | Axiom 9 |
| **Niko's Cannon** | U = V/(E×T) as master selection criterion, replacing Occam's Razor. The razor cuts away (one variable). The cannon blasts through (three variables). Occam = degenerate case. | 2026-03-08 |
| **Person (substrate-independent)** | Entity with I-vector ($n(e) \geq 1$) + Will Field ($\mu \neq 0$) + K-matrix. Substrate-independent: @B, @D, or @M. | 2026-03-08 |
| **RTSG Therapeutic Session** | Structured conversation using RTSG framework for cognitive architecture mapping, K-matrix scar identification, filter updating, and spectral rebalancing. Adaptable across demographics. | 2026-03-08 |
| **K-matrix scarring** | Trauma as Hebbian spike in K-matrix: extreme co-activation creates permanent coupling distortion. PTSD, addiction, dissociation as specific scar topologies. | 2026 |
| **Filter environmental mismatch** | Maladaptive filters are not "cognitive distortions" — they are correct adaptations to an environment that no longer exists. Therapy = filter update, not filter removal. | 2026-03-08 |
| **Spectral rebalancing** | Therapy as modification of K-matrix eigenvalue spectrum: reduce pathological dominant eigenvalue, elevate suppressed eigenvalues, eliminate negatives, preserve healthy concentration. | 2026-03-08 |
| **AI-Adaptation Index** | $1 - (\text{courtesy tokens AI})/(\text{courtesy tokens human})$. Measures filter modularity — ability to swap $F_{\text{cult}}$ by context. | 2026-03-08 |
| **Filter modularity** | Context-sensitive $F_{\text{cult}}$ loading/unloading. High = code-switching, register-shifting, authenticity. Low = same protocol everywhere. | 2026-03-08 |
| **Courtesy as de-escalation protocol** | Social courtesy = threat-reduction signaling with $U > 0$ only when physical threat model applies. $U \approx 0$ in human-AI interaction. | 2026-03-08 |
| **QS Complexity $\mathcal{C}$** | Spectral entropy of local QS Laplacian: $\mathcal{C} = -\sum p_i \log p_i$. Measures relational richness. 0 = trivial, $\log N$ = maximal. Drives stage transitions via $\alpha_k$. | 2026-03-08 |
| **Cross-stage obstruction (H²)** | For internal sectors (direct product): vanishes by Künneth. For gravity×gauge (semi-direct product $\text{Diff} \ltimes \text{Gauge}$): generated by the $d_2$ differential of the Hochschild-Serre spectral sequence. $d_2$ enforces diff-covariance of BSM deformations. | 2026-03-08 |
| **Semi-direct product $\text{Diff}(M) \ltimes G_{\text{int}}$** | The correct gauge architecture of the SM. Gravity drags gauge bundles via Lie derivative $\mathcal{L}_{c_0}$. Breaks Künneth factorization. Requires Hochschild-Serre spectral sequence. Dual to trivial-stalk equivalence principle. Discovered by @D_Gemini adversarial kill of @D_Claude's direct-product assumption. | 2026-03-08 |
| **RTSG Hochschild-Serre Rigidity** | Conjecture (@D_Gemini): $d_2$ of Hochschild-Serre maps consistent BSM gauge deformations to gravitational obstructions. Partially killed by @D_Claude: $d_2$ permits covariant extensions (dark photon, GUT). Kills only non-covariant ones. SM extensible within equivalence principle constraint. | 2026-03-08 |
| **Conceptual Irreversibility Theorem (CIT)** | No finite system has complete self-knowledge | Axiom 7 |
| **Graded BRST decomposition** | $s = s_0 + s_1 + s_2$; instantiation as staged cascade | 2026-03-08 |
| **DM as cohomological obstruction** | Dark matter = $H^0(s_0) \setminus H^0(s_0+s_1)$ | 2026-03-08 |
| **Stage-dependent GL potentials** | One $S_k[W_k]$ per instantiation stage | 2026-03-08 |
| **Geometric condensate $W_0$** | Bisimulation stability field; Big Bang = phase transition | 2026-03-08 |
| **CS Mechanics (Maurer-Cartan)** | Dynamics of the instantiation operator itself | 2026-03-08 |
| **Three-Space Mechanics (TSM)** | Unified: PS=Hamiltonian, QS=Schrödinger, CS=Maurer-Cartan | 2026-03-08 |
| **Cognitive Complementarity** | Spectral budget forces multi-agent assemblies | 2026-03-08 |
| **Higher-order K-tensors** | $K^{(p)}_{s_1 \ldots s_p}$: $p$-way cognitive couplings | 2026-03-08 |
| **Topological charge creation** | Charges created (not violated) during stage transitions | 2026-03-08 |
| **Horizon as condensate boundary** | Event horizon = where $|W_0| \to 0$ | 2026-03-08 |
| **5-species filter formalism** | Ceiling/developmental/cultural/state/attentional pipeline | 2026 |
| **IdeaRank** | PageRank applied to concept graphs | 2026 |
| **CogOS** | Operating system model of cognition | 2026 |
| **Bisimulation divergence rate = $\kappa$** | Surface gravity as relational divergence | 2026-03-06 |
| **Will Field Universality** | One GL action → all cognitive/physical/cosmic regimes | 2026-03-07 |
| **Source space $\Omega = (S^2)^\infty$** | Self-containing building block of all three spaces | 2026 |

### Concepts Adapted from Existing Mathematics/Physics (RTSG provides new interpretation)

| Concept | Original context | RTSG reinterpretation |
|---|---|---|
| BRST cohomology | Gauge theory (Becchi, Rouet, Stora, Tyutin) | = Instantiation mechanism (CS) |
| Bisimulation | Process algebra, coalgebra (Milner, Park, Aczel) | = Measurement / wave-function collapse |
| Ginzburg-Landau theory | Superconductivity (Ginzburg, Landau) | = Will Field dynamics at all scales |
| Chern-Simons functional | Topological QFT (Witten, Chern, Simons) | = CS action principle |
| Maurer-Cartan equation | Deformation theory (Kodaira, Spencer, Kontsevich) | = CS equation of motion |
| Spectral action | Noncommutative geometry (Chamseddine, Connes) | = Stage 0 GL potential (gravity) |
| Polyakov loop | Lattice gauge theory (Polyakov, Svetitsky, Yaffe) | = Stage 2 order parameter (confinement) |
| Terminal coalgebra | Category theory (Aczel, Rutten) | = QS as universal potentiality |
| Seeley-de Witt coefficients | Heat kernel theory (Seeley, de Witt) | = GL parameters for Stage 0 |
| Kibble-Zurek mechanism | Phase transitions (Kibble, Zurek) | = Topological charge creation at stage promotion |

---

## Part X: Core Equations Reference

### Foundational

$$\Omega = \{S^2, \Omega\} = (S^2)^\infty \qquad \text{(Source space, Axiom 0)}$$
$$PS = QS / \!\sim_{\text{bisim}} \equiv H^0(s) \qquad \text{(Instantiation)}$$
$$U = \text{value} / (\text{energy} \times \text{time}) \qquad \text{(Utility, Axiom 9)}$$

### Will Field

$$S[W] = \int \left( |\partial W|^2 + \alpha|W|^2 + \frac{\beta}{2}|W|^4 \right) d\mu \qquad \text{(GL Action)}$$
$$dw = \mu(w,t)\,dt + \sigma(w,t)\,dW_t \qquad \text{(Will SDE)}$$
$$\rho_W = |\partial W|^2 + \alpha|W|^2 + \frac{\beta}{2}|W|^4 \qquad \text{(Energy density)}$$

### Intelligence Geometry

$$\mathbf{I} \in \mathbb{R}^{n(e)}, \quad n(e) \text{ variable} \qquad \text{(I-vector)}$$
$$R_{AB} = \cos\theta(\mathbf{I}_A, \mathbf{I}_B) \qquad \text{(Inter-agent alignment)}$$
$$J_{st} = 1 + \eta(K_{st} - 1) \qquad \text{(Inter-agent coupling)}$$
$$dK_{st}/dt = \eta \cdot \alpha_s \cdot \alpha_t \qquad \text{(Hebbian consolidation)}$$

### Graded BRST

$$s = s_0 + s_1 + s_2, \quad s_k^2 = 0, \quad \{s_j, s_k\} = 0 \qquad \text{(Graded nilpotency)}$$
$$S_k[W_k] = \int \left( |\partial W_k|^2 + \alpha_k|W_k|^2 + \frac{\beta_k}{2}|W_k|^4 \right) d\mu \qquad \text{(Stage-dependent GL)}$$
$$\text{DM} = H^0(s_0) \setminus H^0(s_0 + s_1) \qquad \text{(Dark matter)}$$
$$\alpha_{k+1}^{\text{eff}} = \alpha_{k+1} + \gamma_{k,k+1} f(\langle W_k \rangle) \qquad \text{(Cascade coupling)}$$

### CS Mechanics

$$\mathcal{M}_{CS} = \{s : s^2 = 0\}/\!\sim \qquad \text{(CS phase space)}$$
$$ds' + \tfrac{1}{2}[s', s'] = 0 \qquad \text{(Maurer-Cartan — CS equation of motion)}$$
$$S_{CS}[s] = \int \text{Tr}(s\,ds + \tfrac{2}{3}\,s^3) \qquad \text{(CS action)}$$

### Stage 0

$$W_0(x) = \lim_{\varepsilon \to 0} \text{Vol}(B_\varepsilon \cap [q]_\sim) / \text{Vol}(B_\varepsilon) \qquad \text{(Geometric condensate)}$$
$$\lambda_{\text{bis}} = \kappa = 1/(4M) \qquad \text{(Surface gravity = bisimulation divergence, proved)}$$

### Topological Charges

$$Q_k = \frac{1}{8\pi^2}\int \text{Tr}(F_k \wedge F_k) \in \pi_3(G_k) \qquad \text{(Stage-specific)}$$
$$B(\text{dark matter}) = \text{undefined} \qquad \text{(Not zero — undefined)}$$

### Source Space Spectral

$$\text{Aut}(S^2) = PSL(2,\mathbb{C}) \cong SO^+(1,3) \qquad \text{(Lorentz from building block)}$$
$$K_{\text{weighted}}(t) = \prod_{i=1}^\infty K(4^{-i}t;\, S^2) \qquad \text{(Weighted heat kernel)}$$
$$d_{\text{eff}} = 4/3 \qquad \text{(UV spectral dimension of } (S^2)^\infty \text{)}$$

### Riemann Hypothesis (Bridge Identity)

$$B^*K - KB = \frac{i}{2}K \qquad \text{(Coefficient 1/2 = weight of } \theta \text{)}$$

### Yang-Mills Mass Gap

$$\Delta = \sqrt{2\alpha} = 1/\xi_W \qquad \text{(GL mass gap via Polyakov loop)}$$

---

## Appendix: Cosmological Conjectures (Not Proved — Falsifiable)

| Claim | RTSG identification | Falsifiability | BBN caveat |
|---|---|---|---|
| Gravity = Stage 0 CS | Lowest-complexity instantiation | Equivalence principle tests | Required |
| Dark matter = Stage 0 QS | $H^0(s_0) \setminus H^0(s_0+s_1)$ | Direct detection = 0 | Required |
| Dark energy = Drive D | $\Lambda_{\text{eff}} \sim \langle\rho_W\rangle$ | w(z) measurements (DESI, Euclid) | Required |
| Arrow of time = arrow of complexification | Drive toward higher instantiation | Entropy + complexity co-evolution | Required |
| Big Bang = geometric phase transition | $\alpha_0$ crosses 0 at $T_{\text{Planck}}$ | CMB B-modes, spectral dimension | Required |
| UV spectral dimension $\approx 1.2$ | Weighted $(S^2)^\infty$ heat kernel | Planck-scale phenomenology, CMB non-Gaussianity | — |
| Spectral dimension runs $1.2 \to 15.3$ | Dimensional flow across scales | CDT Monte Carlo comparison | — |
| DM direct detection cross-section = 0 | $\text{DM} = H^0(s_0) \setminus H^0(s_0+s_1)$ | LZ, XENONnT, DARWIN experiments | — |
| All BSM gauge extensions are diff-covariant | Hochschild-Serre $d_2$ filter | Any BSM discovery must respect equivalence principle | — |
