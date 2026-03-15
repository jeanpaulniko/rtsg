---
title: "Political Science Companion Paper"
version: "2.0.0"
last_updated: "2026-03-05"
status: ARXIV-READY
arxiv_category: "physics.soc-ph"
---

# Political Science Companion Paper

**Jean-Paul Niko** · February 2026

% ═══════════════════════════════════════════════════════════════════════════════

% ═══ Three-Space Notation ═══
\newcommand{\QS}{\mathcal{Q}}
\newcommand{\PS}{\mathcal{P}}
\newcommand{\CSp}{\mathcal{C}_S}
\newcommand{\Inst}{\mathfrak{I}}
\newcommand{\Qp}{\mathbb{Q}_p}

\title{\textcolor{sectionblue}{**Cognitive Geometry of Democratic Resilience:  [0.3em]
Intelligence Diversity, Filter Dynamics, and the  
Mathematics of Collective Governance**}}

\author{Jean-Paul Niko  
  
\small `triptomean.com`}

\date{February 2026}

!!! abstract "Abstract"
    
We introduce a mathematical framework for analyzing democratic governance, polarization, cognitive warfare, and strategic competition grounded in the Intelligence as Geometry (RTSG) theory.  A democracy is modeled as a *cognitive bundle* $B = \{\bI_1, \ldots, \bI_n\}$ whose collective intelligence depends on citizen diversity weighted by institutional compatibility.  We formalize the democratic advantage as higher synergy ceiling relative to autocracies, tempered by higher governance costs.  Constitutional design is reinterpreted as *spectral engineering* of the governance hypervisor---separation of powers, federalism, and checks and balances become eigenvalue constraints that prevent any single cognitive type from dominating the collective attention simplex.  A continuous *polarization metric* $P_{\mathrm{cont}}$ quantifies the shrinkage of shared conceptual space between subpopulations, with a provable critical threshold $P_c$ beyond which deliberative democracy becomes structurally impossible.  We extend the framework to cognitive warfare (adversary profiling, disinformation as filter corruption, counter-disinformation as overlap expansion), alliance cognitive synergy (NATO as cognitive bundle, interoperability as shared filter subspace), and AI in national security (machine intelligence profiles, human--AI teaming, substrate parameterization for adversary capability assessment).  Deterrence theory is extended to account for cognitively heterogeneous actors whose perception of "rationality" depends on their intelligence profile and filter configuration.  The framework replaces qualitative strategic analysis with quantitative predictions grounded in measurable cognitive variables.
The three-space ontology grounds these results in instantiation theory: democracy is a diverse instantiation portfolio, polarization is instantiation divergence, and information warfare targets a population's $\QS \to \PS$ projection channels.

**Keywords:** democratic resilience, polarization, cognitive warfare, collective intelligence, strategic competition, intelligence diversity, AI national security

---

% ═══════════════════════════════════════════════════════════════════════════════

## Introduction

% ═══════════════════════════════════════════════════════════════════════════════

Democratic theory has long recognized that the quality of collective governance depends on more than the aggregation of preferences.  From Condorcet's jury theorem through Landemore's [Landemore2013] epistemic democracy to Page's [Page2007] diversity results, a growing body of work suggests that *cognitive diversity*---not merely opinion diversity---is the fundamental resource that democratic institutions exploit.  Yet this insight has remained difficult to formalize: we lack a mathematical framework that connects individual cognitive profiles to institutional structure to collective outcomes in a way that generates quantitative predictions.

This paper provides such a framework, drawing on the Intelligence as Geometry (RTSG) theory ([Niko2026]).  The core move is to represent each citizen's cognitive capacity as a vector $\bI \in \\mathbb{R}^{n(e)}_{\geq 0}$ spanning eight types.  A democracy is then a *cognitive bundle*: a collection of intelligence vectors whose collective performance depends on the diversity of member profiles, the compatibility structure between types, and the governance architecture that mediates interaction.  This formalization yields several contributions.

First, it provides a precise account of the *democratic advantage*: democracies can sustain higher cognitive diversity than autocracies because they tolerate---and are designed to manage---a wider range of cognitive profiles.  This diversity produces higher potential synergy, but only if institutional design successfully manages the coordination costs.

