---
title: "Psychiatry Companion Paper"
version: "2.0.0"
last_updated: "2026-03-05"
status: ARXIV-READY
arxiv_category: "q-bio.NC"
---

# Psychiatry Companion Paper

**Jean-Paul Niko** · February 2026

\begin{center}
{\LARGE\bfseries\color{sectionblue} Intelligence Filters, Affective Geometry, and  [3pt]
Cognitive Thermodynamics:  [3pt]
A Mathematical Framework for Psychiatric  [3pt]
Diagnosis and Treatment Response}

{\large Jean-Paul Niko}  [4pt]
{}  [2pt]
{\small`niko@triptomean.com`}  [12pt]
{\small February 2026}
\end{center}

!!! abstract "Abstract"
    
Contemporary psychiatric diagnosis relies on categorical systems (DSM-5, ICD-11) that poorly capture the dimensional, overlapping, and dynamic nature of mental disorders. We present a mathematical framework---drawn from the "Intelligence as Geometry" (RTSG) program---that models psychiatric conditions as characteristic perturbations of a multi-dimensional cognitive architecture. Each individual carries an variable-dimensional intelligence vector (n=12 for humans) $\bI \in \\mathbb{R}^{n(e)}$ representing capacities across symbolic, spatial, linguistic, social, mnemonic, auditory, kinesthetic, and evaluative domains. Psychiatric conditions are formalized as *filter operators* $\bF$ that distort this vector in disorder-specific patterns: depression attenuates evaluative and mnemonic components while amplifying narrow symbolic loops (rumination); PTSD hyperactivates evaluative gain (hypervigilance) while distorting mnemonic temporal indexing; mania corresponds to high-velocity, high-curvature trajectories through affective space. The framework introduces *cognitive thermodynamics*---entropy, temperature, free energy, and phase transitions for mental states---providing a mathematical account of treatment resistance (deep energy basins), temporary worsening before improvement (thermodynamic necessity), and the impossibility of "removing" trauma (filter irreversibility). The compatibility matrix $\bK$ predicts treatment interaction effects and optimal sequencing. We derive 15 testable clinical hypotheses, each specified with the measurement modality (fMRI, EEG, EMA, psychometric) required for validation. The framework is dimensional, quantitative, transdiagnostic, and aligned with the Research Domain Criteria (RDoC) initiative.

% ═══════════════════════════════════════════════════════════════════════════════

## Introduction: Beyond Categorical Diagnosis

% ═══════════════════════════════════════════════════════════════════════════════

This paper presents a mathematical framework for psychiatry derived from the Intelligence as Geometry (RTSG) program. The core insight is that psychiatric conditions are not categories to be assigned but *geometric distortions* of a multi-dimensional cognitive profile that can be characterized, measured, and predicted with algebraic precision.

The limitations of categorical diagnosis are well documented. The DSM-5 treats disorders as discrete kinds, yet comorbidity rates routinely exceed 50%, suggesting that the boundaries between categories are artifacts of the classification system rather than features of the underlying pathology [caspi2014,kotov2017]. The Research Domain Criteria (RDoC) initiative [insel2010] called for dimensional approaches grounded in neuroscience, but has struggled to provide the mathematical formalism that would make "dimensional" more than a slogan.

Our framework provides exactly this formalism. We model each individual's cognitive architecture as an variable-dimensional *intelligence vector* $\bI \in \\mathbb{R}^{n(e)}$, where each component represents capacity in a distinct cognitive domain. Psychiatric conditions are then formalized as *filter operators*---linear or nonlinear maps $\bF: \\mathbb{R}^{n(e)} \to \\mathbb{R}^{n(e)}$---that distort the intelligence vector in disorder-specific patterns. This yields:

[nosep]
- **Dimensional diagnosis**: An 8D profile, not a binary label.
- **Comorbidity explained**: Disorders with overlapping filter signatures naturally co-occur---high comorbidity is *predicted* by the framework.
- **Treatment interaction**: The compatibility matrix $\bK$ predicts which treatment combinations amplify or interfere.
- **Treatment resistance**: Formalized as the depth of a free-energy basin, with quantitative implications for intervention design.
- **Trauma irreversibility**: A theorem, not a metaphor---filters compose but do not uncommit.

We develop each of these in turn, deriving 15 testable clinical hypotheses along the way. The paper is self-contained but draws on the full RTSG mathematical apparatus detailed in the master treatise [niko2026].

% ═══════════════════════════════════════════════════════════════════════════════

## The Intelligence Vector as Clinical Cognitive Profile

% ═══════════════════════════════════════════════════════════════════════════════

!!! definition "Intelligence Vector"
 \tA

An individual's cognitive profile is an variable-dimensional vector:
\begin{keyeq}
\[
\bI = (I_{\mathrm{symb}},\; I_{\mathrm{spat}},\; I_{\mathrm{ling}},\; I_{\mathrm{soc}},\; I_{\mathrm{mnem}},\; I_{\mathrm{aud}},\; I_{\mathrm{kin}},\; I_{\mathrm{eval}}) \in \\mathbb{R}^{n(e)}
\]
\end{keyeq}
Each component $I_t$ represents capacity in a cognitive type, measured in standardized units ("cogs") calibrated via pairwise ELO tournaments on type-specific tasks.

The eight types correspond to distinct but interacting cognitive systems:

\begin{center}
\small

*[Table — see PDF for formatted version]*

\end{center}

Critically, these types are not independent. They interact through the *compatibility matrix* $\bK$.

!!! definition "Compatibility Matrix"
 \tA

