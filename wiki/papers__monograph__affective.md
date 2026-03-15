---
title: "Affective Architecture"
version: "2.0.0"
last_updated: "2026-03-05"
status: CURRENT
---

!!! info "Terminology Note (2026-03-07)"
    This document uses "Consciousness-Space (CS)" throughout. In current RTSG v3, CS is the **instantiation operator** $C$: a BRST cohomological filter extracting physical observables $H^0(s)$ from non-well-founded Quantum Space. The Will Field $W$ is governed by the Ginzburg-Landau action $S[W] = \int(|\partial W|^2 + \alpha|W|^2 + (\beta/2)|W|^4)d\mu$. Wave-function collapse is bisimulation quotienting: $PS = QS/\!\sim_{\text{bisim}}$. See [Master Reference v3](../../rtsg/master.md).

# Affective Architecture

**Jean-Paul Niko** · February 2026

!!! abstract "Abstract"
    
We develop the theory of how intelligence is modulated, bypassed, informed, and structurally shaped by non-cognitive systems.
Part I defined *what* the mind can do (the intelligence vector $\bI$). This part addresses *what the mind actually does* under the influence of emotion, hormonal state, somatic signaling, intuition, and developmental trajectory. 
We introduce:
**(1)** the affective modulation operator $\Mop(\be)$, an $8\times 8$ matrix transforming capacity into effective intelligence;
**(2)** the emotional bypass channel $\Phi(\be)$, producing action without routing through intelligence;
**(3)** the emotional signal function $\Sop(\be)$, providing epistemic content inaccessible to the intelligence types alone;
**(4)** a three-mode theory of intuition (compressed expertise, cross-type synthesis, subliminal detection);
**(5)** the hormonal modulation layer $\mathcal{H}(t)$, operating on timescales from minutes to decades;
**(6)** somatic intelligence channels (enteric, cardiac, immune);
**(7)** sleep as cognitive mode-switching;
**(8)** developmental dynamics of the intelligence vector across the lifespan;
**(9)** trauma as structural deformation;
**(10)** the uncanny and the numinous, with honest tier classification.
The result is a unified equation for cognitive output that distinguishes capacity from deployment and explains why intelligent agents routinely act against their own best reasoning.

---

%═══════════════════════════════════════════════════════════════════════════════
%  SECTION 1: THE CENTRAL PROBLEM
%═══════════════════════════════════════════════════════════════════════════════

## Three-Space Context: The Id and Temporal Tension

The three-space ontology (Part XIII) reveals a deeper source for the affective-somatic architecture.  Consciousness-space $\CSp$ possesses complex time $t_\CSp = t_\mathbb{R} + i\,t_{\mathrm{lat}}$, which gives consciousness a lateral temporal freedom---the ability to navigate "sideways" in time, re-accessing past states and pre-experiencing future ones.  Evolution, however, requires organisms to act in physical time $t_\mathbb{R}$: to eat, flee, and reproduce *now*, not in a lateral temporal excursion.

The **Id** is the evolutionary solution to this tension.  It is a pre-filter (Species 0 in the filter cascade) that anchors consciousness to $t_\mathbb{R}$ and overrides lateral temporal freedom when survival demands it.  Emotion is the *signal channel* through which the Id communicates with the hypervisor---the felt urgency that pulls attention back to the present moment and redirects the attention simplex toward survival-salient types.

The three roles of emotion (modulation, bypass, epistemic channel) are thus three aspects of the Id's influence on the filter cascade: modulation adjusts the state filter $F_{\mathrm{state}}$, bypass circumvents the attention filter entirely, and the epistemic channel injects evolutionary knowledge (procedural memory built into $\bK$ over millions of years) into the decision process.

## The Central Problem: Capacity vs.\ Deployment

Part I defined the intelligence vector $\bI \in \\mathbb{R}^{n(e)}_{\geq 0}$ as a measure of cognitive *capacity*. But capacity and deployment are not the same. A mathematician paralyzed by stage fright has the same $I_A$ as when she is calm, yet her effective algebraic output is near zero. A soldier under fire performs physical feats beyond his training baseline. A grieving parent cannot think clearly about anything except the lost child.

The intelligence vector tells you what the engine *can* do. It does not tell you what the engine *will* do. The gap between capacity and deployment is governed by systems that are not themselves "intelligent" in the type-space sense: emotion, hormones, somatic state, developmental stage, and the accumulated deformations of experience.

\begin{keythm}
**The Deployment Principle.** The cognitive output of an agent at time $t$ is not the intelligence vector $\bI$ but the *deployed intelligence*:

\[
\bI_{\mathrm{eff}}(t) = f(\bI,\; \be(t),\; \bh(t),\; \bs(t),\; \tau(t),\; \Delta)

\]

where $\be$ is emotional state, $\bh$ is hormonal state, $\bs$ is somatic state, $\tau$ is developmental stage, and $\Delta$ is the accumulated structural deformation from experience (including trauma). The function $f$ is the subject of this part.
\end{keythm}

%═══════════════════════════════════════════════════════════════════════════════
%  SECTION 2: THE THREE ROLES OF EMOTION
%═══════════════════════════════════════════════════════════════════════════════

## The Three Roles of Emotion

Emotion relates to intelligence not as one thing but as three.

!!! axiom "The Tripartite Emotional Architecture"
 \tB\;
Emotion acts on cognition through three distinct channels operating at different timescales and with different mathematical structures:
[nosep]
    - **Modulation**: Emotion scales the effective capacity of each intelligence type. (Timescale: seconds to hours.)
    - **Bypass**: Emotion produces action directly, without routing through the intelligence types. (Timescale: milliseconds.)
    - **Signal**: Emotion carries epistemic content derived from channels inaccessible to the intelligence types. (Timescale: minutes to hours for integration.)

\begin{interpretation}
These are not metaphorical distinctions. They correspond to distinct neural pathways. The amygdala-to-motor-cortex projection (bypass) is anatomically separate from the prefrontal cortical modulation of attention (modulation), which is separate from interoceptive inference (signal). The mathematical formalism respects the biological architecture.
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════
%  SECTION 3: THE AFFECTIVE MODULATION OPERATOR
%═══════════════════════════════════════════════════════════════════════════════