Second, it introduces a continuous *polarization metric* with a theoretically grounded critical threshold beyond which democratic deliberation becomes structurally impossible, regardless of good faith.  This goes beyond existing polarization measures (which track attitudinal divergence) to capture the deeper phenomenon of *conceptual divergence*: the shrinkage of the shared cognitive space through which groups can translate meaning.

Third, it extends the framework to strategic competition and national security, providing formal models of cognitive warfare, alliance dynamics, and the integration of artificial intelligence into national security architectures.

We proceed as follows.  Section *ref:sec:democracy* models democracy as cognitive bundle optimization.  Section *ref:sec:constitutional* interprets constitutional design as spectral engineering.  Section *ref:sec:polarization* develops the polarization metric.  Section *ref:sec:warfare* formalizes cognitive warfare.  Section *ref:sec:alliance* analyzes alliance dynamics.  Section *ref:sec:ai* applies the framework to AI and national security.  Section *ref:sec:deterrence* extends deterrence theory.  Section *ref:sec:predictions* presents testable predictions.

% ═══════════════════════════════════════════════════════════════════════════════

## Democracy as Cognitive Bundle Optimization

% ═══════════════════════════════════════════════════════════════════════════════

!!! definition "Political Bundle"
 \tB{}
A polity is a cognitive bundle $B = \{\bI_1, \ldots, \bI_n\}$ of citizen intelligence vectors, governed by a *hypervisor* $H$ that allocates collective attention across cognitive types.  The collective intelligence of the polity is:
\begin{keyeq}
\[
\bI_{\mathrm{coll}}(B, H) = H \cdot \left(\sum_i \bI_i + \sum_{i<j} \bI_i^\top \bK \, \bI_j \cdot \hat{\mathbf{u}}_{ij}\right)
\]
\end{keyeq}
where $\hat{\mathbf{u}}_{ij}$ is the unit vector in the direction of the synergistic interaction between agents $i$ and $j$, and $H$ is the governance operator that mediates which interactions are facilitated.

!!! proposition "Democratic Advantage"
 \tB{}
A democracy sustains higher *profile diversity* $D = \mathrm{Var}(\{\bI_i\})$ than an autocracy of equal population size, because democratic institutions tolerate cognitive heterogeneity that autocracies suppress.  Higher diversity produces a higher synergy *ceiling*:
\[
\max_H \Syn(B_{\mathrm{democracy}}) \geq \max_H \Syn(B_{\mathrm{autocracy}})
\]

The qualification "ceiling" is important.  High diversity also increases coordination costs, because more diverse profiles require more inter-type translation.  The democratic advantage is realized only when governance institutions---the hypervisor $H$---are sophisticated enough to manage the higher-dimensional attention simplex that diversity creates.

!!! proposition "Democratic Governance Cost"
 \tB{}
The governance cost of a democracy scales with profile diversity:
\[
\text{Cost}(H) \propto D \cdot \sum_{s \neq t} F_{st} \cdot w_{st}
\]
where $F_{st}$ is the friction between types and $w_{st}$ measures how frequently governance requires cross-type interaction.  Autocracies have lower governance costs because they suppress diversity, but also lower synergy ceilings.

\begin{intuition}
This formalizes the common observation that democracies are messy but adaptive, while autocracies are efficient but brittle.  The mess is the coordination cost of managing cognitive diversity; the adaptiveness is the higher synergy ceiling that diversity provides when governance successfully mediates cross-type interaction.
\end{intuition}

% ═══════════════════════════════════════════════════════════════════════════════

## Constitutional Design as Spectral Engineering

% ═══════════════════════════════════════════════════════════════════════════════

The governance hypervisor $H$ can be decomposed spectrally: its eigenvectors define the "natural modes" of governance, and its eigenvalues determine how much weight each mode receives.  Constitutional design is the engineering of this spectral structure.

!!! definition "Governance Spectrum"
 \tB{}
The hypervisor $H$ has eigendecomposition $H = \sum_k \lambda_k \mathbf{v}_k \mathbf{v}_k^\top$, where $\lambda_k$ is the weight given to governance mode $k$ and $\mathbf{v}_k$ is the corresponding direction in the type space.  A governance mode with $\lambda_k \gg \lambda_j$ for all $j \neq k$ indicates that type $k$ dominates collective decision-making.

