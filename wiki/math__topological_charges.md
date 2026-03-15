---
title: "Layer 4 — Conserved Charges as Topological Invariants of the BRST Complex"
nav_title: "Topological Charges"
version: "1.0.0"
last_updated: "2026-03-08"
status: "active development — Layer 4 of instantiation cascade formalization"
---

# Layer 4 — Conserved Charges as Topological Invariants of the BRST Complex

**Jean-Paul Niko · Sole Author**

!!! info "Purpose"
    This page answers the blocking question from [Graded BRST](../rtsg/graded_brst.md) §5.1: does baryon number conservation forbid dark matter promotion? We show that conserved quantum numbers are **topological invariants of individual BRST complexes** — they exist only within the stage whose topology defines them. Below that stage, the charge is undefined. This dissolves the blocking constraint and determines exactly when and how stage transitions can occur.

!!! danger "Integrity"
    Conjectures labeled. The SM results on anomalies and topology are established physics. The RTSG interpretations are new. Mark the boundary clearly.

---

## 1. The Question

Can dark matter (Stage 0 only) undergo promotion to visible matter (Stage 1+)? The [Graded BRST](../rtsg/graded_brst.md) framework identified a blocking constraint: baryon number conservation. If dark matter carries no baryon number and baryonic matter does, where does the baryon number come from during promotion?

Three options were listed. We now develop **Option 3**: baryon number is a topological invariant of the Stage 2 BRST complex, undefined below Stage 2. This turns out to be not just the most natural option — it's the one forced by the mathematics.

---

## 2. Conserved Charges in the Standard Model — The Topological Picture

### 2.1 Noether Charges vs. Topological Charges

In the SM, conserved charges have two distinct origins:

| Type | Source | Example | Exact? |
|---|---|---|---|
| **Noether** | Continuous symmetry of the Lagrangian | Electric charge $Q$ (from $U(1)_{\text{EM}}$) | Yes (perturbatively) |
| **Topological** | Homotopy of the gauge configuration space | Baryon number $B$ (from $\pi_3(SU(3))$) | No — anomalous |

Electric charge $Q$ is a Noether charge: it arises from the $U(1)_{\text{EM}}$ gauge symmetry that survives electroweak breaking. It is exactly conserved at all energies.

Baryon number $B$ and lepton number $L$ are **not** gauge symmetries. They are accidental global symmetries of the SM Lagrangian, violated by:

- **Electroweak sphalerons** at $T > T_{\text{EW}} \sim 160\,\text{GeV}$ (non-perturbative $SU(2)_L$ instantons)
- **ABJ anomaly**: $\partial_\mu j_B^\mu = \frac{N_f}{32\pi^2} \text{Tr}(F_{\mu\nu} \tilde{F}^{\mu\nu}) \neq 0$

The combination $B - L$ is anomaly-free and exactly conserved. But $B$ alone is not.

### 2.2 The Homotopy Origin of Baryon Number

In the SM, the vacuum structure of $SU(2)_L$ is characterized by:

$$\pi_3(SU(2)) = \mathbb{Z}$$

The integer winding number $n \in \mathbb{Z}$ labels topologically distinct vacua $|n\rangle$. Tunneling between adjacent vacua ($|n\rangle \to |n+1\rangle$) is the instanton/sphaleron process. Each such transition changes baryon number by $\Delta B = N_f = 3$ (one unit per generation).

Similarly, in the QCD sector:

$$\pi_3(SU(3)) = \mathbb{Z}$$

The QCD $\theta$-vacuum is a superposition of winding sectors. The strong CP problem and the axion are consequences of this topology.

**Key point:** These topological charges only exist because $\pi_3(G) \neq 0$ for the relevant gauge group $G$. If $G$ had trivial $\pi_3$, these charges would not exist.

---

## 3. Stage-Dependent Topology

### 3.1 Each Stage Has Its Own Homotopy

The graded BRST decomposition $s = s_0 + s_1 + s_2$ assigns a gauge group to each stage. Each group has its own homotopy:

| Stage | Gauge group $G_k$ | $\pi_0$ | $\pi_1$ | $\pi_2$ | $\pi_3$ | Physical meaning |
|---|---|---|---|---|---|---|
| 0 | $\text{Diff}(M)$ | Connected (for connected $M$) | Mapping class group | — | — | No topological charges at Stage 0 |
| 1 | $SU(2)_L \times U(1)_Y$ | 0 | 0 | 0 | $\mathbb{Z}$ | Electroweak winding → sphaleron $B$-violation |
| 2 | $SU(3)_c$ | 0 | 0 | 0 | $\mathbb{Z}$ | Color winding → $\theta$-vacuum, strong CP |
| After EWSB | $U(1)_{\text{EM}}$ | 0 | $\mathbb{Z}$ | 0 | 0 | Magnetic monopoles (if they exist); electric charge quantization |