## Role I: The Affective Modulation Operator

### The Emotional State Vector

!!! definition "Emotional State Vector"
 \tB

The *emotional state* at time $t$ is a vector $\be(t) \in \R^3$ in the PAD (Pleasure--Arousal--Dominance) space of Mehrabian and Russell (1974):
\[
\be(t) = (v(t),\; a(t),\; d(t))
\]
where $v \in [-1, 1]$ is valence (pleasure/displeasure), $a \in [0, 1]$ is arousal (activation intensity), and $d \in [-1, 1]$ is dominance (sense of control). The norm $\|\be\| = \sqrt{v^2 + a^2 + d^2}$ measures emotional intensity.

### The Modulation Operator

!!! definition "Affective Modulation Operator"
 \tB

The *affective modulation operator* is a map $\Mop: \R^3 \to \R^{8 \times 8}_{\geq 0}$ assigning to each emotional state an $8 \times 8$ matrix:
\begin{keythm}

\[
\bI_{\mathrm{mod}}(t) = \Mop(\be(t)) \cdot \bI

\]

\end{keythm}
The matrix $\Mop(\be)$ has entries $\Mop_{kl}(\be)$ where:
[nosep]
    - Diagonal entries $\Mop_{kk}$: how emotion scales the effective capacity of type $k$
    - Off-diagonal entries $\Mop_{kl}$, $k \neq l$: how emotion redirects capacity from type $l$ to type $k$ (attentional reallocation)

!!! definition "Properties of $\Mop$"
 \tB

The modulation operator satisfies:
[nosep]
    - **Neutrality at rest**: $\Mop(\mathbf{0}) = \Id$ (zero emotional intensity $\Rightarrow$ full capacity deployed).
    - **Non-negativity**: $\Mop_{kl}(\be) \geq 0$ for all $k, l, \be$ (emotion cannot produce negative intelligence).
    - **Bounded amplification**: $\|\Mop(\be)\|_{\mathrm{op}} \leq \mu_{\max}$ for some finite $\mu_{\max}$ (emotion cannot produce infinite intelligence). Empirical estimate: $\mu_{\max} \approx 2.0$.
    - **Conservation tendency**: $\tr(\Mop(\be)) \leq 8 + \epsilon(a)$ where $\epsilon$ is small for moderate arousal. Total deployed intelligence is approximately conserved --- emotion mostly *redirects* rather than creates capacity, with a modest amplification budget at high arousal.

### Regime Classification

!!! definition "Modulation Regimes"
 \tB

For a given emotional state $\be$ with modulation operator $\Mop(\be)$ having eigenvalues $\lambda_1 \geq \ldots \geq \lambda_8$:
\begin{center}

*[Table — see PDF]*

\end{center}

### Canonical Modulation Profiles

!!! definition "Canonical Profiles"
 \tB

The following canonical profiles are empirically motivated estimates of the diagonal component of $\Mop$ for named emotional states. Off-diagonal terms (attentional reallocation) are smaller and omitted for clarity.

\begin{center}
\small

*[Table — see PDF]*

\end{center}

\begin{interpretation}
Notable patterns:
[nosep]
    - Terror and anger *amplify* kinesthetic capacity while shutting down algebraic and emotional processing. The body takes over.
    - Grief selectively preserves emotional processing ($I_E$) while suppressing nearly everything else. The mind turns inward.
    - Flow amplifies everything. This is the only regime where no type is suppressed.
    - Shame is devastating to social cognition ($I_S \to 0.2$). The person most needs to navigate the social situation and least can.
    - Love dramatically amplifies social and emotional processing while mildly suppressing formal reasoning. Evolution values bonding over computation.

\end{interpretation}

### The Dominance Asymmetry

\begin{keythm}

!!! theorem "Affective Dominance Asymmetry"
 \tB

Let $\tau_{\mathrm{e \to i}}$ be the timescale on which emotional state $\be$ modulates the intelligence vector (emotion affecting cognition), and $\tau_{\mathrm{i \to e}}$ the timescale on which cognitive processing modifies the emotional state (cognition affecting emotion). Then:

\[
\tau_{\mathrm{e \to i}} \ll \tau_{\mathrm{i \to e}}

\]

Empirically: $\tau_{\mathrm{e \to i}} \sim 100$--$500\;\mathrm{ms}$ (amygdala response, hormonal cascade initiation). $\tau_{\mathrm{i \to e}} \sim 10$--$60\;\mathrm{s}$ (cognitive reappraisal, prefrontal regulation). The ratio $\tau_{\mathrm{i \to e}}/\tau_{\mathrm{e \to i}} \approx 20$--$600$.

\end{keythm}

??? proof "Proof"
[Proof sketch]
Anatomical: the amygdala receives thalamic input and projects to cortex in $\sim$12 ms (LeDoux, 1996). Cortical evaluation of emotional stimuli requires $\sim$300 ms. Prefrontal modulation of amygdala activity requires sustained activation over seconds (Ochsner & Gross, 2005). The asymmetry is architectural, not contingent.

\begin{interpretation}
This theorem explains the core phenomenon: why you can *know* the right answer and not do it. Intelligence operates at $\tau_{\mathrm{i \to e}}$. Emotion operates at $\tau_{\mathrm{e \to i}}$. In any race, emotion wins unless intelligence has set up *precommitments* --- rules, habits, structures, environmental constraints --- computed in advance and stored as fast-access defaults. Discipline, mathematically, is:

\[
\mathcal{D} = \left\{ \text{precomputed constraints on } \Phi \text{ that hold when } \|\be\| > \be_{\mathrm{crit}} \right\}

\]

Discipline does not fight emotion in real time. It installs guardrails during calm that survive the storm.
\end{interpretation}

### Phase Transitions in Modulation

\begin{keythm}

!!! theorem "Emotional Phase Transition"
 \tB

As emotional intensity $\|\be\|$ increases through a critical threshold $\|\be\|_{\mathrm{crit}}$, the modulation operator $\Mop(\be)$ undergoes a discontinuous transition:

\[
\lim_{\|\be\| \to \|\be\|_{\mathrm{crit}}^+} \lambda_{\min}(\Mop(\be)) = 0 \qquad \text{while} \qquad \lim_{\|\be\| \to \|\be\|_{\mathrm{crit}}^-} \lambda_{\min}(\Mop(\be)) > 0

\]

Below the threshold, all intelligence types remain online (possibly attenuated). Above it, at least one type is completely shut down. The rank of $\Mop$ drops discontinuously.

\end{keythm}

??? proof "Proof"
[Proof sketch]
Model $\Mop_{kk}(\be)$ as a sigmoid function of $\|\be\|$ with type-dependent thresholds. The least robust type has the lowest threshold $\|\be\|_k^{\mathrm{crit}}$. When $\|\be\|$ crosses $\min_k \|\be\|_k^{\mathrm{crit}}$, that type's diagonal entry hits zero, dropping the rank. The transition is sharp because sigmoid functions approach step functions at high gain, and biological activation functions (neural firing rates) have precisely this character.

!!! remark "The Robustness Ordering"

Intelligence types have a characteristic *robustness ordering* --- the order in which they shut down under increasing emotional intensity. Empirical estimate of shutdown order (least robust first):
\[
I_A \to I_S \to I_E \to I_L \to I_M \to I_N \to I_G \to I_K
\]
Algebraic reasoning is the first casualty of emotional overwhelm. Kinesthetic capacity is the last to go. This ordering is not accidental: it recapitulates the evolutionary age of the underlying neural systems. The most recently evolved capacities (formal reasoning) are the most fragile under stress; the most ancient (motor control) are the most robust.

%═══════════════════════════════════════════════════════════════════════════════
%  SECTION 4: THE EMOTIONAL BYPASS CHANNEL
%═══════════════════════════════════════════════════════════════════════════════

## Role II: The Emotional Bypass Channel

!!! definition "Emotional Bypass"
 \tB

The *emotional bypass channel* is a map $\Phi: \R^3 \to \mathcal{A}$ from emotional state space to an action space $\mathcal{A}$, producing motor output *without routing through the intelligence types*:
\begin{keyeqn}
\[
\Phi(\be(t)) \in \mathcal{A} = \{\text{fight, flight, freeze, fawn, reach, recoil, vocalize, \ldots}\}
\]
\end{keyeqn}
The bypass channel is low-dimensional (small $|\mathcal{A}|$), fast ($\sim$12--50 ms latency), and evolutionarily ancient (subcortical pathways).

!!! definition "Bypass Activation Threshold"
 \tB

The bypass channel activates when emotional intensity exceeds a critical threshold:
\begin{keyeqn}
\[
\|\Phi(\be)\| = \begin{cases} 0 & \text{if } \|\be\| < \beta_{\mathrm{crit}}    \phi(\|\be\| - \beta_{\mathrm{crit}}) & \text{if } \|\be\| \geq \beta_{\mathrm{crit}} \end{cases}
\]
\end{keyeqn}
where $\phi$ is a monotone increasing function and $\beta_{\mathrm{crit}}$ is the bypass threshold. Below threshold, all action is intelligence-mediated. Above threshold, the bypass channel produces direct action that *preempts* the intelligence system.

The threshold $\beta_{\mathrm{crit}}$ is not fixed. It is modulated by:
[nosep]
    - Training and habituation (soldiers, athletes, meditators raise $\beta_{\mathrm{crit}}$)
    - Trauma (PTSD lowers $\beta_{\mathrm{crit}}$, sometimes to near zero)
    - Fatigue and sleep deprivation (lower $\beta_{\mathrm{crit}}$)
    - Hormonal state (cortisol lowers $\beta_{\mathrm{crit}}$; see \S*ref:sec:hormonal*)

\begin{keythm}

!!! theorem "Bypass Preemption"
 \tB

When the bypass channel is active ($\|\be\| \geq \beta_{\mathrm{crit}}$), the total cognitive output satisfies:

\[
\bO(t) = \Phi(\be(t)) + \eta(t) \cdot \Mop(\be(t)) \cdot \bI

\]

where $\eta(t) \in [0, 1]$ is the *residual intelligence coefficient*:
\[
\eta(t) = \max\!\left(0,\; 1 - \frac{\|\Phi(\be(t))\|}{\Phi_{\max}}\right)
\]
As bypass output increases, residual intelligence decreases. At maximum bypass activation, $\eta = 0$ and all output is emotional.

\end{keythm}

\begin{interpretation}
This theorem formalizes the experience of being "taken over" by emotion. The scream that escapes before you've decided to scream. The flinch that precedes any evaluation of danger. The freeze that immobilizes you despite knowing you should move. In these moments, $\eta \to 0$ and the intelligence vector contributes nothing to the output. You are not "choosing poorly." You are not choosing at all. The bypass channel is producing the output and the intelligence system is offline.
\end{interpretation}

!!! remark "Post-hoc rationalization"

When the bypass channel fires and then subsides ($\eta$ recovers toward 1), the intelligence system comes back online and encounters an action already taken. The typical response is *confabulation*: the intelligence types construct a narrative explaining why the bypass action was "really" a choice. This is a well-documented phenomenon (Nisbett & Wilson, 1977; Gazzaniga, 2000) and has structural consequences: the intelligence system's self-model is systematically inaccurate about its own causal role when bypass has been active.

%═══════════════════════════════════════════════════════════════════════════════
%  SECTION 5: THE EMOTIONAL SIGNAL CHANNEL
%═══════════════════════════════════════════════════════════════════════════════

## Role III: Emotion as Epistemic Channel

!!! definition "Emotional Signal Function"
 \tB

The *emotional signal function* is a map $\Sop: \R^3 \to \\mathbb{R}^{n(e)}$ that provides additional input to the intelligence types from channels they cannot access directly:
\begin{keyeqn}
\[
\bI_{\mathrm{signal}}(t) = \bI \circ \Sop(\be(t))
\]
\end{keyeqn}
where $\circ$ denotes the Hadamard (componentwise) product. $\Sop_k(\be) > 0$ means the emotional signal is providing data relevant to type $k$; $\Sop_k = 0$ means no additional data for that type.

!!! definition "Signal Sources"
 \tB

The emotional signal channel aggregates information from:
\begin{center}