The symmetric matrix $\bK \in \R^{8 \times 8}$ encodes pairwise interactions between intelligence types:
\begin{keyeq}
\[
K_{st} \begin{cases}
> 1 & \text{types $s$ and $t$ amplify each other (positive coupling)}   
= 1 & \text{independent}   
< 1 & \text{types $s$ and $t$ interfere (inhibitory coupling)}
\end{cases}
\]
\end{keyeq}
The diagonal entries $K_{tt} = 1$. Off-diagonal entries are estimated from cognitive training transfer studies, neuroimaging functional connectivity, and psychometric cross-loadings.

\begin{intuition}
The $\bK$ matrix is to cognitive types what functional connectivity is to brain regions. When $K_{\mathrm{soc}, \mathrm{eval}} = 1.3$, improving social cognition tends to amplify evaluative processing---social support genuinely helps depressed patients evaluate their situation more accurately. When $K_{\mathrm{symb}, \mathrm{soc}} = 0.6$, intense symbolic processing inhibits social cognition---the ruminative patient who "can't stop thinking" also "can't connect."
\end{intuition}

For clinical purposes, a patient's profile is not the raw vector $\bI_{\mathrm{raw}}$ but the *effective* vector after all filters have been applied: $\bI_{\mathrm{eff}} = \bF(\bI_{\mathrm{raw}})$. The filter formalism makes this precise.

% ═══════════════════════════════════════════════════════════════════════════════

## Filter Operators: A Mathematical Language for Psychopathology

% ═══════════════════════════════════════════════════════════════════════════════

The central claim of this paper is that every psychiatric condition can be characterized by a *filter signature*---a specific pattern of attenuation, amplification, and distortion applied to the intelligence vector.

!!! definition "Cognitive Filter"
 \tA

A cognitive filter is a map $\bF: \\mathbb{R}^{n(e)} \to \\mathbb{R}^{n(e)}$ that transforms the intelligence vector. In the linear regime, $\bF$ is an $8 \times 8$ matrix:
\begin{keyeq}
\[
\bI_{\mathrm{eff}} = \bF \cdot \bI_{\mathrm{raw}}, \qquad F_{st} \in [0, \infty)
\]
\end{keyeq}
A diagonal filter $\bF = \diag(f_1, \ldots, f_8)$ attenuates ($f_t < 1$) or amplifies ($f_t > 1$) each type independently. Off-diagonal entries model cross-type distortion.

The RTSG framework identifies five species of filter, operating at different timescales:

\begin{center}
\small

*[Table — see PDF for formatted version]*

\end{center}

!!! theorem "Filter Composition"
 \tA

Filters compose by matrix multiplication:
\begin{keyeq}
\[
\bI_{\mathrm{eff}} = F_{\mathrm{attn}} \circ \Fstate \circ \Fcult \circ \Fdev \circ \Fceil(\bI_{\mathrm{raw}})
\]
\end{keyeq}
The composition is generally non-commutative: the order in which filters are applied matters. In particular, $\Fdev \circ \Fceil \neq \Fceil \circ \Fdev$ whenever developmental experience interacts with substrate constraints.

!!! theorem "Filter Irreversibility"
 \tA

For any lossy filter $\bF$ (i.e., $\det(\bF) < 1$), there exists no inverse filter $\bF^{-1}$ such that $\bF^{-1} \circ \bF = \mathrm{Id}$ on the full type space. Information destroyed by a filter cannot be recovered.

This is the mathematical statement of a clinical reality: you cannot "un-trauma" a brain. Trauma therapy does not remove the traumatic filter---it adds compensatory filters that partially restore the effective intelligence vector through a different pathway. The composition $\bF_{\mathrm{therapy}} \circ \bF_{\mathrm{trauma}}$ can approximate normative function, but the underlying trajectory through filter space is permanently altered.

\begin{clinical}
Filter irreversibility explains why trauma-informed care emphasizes *coping* and *integration* rather than *erasure*. Van der Kolk's observation that "the body keeps the score" [vanderkolk2014] is a clinical description of an algebraic fact: the developmental filter $\Fdev$ applied during critical periods compresses the intelligence vector in ways that no subsequent state filter can fully invert.
\end{clinical}

% ═══════════════════════════════════════════════════════════════════════════════

## Disorder Filter Signatures

% ═══════════════════════════════════════════════════════════════════════════════

Each psychiatric condition corresponds to a characteristic filter signature---a specific pattern of attenuations, amplifications, and cross-type distortions. We present six canonical signatures, each derived from the RTSG filter formalism and mapped to clinical phenomenology.

### Major Depressive Disorder

!!! definition "Depression Filter"
 \tB

The depressive state filter $\Fstate^{\mathrm{dep}}$ is characterized by:
\begin{keyeq}

\[\begin{aligned}
f_{\mathrm{eval}} &\approx 0.3 \quad \text{(severe attenuation: anhedonia)}    
f_{\mathrm{mnem}} &\approx 0.5 \quad \text{(memory consolidation impaired)}    
f_{\mathrm{soc}} &\approx 0.4 \quad \text{(social withdrawal)}    
f_{\mathrm{symb}} &\approx 1.4 \text{ (narrow band)} \quad \text{(rumination)}    
f_{\mathrm{kin}} &\approx 0.5 \quad \text{(psychomotor retardation)} 
\end{aligned}\]

\end{keyeq}
The amplification of $I_{\mathrm{symb}}$ is *narrow-band*: it enhances repetitive symbolic loops while suppressing novel symbolic exploration. Formally, $f_{\mathrm{symb}}$ acts as a high-gain, low-bandwidth filter---amplifying a small subspace of symbolic processing (self-referential negative cognition) while attenuating the rest.