### 3.2 The Stage-Dependence Theorem

**Theorem 1 (Topological charges are stage-specific).** *Let $Q_k$ be a topological charge arising from $\pi_n(G_k) \neq 0$ for some $n$. Then $Q_k$ is:*

1. *Defined only for states in $H^0(s_0 + \ldots + s_k)$ — states that have been instantiated through stage $k$*
2. *Undefined for states in $H^0(s_0 + \ldots + s_{k-1}) \setminus H^0(s_0 + \ldots + s_k)$ — states instantiated only through stage $k-1$*
3. *Conserved (modulo anomalies) within stage $k$ dynamics*

*Proof.* A topological charge $Q_k$ is defined by the winding number of a gauge field configuration in $G_k$:

$$Q_k = \frac{1}{8\pi^2} \int \text{Tr}(F_k \wedge F_k) \in \mathbb{Z}$$

This integral requires the gauge field $A_k$ of stage $k$ to exist. But $A_k$ only exists for states that are $s_k$-closed — states in the image of the stage $k$ BRST cohomology. For states outside $H^0(s_k)$, the gauge field $A_k$ is not defined (these states are not even coupled to the stage $k$ gauge sector), and the integral $Q_k$ has no meaning.

A state in $H^0(s_0) \setminus H^0(s_0 + s_1)$ (dark matter) has no $SU(2)_L \times U(1)_Y$ gauge field. The electroweak topological charge (sphaleron winding) is undefined for it. Similarly, baryon number — which depends on the electroweak winding via the ABJ anomaly — is undefined.

For states within $H^0(s_0 + \ldots + s_k)$, the charge $Q_k$ is conserved by the dynamics of stage $k$ (modulo anomalous violations by instantons/sphalerons of stage $k$). $\square$

### 3.3 Consequences for the Full Charge Spectrum

**Corollary 1 (Dark matter has no baryon number).**

Dark matter $\in H^0(s_0) \setminus H^0(s_0 + s_1)$. The electroweak gauge field does not exist for dark matter. The sphaleron winding that defines baryon number change is undefined. Therefore:

$$\boxed{B(\text{dark matter}) = \text{undefined} \quad (\text{not zero — undefined})}$$

This is stronger than "dark matter has $B = 0$." A state with $B = 0$ still lives in the space where $B$ is defined (a meson, for example). Dark matter lives **outside** the space where $B$ is defined. There is no baryon number to conserve or violate.

**Corollary 2 (Electric charge at Stage 1).**

After EWSB, electric charge $Q$ is the Noether charge of $U(1)_{\text{EM}}$. This is a gauge symmetry (not topological), so $Q$ is exactly conserved within Stage 1. It is a **Noether invariant** of $s_1$:

$$s_1 Q = 0 \qquad \text{(charge is BRST-invariant)}$$

Dark matter, being outside $H^0(s_1)$, has no electric charge — again, not zero but undefined.

**Corollary 3 (Color charge at Stage 2).**

Color charge $\{r, g, b\}$ is the gauge quantum number of $SU(3)_c$. It is defined only within $H^0(s_2)$. Quarks carry color; hadrons are color-singlets. Dark matter and unconfined visible matter both lack defined color charge for different reasons:

- Dark matter: outside Stage 2 entirely (and Stages 1+)
- Free quarks: inside Stage 1, carry color, but are not in $H^0(s_2)$ (not color-singlets)
- Hadrons: inside $H^0(s_2)$, color-singlet, net color charge = 0

---

## 4. Stage Transitions and Charge Creation

### 4.1 Promotion Creates Charges, Not Violates Them

**Theorem 2 (Charge creation at stage transition).** *When a state undergoes promotion from stage $k$ to stage $k+1$, the topological charges of stage $k+1$ are not violated — they are* ***created***. *The state transitions from a space where $Q_{k+1}$ is undefined to a space where $Q_{k+1}$ takes a definite value.*

*The value of $Q_{k+1}$ acquired during promotion is determined by the topology of the transition path in the stage $k+1$ gauge configuration space.*

**Physical analogy:** When water freezes into ice, the crystal lattice has topological defects (dislocations, grain boundaries) characterized by Burgers vectors $\vec{b} \in \mathbb{Z}^3$. Before freezing, the liquid has no crystal structure — $\vec{b}$ is undefined, not zero. The act of crystallization creates the lattice and simultaneously assigns defect charges. Similarly, stage promotion creates the gauge structure and simultaneously assigns the topological charges.

### 4.2 The Kibble-Zurek Mechanism at Each Stage