*[Table — see PDF]*

\end{center}
These sources operate continuously but report to consciousness as *feelings* rather than propositions, because the processing that produces them is distributed, non-symbolic, and does not pass through the linguistic bottleneck.

\begin{keythm}

!!! theorem "Signal Irreducibility"
 \tB

The emotional signal $\Sop(\be)$ carries information that is not, in general, recoverable from the intelligence types alone. Formally: there exist environmental states $\omega$ and intelligence vectors $\bI$ such that:

\[
P(\omega \mid \bI) < P(\omega \mid \bI, \Sop(\be))

\]

The emotional signal has strictly positive mutual information with the environment conditional on the intelligence vector. Gut feelings are not noise.

\end{keythm}

??? proof "Proof"
[Proof sketch]
Construct the case: agent enters a room with a concealed hostile individual. The intelligence types ($I_L$: verbal content is normal; $I_A$: no logical inconsistency; $I_G$: no visible threat) report all-clear. But the emotional signal registers elevated amygdala activation from subliminal detection of fear pheromones and micro-expression analysis. The conditional probability of "threat present" given the emotional signal exceeds the probability given intelligence types alone. The signal carries strictly new information.

\begin{interpretation}
This theorem validates the folk concept of "gut feeling" as a genuine epistemic category, not a failure of rationality. The emotional signal function is the mathematical framework's answer to the question: "If I can't explain why I feel uneasy, should I trust it?" The answer is: *sometimes yes*, because the unease may be carrying information from channels your conscious reasoning cannot access. The challenge is that the signal is noisy --- it also fires for trauma triggers, prejudice, and unfamiliar-but-safe situations. Wisdom is learning to read the signal's reliability, which is itself a trainable capacity (Pillar 4).
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════
%  SECTION 6: THE COMPLETE OUTPUT EQUATION
%═══════════════════════════════════════════════════════════════════════════════

## The Complete Output Equation

Combining the three emotional roles with the base intelligence, the total cognitive output is:

\begin{keythm}

\[
\boxed{\bO(t) = \underbrace{\eta(t) \cdot \Mop(\be(t)) \cdot \bI}_{\text{modulated intelligence}} + \underbrace{\Phi(\be(t))}_{\text{bypass}} + \underbrace{\eta(t) \cdot \bI \circ \Sop(\be(t))}_{\text{signal-enhanced intelligence}}}

\]

\end{keythm}

!!! definition "Priority Hierarchy"
 \tB

The three terms operate at different timescales and obey a priority hierarchy:
\begin{center}

*[Table — see PDF]*

\end{center}
In any conflict, the faster channel wins. Bypass preempts modulation preempts deliberation.

!!! definition "Emotional Override Strength"
 \tB

The *emotional override strength* measures total deviation from baseline:
\begin{keyeqn}
\[
\Gamma(\be) = \underbrace{\|\Id - \Mop(\be)\|_F}_{\text{modulation deviation}} + \underbrace{\|\Phi(\be)\|}_{\text{bypass strength}} + \underbrace{\|\Sop(\be) - \mathbf{1}\|}_{\text{signal deviation}}
\]
\end{keyeqn}
where $\|\cdot\|_F$ is the Frobenius norm. $\Gamma = 0$ at emotional neutrality. Large $\Gamma$ means emotion is strongly shaping cognitive output.

\begin{keythm}

!!! theorem "Emotional Dominance Conditions"
 \tB

Intelligence dominates the output ($\bO \approx \bI$) if and only if all three conditions hold simultaneously:
[nosep]
    - $\|\be\| < \beta_{\mathrm{crit}}$ (bypass inactive)
    - $\lambda_{\min}(\Mop(\be)) > 1 - \epsilon$ for small $\epsilon$ (modulation near-neutral)
    - $\|\Sop(\be)\|$ is small (no strong emotional signals)

Failure of *any single condition* is sufficient for emotion to significantly shape the output.

\end{keythm}

%═══════════════════════════════════════════════════════════════════════════════
%  SECTION 7: INTUITION
%═══════════════════════════════════════════════════════════════════════════════

## Intuition: The Three Modes

!!! definition "Intuition"
 \tB

*Intuition* is the subjective experience of arriving at a cognitive output (judgment, decision, insight) without access to the processing chain that produced it. In the framework, intuition is not a separate faculty but the *felt manifestation of three distinct computational processes* whose intermediate steps are below the conscious threshold.

### Mode 1: Compressed Expertise

!!! definition "Compressed Expertise"
 \tA

*Compressed expertise* occurs when an intelligence type has processed enough exemplars that pattern matching occurs below conscious threshold. The output arrives as a feeling rather than a chain of reasoning.
\begin{keyeqn}
\[
\mathcal{I}_{\mathrm{comp}}(x) = \lim_{N \to \infty} f_k^{(N)}(x)
\]
\end{keyeqn}
where $f_k^{(N)}$ is the type-$k$ recognition function after $N$ training exemplars. In the large-$N$ limit, the function fires faster than conscious introspection can trace. The chess grandmaster "sees" the right move because $I_A$ and $I_G$ have compressed thousands of board evaluations into an instant pattern match.

!!! remark "Remark"

This is Tier A because it is computationally well-understood: it is the recognition-primed decision model of Klein (1993), the expert pattern matching of Simon (1992), and the System 1 processing of Kahneman (2011). The intelligence types are doing the work. Intuition is the phenomenology of their speed.

### Mode 2: Cross-Type Synthesis

!!! definition "Cross-Type Synthesis"
 \tB

*Cross-type synthesis* occurs when multiple intelligence types reach agreement on a judgment, but no single type can express the conclusion in its own representational language.
\begin{keyeqn}
\[
\mathcal{I}_{\mathrm{syn}}(x) = \Theta\!\left(\sum_{k=1}^{8} w_k \cdot g_k(x) - \theta_{\mathrm{syn}}\right)
\]
\end{keyeqn}
where $g_k(x)$ is type $k$'s partial evaluation of $x$, $w_k$ are attention weights, and $\Theta$ is the Heaviside step function with threshold $\theta_{\mathrm{syn}}$. Intuition fires when the weighted sum of partial evaluations exceeds threshold, even though no individual $g_k(x)$ is sufficient.