\begin{intuition}
Anhedonia *is* the attenuated evaluative system: the patient's $I_{\mathrm{eval}}$ can no longer assign positive value to experiences, food, relationships, or future plans. Rumination *is* the amplified narrow symbolic loop: without evaluative termination ($K_{\mathrm{eval},\mathrm{symb}}$ normally provides a "stop signal" when symbolic processing reaches a conclusion), the symbolic system cycles without resolution.
\end{intuition}

\begin{prediction}
If depression attenuates $I_{\mathrm{eval}}$ specifically, then depressed patients should show preserved performance on purely spatial or purely linguistic tasks but impaired performance on tasks requiring evaluative judgment (aesthetic discrimination, reward learning, cost-benefit analysis). Measurement: cognitive task battery with type-specific subtests, comparing depressed vs.\ matched controls. Effect size prediction: $d \geq 0.8$ for evaluative tasks, $d < 0.3$ for spatial/linguistic tasks.
\end{prediction}

### Post-Traumatic Stress Disorder

!!! definition "PTSD Filter"
 \tB

The trauma filter $\Ftrauma^{\mathrm{PTSD}}$ combines a state filter with a permanent developmental modification:
\begin{keyeq}

\[\begin{aligned}
f_{\mathrm{eval}} &\approx 2.5 \quad \text{(hypervigilance: evaluative gain at maximum)}   
f_{\mathrm{soc}} &\approx 0.3 \quad \text{(trust withdrawal, social isolation)}   
f_{\mathrm{mnem}} &: \text{distorted temporal indexing (intrusive memories)}   
f_{\mathrm{kin}} &\approx 1.5 \quad \text{(startle response, motor hyperactivation)}
\end{aligned}\]

\end{keyeq}
The mnemonic distortion is *not* a simple attenuation. Rather, the trauma filter introduces off-diagonal coupling: $F_{\mathrm{mnem},\mathrm{eval}} \gg 0$, meaning that mnemonic retrieval becomes yoked to evaluative threat assessment. Memories are retrieved not by temporal context but by threat-relevance.

\begin{clinical}
The off-diagonal term $F_{\mathrm{mnem},\mathrm{eval}}$ formalizes the clinical observation that PTSD flashbacks are *triggered* by threat-relevant cues rather than recalled voluntarily. The memory system has been rewired to serve the hyperactivated evaluative system. EMDR and prolonged exposure therapy work by gradually decoupling mnemonic retrieval from evaluative threat assessment---mathematically, reducing $F_{\mathrm{mnem},\mathrm{eval}}$ back toward zero, which does not require inverting the original trauma filter but rather applying a compensatory off-diagonal correction.
\end{clinical}

### Bipolar Disorder: Mania

!!! definition "Manic Trajectory"
 \tB

Mania is not a static filter but a *trajectory* through the psychophysiological state space $\bPsi(t)$ characterized by:
\begin{keyeq}

\[\begin{aligned}
\|\dot{\bPsi}\| &\gg \|\dot{\bPsi}_{\mathrm{norm}}\| \quad \text{(high velocity: rapid cycling)}   
\kappa(\bPsi) &\gg \kappa_{\mathrm{norm}} \quad \text{(high curvature: instability)}   
r_{\mathrm{basin}} &\gg r_{\mathrm{norm}} \quad \text{(large attractor basin: expansive state)}
\end{aligned}\]

\end{keyeq}
where $\kappa$ denotes the curvature of the trajectory through PAD affective space and $r_{\mathrm{basin}}$ is the radius of the attractor basin around the current state.

\begin{intuition}
The manic patient occupies a large basin of attraction---many states feel compatible and reinforcing---but the trajectory through this basin is fast and unstable. The high curvature means rapid, unpredictable direction changes: the patient is euphoric, then irritable, then grandiose, with transitions that are too fast for social or institutional systems to track. The large basin means the patient feels "everything connects"---which is sometimes true (genuine creative insight during hypomania) and sometimes catastrophically false (psychotic mania).
\end{intuition}

The filter signature during mania includes:

\[\begin{aligned}
f_{\mathrm{eval}} &\approx 2.0 \quad \text{(inflated positive valuation: grandiosity)}   
f_{\mathrm{symb}} &\approx 1.8 \quad \text{(pressured thought, flight of ideas)}   
f_{\mathrm{soc}} &\approx 1.5 \quad \text{(disinhibition, hypersociality)}   
f_{\mathrm{kin}} &\approx 1.6 \quad \text{(psychomotor activation, decreased sleep need)}
\end{aligned}\]

\begin{prediction}
If mania is characterized by high trajectory velocity in PAD space, then ecological momentary assessment (EMA) data from manic patients should show significantly higher variance in affect ratings across short time intervals (hours) compared to euthymic periods and healthy controls. Measurement: smartphone-based EMA with 4-hourly mood sampling. Prediction: $\mathrm{Var}(\Delta \be / \Delta t)_{\mathrm{manic}} > 3 \times \mathrm{Var}(\Delta \be / \Delta t)_{\mathrm{euthymic}}$.
\end{prediction}

### Obsessive-Compulsive Disorder

!!! definition "OCD Filter"
 \tB

The OCD filter is characterized by a tight symbolic loop with failed evaluative termination:
\begin{keyeq}

\[\begin{aligned}
f_{\mathrm{symb}} &\approx 2.0 \quad \text{(symbolic hyperactivation in narrow band)}   
K_{\mathrm{eval},\mathrm{symb}} &\to 0 \quad \text{(evaluative termination signal broken)}   
f_{\mathrm{kin}} &: \text{compulsive motor output (behavioral compulsions)}
\end{aligned}\]