When a system crosses a phase transition (stage promotion), the order parameter cannot correlate across the entire system simultaneously. Independent domains form, and at domain boundaries, topological defects arise. This is the **Kibble-Zurek mechanism**.

At Stage 1 (electroweak): the Kibble-Zurek mechanism during EWSB produces electroweak strings and monopoles (if the transition is first-order). The sphaleron configuration is the unstable saddle point.

At Stage 2 (confinement): the Kibble-Zurek mechanism during the QCD phase transition produces color flux tubes connecting quark-antiquark pairs → hadronization.

**For dark matter promotion:** If a dark matter region undergoes Stage 1 promotion (local EWSB), the Kibble-Zurek mechanism determines what charges are created:

$$\Delta B = \frac{N_f}{8\pi^2} \int_{\text{transition}} \text{Tr}(F_1 \wedge F_1) \in \mathbb{Z}$$

The baryon number created during promotion is the **winding number of the gauge field configuration that forms during the transition**. It is not transferred from anywhere — it is created by the topology of the nascent gauge field.

### 4.3 Charge Balance and CPT

**Proposition 9 (Charge balance at promotion — Conjecture).** *Stage promotion in a CPT-invariant theory produces equal amounts of charge and anti-charge on average. Net charge creation requires CPT violation at the transition, which maps to the standard Sakharov conditions for baryogenesis:*

1. *Baryon number violation* → provided by the sphaleron topology of Stage 1 ($\pi_3(SU(2)) = \mathbb{Z}$)
2. *C and CP violation* → provided by CKM phase in the quark sector
3. *Departure from thermal equilibrium* → provided by the phase transition dynamics (first-order EWPT or non-equilibrium promotion)

**RTSG reading of baryogenesis:** The matter-antimatter asymmetry was created during Stage 1 promotion (EWSB) in the early universe. The Sakharov conditions are not mysterious requirements — they are the **topological and dynamical prerequisites** for net charge creation during a stage transition.

---

## 5. The Charge Lattice

### 5.1 Complete Classification

Combining all stages, the full conserved charge lattice of a state depends on its instantiation depth:

| Instantiation level | Defined charges | Undefined charges |
|---|---|---|
| Raw QS ($\Gamma \setminus H^0(s_0)$) | None | All |
| Stage 0 ($H^0(s_0) \setminus H^0(s_0+s_1)$) = DM | Energy-momentum $p^\mu$ (from Diff invariance) | $Q$, $B$, $L$, color, isospin, hypercharge |
| Stage 1 ($H^0(s_0+s_1) \setminus H^0(s)$) | $p^\mu$, $Q$, $T_3$, $Y$, $B$ (anomalous), $L$ (anomalous) | Color |
| Stage 2 ($H^0(s)$) = baryonic matter | All SM charges | None |

### 5.2 The Energy-Momentum Exception

Energy-momentum $p^\mu$ is special: it is the Noether charge of Diff$(M)$ (Stage 0). It is the **only charge that dark matter carries**, and it is the reason dark matter gravitates.

$$s_0 \, T_{\mu\nu} = 0 \qquad \text{(stress-energy is Stage 0 BRST-invariant)}$$

This is exactly what we observe: dark matter has gravitational mass but no electromagnetic or color charges.

### 5.3 $B - L$ as Cross-Stage Invariant

In the SM, $B - L$ is anomaly-free: the ABJ anomaly cancels between baryons and leptons. In the graded BRST picture:

**Proposition 10 ($B - L$ conservation — Conjecture).** *The combination $B - L$ is an invariant of the $s_1 + s_2$ complex jointly, not of either $s_1$ or $s_2$ alone. It is the unique anomaly-free combination because it corresponds to a non-trivial element of $H^0(s_1 + s_2)$ that is not in the image of either $H^0(s_1)$ or $H^0(s_2)$ separately.*

**Physical reading:** $B - L$ is the charge that measures the **net fermionic content** of a state across both electroweak and color sectors simultaneously. It is the "inter-stage topological invariant" — the charge that persists through the entire instantiation cascade from Stage 1 onward.

⚠ **Status: Conjecture.** The standard anomaly cancellation is proven physics. The cohomological interpretation as an inter-stage invariant is new.

---

## 6. Implications for Dark Matter Models

### 6.1 What Dark Matter Is (Refined)

In the graded BRST + topological charge picture:

$$\text{DM} = \{|\psi\rangle \in H^0(s_0) : s_1|\psi\rangle \neq 0\}$$

Dark matter consists of states with:
- Well-defined energy-momentum (gravitates) ✓
- No gauge field structure for $SU(2)_L \times U(1)_Y$ → no electric charge, no weak interaction
- No color structure → no strong interaction
- Topological charges $B$, $L$, $Q$ are all **undefined** (not zero)