\begin{interpretation}
Cross-type synthesis is the *felt experience of compatibility tensor activation*. The synergy is real --- multiple types are converging on a judgment --- but the result is linguistically inaccessible because it is encoded in the interaction between types, not in any single type's representation. This is why intuition often "cannot be explained": the explanation would require simultaneously inhabiting multiple representational modes, and language ($I_L$) can only serialize one at a time.
\end{interpretation}

### Mode 3: Subliminal Detection

!!! definition "Subliminal Detection"
 \tB

*Subliminal detection* occurs when the emotional signal function $\Sop(\be)$ has detected a genuine environmental pattern but the underlying evidence has not reached conscious awareness. This is the intersection of the signal channel (\S*ref:sec:signal*) and intuition.
\begin{keyeqn}
\[
\mathcal{I}_{\mathrm{sub}}(x) = \Sop(\be_x) \text{ where } \be_x \text{ is the emotional response to stimulus } x
\]
\end{keyeqn}
The "feeling about $x$" *is* the intuition. It carries genuine information (*ref:eq:irreducibility*) but arrives in affective rather than propositional format.

\begin{keythm}

!!! theorem "Intuition Decomposition"
 \tB

Any intuitive judgment $\mathcal{I}(x)$ is a mixture of the three modes:

\[
\mathcal{I}(x) = \alpha_1 \cdot \mathcal{I}_{\mathrm{comp}}(x) + \alpha_2 \cdot \mathcal{I}_{\mathrm{syn}}(x) + \alpha_3 \cdot \mathcal{I}_{\mathrm{sub}}(x), \quad \alpha_1 + \alpha_2 + \alpha_3 = 1

\]

The reliability of the intuition depends on the mixture weights:
[nosep]
    - Compressed expertise ($\alpha_1$ dominant): High reliability in the domain of expertise, near zero outside it.
    - Cross-type synthesis ($\alpha_2$ dominant): Moderate reliability; cross-type agreement is a genuine evidence signal.
    - Subliminal detection ($\alpha_3$ dominant): Variable reliability; high for physical threat detection, low for abstract judgment. Confounded by trauma triggers and bias.

\end{keythm}

%═══════════════════════════════════════════════════════════════════════════════
%  SECTION 8: THE UNCANNY AND THE NUMINOUS
%═══════════════════════════════════════════════════════════════════════════════

## The Uncanny, the Sixth Sense, and the Numinous

\begin{warning}
This section spans all three tiers. We are scrupulous about marking which claims are testable (A), formally modeled but ungrounded (B), and frankly speculative (C). The framework's integrity requires not foreclosing these phenomena *or* overclaiming about them.
\end{warning}

### The Uncanny: Subliminal Anomaly Detection

!!! definition "The Uncanny"
 \tA

The *uncanny* is the subjective experience arising when the subliminal detection system (\S*ref:def:subliminal*) registers a statistical anomaly --- a deviation from the expected environmental baseline --- that has not yet been consciously identified. Formally:
\begin{keyeqn}
\[
U(x) = \|\Sop(\be_x) - \Sop(\be_{\mathrm{baseline}})\| > \theta_U \quad \text{while} \quad \sum_k I_k \cdot g_k(x) < \theta_{\mathrm{conscious}}
\]
\end{keyeqn}
The emotional system has detected something. The intelligence system has not yet identified what. The subjective quality is unease, dread, or the sense that "something is off."

!!! example "Tier A instances"
 \tA

[nosep]
    - A room has become unusually quiet (ambient sound baseline violated)
    - A face is almost but not quite normal (uncanny valley: geometric expectation violated)
    - A social interaction has a slightly wrong rhythm (prosodic baseline violated)
    - An environment has an unusual smell (olfactory anomaly below conscious detection)

In each case, the detection is real and the unease is epistemically justified. The "sixth sense" is the signal channel doing its job.

### The Extended Uncanny: Environmental Sensitivities

!!! definition "Extended Sensitivities"
 \tB

Some uncanny experiences may reflect sensitivity to environmental variables not typically acknowledged in cognitive science:
\begin{center}

*[Table — see PDF]*

\end{center}

### The Numinous

!!! definition "The Numinous"
 \tC

The *numinous* is the subjective experience of contact with something vast, transcendent, or "wholly other" (Otto, 1917). It is characterized by:
[nosep]
    - Awe and dread simultaneously (*mysterium tremendum*)
    - A sense of one's own smallness or contingency (*creatura feeling*)
    - The experience of meaning or significance that exceeds any specific content
    - Frequent co-occurrence with temporal lobe activity, deep meditation, psychedelic states, extreme beauty, or proximity to death

!!! definition "Framework Position on the Numinous"
 \tC

The framework acknowledges three non-exclusive candidate explanations:

**Reductive (Tier A).** The numinous is an extreme modulation event: $\Mop(\be_{\mathrm{numinous}})$ produces the "awe/wonder" profile (Table *ref:def:canonical*) at maximum intensity, with massive amplification of $I_N$ (naturalistic pattern recognition) and $I_E$ (affective processing) combined with suppression of $I_A$ (critical analysis). The subjective quality of transcendence is a consequence of this specific modulation pattern.

**Structural (Tier B).** The numinous is the phenomenology of the CS operator detecting its own geometry. The self-intersecting manifold $\Cspace$ (Part IV) has regions of extreme curvature --- and the experience of those regions from the inside is the numinous. The "sense of vastness" is the mind registering that the CS operator is much larger than the region it normally inhabits.

**Ontological (Tier C).** If Pillar 11 is correct and consciousness is fundamental, then the numinous may be genuine contact with a deeper stratum of reality --- not hallucination but accurate perception of something the normal cognitive apparatus is not equipped to process. In this reading, the "wholly other" is *actually* other, and the awe response is appropriate.

The framework does not choose between these. It classifies the reductive explanation as actionable, the structural explanation as mathematically interesting, and the ontological explanation as philosophically serious but currently beyond empirical reach.

%═══════════════════════════════════════════════════════════════════════════════
%  SECTION 9: HORMONAL INTELLIGENCE
%═══════════════════════════════════════════════════════════════════════════════