\end{keyeq}
The distinguishing feature from depression is that the OCD loop is *anxiogenic* (driven by threat-evaluation) rather than *ruminative* (driven by self-referential negative cognition). The evaluative component is not attenuated but *disconnected*---$K_{\mathrm{eval},\mathrm{symb}}$ drops, meaning evaluative judgment cannot terminate the symbolic loop even though $I_{\mathrm{eval}}$ itself remains functional.

\begin{prediction}
If $K_{\mathrm{soc},\mathrm{symb}} = 0.6$ in OCD patients (as the framework predicts), then group therapy for OCD may *interfere* with symbolic rumination reduction rather than help---the social component activates a channel that has inhibitory coupling with the overactive symbolic system. Prediction: group CBT for OCD should show smaller effect sizes than individual CBT, specifically because the social component introduces noise into the symbolic processing channel. This is testable via a randomized comparison with process measures tracking both social engagement and obsessive thought frequency during sessions.
\end{prediction}

### ADHD

!!! definition "ADHD Filter"
 \tB

ADHD is characterized by a hypervisor spectral shift---too many eigenvalues above the attention threshold:
\begin{keyeq}

\[\begin{aligned}
&\text{Let } \lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_8 \text{ be eigenvalues of the attention operator.}   
&\text{Normative: } \lambda_1 \gg \lambda_2 > \cdots > \lambda_8 \approx 0 \quad \text{(dominant focus)}   
&\text{ADHD: } \lambda_1 \approx \lambda_2 \approx \lambda_3 \approx \cdots \quad \text{(flat spectrum)}
\end{aligned}\]

\end{keyeq}
A flat eigenvalue spectrum means that many cognitive types simultaneously compete for conscious presentation. Nothing achieves clear dominance in the attention simplex, producing the phenomenology of distractibility, rapid topic-switching, and difficulty sustaining single-type focus.

\begin{intuition}
The normative attention system has a sharp spectral gap: one or two eigenvalues dominate, producing clear focus. The ADHD system has a flat spectrum: everything is equally "interesting," meaning nothing can be selectively prioritized. Stimulant medication (methylphenidate, amphetamine) works by *sharpening the spectral gap*---increasing the dominant eigenvalue relative to the rest, not by adding focus but by suppressing the competitors.
\end{intuition}

\begin{prediction}
If ADHD corresponds to a flat eigenvalue spectrum, then EEG spectral analysis during sustained attention tasks should show reduced alpha-band suppression (alpha indexes the dominant eigenvalue) and elevated theta/beta ratios (reflecting competition among multiple channels). This is already partially confirmed by existing EEG-ADHD literature [arns2013], but the framework makes the sharper prediction that the *number* of competing eigenvalues above threshold $\delta$ correlates with ADHD severity: $|\{k : \lambda_k > \delta\}| \propto \text{ADHD severity}$.
\end{prediction}

### Autism Spectrum

!!! definition "Autism Filter"
 \tB

Autism involves a developmental filter $\Fdev^{\mathrm{ASD}}$ that reshapes the $\bK$ matrix:
\begin{keyeq}

\[\begin{aligned}
K_{\mathrm{soc},*} &\quad \text{attenuated across the board}   
K_{\mathrm{symb},\mathrm{spat}} &\quad \text{amplified (systemizing over empathizing)}
\end{aligned}\]

\end{keyeq}
This is not a deficit model: the autistic $\bK$ matrix produces *different* synergy patterns. The reduced social coupling means that social information provides less amplification to other types, while the enhanced symbolic-spatial coupling produces the characteristic strengths in pattern recognition, systematization, and detail-oriented processing [baron-cohen2009].

\begin{clinical}
The filter model reframes autism as a different $\bK$ configuration rather than a deficit in a single domain. This aligns with the neurodiversity perspective: the autistic individual has a different coupling structure that produces both characteristic challenges (reduced social amplification) and characteristic strengths (enhanced systematic-spatial synergy). Interventions should be evaluated by whether they expand the individual's effective capability profile rather than forcing normative $\bK$ values.
\end{clinical}

% ═══════════════════════════════════════════════════════════════════════════════

## The Affective Geometry of Mental States

% ═══════════════════════════════════════════════════════════════════════════════

Beyond the intelligence vector, each individual occupies a position in *affective space*---a geometric model of emotional state that is richer and more clinically informative than single-scale measures like the PHQ-9 or GAD-7.

!!! definition "Emotional State Vector"
 \tB

The emotional state at time $t$ is a vector $\be(t) \in \R^3$ in the PAD space of Mehrabian and Russell [mehrabian1974]:
\begin{keyeq}
\[
\be(t) = \bigl(v(t),\; a(t),\; d(t)\bigr)
\]
\end{keyeq}
where $v \in [-1,1]$ is valence (pleasure/displeasure), $a \in [0,1]$ is arousal (activation intensity), and $d \in [-1,1]$ is dominance (sense of control). The norm $\|\be\| = \sqrt{v^2 + a^2 + d^2}$ measures emotional intensity.

!!! definition "Psychophysiological State"
 \tB

The full psychophysiological state combines the intelligence vector with the emotional state:
\begin{keyeq}
\[
\bPsi(t) = \bigl(\bI_{\mathrm{eff}}(t),\; \be(t)\bigr) \in \R^{11}
\]
\end{keyeq}
A psychiatric trajectory is a curve $\bPsi: [0,T] \to \R^{11}$ through this combined space.

This geometric framing yields several clinical constructs:

[nosep]
- **Velocity** $\|\dot{\bPsi}\|$: Rate of state change. High in mania, low in depression.
- **Curvature** $\kappa$: Trajectory unpredictability. High in rapid cycling, low in stable states.
- **Basin depth**: The energy barrier that must be overcome to exit the current state. Deep basins correspond to treatment-resistant states.
- **Basin radius**: The range of perturbations the state can absorb without transitioning. Large in mania (expansive), small in anxiety (brittle).

\begin{prediction}
Ecological momentary assessment via smartphone apps can measure $\be(t)$ at high temporal resolution (hourly self-reports on valence, arousal, and dominance). The derived trajectory metrics---velocity $\|\dot{\be}\|$, curvature $\kappa$, and variability $\mathrm{Var}(\be)$---should discriminate between diagnostic categories with higher sensitivity than cross-sectional symptom scales. Specifically: velocity discriminates mania from depression ($p < 0.001$), curvature discriminates rapid cycling from stable bipolar ($p < 0.01$), and basin depth (estimated from state transition frequencies) discriminates treatment-resistant from treatment-responsive depression ($p < 0.01$).
\end{prediction}

% ═══════════════════════════════════════════════════════════════════════════════

## Affective Modulation of Cognitive Performance

% ═══════════════════════════════════════════════════════════════════════════════

Emotion does not merely accompany cognition---it modulates the effective intelligence vector. The *affective modulation operator* formalizes how emotional state alters cognitive performance.

!!! definition "Affective Modulation Operator"
 \tB

The modulation operator $M(\be): \\mathbb{R}^{n(e)} \to \\mathbb{R}^{n(e)}$ transforms the intelligence vector as a function of emotional state:
\begin{keyeq}
\[
\bI_{\mathrm{modulated}} = M(\be) \cdot \bI_{\mathrm{eff}}
\]
\end{keyeq}
In the linear regime, $M(\be) = \mathrm{Id} + \sum_{j} e_j \cdot \bG_j$, where $\bG_j$ are gain matrices for each PAD dimension and $e_j \in \{v, a, d\}$.

The modulation produces three clinically significant regimes:

[nosep]
- **Facilitation** ($M_{tt} > 1$): Moderate arousal enhances performance on the relevant type. The Yerkes--Dodson law is a consequence: $M_{tt}(a)$ is an inverted-U function of arousal.

- **Disruption** ($M_{tt} < 1$): Extreme emotional states (high arousal with low dominance, i.e., panic) attenuate cognitive function across all types except evaluative threat detection. This is the phenomenology of anxiety: $I_{\mathrm{eval}}$ is amplified while everything else is suppressed.

- **Dominance asymmetry**: Low dominance ($d < 0$) selectively attenuates $I_{\mathrm{ling}}$ and $I_{\mathrm{soc}}$ (the "can't speak" and "can't connect" effects of feeling powerless), while high dominance amplifies $I_{\mathrm{eval}}$ and $I_{\mathrm{symb}}$ (the "decisive clarity" of agency).

\begin{clinical}
The dominance asymmetry has immediate implications for clinical practice. A patient who feels powerless ($d \ll 0$) has a modulated intelligence vector with suppressed social and linguistic components---precisely the components required for therapeutic conversation. Effective therapy must first address the dominance deficit before the patient has the cognitive resources to engage with verbal, insight-oriented treatment. This provides mathematical justification for approaches that prioritize agency restoration (behavioral activation, graded exposure, motivational interviewing) before insight-oriented work.
\end{clinical}

% ═══════════════════════════════════════════════════════════════════════════════

## Cognitive Thermodynamics of Mental Illness

% ═══════════════════════════════════════════════════════════════════════════════

The RTSG framework introduces thermodynamic concepts---entropy, temperature, free energy, and phase transitions---to the clinical domain, providing a mathematical account of treatment dynamics.

### Cognitive Temperature and Entropy

!!! definition "Cognitive Temperature"
 \tA

The cognitive temperature $\Tcog \geq 0$ is the variance of attention fluctuations around equilibrium:
\begin{keyeq}
\[
\Tcog = \frac{1}{n-1}\sum_{t=1}^{n} \lambda_t^*\, \bigl\langle(\delta\lambda_t)^2\bigr\rangle
\]
\end{keyeq}
where $\lambda^*$ is the equilibrium attention allocation and $\delta\lambda_t = \lambda_t - \lambda_t^*$.

Clinical interpretation: At $\Tcog \approx 0$, the patient is locked into a rigid attentional pattern (obsessive focus, catatonia, perseveration). At high $\Tcog$, attention wanders without structure (delirium, manic distractibility, dissociation). Healthy function operates in a moderate range where the system can both sustain focus and flexibly redirect.

### Cognitive Free Energy and Treatment Landscapes

!!! definition "Cognitive Free Energy"
 \tB

The cognitive free energy combines internal energy with entropic cost:
\begin{keyeq}
\[
\Fcog = U_{\mathrm{cog}} - \Tcog \cdot S_{\mathrm{cog}}
\]
\end{keyeq}
where $U_{\mathrm{cog}}$ is the cognitive energy (cost of maintaining the current allocation) and $S_{\mathrm{cog}} = -\sum_t \lambda_t \ln \lambda_t$ is the attention entropy.

Mental states correspond to *minima* of the free energy landscape $\Fcog(\lambda)$. This yields a powerful clinical vocabulary:

[nosep]
- A **stable disorder** (chronic depression, persistent OCD) is a *deep local minimum*---the free energy basin is deep enough that the system cannot escape via thermal fluctuations alone.
- **Treatment resistance** = basin depth exceeds available activation energy. The deeper the basin, the more intensive the intervention required to escape it.
- **Relapse** = the system falls back into its original basin after insufficient perturbation. The disorder basin still exists; treatment must either fill it in (structural change) or move the system far enough away that the basin is no longer the closest minimum.
- **Temporary worsening** before improvement is a thermodynamic necessity: escaping a deep basin requires climbing the energy barrier, which *transiently increases* $\Fcog$. The well-documented clinical observation of initial symptom worsening during treatment (e.g., increased anxiety during exposure therapy, activation syndrome with SSRIs) has a mathematical explanation.