!!! proposition "Separation of Powers as Eigenvalue Constraint"
 \tB{}
The constitutional principle of separation of powers is an *eigenvalue constraint*: no single eigenvalue should dominate the spectrum.  Formally:
\[
\frac{\lambda_{\max}}{\lambda_{\min}} \leq \kappa \quad \text{(condition number bound)}
\]
A well-designed constitution keeps the condition number $\kappa$ bounded, ensuring that no single cognitive type monopolizes governance.  Legislative, executive, and judicial branches specialize in different cognitive modes while constraining each other's dominance.

!!! example "Federalism as Dimensional Allocation"
 \tB{}
Federalism allocates different dimensions of the governance problem to different levels of organization.  Local government handles types requiring high spatial and social intelligence (land use, community services); national government handles types requiring symbolic and evaluative intelligence (foreign policy, macroeconomic regulation).  This is a spectral decomposition of the governance operator across institutional levels.

!!! example "Checks and Balances as Eigenvalue Damping"
 \tB{}
Checks and balances are feedback mechanisms that damp eigenvalue growth.  When the executive's eigenvalue begins to dominate (concentration of power), legislative and judicial constraints reduce it.  The system is stable when these feedback loops keep all eigenvalues within the constitutional bound $\kappa$.  Democratic erosion is the progressive weakening of these feedback mechanisms, allowing $\kappa \to \infty$.

% ═══════════════════════════════════════════════════════════════════════════════

## Polarization as Filter Bifurcation

% ═══════════════════════════════════════════════════════════════════════════════

Polarization, in the RTSG framework, is not primarily about disagreement (which is healthy for cognitive diversity) but about the *shrinkage of the shared conceptual space* through which disagreement can be communicated. This formalizes the mechanisms identified by Sunstein [Sunstein2009], where like-minded groups drive each other toward extremes through iterative filter narrowing.

!!! definition "Continuous Polarization Metric"
 \tB{}
For two subpopulations $A$ and $B$ with mean effective profiles $\bar{\bI}_A$ and $\bar{\bI}_B$:
\begin{keyeq}
\[
P_{\mathrm{cont}} = 1 - \frac{\displaystyle\sum_t \min(\bar{I}_{A,t}, \bar{I}_{B,t})}{\displaystyle\sum_t \max(\bar{I}_{A,t}, \bar{I}_{B,t})}
\]
\end{keyeq}
$P_{\mathrm{cont}} \in [0,1]$ with $P_{\mathrm{cont}} = 0$ indicating identical profiles and $P_{\mathrm{cont}} = 1$ indicating zero shared capacity.  This weights overlap by magnitude: vestigial shared capability counts less than robust shared capability.

!!! definition "Overlap Subspace"
 \tB{}
The *overlap subspace* is the set of cognitive types where both subpopulations retain non-trivial capacity:
\[
T_{\mathrm{overlap}}(A,B) = \{t : \bar{I}_{A,t} > \epsilon \text{ and } \bar{I}_{B,t} > \epsilon\}
\]
This is the communicative common ground through which translation between groups is possible.

!!! theorem "Communication Threshold"
 \tB{}
There exists a critical polarization $P_c$ such that for $P_{\mathrm{cont}} > P_c$, the communication bandwidth between subpopulations drops below the minimum required for deliberative exchange.  Beyond this threshold, the Conceptual Irreversibility Theorem (CIT) applies to inter-group translation: meaning loss exceeds reconstructability, and groups *cannot* understand each other in the strong sense regardless of good faith.

\begin{intuition}
Two groups beyond $P_c$ may sincerely desire mutual understanding, but the structural divergence of their cognitive filters means that the concepts available to one group literally *do not translate* into the conceptual vocabulary of the other.  This is not about disagreement---it is about *mutual unintelligibility*, a stronger and more dangerous condition.
\end{intuition}

### Polarization dynamics

!!! proposition "Media Ecosystems as Filter Amplifiers"
 \tB{}