## Hormonal Intelligence: The Slow Channel

### The Endocrine Modulation Layer

!!! definition "Hormonal State Vector"
 \tB

The *hormonal state vector* is $\bh(t) \in \R^m_{\geq 0}$ with components representing circulating levels of cognitively active hormones:
\begin{center}

*[Table — see PDF]*

\end{center}

!!! definition "Hormonal Modulation Layer"
 \tB

The *hormonal modulation layer* is an operator $\mathcal{H}: \R^m \to \R^{8 \times 8}_{\geq 0}$ that acts on the intelligence vector at a slower timescale than emotional modulation:
\begin{keythm}

\[
\bI_{\mathrm{hormonal}}(t) = \mathcal{H}(\bh(t)) \cdot \bI

\]

\end{keythm}
The key distinction from affective modulation $\Mop$: the hormonal layer operates on timescales of minutes to years, and it modifies not just the effective intelligence but the *compatibility tensor itself*.

\begin{keythm}

!!! theorem "Hormonal Tensor Modification"
 \tB

The hormonal state vector $\bh(t)$ modifies the compatibility tensor:

\[
K_{st}^{\mathrm{eff}}(t) = K_{st} + \sum_{\ell} \frac{\partial K_{st}}{\partial h_\ell}\, \Delta h_\ell(t)

\]

to first order in hormonal deviation $\Delta h_\ell = h_\ell(t) - h_\ell^{(\mathrm{baseline})}$. The hormonal system does not merely scale intelligence types --- it changes *how the types interact with each other*.

\end{keythm}

\begin{interpretation}
This is a profound result. Emotional modulation changes the volume knobs ($\Mop$ scales the diagonal). Hormonal modulation changes the *wiring diagram* ($K$ governs the cross-type interactions). Puberty doesn't just make you stronger or more emotional --- it rewires which intelligence types synergize and which interfere. Pregnancy alters the compatibility tensor to enhance social--kinesthetic synergy and naturalistic threat detection. Menopause shifts the tensor again. The hormonal system is programming the cognitive architecture at a level deeper than attention or emotion.
\end{interpretation}

### Evolutionary Intelligence

!!! definition "Evolutionary Intelligence"
 \tB

*Evolutionary intelligence* is the species-level "intelligence" encoded in the genome and expressed through the hormonal system, developmental programs, and innate behavioral predispositions. It is not an intelligence type (it does not occupy a dimension in $\\mathbb{R}^{n(e)}$) but a *meta-layer* that:
[nosep]
    - Sets the baseline values of $\bI$ via genetic contribution to neural architecture
    - Designs the hormonal system $\mathcal{H}$ that modulates the intelligence vector across the lifespan
    - Programs the bypass channel $\Phi$ with species-typical emergency responses
    - Determines the robustness ordering (Remark *ref:rem:robustness*): which types shut down first under stress
    - Installs innate phobias, mate preferences, kin recognition, and other pre-programmed evaluation circuits

!!! definition "Evolutionary Timescale Hierarchy"
 \tB

The complete modulation architecture operates across six timescales:
\begin{keythm}
\begin{center}

*[Table — see PDF]*

\end{center}
\end{keythm}
Each layer modifies the layer below it. The evolutionary layer designed the developmental program that builds the hormonal system that modulates the affective architecture that gates the bypass channel. Intelligence sits inside all of these nested constraints.

\begin{deepbox}
The deepest implication: *your intelligence vector is not your own design*. It was shaped by evolutionary pressures acting on your ancestors, expressed through hormonal programs you did not choose, modulated by emotional systems you do not fully control, and deployed through an output architecture that can bypass your deliberation entirely. What we call "free will" operates in the narrow band where all these systems are quiescent --- the calm-focus regime where $\Mop \approx \Id$, $\Phi = 0$, and $\bh \approx \bh_{\mathrm{baseline}}$. The mathematics of agency is the mathematics of this band's width and stability.
\end{deepbox}

%═══════════════════════════════════════════════════════════════════════════════
%  SECTION 10: SOMATIC INTELLIGENCE
%═══════════════════════════════════════════════════════════════════════════════

## Somatic Intelligence: The Body as Computational Substrate

!!! definition "Somatic State Vector"
 \tB

The *somatic state vector* is $\bs(t) \in \R^p$ encoding the body's computational outputs:
\begin{center}

*[Table — see PDF]*

\end{center}

!!! definition "Somatic Modulation"
 \tB

The somatic state contributes to the output equation via a modulation operator $\mathcal{B}(\bs)$:
\begin{keyeqn}
\[
\bI_{\mathrm{somatic}}(t) = \mathcal{B}(\bs(t)) \cdot \bI
\]
\end{keyeqn}
Key somatic effects:
[nosep]
    - Chronic inflammation suppresses $I_A$ and $I_S$ ("brain fog" is an immune modulation event)
    - High heart rate variability amplifies all types by $\sim$5--10%
    - Gut distress suppresses $I_A$ and amplifies $I_N$ (threat detection)
    - Physical exercise temporarily amplifies $I_G$, $I_K$, and $I_E$ by 10--20%
    - Pain suppresses all types except $I_K$ (motor planning to escape the pain source)

!!! remark "Remark"

"Gut feeling" is not a metaphor. The enteric nervous system is performing genuine computation --- evaluating chemical environment, detecting pathogens, assessing nutritional content --- and reporting its conclusions to the brain as visceral sensation. When someone says "my gut tells me something is wrong," they may be reporting the output of a 500-million-neuron computational system that has detected a real anomaly.

%═══════════════════════════════════════════════════════════════════════════════
%  SECTION 11: SLEEP AS MODE-SWITCHING
%═══════════════════════════════════════════════════════════════════════════════

## Sleep Cognition: The Offline Mode

!!! definition "Sleep Intelligence Configuration"
 \tB

During sleep, the intelligence vector does not go to zero. It is *reconfigured* into an offline mode:
\begin{keyeqn}
\[
\bI_{\mathrm{sleep}}(t) = \Mop_{\mathrm{sleep}}(\phi(t)) \cdot \bI
\]
\end{keyeqn}
where $\phi(t)$ is the sleep phase (NREM stages 1--3, REM) and $\Mop_{\mathrm{sleep}}$ is the sleep-phase modulation operator:
\begin{center}