!!! theorem "Second Law of Cognitive Thermodynamics"
 \tB

For an isolated cognitive system, the attention entropy $S_{\mathrm{cog}}$ does not decrease over time:
\[
\frac{dS_{\mathrm{cog}}}{dt} \geq 0
\]
Applied to treatment: any intervention that *reduces* entropy (increases order, focuses attention) requires energy input from outside the system---therapeutic effort, pharmacological modulation, environmental structuring, or social support.

\begin{clinical}
The Second Law explains why "just try harder" fails as psychiatric advice. Reducing cognitive entropy (achieving focused, purposeful thought) requires energy input from an external source. For a depressed patient whose internal energy is depleted ($U_{\mathrm{cog}} \approx 0$, corresponding to psychomotor retardation and anergia), the only path to lower entropy is external energy: medication that raises $U_{\mathrm{cog}}$, behavioral activation that provides structured external demands, or social support that functions as an external organizing force.
\end{clinical}

### Phase Transitions

!!! definition "Cognitive Phase Transition"
 \tB

A phase transition occurs when continuous variation of a control parameter (medication dose, stress level, sleep deprivation) causes a discontinuous change in the equilibrium attention allocation $\lambda^*$:
\begin{keyeq}
\[
\exists\, \theta_c : \quad \lim_{\theta \to \theta_c^-} \lambda^*(\theta) \neq \lim_{\theta \to \theta_c^+} \lambda^*(\theta)
\]
\end{keyeq}

\begin{intuition}
Psychotic breaks, manic episodes, panic attacks, and dissociative switches are all phase transitions: continuous stress produces a sudden, discontinuous shift in the cognitive state. The framework predicts that these transitions exhibit the hallmarks of physical phase transitions---critical slowing down (increased response time to perturbations near the threshold), increased fluctuations (mood instability preceding a manic episode), and hysteresis (the stress level needed to trigger the transition differs from the level needed to reverse it, which is why manic episodes resolve at a lower stress threshold than the one that triggered them).
\end{intuition}

\begin{prediction}
If manic episodes are cognitive phase transitions, then the pre-manic period should show critical slowing down---measurable as increased autocorrelation in EMA mood ratings and decreased response to perturbations. This is an early-warning signal that is detectable *before* the episode manifests clinically. Measurement: time-series analysis of smartphone EMA data in bipolar patients. Prediction: autocorrelation of mood ratings increases by $>50%$ in the 72 hours preceding manic onset compared to stable baseline periods.
\end{prediction}

% ═══════════════════════════════════════════════════════════════════════════════

## Treatment Interaction and Sequencing via the $\bK$ Matrix

% ═══════════════════════════════════════════════════════════════════════════════

The compatibility matrix $\bK$ does not merely describe cognitive type interactions---it predicts which treatment combinations will amplify or interfere with each other.

!!! proposition "Treatment Interaction Prediction"
 \tB

Let treatment $A$ target intelligence type $s$ and treatment $B$ target type $t$. If $K_{st} > 1$, the treatments are *synergistic*: applying both produces greater improvement than the sum of individual effects. If $K_{st} < 1$, the treatments *interfere*: the combination is subadditive.

This generates specific, testable predictions for treatment combinations:

\begin{center}
\small

*[Table — see PDF for formatted version]*

\end{center}

\begin{prediction}
If each compound has a characteristic filter signature, then cognitive testing under controlled pharmacological conditions should reveal type-specific performance changes matching the predicted signature. For example: caffeine should improve performance on tasks requiring sustained single-type focus (reduced $\Tcog$) but not on tasks requiring flexible multi-type integration (which benefit from moderate $\Tcog$). This is testable via a double-blind caffeine/placebo crossover study with a battery of type-specific cognitive tasks.
\end{prediction}

% ═══════════════════════════════════════════════════════════════════════════════

## Comorbidity as Filter Overlap

% ═══════════════════════════════════════════════════════════════════════════════

The filter framework provides a natural explanation for the high rates of psychiatric comorbidity that embarrass categorical systems.

!!! proposition "Comorbidity Prediction"
 \tB

Two disorders $D_1$ and $D_2$ with filter signatures $\bF_1$ and $\bF_2$ will show high comorbidity if and only if their filter signatures share common components:
\begin{keyeq}
\[
\text{Comorbidity}(D_1, D_2) \propto \frac{\|\bF_1 \circ \bF_2 - \bF_1\| + \|\bF_1 \circ \bF_2 - \bF_2\|}{\|\bF_1 - \mathrm{Id}\| + \|\bF_2 - \mathrm{Id}\|}
\]
\end{keyeq}
When $\bF_1$ and $\bF_2$ perturb overlapping components, the composition $\bF_1 \circ \bF_2$ is close to both individual filters---each disorder "prepares the ground" for the other.

Examples:
[nosep]
- **Depression + Anxiety**: Both attenuate $I_{\mathrm{eval}}$ (depression: attenuation of positive evaluation; anxiety: amplification of threat evaluation). The shared evaluative perturbation means each condition exacerbates the other.
- **PTSD + Depression**: Trauma filter attenuates $I_{\mathrm{soc}}$ and distorts $I_{\mathrm{mnem}}$; depression filter attenuates $I_{\mathrm{eval}}$ and $I_{\mathrm{mnem}}$. The shared mnemonic distortion is the comorbidity mechanism.
- **ADHD + Anxiety**: ADHD flattens the eigenvalue spectrum; anxiety amplifies $I_{\mathrm{eval}}$. These are *orthogonal* perturbations---the comorbidity rate should be lower than depression-anxiety. This is consistent with epidemiological data.