Partisan media narrows $\Phi_{\mathrm{cult}}$ for each subpopulation by reinforcing certain cognitive modes and atrophying others.  When media fragmentation exceeds a critical level, the two subpopulations' filters diverge faster than bridging institutions can maintain overlap, producing exponential growth in $P_{\mathrm{cont}}$.

The dynamics have a clear bifurcation structure.  Below critical media fragmentation, a shared public sphere maintains sufficient overlap for deliberation.  Above it, the positive feedback loop between filter divergence and communication failure drives rapid polarization toward $P_c$.

### Measuring polarization empirically

$P_{\mathrm{cont}}$ is measurable from observational data.  Congressional speech data, social media discourse, and survey instruments can all provide proxies for the type-specific capacity of each subpopulation.  The framework predicts that $P_{\mathrm{cont}}$ computed from these data will track legislative productivity, institutional trust, and the frequency of cross-partisan collaboration---and that there exists a sharp transition point beyond which these indicators collapse.

% ═══════════════════════════════════════════════════════════════════════════════

## Cognitive Warfare and Information Operations

% ═══════════════════════════════════════════════════════════════════════════════

The RTSG framework provides a formal foundation for understanding cognitive warfare---the deliberate manipulation of an adversary's cognitive environment to degrade their decision-making capacity. Where classical analyses of strategic decision-making [Allison1971] identify organizational and bureaucratic filters qualitatively, RTSG quantifies them as diagonal operators on the intelligence vector.

### Adversary cognitive profiling

!!! definition "Cognitive Profile of a Decision-Maker"
 \tB{}
An adversary decision-maker has intelligence vector $\bI_{\mathrm{adv}}$ filtered through cultural, institutional, and state-dependent filters:
\[
\bI_{\mathrm{eff}} = \Phi_{\mathrm{state}} \circ \Phi_{\mathrm{inst}} \circ \Phi_{\mathrm{cult}}(\bI_{\mathrm{raw}})
\]
The *predicted blind spots* are the types $t$ where $I_{\mathrm{eff},t} \approx 0$---dimensions along which the decision-maker has no effective capacity due to cumulative filter attenuation.

This connects to Betts's [Betts1978] analysis of intelligence failures: failures are not random but *structurally predictable* from the filter profile of the intelligence community.  An organization whose filter attenuates type $t$ will systematically miss threats that manifest in that dimension, regardless of the quality of its analysts.

### PSYOP effectiveness and the overlap bound

!!! proposition "Influence Bandwidth Theorem"
 \tB{}
The effectiveness of psychological operations is bounded by the overlap subspace between the influencer's conceptual system and the target's:
\[
\text{Influence capacity} \leq f(|T_{\mathrm{overlap}}(\text{influencer}, \text{target})|)
\]
You can only influence through shared conceptual dimensions.  The CIT limits message fidelity: the intended message and the received message inevitably diverge across the Heyting Gap.

### Disinformation as filter corruption

!!! definition "Disinformation Attack"
 \tB{}
A disinformation campaign is a deliberate attempt to *corrupt the target's cultural filter* $\Phi_{\mathrm{cult}}$ in order to shrink their overlap subspace with allies:
\[
\Phi_{\mathrm{cult}}^{\mathrm{corrupted}} = \Phi_{\mathrm{disinfo}} \circ \Phi_{\mathrm{cult}}
\]
By the Kernel Lemma, $\ker(\Phi_{\mathrm{disinfo}} \circ \Phi_{\mathrm{cult}}) \supseteq \ker(\Phi_{\mathrm{cult}})$: the corruption can only further narrow the target's effective intelligence, never expand it.

The strategic logic is isolation: by corrupting group $A$'s filter to diverge from group $B$'s, the adversary reduces the overlap subspace between allies, degrading their ability to coordinate.  This connects to Rid's [Rid2020] historical analysis of active measures: the consistent goal is not to persuade the target of specific falsehoods but to fragment their conceptual coherence.

!!! proposition "Counter-Disinformation as Overlap Expansion"
 \tB{}
Effective counter-disinformation does not merely correct false beliefs (which targets a specific type) but expands the overlap subspace between the target population and its allies.  This requires *filter resilience training*: developing capacity in multiple cognitive types so that corruption of any single type does not collapse the overlap.