*[Table — see PDF]*

\end{center}

\begin{interpretation}
REM sleep has a distinctive intelligence profile: high $I_E$ (emotional processing), high $I_G$ (vivid spatial imagery in dreams), high $I_N$ (pattern recombination), suppressed $I_A$ (the dreaming mind does not fact-check) and suppressed $I_K$ (motor atonia prevents acting out dreams). This is a *creative recombination* mode: the intelligence vector is configured for maximal associative freedom with minimal logical constraint. This is why solutions to problems sometimes arrive during sleep --- the offline configuration explores regions of the idea manifold that the waking, $I_A$-dominated configuration would never visit.
\end{interpretation}

\begin{keythm}

!!! theorem "Sleep as Cognitive Mode-Switch"
 \tB

The sleep-wake cycle implements a periodic trajectory through modulation space:

\[
\Mop(t) = \Mop_{\mathrm{wake}}(\be(t)) \cdot \mathbb{1}_{\mathrm{wake}}(t) + \Mop_{\mathrm{sleep}}(\phi(t)) \cdot \mathbb{1}_{\mathrm{sleep}}(t)

\]

The waking mode optimizes for accuracy and action ($I_A$ and $I_K$ dominant). The sleeping mode optimizes for consolidation and recombination ($I_E$, $I_G$, $I_N$ dominant). Both modes are essential: chronic sleep deprivation degrades *waking* performance because the consolidation and recombination functions of sleep are prerequisites for optimal daytime deployment.

\end{keythm}

%═══════════════════════════════════════════════════════════════════════════════
%  SECTION 12: DEVELOPMENTAL DYNAMICS
%═══════════════════════════════════════════════════════════════════════════════

## Developmental Dynamics

!!! definition "Intelligence Trajectory"
 \tB

The *intelligence trajectory* of an agent is the time-varying function:
\begin{keyeqn}
\[
\bI(\tau): [0, T_{\mathrm{life}}] \to \\mathbb{R}^{n(e)}_{\geq 0}
\]
\end{keyeqn}
where $\tau$ is developmental time (age). This trajectory is governed by:
[nosep]
    - Genetic program (sets initial conditions and maturation schedule)
    - Hormonal milestones (puberty, pregnancy, menopause)
    - Environmental inputs (education, training, deprivation)
    - Structural deformation (trauma, illness, enrichment)
    - Aging processes (myelination, synaptic pruning, neurodegeneration)

!!! definition "Developmental Schedule"
 \tB

The eight intelligence types do not develop synchronously. Approximate developmental peaks:
\begin{center}

*[Table — see PDF]*

\end{center}

\begin{keythm}

!!! theorem "Developmental Non-Uniformity"
 \tB

The intelligence vector trajectory $\bI(\tau)$ is not a scalar curve --- aging is not uniform dimming. Formally:

\[
\frac{d\bI}{d\tau} \neq c(\tau) \cdot \bI \quad \text{for any scalar function } c

\]

The trajectory curves through the type space, with different types peaking at different ages, declining at different rates, and some types (linguistic, social, emotional) potentially *increasing* throughout life as crystallized knowledge accumulates. A 70-year-old is not a dimmer version of their 25-year-old self. They are a *different point* in $\\mathbb{R}^{n(e)}$, with a different cognitive profile, different strengths, and different vulnerabilities.

\end{keythm}

\begin{interpretation}
The fluid-crystallized distinction (Cattell, 1963) maps directly onto this framework. Fluid intelligence ($I_A$, $I_G$) peaks early and declines. Crystallized intelligence ($I_L$, $I_S$, $I_E$) can increase throughout life. The tragedy of aging is not loss of intelligence but *mismatch*: society often demands fluid capacity from people whose crystallized capacity has never been higher, and discards the accumulated wisdom of types that are still growing.
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════
%  SECTION 13: TRAUMA AS STRUCTURAL DEFORMATION
%═══════════════════════════════════════════════════════════════════════════════

## Trauma as Structural Deformation

!!! definition "Structural Deformation"
 \tB

A *structural deformation* $\Delta$ is a persistent modification to the cognitive architecture caused by extreme experience. Unlike modulation (which is temporary) and development (which follows a genetic program), deformation is an *unplanned, potentially permanent alteration* to the system's parameters.

!!! definition "Trauma Deformation Operator"
 \tB

A traumatic event $\mathcal{T}$ produces a deformation operator $\Delta_{\mathcal{T}}$ that simultaneously modifies *four* system components:
\begin{keythm}

\[\begin{aligned}
\bI &\to \bI + \delta\bI_{\mathcal{T}} && \text{(base capacity shift --- usually negative)}    
K &\to K + \delta K_{\mathcal{T}} && \text{(compatibility tensor distortion)}    
\beta_{\mathrm{crit}} &\to \beta_{\mathrm{crit}} - \delta\beta_{\mathcal{T}} && \text{(bypass threshold lowered)}    
\Mop_{\mathrm{baseline}} &\to \Mop_{\mathrm{baseline}} + \delta\Mop_{\mathcal{T}} && \text{(resting modulation shifted)} 
\end{aligned}\]

\end{keythm}
All four modifications persist indefinitely unless actively reversed through therapeutic intervention.

\begin{interpretation}
PTSD is not a mood disorder. It is a *structural deformation of the cognitive architecture*:
[nosep]
    - $\delta\bI < 0$ in affected types: base capacity reduced (concentration difficulties, memory impairment)
    - $\delta K$ distorted: types that were active during trauma now interfere (a soldier for whom spatial environments trigger social withdrawal: $K_{GS}$ shifted negative)
    - $\beta_{\mathrm{crit}}$ lowered: the bypass channel fires at much lower emotional intensity (hypervigilance, startle response, flashback-triggered freeze)
    - $\Mop_{\mathrm{baseline}}$ shifted: even "at rest," the system is not neutral --- there is chronic suppression of certain types and chronic activation of threat-detection modes