\begin{intuition}
Caspi et al. [caspi2014] proposed a general psychopathology factor (the "$p$ factor") underlying all mental disorders. In our framework, the $p$ factor is the *norm* of the total filter perturbation: $\|p\| = \|\bF_{\mathrm{total}} - \mathrm{Id}\|$. A large $p$ means the total filter is far from identity---the individual is heavily filtered, making multiple disorder diagnoses likely. But the $p$ factor is a scalar shadow of a matrix: two individuals with identical $\|p\|$ can have completely different disorder profiles depending on *which* filter components are perturbed.
\end{intuition}

% ═══════════════════════════════════════════════════════════════════════════════

## Connection to Existing Frameworks

% ═══════════════════════════════════════════════════════════════════════════════

The RTSG psychiatric framework connects to several major research programs:

**Research Domain Criteria (RDoC).** The RDoC initiative [insel2010] proposed dimensional, biologically grounded constructs to replace categorical diagnosis. Our eight intelligence types map onto RDoC domains: $I_{\mathrm{eval}}$ corresponds to Positive and Negative Valence Systems, $I_{\mathrm{soc}}$ to Systems for Social Processes, $I_{\mathrm{mnem}}$ to Cognitive Systems (memory), and the attention simplex to Arousal/Regulatory Systems. The framework adds what RDoC lacks: algebraic structure (the $\bK$ matrix) and dynamic formalism (cognitive thermodynamics).

**HiTOP.** The Hierarchical Taxonomy of Psychopathology [kotov2017] organizes psychopathology dimensionally into spectra and subfactors. The filter formalism provides a generative model: each HiTOP spectrum corresponds to a principal component of the filter perturbation matrix $\bF - \mathrm{Id}$. The Internalizing spectrum reflects evaluative-mnemonic filter perturbations; the Externalizing spectrum reflects evaluative-kinesthetic perturbations with disinhibition.

**Network Theory.** Borsboom's network approach [borsboom2017] models disorders as self-reinforcing symptom networks. The $\bK$ matrix is the formal counterpart: it specifies the coupling strengths between cognitive dimensions. Symptoms in Borsboom's networks correspond to attenuated or amplified intelligence types, and the self-reinforcing loops correspond to positive-feedback cycles in the filter composition (e.g., $I_{\mathrm{eval}} \downarrow \to I_{\mathrm{soc}} \downarrow$ via $K_{\mathrm{eval},\mathrm{soc}} > 1 \to I_{\mathrm{eval}} \downarrow$ further via social isolation removing evaluative support).

**Computational Psychiatry.** Friston's free energy principle [friston2014] models psychopathology as aberrant predictive processing. Our cognitive free energy $\Fcog$ is structurally analogous but operates on the intelligence vector rather than sensory prediction. The frameworks are compatible: $\Fcog$ governs the macro-level attention landscape, while Friston's variational free energy governs micro-level perceptual inference.

**Constructed Emotion Theory.** Barrett's theory [barrett2017] that emotions are constructed from interoceptive predictions is compatible with our affective modulation operator. The PAD emotional state vector $\be(t)$ is the low-dimensional summary of Barrett's interoceptive prediction state, and the modulation operator $M(\be)$ formalizes how this constructed emotional state alters cognitive performance.

% ═══════════════════════════════════════════════════════════════════════════════

## Summary of Testable Predictions

% ═══════════════════════════════════════════════════════════════════════════════

We collect the testable predictions distributed throughout the paper:

\begin{center}
\small
\begin{tabularx}{\textwidth}{@{}clXl@{}}
\toprule
**#** & **Disorder** & **Prediction** & **Method**   
\midrule
1 & MDD & Preserved spatial/linguistic but impaired evaluative task performance & Cognitive battery   
2 & MDD & Rumination frequency correlates with $f_{\mathrm{symb}} / f_{\mathrm{eval}}$ ratio & RRS + cognitive tasks   
3 & Mania & EMA affect velocity $>3\times$ euthymic baseline & Smartphone EMA   
4 & Mania & Critical slowing down 72h before onset & EMA autocorrelation   
5 & OCD & Group CBT $<$ individual CBT (social interference) & RCT comparison   
6 & OCD & Symbolic hyperactivation localizes to narrow frequency band & fMRI   
7 & ADHD & Eigenvalue count above threshold $\propto$ severity & EEG spectral   
8 & ADHD & Stimulants sharpen spectral gap (increased $\lambda_1/\lambda_2$) & EEG pre/post   
9 & ASD & Enhanced $K_{\mathrm{symb},\mathrm{spat}}$ but reduced $K_{\mathrm{soc},*}$ & Cognitive transfer tasks   
10 & PTSD & Mnemonic-evaluative coupling $F_{\mathrm{mnem},\mathrm{eval}}$ elevated & Memory retrieval + threat cue paradigm   
11 & General & Music therapy synergistic with CBT ($K_{\mathrm{aud},\mathrm{eval}} > 1$) & Adjunctive RCT   
12 & General & Treatment sequence effects match $\bK$ predictions & Sequential RCT   
13 & General & Phase transition early-warning signals precede episodes & EMA time-series   
14 & General & Caffeine improves focused but not flexible cognition & Crossover trial   
15 & General & Comorbidity rates $\propto$ filter overlap & Epidemiological data   
\bottomrule
\end{tabularx}
\end{center}