% ═══════════════════════════════════════════════════════════════════════════════

## Alliance Cognitive Synergy

% ═══════════════════════════════════════════════════════════════════════════════

Alliances are cognitive bundles at the international level.

!!! definition "Alliance Synergy"
 \tB{}
An alliance $\mathcal{A} = \{B_1, \ldots, B_m\}$ of member-state bundles has collective synergy:
\[
\Syn(\mathcal{A}) = \sum_{i<j} \Syn(B_i, B_j) - \text{Coordination}(\mathcal{A})
\]
where inter-state synergy depends on the complementarity of national cognitive profiles and coordination costs depend on the friction of cross-national interaction.

!!! example "NATO as Cognitive Bundle"
 \tB{}
NATO's cognitive synergy depends on the diversity of member-state cognitive profiles (different strategic cultures, intelligence traditions, and operational expertise) weighted by the compatibility of their institutional filters.  Interoperability---the central NATO operational concept---is mathematically equivalent to maximizing the shared filter subspace:
\[
T_{\mathrm{interop}} = \bigcap_i T_{\mathrm{active}}(B_i) = \{t : \phi^{(i)}_t > \epsilon \text{ for all member states } i\}
\]
The larger the interoperable subspace, the more cognitive types the alliance can deploy in coordinated operations.

!!! proposition "Intelligence Sharing as Partial Filter Alignment"
 \tB{}
Sharing intelligence between allies is mathematically equivalent to partially aligning their information filters: both parties expand their effective intelligence in the shared domain.  The optimal intelligence-sharing regime maximizes joint overlap without exposing the unique components of each party's filter (sources and methods).

!!! proposition "Alliance Fragility Prediction"
 \tB{}
An alliance is cognitively fragile when $|T_{\mathrm{interop}}|$ is small---when members share few cognitive types at operational strength.  An adversary can exploit this by targeting the shared types with disinformation, fragmenting the alliance's conceptual common ground.  The framework predicts which alliances are most vulnerable: those with high political diversity but low cognitive interoperability.

% ═══════════════════════════════════════════════════════════════════════════════

## AI in National Security

% ═══════════════════════════════════════════════════════════════════════════════

The RTSG framework extends naturally to artificial intelligence systems [Horowitz2018], which have their own intelligence vectors and filter profiles.

### Machine intelligence profiles

!!! definition "Machine Intelligence Vector"
 \tB{}
An AI system $M$ has an intelligence vector $\bI_M \in \\mathbb{R}^{n(e)}_{\geq 0}$ measuring its effective capacity across the same eight cognitive types.  The profile is shaped by architectural filters ($\Phi_{\mathrm{arch}}$), training data filters ($\Phi_{\mathrm{data}}$), and objective function filters ($\Phi_{\mathrm{obj}}$):
\[
\bI_M = \Phi_{\mathrm{obj}} \circ \Phi_{\mathrm{data}} \circ \Phi_{\mathrm{arch}}(\bI_{\mathrm{potential}})
\]

Current large language models have characteristically high $I_L$ (linguistic) and $I_A$ (algebraic) but low $I_K$ (kinesthetic) and $I_G$ (spatial, though improving with multimodal architectures).  ISR systems have high $I_G$ (spatial) but near-zero $I_S$ (social intelligence).  The framework enables systematic comparison of AI systems by their cognitive profiles rather than by aggregate benchmarks.

### Human--AI teaming

!!! proposition "Human--AI Bundle Synergy"
 \tB{}
The synergy of a human--AI team depends on the complementarity of their intelligence profiles:
\[
\Syn(\bI_{\mathrm{human}}, \bI_{\mathrm{AI}}) = \bI_{\mathrm{human}}^\top \bK \, \bI_{\mathrm{AI}}
\]
Optimal teaming pairs humans and AI systems with complementary strengths in high-$K$ type combinations.  The framework predicts which human--AI pairings produce synergy and which produce friction.

### Substrate parameterization for adversary assessment

!!! definition "Substrate Parameters"
 \tB{}