### 6.2 Dark Matter Annihilation vs. Promotion

Two distinct processes, often conflated:

| Process | Mechanism | Charge accounting | Observable |
|---|---|---|---|
| **DM annihilation** | DM + DM → SM particles (assumes DM has some coupling to SM) | Charges created in pairs (particle + antiparticle) | Gamma rays, neutrinos |
| **DM promotion** | DM undergoes local stage transition → acquires gauge structure | Charges created by Kibble-Zurek topology | Phase transition signatures, gravitational waves |

Standard WIMP/axion models assume DM has feeble SM couplings → annihilation. The RTSG picture is different: DM has **no** SM coupling at all (it's outside the relevant BRST cohomology). The only path to visibility is **stage promotion** — a local phase transition.

### 6.3 Falsifiable Distinction

If DM is purely Stage 0 (RTSG prediction), then:

1. **Direct detection cross-section = 0** (not just small — exactly zero), because there is no gauge field to mediate scattering
2. **Indirect detection (annihilation) = 0** for the same reason
3. The only observable signatures are gravitational + potential promotion events

This is a strong, falsifiable prediction. If direct detection experiments (LZ, DARWIN) find a non-zero cross-section, RTSG's Stage 0 identification of DM is wrong.

⚠ **Caveat:** This applies to the purest form of the RTSG DM picture. Mixed models (some DM at Stage 0, some with feeble Stage 1 coupling) are possible but less elegant.

---

## 7. Open Gaps (Honest)

1. **Diff$(M)$ topology.** The homotopy groups of Diff$(M)$ for general 4-manifolds $M$ are subtle and largely unknown. We used "no topological charges at Stage 0" loosely — this needs refinement. For $M = \mathbb{R}^4$, Diff is contractible (Cerf). For compact $M$, the mapping class group $\pi_0(\text{Diff})$ is non-trivial. This may give rise to gravitational topological sectors (gravitational instantons). How do these interact with stage transitions?

2. **Anomaly cancellation from BRST.** The statement that $B - L$ is an inter-stage invariant needs a rigorous BRST cohomological derivation. The standard anomaly calculation (triangle diagrams) should be re-derivable as a cohomological obstruction in the graded complex.

3. **Kibble-Zurek quantitative predictions.** The claim that promotion creates charges via Kibble-Zurek requires computing the defect density during a local stage transition. The critical exponents from Stage 0 (§6 of [Stage 0 Gravity](../rtsg/stage0_gravity.md)) would feed into this.

4. **DM self-interaction.** If DM is purely Stage 0, it interacts only gravitationally. But some astrophysical observations suggest DM self-interaction ($\sigma/m \sim 1\,\text{cm}^2/\text{g}$). Could there be a Stage 0 self-interaction beyond gravity? The GL self-coupling $\beta_0|W_0|^4$ provides one, but its strength relative to gravity needs computation.

5. **Layer 3 dependence.** The assignment of gauge groups to stages is still post hoc. Layer 3 (source space gauge derivation) would make the entire topological charge analysis derivable from first principles.

---

## 8. Summary Equations

$$Q_k = \frac{1}{8\pi^2}\int \text{Tr}(F_k \wedge F_k) \in \pi_3(G_k) \cong \mathbb{Z}$$

$$B(\text{dark matter}) = \text{undefined} \quad (\text{not zero})$$

$$\Delta B_{\text{promotion}} = \frac{N_f}{8\pi^2}\int_{\text{transition}} \text{Tr}(F_1 \wedge F_1)$$

$$s_0\, T_{\mu\nu} = 0 \quad \text{(energy-momentum = unique Stage 0 charge)}$$

---

## 9. Relation to Existing Wiki Pages

- **[Graded BRST](../rtsg/graded_brst.md)**: Gap 5 (topological charges) → this page. Resolves §5.1 blocking constraint.
- **[Stage 0 Gravity](../rtsg/stage0_gravity.md)**: Stage 0 carries only $p^\mu$. Equivalence principle = trivial stalk.
- **[Source Space](../rtsg/source_space.md)**: $\pi_2((S^2)^\infty) = \mathbb{Z}^\infty$, $\pi_3$ via Aut$(S^2) = PSL(2,\mathbb{C})$.
- **[Master](../rtsg/master.md)** §VIII: Dark matter = uncondensed Will Field → now refined as Stage 0 with undefined charges.
- **[Three Spaces](../rtsg/three_spaces.md)**: DM = Stage 0 QS → charge-theoretic refinement.
- **[Langlands Bridge](../rtsg/langlands_bridge.md)**: If CS = Langlands functor, charge creation at stage transition = functorial assignment of Galois representations.