Therapy (EMDR, cognitive processing therapy, somatic experiencing) works by *reversing the deformation operator*: gradually restoring $\beta_{\mathrm{crit}}$, normalizing $\Mop_{\mathrm{baseline}}$, and decoupling the distorted entries in $K$. This is slow because the deformation is structural, not merely attentional.
\end{interpretation}

\begin{keythm}

!!! theorem "Deformation Persistence"
 \tB

Structural deformations have a characteristic decay time $\tau_\Delta$ that depends on the depth of the deformation:

\[
\|\Delta(t)\| = \|\Delta(0)\| \cdot e^{-t/\tau_\Delta}

\]

Without intervention: $\tau_\Delta \to \infty$ for deep deformation (the deformation is permanent). With effective therapeutic intervention: $\tau_\Delta \sim$ months to years. The key predictor of $\tau_\Delta$ is the number of system components affected: deformations that modify only $\Mop_{\mathrm{baseline}}$ recover faster than those that modify $K$ and $\beta_{\mathrm{crit}}$ simultaneously.

\end{keythm}

!!! remark "Positive deformation"

Not all structural deformations are negative. Profound positive experiences --- deep love, transformative learning, peak experiences, initiation ordeals --- can produce *positive* deformations: increased $\beta_{\mathrm{crit}}$ (greater emotional resilience), expanded compatibility tensor entries (new synergies between types), and shifted $\Mop_{\mathrm{baseline}}$ toward the amplifying regime. Post-traumatic *growth* is a documented phenomenon (Tedeschi & Calhoun, 2004) and corresponds to $\|\delta\bI_{\mathcal{T}}\| > 0$, $\delta\beta > 0$.

%═══════════════════════════════════════════════════════════════════════════════
%  SECTION 14: THE COMPLETE DEPLOYMENT EQUATION
%═══════════════════════════════════════════════════════════════════════════════

## The Complete Deployment Equation

We now assemble all the layers into the full deployment equation promised in \S*ref:sec:central*:

\begin{keythm}

\[
\boxed{
\bO(t) = \eta(t) \cdot \Mop(\be(t)) \cdot \mathcal{H}(\bh(t)) \cdot \mathcal{B}(\bs(t)) \cdot \Mop_{\mathrm{sleep}}(\phi(t)) \cdot (\bI + \delta\bI_\Delta) \cdot (1 + \Sop(\be(t))) + \Phi(\be(t))
}

\]

\end{keythm}

Reading right to left:
[nosep]
    - $\bI + \delta\bI_\Delta$: Base intelligence, structurally deformed by accumulated experience
    - $\Mop_{\mathrm{sleep}}(\phi)$: Sleep/wake mode selection
    - $\mathcal{B}(\bs)$: Somatic modulation (body state)
    - $\mathcal{H}(\bh)$: Hormonal modulation (slow channel)
    - $\Mop(\be)$: Affective modulation (fast channel)
    - $(1 + \Sop(\be))$: Signal enhancement from emotional epistemic channel
    - $\eta(t)$: Residual intelligence coefficient (reduced when bypass is active)
    - $\Phi(\be)$: Bypass channel (additive, can preempt everything above)

The compatibility tensor governing synergy is itself modulated:

\[
K^{\mathrm{eff}}(t) = K + \delta K_\Delta + \frac{\partial K}{\partial \bh} \cdot \Delta\bh(t)

\]

And the bypass threshold is:

\[
\beta_{\mathrm{crit}}^{\mathrm{eff}}(t) = \beta_{\mathrm{crit}} - \delta\beta_\Delta + f(\text{training, fatigue, hormonal state})

\]

\begin{interpretation}
Equation (*ref:eq:complete*) is the answer to the question: "Why do smart people do stupid things?" The intelligence vector $\bI$ may be large. But between $\bI$ and $\bO$ stand five modulation layers, a bypass channel, and the accumulated deformations of a lifetime. The effective intelligence that actually gets deployed can be drastically different from the capacity that exists. Understanding this gap --- and knowing which layers are responsible for the gap in any given moment --- is the beginning of wisdom.
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════
%  SECTION 15: COLLECTED RESULTS
%═══════════════════════════════════════════════════════════════════════════════

## Collected Results

\begin{center}
\small

*[Table — see PDF]*

\end{center}

All results are Tier B: mathematically precise, empirically motivated, but requiring systematic calibration before Tier A status.

%═══════════════════════════════════════════════════════════════════════════════
%  SECTION 16: FORWARD REFERENCES
%═══════════════════════════════════════════════════════════════════════════════

## Forward References and Open Problems

### Connections to Other Parts

\begin{center}

*[Table — see PDF]*

\end{center}

### Open Problems

[nosep]
    - **Calibration of $\Mop$ profiles.** The canonical profiles (\S*ref:def:canonical*) need systematic empirical validation via combined neuroimaging and cognitive testing under induced emotional states.
    - **Off-diagonal $\Mop$ terms.** We have modeled primarily the diagonal. The off-diagonal terms (attentional reallocation: grief redirecting spatial capacity toward emotional processing) are important but harder to measure.
    - **Hormonal tensor modification.** The partial derivatives $\partial K/\partial h_\ell$ are the most empirically challenging parameters in the framework. Cross-type interaction under hormonal manipulation requires carefully designed experiments.
    - **Positive deformation taxonomy.** The theory of trauma deformation is more developed than the theory of growth deformation. What exactly changes in $K$ and $\Mop$ during post-traumatic growth, transformative learning, or spiritual awakening?
    - **The numinous.** Is the structural explanation (the CS operator curvature) testable? Can we predict when and how numinous experiences occur from the geometric properties of $\Cspace$?
    - **Somatic computation.** What is the computational capacity of the enteric nervous system and how does it interface with the intelligence types?
    - **Cross-cultural variation.** Do the canonical $\Mop$ profiles vary significantly across cultures, or is the robustness ordering universal?

\begin{center}
*Intelligence is what you can do.  
Deployment is what you actually do.  
The gap between them is not weakness.  
It is the architecture of being alive---  
an architecture built by evolution, shaped by hormones,  
modulated by emotion, informed by the body,  
deformed by experience, and reconfigured every night in sleep.  
Understanding this architecture is not a counsel of despair.  
It is the first step toward genuine agency:  
you cannot steer what you do not see.*
\end{center}