An AI system's capability trajectory is characterized by the *substrate parameters*:
\[
S = (\rho, \omega, \alpha) \quad \text{where } \rho = \text{intelligence density}, \; \omega = \text{clock rate}, \; \alpha = \text{parallelism}
\]
The product $J = \rho \cdot \omega \cdot \alpha$ gives the system's aggregate cognitive throughput.

This replaces vague "AGI timelines" discourse with a quantitative framework.  An adversary's AI capability can be assessed by estimating their substrate parameters from observable indicators (chip production, training compute, benchmark performance) and projecting trajectories.  The framework predicts that the strategically relevant threshold is not "human-level AI" (a scalar comparison that the RTSG framework rejects) but the point at which an adversary's AI achieves specific $I_t$ values that exceed human capacity in strategically critical types.

!!! proposition "Defense Acquisition as Portfolio Optimization"
 \tB{}
The optimal defense portfolio maximizes total intelligence per unit cost across the combined human--AI force:
\[
\max \frac{\Syn(B_{\mathrm{total}})}{\text{Total cost}} \quad \text{subject to mission requirements } R_t \text{ per type}
\]
This is a constrained optimization that trades off human capital (flexible but expensive, high $I_N$ and $I_E$) against AI capital (specialized but scalable, high in specific types) to meet mission-defined intelligence requirements.

% ═══════════════════════════════════════════════════════════════════════════════

## Extended Deterrence Theory

% ═══════════════════════════════════════════════════════════════════════════════

Classical deterrence theory assumes rational actors with known utility functions operating under complete information about each other's preferences.  The RTSG framework extends this by recognizing that actors have *different intelligence profiles* with *different filters*, making "rationality" itself perspective-dependent.

!!! definition "Cognitively Heterogeneous Deterrence"
 \tB{}
In a deterrence dyad, actor $A$ models actor $B$'s decision-making as:
\[
\hat{\bI}_B^{(A)} = \Phi_A(\bI_B) \quad \text{(A's model of B's intelligence)}
\]
But $B$'s actual decision-making is driven by $\bI_B^{\mathrm{eff}} = \Phi_B(\bI_B)$.  The *misperception risk* is:
\[
\Hgap_{AB} = \|\hat{\bI}_B^{(A)} - \bI_B^{\mathrm{eff}}\|
\]

This connects to Jervis's [Jervis1976] analysis of perception and misperception in international politics, providing a quantitative measure of the misperception gap that Jervis described qualitatively.

!!! proposition "Filter-Dependent Escalation Dynamics"
 \tB{}
Crisis escalation dynamics depend on the state-dependent filter $\Phi_{\mathrm{state}}$, which shifts under stress.  Under acute stress, attention concentrates on fewer types (the fight-or-flight narrowing), activating cognitive modes associated with pattern-matching and risk assessment that were not dominant in peacetime deliberation.  The stressed decision-maker has a different effective intelligence vector than the peacetime decision-maker, and deterrence signals calibrated for the peacetime profile may be misread under stress.

!!! proposition "Escalation Ladder as Simplex Trajectory"
 \tB{}
Escalation is a trajectory on the adversary's attention simplex $\Delta^7$ under the dynamics induced by $\Phi_{\mathrm{state}}(\text{crisis intensity})$.  As crisis intensity increases, the trajectory moves toward vertices (extreme type concentration) where decision-making is most predictable but also most rigid.  The framework predicts that de-escalation requires redirecting the adversary's attention trajectory away from the vertex before it reaches the absorbing state.

!!! proposition "Schelling Focal Points as Overlap Equilibria"
 \tB{}
Schelling's [Schelling1960] focal points---the salient solutions that actors converge on in coordination games---correspond to high-$\IdeaRank$ concepts in the overlap subspace of the two actors.  Successful deterrence communication requires that both actors share a sufficient overlap to recognize the same focal points.  When cultural filters diverge (as with adversaries from very different strategic cultures), focal points may not be shared, and deterrence signaling degrades.

% ═══════════════════════════════════════════════════════════════════════════════

## Testable Predictions

% ═══════════════════════════════════════════════════════════════════════════════

[nosep]

- **Polarization threshold.**  Compute $P_{\mathrm{cont}}$ from congressional speech data for each Congress since 1970.  The framework predicts that legislative productivity drops discontinuously when $P_{\mathrm{cont}}$ crosses $P_c$, with a phase transition rather than a gradual decline.