% ═══════════════════════════════════════════════════════════════════════════════

## Limitations and Scope

% ═══════════════════════════════════════════════════════════════════════════════

This framework is a *research tool*, not a diagnostic instrument. Several important limitations must be noted:

**Parameter estimation.** The filter signatures presented here (e.g., $f_{\mathrm{eval}} \approx 0.3$ for depression) are theoretically derived estimates. Empirical calibration requires systematic cognitive profiling studies across clinical populations. The framework predicts the *pattern* of perturbation; the exact values are an open research program.

**Linearity assumption.** The filter formalism uses linear operators in first approximation. Actual psychiatric perturbations likely involve nonlinear interactions (e.g., threshold effects where $I_{\mathrm{eval}}$ below a critical value triggers a qualitatively different regime). The linear model is a tractable starting point, not a claim about the true dynamics.

**Pairwise $\bK$ matrix.** The compatibility matrix captures pairwise interactions between intelligence types. Higher-order interactions (three-way synergies or inhibitions) may be clinically significant but are not modeled in the current framework.

**Individual variation.** Different patients with the same diagnosis may have different filter signatures. The canonical signatures presented here are population-level prototypes; personalized psychiatry would estimate individual filter profiles from comprehensive cognitive assessment.

**No clinical validation yet.** The 15 predictions are empirically testable but have not yet been tested within this framework. The framework should be evaluated by its predictive success, not adopted as clinical truth before validation.

% ═══════════════════════════════════════════════════════════════════════════════

## Conclusion

% ═══════════════════════════════════════════════════════════════════════════════

We have presented a mathematical framework for psychiatry that models mental disorders as characteristic filter perturbations of a multi-dimensional cognitive architecture. The framework provides:

[nosep]
- **Dimensional diagnosis**: 8D cognitive profiles replace binary labels.
- **Filter signatures**: Each disorder is characterized by a specific pattern of attenuation, amplification, and cross-type distortion.
- **Treatment prediction**: The $\bK$ matrix predicts treatment synergies and interferences.
- **Dynamic formalism**: Cognitive thermodynamics provides a mathematical account of treatment resistance, relapse, and temporary worsening.
- **Comorbidity explanation**: High comorbidity is a prediction of overlapping filter signatures, not an embarrassment for the classification system.
- **Filter irreversibility**: The mathematical impossibility of "removing" a lossy filter provides formal foundations for trauma-informed care.

The framework is aligned with dimensional approaches (RDoC, HiTOP), compatible with computational psychiatry (Friston's free energy), and generates 15 testable predictions that can be evaluated with existing neuroimaging, psychometric, and ecological momentary assessment technologies. It offers not a finished theory but a mathematical scaffold on which a quantitative, transdiagnostic psychiatry can be built.

*This paper is a companion extraction from the master treatise "Intelligence as Geometry" (Niko, 2026). The full mathematical development, including proofs, additional applications, and the complete filter formalism, is available in the parent document.*

% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
Three-Space Psychiatry}

The three-space ontology reframes psychiatric pathology as disruptions of the instantiation process or the filter cascade.

**Id filter dysregulation.**  PTSD represents chronic Id filter activation: the pre-filter remains engaged long after the survival threat has passed, anchoring consciousness to a narrow band of $t_\mathbb{R}$ and suppressing $t_{\mathrm{lat}}$ navigation.  The "flashback" is a failure of the Id to release: consciousness is trapped in a past-$t_\mathbb{R}$ moment, unable to navigate laterally.  Treatment targets Id recalibration.

**Psychosis as filter cascade inversion.**  In psychotic states, the normal filter ordering (Id $\to$ Ceiling $\to$ Dev $\to$ Cult $\to$ State $\to$ Attn) may invert: attention filters override cultural and developmental filters, producing instantiations inconsistent with shared $\PS$.  Hallucinations are private instantiations that fail to converge with the community's shared instantiation ($\CSp_{\mathrm{shared}}$).

**Dissociation as hypervisor failure.**  Dissociative disorders correspond to disruption of the hypervisor fixed point (Proposition XIII.7 of the monograph).  When the contraction ratio $\kappa$ of the actualization operator approaches or exceeds 1, the hypervisor becomes unstable, and the self-interpreting ground state fragments.  Depersonalization is the phenomenological signature of a hypervisor approaching instability; dissociative identity disorder represents multiple competing near-fixed-points.

## References

*See PDF for full bibliography.*
---

## v2 Integration: GNEP Failure Modes & Lyapunov Diagnostics (TMP-20260217)

**Psychiatric conditions as GNEP failure modes:**

| Condition | GNEP Failure | Lyapunov Signature |
|---|---|---|
| ADHD-spectrum | Hypervisor overload | λ near 0, high variance |
| OCD-spectrum | Assembly locked | λ << 0, rigid attractor |
| Dissociation / DID | Assembly fragmentation | λ bifurcates across sub-agents |
| Antisocial pathology | Id constraint violation | $\lambda < 0$ (GL ground state), wrong attractor |
| Mania / psychosis-spectrum | Drive D excess | $\lambda > 0$ (GL above critical temperature), unstable |

**Lyapunov diagnostic principle:**
- $\lambda < 0$ (GL ground state): stable attractor (health or pathological fixation)
- λ = 0: bifurcation (acute crisis, insight moment, medication onset)
- $\lambda > 0$ (GL above critical temperature): unstable/chaotic (acute psychosis, mania, dissociation)

The Schopenhauer-Nietzsche Transition maps onto therapeutic trajectory: undirected distress (σdW) → directed recovery (μdt + σdW) → stable integration ($\lambda < 0$ (GL ground state)).