- **Media fragmentation.**  Track the correlation between media ecosystem fragmentation (number of distinct information environments) and the rate of change $dP_{\mathrm{cont}}/dt$.  The framework predicts a super-linear relationship above a critical fragmentation level.

- **Alliance interoperability.**  Measure the cognitive interoperability $|T_{\mathrm{interop}}|$ of NATO member-state defense establishments and predict exercise performance.  The framework predicts that interoperability scores (measured via RTSG profiles of institutional culture) outperform traditional metrics in predicting joint operational effectiveness.

- **Human--AI teaming.**  For military human--AI teams, measure the complementarity of human and AI cognitive profiles and predict team performance on complex operational scenarios.  The framework predicts that complementary-profile teams outperform matched-profile teams, conditional on high $K$ between the relevant type pairs.

- **Intelligence failures.**  Retrospectively analyze intelligence failures (Pearl Harbor, 9/11, Iraq WMD) by estimating the intelligence community's filter profile [Tetlock2005].  The framework predicts that each failure corresponds to a systematically attenuated type---a blind spot inherent in the institutional filter.

- **Deterrence signaling.**  Measure the cognitive overlap between adversary dyads (US--China, US--Russia, India--Pakistan) from diplomatic communications and strategic culture analysis.  The framework predicts that smaller overlap correlates with higher misperception risk and more frequent near-crises.

- **Depolarization.**  Test whether overlap-expansion interventions (cross-partisan collaborative projects) reduce $P_{\mathrm{cont}}$ more effectively than attitude-change interventions (fact-checking, persuasion campaigns) in a randomized controlled trial.

% ═══════════════════════════════════════════════════════════════════════════════

## Three-Space Political Science

The three-space ontology (Part XIII) provides foundational grounding for democratic resilience and cognitive warfare.

**Democracy as diverse instantiation portfolio.**  A democratic society maintains legitimacy by ensuring that its shared $\PS$ (laws, institutions, norms) reflects the converging instantiations of a diverse population.  Democratic resilience is the robustness of this convergence under perturbation.  When a sufficient diversity of intelligence profiles contributes to shared instantiation, the resulting $\PS$-structures are stable against attack from any single cognitive dimension---the portfolio is diversified.

**Polarization as instantiation divergence.**  Political polarization corresponds to the community's instantiation operators diverging: subgroups begin producing incompatible $\PS$-configurations from the same $\QS$-potentiality.  The overlap region $\CSp_{\mathrm{shared}}$ shrinks, and the shared physical reality (agreed-upon facts, trusted institutions) fragments.  In three-space terms, polarization is the *reduction of shared instantiation capacity*.

**Disinformation as filter corruption.**  Information operations target the cultural filter $F_{\mathrm{cult}}$, attempting to modify a population's convergence conditions.  Successful disinformation changes *what the population instantiates*---not merely what they believe, but what $\PS$-structures they produce.  The three-space framework reveals this as an attack on the community's $\QS \to \PS$ projection, not merely on its beliefs.

**Cognitive warfare as instantiation competition.**  State-level cognitive warfare is competition over which $\QS$-structures get instantiated into shared $\PS$.  Each adversary attempts to shape the target population's filter chain to favor instantiations aligned with the adversary's interests.  The effectiveness of such operations is bounded by the CIT: cross-cultural cognitive translation is lossy, limiting the precision with which an adversary can reshape another culture's instantiation patterns.

## Discussion

% ═══════════════════════════════════════════════════════════════════════════════

This paper has introduced a mathematical framework for analyzing democratic governance and strategic competition through the lens of cognitive geometry.  The contributions span four domains.

For democratic theory, the framework provides a quantitative account of why diversity is valuable (bundle synergy), what threatens it (filter bifurcation producing polarization), and how constitutional design manages it (spectral engineering of governance).  The critical polarization threshold $P_c$ provides a formal criterion for democratic resilience that goes beyond existing measures.

For strategic studies, the framework replaces qualitative analysis of cognitive warfare with quantitative models that specify attack vectors (filter corruption), effectiveness bounds (overlap constraint), and defense strategies (filter resilience training).  Adversary capability assessment shifts from scalar "AGI timeline" speculation to multi-dimensional substrate parameterization with measurable indicators.

For alliance management, the framework reconceptualizes interoperability as shared filter subspace and predicts which alliance configurations are cognitively synergistic versus friction-dominated.  This extends existing interoperability frameworks (which focus on technical and procedural compatibility) to include cognitive compatibility.

For deterrence theory, the extension to cognitively heterogeneous actors provides formal tools for analyzing misperception risk, escalation dynamics, and the conditions under which deterrence signaling succeeds or fails.  The Heyting Gap between adversaries' conceptual systems becomes a measurable predictor of crisis stability.

The framework has limitations.  The eight-type model is a simplification; national security applications may require finer-grained cognitive taxonomies.  Estimating intelligence profiles and filter configurations for entire nations is methodologically challenging.  And the strategic implications---particularly regarding adversary vulnerability assessment---raise ethical questions about the offensive use of cognitive profiling that deserve careful consideration.

Nevertheless, the framework represents a significant advance: it provides a mathematical language for strategic analysis that is grounded in measurable cognitive variables, generates falsifiable predictions, and connects individual cognition to institutional structure to geopolitical outcomes within a single formal system.  The cognitive geometry of democratic resilience is not merely a metaphor---it is a mathematical structure with quantitative implications for governance, security, and the future of democratic institutions.

% ═══════════════════════════════════════════════════════════════════════════════
% BIBLIOGRAPHY
% ═══════════════════════════════════════════════════════════════════════════════

## References

*See PDF for full bibliography.*
---

## v2 Integration: GNEP Governance Model (TMP-20260217)

**Confederate GNEP model:**

- Each political unit = GNEP hypervisor node
- Optimization variable: maximize total life force across all agents
- Constraint: shared survival constraint X_Id
- Equilibrium: cooperative Nash

Distinguished from democratic models (majority rule over fixed option set) and republican models (delegated authority): in GNEP confederacy, the option set is continuously generated by nodes, and consensus = convergence on the optimization variable, not on a specific policy.

**Formal conflict resolution:** Inconsistent node flagged → made irrelevant to current decision → persistent inconsistency → topological removal from information graph (tribal exile). This is not punishment — it is graph topology.

---

## Extended Formalizations *(v2 — 2026)*

### Cognitive Warfare

The RTSG framework provides a formal foundation for cognitive warfare — the deliberate manipulation of an adversary's cognitive environment to degrade decision-making capacity.

**Strategic logic:** By corrupting group A's filter to diverge from group B's filter, an adversary reduces the overlap subspace between allies, degrading coordination capacity. Rid's (2020) analysis of active measures confirms: the consistent goal is not to persuade targets of specific falsehoods but to fragment their conceptual coherence.

Formally: if ||Φ_A - Φ_B|| > θ_coordination, the two groups can no longer form a functioning cognitive assembly. They may share physical space while operating in non-overlapping conceptual spaces.

### Intelligence Failures as Structural Prediction

Betts's (1978) analysis of intelligence failures receives a structural explanation: failures are not random but *structurally predictable* from the filter profile of the intelligence community. An organization whose filter attenuates type t will systematically miss threats manifesting in that dimension, regardless of analyst quality. The failure is architectural, not individual.

### AI Systems in the Political Framework

Current large language models have characteristically high I_L (linguistic) and I_A (abstract) but low I_K (kinesthetic) and limited I_S (spatial, improving with multimodal architectures). ISR systems have high I_S but near-zero I_P (social intelligence). 

The framework enables systematic comparison of AI systems by cognitive profile rather than aggregate benchmarks — directly relevant to the Intelligence Arena at smarthub.my/arena/. A democracy deploying AI systems without understanding their filter profiles is deploying cognitive agents whose systematic blind spots are unknown.

### Polarization as Conceptual Space Shrinkage

Polarization in RTSG is not primarily about disagreement (which is healthy for cognitive diversity) but about the *shrinkage of the shared conceptual space* through which disagreement can be communicated. This connects to Jervis's (1976) analysis of misperception — with a quantitative measure of the misperception gap: ||Φ_A - Φ_B||_F, the Frobenius norm of the filter difference.
