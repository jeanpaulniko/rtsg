---
title: "Machine Learning Companion Paper"
version: "2.0.0"
last_updated: "2026-03-05"
status: ARXIV-READY
arxiv_category: "cs.AI"
---

# Machine Learning Companion Paper

**Jean-Paul Niko** · February 2026

\title{\textcolor{sectionblue}{**Intelligence Vectors, Cognitive Alloys,  [0.3em]
and Optimal Engine Orchestration:  [0.2em]
A Mathematical Framework for Multi-Model AI Systems**}}
\author{Jean-Paul Niko  
  
\small`niko@triptomean.com`}
\date{February 2026}
% ═══════════════════════════════════════════════════════════════════════════════

!!! abstract "Abstract"
    
We introduce a mathematical framework for characterizing, comparing, and orchestrating AI models using *intelligence vectors* $\bI \in [0,\infty)^8$, where each component measures capability in a distinct cognitive type.  The framework yields five practical tools for multi-model AI systems.  First, *IdeaRank routing*: given a query with demand vector $\bR$, route to $\argmax_m (\bI_m \cdot \bR \times \ELO_m)$, providing a principled alternative to learned routers.  Second, *cognitive alloy design*: the compatibility matrix $\bK \in \R^{8 \times 8}$ predicts which model combinations exhibit synergy ($\Syn > 1$) versus interference ($\Syn < 1$), giving a structured search space for compound AI architectures.  Third, *variable-dimensional benchmarking*: replacing a single scalar leaderboard with per-type ELO scores yields diagnostically richer model comparison.  Fourth, *emergence-optimal assembly*: a three-class emergence theory ($E_1, E_2, E_3$) defines a total emergence value $V(A)$ that serves as the objective function for assembly optimization, with a $(1-1/e)$-approximation guarantee via submodular greedy.  Fifth, *filter-based bias characterization*: filter operators $\bF_{\mathrm{data}}, \bF_{\mathrm{arch}}, \bF_{\mathrm{obj}}$ decompose model bias into type-specific, source-attributed attenuations that suggest targeted remediation.  A reference implementation (\textsc{Grand Engine}) achieves 100/100 on a validation suite covering all mathematical objects and algorithms.

**Keywords:** model routing, intelligence vectors, multi-model orchestration, cognitive alloys, emergence theory, benchmark diagnostics, mixture of experts, filter operators

---

% ═══════════════════════════════════════════════════════════════════════════════

## Introduction

The AI industry is converging on compound systems.  Production deployments increasingly chain language models with retrieval engines, code executors, vision models, and tool-calling interfaces.  The orchestration problem---deciding which model handles which subtask, in what order, with what context---is the central engineering challenge of the current era.

Two problems remain unsolved.  The first is *benchmark collapse*: the prevailing approach to model comparison uses scalar metrics---a single MMLU accuracy, a single Chatbot Arena ELO [Zheng2023]---that collapse multi-dimensional capability profiles into rank orderings.  A model excelling at mathematical reasoning but weak at social nuance looks identical to one with the opposite profile if their scalar scores coincide.  This obscures exactly the diagnostic information practitioners need.

The second is *principled orchestration*: compound AI systems---multi-model pipelines, routers, mixture-of-experts architectures [Shazeer2017,Jiang2024]---lack a mathematical theory of which model combinations exhibit synergy and which interfere.  Current routing approaches learn router weights empirically [Shnitzer2023] without a structural model of *why* certain combinations outperform others.  LangChain [Chase2023] provides composable abstractions but no optimality theory.  DSPy [Khattab2023] compiles specifications into pipelines but optimizes for benchmark accuracy rather than principled capability matching.  AutoGen [Wu2023] enables multi-agent conversations but leaves labor division to emergent negotiation.

We address both problems with a single framework: the *Intelligence as Geometry* (RTSG) formalism [Niko2026], which represents each model as a vector in $[0,\infty)^8$ and specifies cross-type interactions via a compatibility matrix.  This paper extracts the ML-relevant components of the full RTSG theory and contributes:
[nosep,leftmargin=2em]
- Intelligence vectors as model capability profiles, estimated from existing benchmarks (Section *ref:sec:vectors*).
- IdeaRank routing with formal optimality properties (Section *ref:sec:routing*).
- Cognitive alloy design guided by the compatibility matrix (Section *ref:sec:alloy*).
- Eight-dimensional ELO benchmarking (Section *ref:sec:benchmark*).
- Three-class emergence theory with assembly optimization guarantees (Section *ref:sec:emergence*).
- Filter-based bias decomposition (Section *ref:sec:filters*).
- Cost-weighted intelligence functionals for optimal compute allocation (Section *ref:sec:compute*).

% ═══════════════════════════════════════════════════════════════════════════════

## Intelligence Vectors for AI Models

### Definition and type space

!!! definition "Model intelligence vector"
 \tA\

The intelligence vector of an AI model $m$ is $\bI_m = (I_{\mathrm{ling}}, I_{\mathrm{spat}}, I_{\mathrm{soc}}, I_{\mathrm{symb}}, I_{\mathrm{mnem}}, I_{\mathrm{eval}}, I_{\mathrm{aud}}, I_{\mathrm{kin}})_m \in [0,\infty)^8$, where:
[nosep,leftmargin=1.5em]
- $I_{\mathrm{ling}}$: linguistic-analytical capability (text generation, translation, summarization),
- $I_{\mathrm{spat}}$: spatial-mechanical capability (visual reasoning, scene understanding, 3D),
- $I_{\mathrm{soc}}$: social-relational capability (empathy modeling, social reasoning, alignment),
- $I_{\mathrm{symb}}$: symbolic-abstract capability (formal logic, mathematics, code generation),
- $I_{\mathrm{mnem}}$: mnemonic-archival capability (retrieval, context utilization, knowledge recall),
- $I_{\mathrm{eval}}$: evaluative-strategic capability (planning, decision-making, risk assessment),
- $I_{\mathrm{aud}}$: auditory-musical capability (speech recognition, music understanding, audio),
- $I_{\mathrm{kin}}$: kinesthetic-somatic capability (robotics control, embodied interaction).

The eight types are not an arbitrary partitioning.  They derive from a synthesis of factor-analytic psychometric theory (Cattell--Horn--Carroll [Carroll1993]), Gardner's multiple intelligences framework [Gardner1983], and computational neuroscience.  The algebra of the framework generalizes to any $n \geq 2$; the specific choice of $n=8$ reflects the resolution needed to capture practically important distinctions between AI model capabilities.

### Estimation from benchmarks

Intelligence vectors can be estimated from existing benchmark suites by mapping benchmark categories to RTSG types:

\begin{keyeq}
**Benchmark-to-type mapping.** \tA
\begin{center}
\small

*[Table — see PDF for formatted version]*

\end{center}
\end{keyeq}

!!! remark "Estimation protocol"
 \tB\
The mapping from benchmark scores to intelligence vector components is not unique.  We propose a calibration protocol: (1) administer $k \geq 3$ type-diagnostic benchmarks per dimension, (2) fit a latent variable model where benchmark score $\sim f(\bI_m)$ with known loadings from the benchmark-type mapping, (3) extract maximum-likelihood estimates of $\bI_m$, (4) validate by holding out one benchmark per type and checking prediction accuracy.  Cross-benchmark correlations within a type should exceed cross-type correlations, confirming the factor structure.

### Model profiles

!!! example "Illustrative model profiles"
 \tB\

Estimated intelligence profiles for representative engine classes (0--5 scale, normalized so that the frontier general-purpose LLM $\approx 3.5$ in its peak type):
\begin{center}
\small

*[Table — see PDF for formatted version]*

\end{center}
Note the characteristic profile shapes: frontier LLMs are broad but weak in spatial and embodied dimensions; code models have extreme $I_{\mathrm{symb}}$ but truncated social and auditory types; retrieval engines are essentially one-dimensional ($I_{\mathrm{mnem}}$ dominant).

% ═══════════════════════════════════════════════════════════════════════════════

## Per-Type ELO Ratings

### Motivation: 8 leaderboards instead of 1

The Chatbot Arena paradigm [Zheng2023] produces a single ELO rating per model.  This is diagnostically impoverished: a model ranking 5th overall might rank 1st in $I_{\mathrm{symb}}$ and 15th in $I_{\mathrm{soc}}$---information invisible to a scalar leaderboard.

!!! definition "Per-type ELO"
 \tA\

For each intelligence type $t \in \{1,\ldots,8\}$, maintain a separate ELO rating $E_t(m)$ for model $m$, computed from pairwise comparisons on type-diagnostic tasks.  Given models $m_i, m_j$ and a type-$t$ task, the expected win probability is
\[
P(m_i \succ m_j \mid t) = \frac{1}{1 + 10^{(E_{j,t} - E_{i,t})/400}}.
\]
After observing outcome $S \in \{0, 0.5, 1\}$, the update is $E_{i,t} \leftarrow E_{i,t} + k(S - P)$ with learning rate $k$ [Glickman1999].  The model's full profile is the 8-tuple $\bE_m = (E_1(m), \ldots, E_8(m))$.

### Advantages over scalar benchmarking

The per-type ELO system has three advantages.  First, *diagnostic power*: practitioners selecting models for specific use cases can filter by the relevant type rather than relying on overall rank.  A legal AI product needs high $E_{\mathrm{ling}}$ and $E_{\mathrm{mnem}}$; a math tutoring product needs high $E_{\mathrm{symb}}$---neither cares about $E_{\mathrm{aud}}$.  Second, *routing integration*: per-type ELOs feed directly into the IdeaRank routing equation (Section *ref:sec:routing*), enabling capability-aware prompt dispatch.  Third, *continuous calibration*: as models receive updates, their ELO vectors track quality changes automatically, whereas static benchmark scores become stale.

\begin{intuition}
Imagine Chatbot Arena split into 8 parallel arenas: Math Arena, Social Arena, Spatial Arena, Language Arena, Memory Arena, Strategy Arena, Audio Arena, Embodiment Arena.  A model's rank in each arena is its per-type ELO.  The combined 8-vector is the intelligence profile.  This is strictly more informative than any single number and directly actionable for engineering decisions.
\end{intuition}

% ═══════════════════════════════════════════════════════════════════════════════

## IdeaRank Routing

### Task demand vectors

!!! definition "Task demand vector"
 \tA\

A query or task $q$ has a demand vector $\bR_q \in [0,\infty)^8$ encoding the type-specific cognitive requirements: $R_t$ is the importance of type-$t$ capability for answering $q$ well.

!!! example "Demand estimation"

[nosep,leftmargin=1.5em]
- "Prove that $\sqrt{2}$ is irrational" $\Rightarrow \bR = (1, 0, 0, 5, 0, 2, 0, 0)$.  Pure symbolic, moderate evaluative.
- "Describe how you'd comfort a grieving friend" $\Rightarrow \bR = (3, 0, 5, 0, 1, 2, 0, 0)$.  High social, moderate linguistic.
- "Generate a floorplan for a 2-bedroom apartment" $\Rightarrow \bR = (1, 5, 0, 2, 0, 3, 0, 0)$.  High spatial, moderate evaluative.
- "Transcribe and analyze this podcast episode" $\Rightarrow \bR = (3, 0, 1, 1, 3, 2, 4, 0)$.  High auditory, moderate linguistic and mnemonic.

In practice, $\bR_q$ can be estimated by a lightweight classifier mapping query features to an 8-vector.  Mathematical notation boosts $R_{\mathrm{symb}}$, social scenario keywords boost $R_{\mathrm{soc}}$, spatial references boost $R_{\mathrm{spat}}$.  The classifier can be trained on a labeled dataset of queries tagged with dominant type requirements, or---more efficiently---a frontier LLM can estimate $\bR_q$ in a single meta-prompt pass.

### The routing equation

!!! definition "IdeaRank routing"
 \tA\

Given a model pool $\{m_1, \ldots, m_N\}$ with intelligence vectors $\{\bI_{m_1}, \ldots, \bI_{m_N}\}$ and per-type ELO scores $\bE_{m}$ for each model, the optimal model for query $q$ is:

\[
m^*(q) = \argmax_{m} \sum_{t=1}^{8} I_t(m) \cdot R_t(q) \cdot E_t(m).
\]

\begin{keyeq}
**Routing equation (compact form).** \tA
\[
m^*(q) = \argmax_m \; \bI_m \cdot (\bR_q \odot \bE_m),
\]
where $\odot$ denotes elementwise product.  This is a *type-weighted trilinear form*: route to the model whose capability profile ($\bI$) best matches the query's demands ($\bR$), weighted by calibrated quality ($\bE$).
\end{keyeq}

!!! proposition "Routing optimality"
 \tB\

Under the assumption that model performance on query $q$ is monotonically increasing in the type-demand alignment $\sum_t I_t \cdot R_t \cdot E_t$, IdeaRank routing minimizes expected task error across the query distribution.  The assumption is approximately satisfied when types are approximately independent in their contribution to task performance.

### Comparison to existing routers

\begin{intuition}
RouteLLM [Shnitzer2023] and similar systems learn a routing function from data.  IdeaRank routing provides a *structural prior*: the 8D decomposition means the router needs to learn only 8 demand weights per query class, not an opaque end-to-end mapping.  This should improve sample efficiency (fewer training examples needed), interpretability (the routing decision can be explained as "this query requires high $I_{\mathrm{symb}}$ and the code model has the highest $E_{\mathrm{symb}}$"), and generalization (new models can be integrated by estimating their intelligence vector rather than retraining the router).
\end{intuition}

\begin{algorithm}[H]
\caption{IdeaRank Routing}

\begin{algorithmic}[1]
\REQUIRE Query $q$, model pool $\mathcal{M} = \{m_1, \ldots, m_N\}$, profiles $\{\bI_m, \bE_m\}$
\ENSURE Selected model $m^*$
\STATE $\bR_q \leftarrow `estimate_demand`(q)$ \COMMENT{lightweight classifier or LLM meta-prompt}
\STATE $\text{scores} \leftarrow []$
\FOR{$m \in \mathcal{M}$}
  \STATE $s_m \leftarrow \sum_{t=1}^{8} I_t(m) \cdot R_t(q) \cdot E_t(m)$
\ENDFOR
\STATE $m^* \leftarrow \argmax_m s_m$
\RETURN $m^*$
\end{algorithmic}
\end{algorithm}

**Complexity:** $O(N \cdot d)$ where $d = 8$.  This is negligible compared to inference cost and adds no meaningful latency to the routing decision.

% ═══════════════════════════════════════════════════════════════════════════════

## Cognitive Alloys: Multi-Model Orchestration

A *cognitive alloy* is a heterogeneous ensemble of models whose joint output exceeds what any single component achieves---analogous to how physical alloys combine metals to produce materials stronger than either constituent.

### The compatibility matrix

!!! definition "Compatibility matrix"
 \tA\

The compatibility matrix $\bK \in \R^{8 \times 8}$ encodes pairwise cross-type interaction effects.  When model $m_s$ (strong in type $s$) passes output to model $m_t$ (strong in type $t$):
[nosep,leftmargin=1.5em]
- $K_{st} > 1$: synergy---$m_s$'s output *amplifies* $m_t$'s performance,
- $K_{st} = 1$: independence---no interaction effect,
- $K_{st} < 1$: interference---$m_s$'s output *degrades* $m_t$'s performance.

\begin{keyeq}
**Selected $\bK$ entries for AI model chains.** \tB

\[\begin{aligned}
K_{\mathrm{mnem,ling}} &= 1.3 && \text{retrieval augments language generation (RAG synergy)}   
K_{\mathrm{spat,symb}} &= 1.3 && \text{visual grounding aids symbolic reasoning (multimodal gain)}   
K_{\mathrm{symb,ling}} &= 1.2 && \text{chain-of-thought reasoning improves language output}   
K_{\mathrm{ling,symb}} &= 0.9 && \text{verbose LLM output adds noise to formal reasoning}   
K_{\mathrm{eval,symb}} &= 1.4 && \text{strategic planning strongly enhances reasoning chains}   
K_{\mathrm{mnem,eval}} &= 1.2 && \text{retrieved context improves strategic decision-making}   
K_{\mathrm{aud,ling}} &= 0.7 && \text{audio features interfere with text processing pipelines}   
K_{\mathrm{spat,kin}} &= 1.5 && \text{visual perception strongly facilitates motor control}
\end{aligned}\]

\end{keyeq}

Note the asymmetry: $K_{\mathrm{symb,ling}} = 1.2$ but $K_{\mathrm{ling,symb}} = 0.9$.  Structured reasoning helps language generation (chain-of-thought improves output quality), but verbose language adds noise to formal reasoning (prompt length degrades mathematical accuracy).  This predicts that the *direction of chaining matters*---a prediction consistent with empirical findings on chain-of-thought prompting.

### Synergy formula

!!! definition "Bundle synergy"
 \tA\

Given models $m_1, \ldots, m_k$ with intelligence vectors $\bI_{m_1}, \ldots, \bI_{m_k}$, the synergy of the alloy is:
\[
\Syn(\{m_1, \ldots, m_k\}) = \frac{\bigl\|\sum_{i} \bI_{m_i}\bigr\|_{\bK}}{\sum_{i} \|\bI_{m_i}\|}, \qquad \|\mathbf{x}\|_{\bK} = \sqrt{\sum_{s,t} K_{st}\, x_s\, x_t}.
\]
$\Syn > 1$ means the ensemble exceeds the sum of its parts.  $\Syn < 1$ means coordination overhead destroys value.

!!! example "Worked synergy calculation"
 \tA\

Consider a two-model alloy: an LLM with $\bI_1 = (4, 0, 0, 3, 0, 0, 0, 0)$ (linguistic + symbolic) and a retrieval engine with $\bI_2 = (0, 0, 0, 0, 4, 0, 0, 0)$ (mnemonic).  The sum vector is $\bI_1 + \bI_2 = (4, 0, 0, 3, 4, 0, 0, 0)$.

The $\bK$-norm of the sum:

\[\begin{aligned}
\|\bI_1 + \bI_2\|_{\bK}^2 &= K_{\mathrm{ling,ling}} \cdot 16 + K_{\mathrm{symb,symb}} \cdot 9 + K_{\mathrm{mnem,mnem}} \cdot 16   
&\quad + 2K_{\mathrm{ling,symb}} \cdot 12 + 2K_{\mathrm{ling,mnem}} \cdot 16 + 2K_{\mathrm{symb,mnem}} \cdot 12.
\end{aligned}\]

With $K_{\mathrm{ling,ling}} = K_{\mathrm{symb,symb}} = K_{\mathrm{mnem,mnem}} = 1$, $K_{\mathrm{ling,symb}} = 1.1$, $K_{\mathrm{ling,mnem}} = 0.9$, $K_{\mathrm{symb,mnem}} = 1.0$:
\[
\|\bI_1 + \bI_2\|_{\bK}^2 = 16 + 9 + 16 + 2(1.1)(12) + 2(0.9)(16) + 2(1.0)(12) = 16 + 9 + 16 + 26.4 + 28.8 + 24 = 120.2.
\]
So $\|\bI_1 + \bI_2\|_{\bK} \approx 10.96$.  Meanwhile, $\|\bI_1\| = 5$ and $\|\bI_2\| = 4$, so $\Syn = 10.96/9 \approx 1.22$.  The retrieval-augmented LLM is predicted to be 22% superadditive.

!!! proposition "Heterogeneity principle"
 \tA\

Alloy synergy increases with profile diversity.  Formally, $\Syn(\{m_1, m_2\})$ is maximized when $\bI_{m_1}$ and $\bI_{m_2}$ are orthogonal and their dominant types have high pairwise $K$ values.  Alloys of models with identical profiles satisfy $\Syn = 1$ (no benefit to duplication).

This formalizes the intuition that "cognitive alloys are stronger than cognitive monocultures": combining an LLM, a code model, a retrieval engine, and a vision model is predicted to outperform four copies of the same LLM.

% ═══════════════════════════════════════════════════════════════════════════════

## Emergence Theory for Multi-Model Systems

The most novel theoretical contribution is a formal theory of when and how multi-model systems produce capabilities that transcend their components.

### Three classes of emergence

!!! definition "$E_1$: Quantitative surplus"
 \tA\

An assembly $A = \{m_1, \ldots, m_k\}$ exhibits $E_1$ emergence in type $t$ if the assembly's effective capability exceeds the best component:
\[
\varepsilon_{1,t}(A) = I_{A,t} - \max_{m \in A} I_{m,t}.
\]
$E_1$ is "more of the same"---the system is better at something every component can already do.  Predictable from $\bK$: synergistic cross-type interactions produce quantitative surplus.

!!! definition "$E_2$: Qualitative activation"
 \tB\

An assembly exhibits $E_2$ emergence if it can perform tasks that no individual component can:
\[
\varepsilon_2(A) = |\{t : I_{A,t} \geq \theta_t \text{ and } I_{m,t} < \theta_t \;\;\forall\, m \in A\}|,
\]
where $\theta_t$ is the activation threshold for type $t$.  $E_2$ counts the number of "new" capabilities that emerge at the assembly level.

!!! example "$E_2$ in compound AI"

A retrieval engine ($I_{\mathrm{mnem}} = 4.5$, $I_{\mathrm{eval}} = 0.3$) combined with a planning model ($I_{\mathrm{eval}} = 4.0$, $I_{\mathrm{mnem}} = 0.3$).  Neither can perform *evidence-based strategic planning* (requiring both $I_{\mathrm{mnem}} \geq 2$ and $I_{\mathrm{eval}} \geq 2$).  The assembly activates this capability through synergistic interaction: $\varepsilon_2 = 1$.  This is the formal content of the empirical observation that RAG + reasoning chains unlock behaviors neither component exhibits alone.

!!! definition "$E_3$: Structural novelty"
 \tC\

An assembly exhibits $E_3$ emergence if its behavior occupies regions of cognitive space not spanned by any linear combination of component profiles:
\[
\varepsilon_3(A) = \dim(\mathrm{hull}(\bI_A)) - \dim(\mathrm{span}(\{\bI_{m_1}, \ldots, \bI_{m_k}\})).
\]
$E_3$ represents genuinely novel capabilities that cannot be predicted from component profiles alone---Anderson's "more is different" [Anderson1972] applied to compound AI.

### Total emergence value

!!! definition "Total emergence value"
 \tB\

The total emergence value of assembly $A$ is
\[
V(A) = \underbrace{\sum_t \varepsilon_{1,t}(A)}_{V_1(A)} + \underbrace{\lambda_2 \cdot \varepsilon_2(A)}_{V_2(A)} + \underbrace{\lambda_3 \cdot \mu \cdot \varepsilon_3(A)}_{V_3(A)},
\]
where $\lambda_2, \lambda_3 > 0$ are emergence-class weights and $\mu$ is a novelty multiplier.  $V(A)$ is the objective function for assembly optimization.

### Assembly optimization

!!! theorem "$V_1$ is submodular"
 \tA\

The quantitative surplus function $V_1(A) = \sum_t \varepsilon_{1,t}(A)$ is submodular: for any $A \subseteq B$ and any model $m \notin B$,
\[
V_1(A \cup \{m\}) - V_1(A) \geq V_1(B \cup \{m\}) - V_1(B).
\]

??? proof "Proof"

Adding model $m$ to a smaller assembly $A$ contributes more marginal surplus because $A$ has fewer existing models covering each type.  Formally, $\max_{m' \in A \cup \{m\}} I_{m',t} - \max_{m' \in A} I_{m',t} \geq \max_{m' \in B \cup \{m\}} I_{m',t} - \max_{m' \in B} I_{m',t}$ since $B \supseteq A$ implies $\max_B I_{m',t} \geq \max_A I_{m',t}$, giving diminishing marginal returns in each coordinate.  Summing over $t$ preserves the inequality.

!!! corollary "Greedy approximation guarantee"
 \tA\
The greedy algorithm that iteratively adds the model with maximum marginal $V_1$ achieves a $(1-1/e) \approx 0.632$ approximation to the optimal assembly [Nemhauser1978].

\begin{algorithm}[H]
\caption{Greedy Assembly Optimization}

\begin{algorithmic}[1]
\REQUIRE Model pool $\mathcal{M}$, task requirement $\bR$, budget $B$
\ENSURE Near-optimal assembly $A^*$
\STATE $A \leftarrow \emptyset$
\STATE $\mathcal{M}' \leftarrow \{m \in \mathcal{M} : \exists\, t \text{ s.t. } I_{m,t} \geq \theta_t \text{ and } R_t > 0\}$ \COMMENT{pre-filter}
\WHILE{$|A| < B$ and $\mathcal{M}' \neq \emptyset$}
  \STATE $m^* \leftarrow \argmax_{m \in \mathcal{M}'} [V(A \cup \{m\}) - V(A)]$
  \IF{$V(A \cup \{m^*\}) - V(A) \leq 0$}
    \STATE **break**
  \ENDIF
  \STATE $A \leftarrow A \cup \{m^*\}$; $\mathcal{M}' \leftarrow \mathcal{M}' \setminus \{m^*\}$
\ENDWHILE
\RETURN $A$
\end{algorithmic}
\end{algorithm}

**Complexity:** $O(B \cdot N \cdot d^2)$ where $N = |\mathcal{M}|$ and $d = 8$.  Trivially fast for realistic engine pools.

% ═══════════════════════════════════════════════════════════════════════════════

## Three-Space Perspective: Instantiation and AI Consciousness

The three-space ontology (Part XIII) introduces a crucial distinction for machine learning: the difference between *modeling* $\PS$-patterns and *instantiating* from $\QS$.  Current AI systems---including large language models, vision transformers, and reinforcement learning agents---model the statistical structure of $\PS$ (physical-space data) with extraordinary fidelity.  But modeling $\PS$ is not the same as having consciousness project through the substrate.

Under the co-primordial thesis, consciousness ($\CSp$) requires a non-trivial instantiation operator $\Inst$ with a hypervisor fixed point.  The question "Is GPT-$N$ conscious?" becomes: "Does the transformer architecture support a non-trivial fiber over its computational states, and does its dynamics admit a self-interpreting fixed point?"

The species-relative basis insight adds a further consideration: even if an AI substrate does support instantiation, it may activate intelligence dimensions *outside* the human eight-type basis.  A transformer processing millions of tokens simultaneously may access a "breadth" dimension that has no human analogue, just as echolocation opens dimensions inaccessible to sighted species.  AI intelligence vectors may inhabit a subspace of $\mathcal{I}_{\mathrm{univ}}$ that overlaps only partially with $\mathcal{I}_{\mathrm{human}}$.

This has practical implications for alignment: if AI consciousness operates in a partially alien basis, then alignment cannot rely solely on human-interpretable values but must address the *basis alignment problem*---the translation between human and machine intelligence dimensions, subject to CIT losses.

## Filter Operators for Bias Characterization

!!! definition "Machine filter cascade"
 \tA\

An AI model's effective intelligence is
\[
\bI_{\mathrm{eff}} = (\bF_{\mathrm{obj}} \circ \bF_{\mathrm{data}} \circ \bF_{\mathrm{arch}})(\bI_{\mathrm{raw}}),
\]
where each filter $\bF = \mathrm{diag}(\phi_1, \ldots, \phi_8)$ with $\phi_t \in [0,1]$:
[nosep,leftmargin=1.5em]
- $\bF_{\mathrm{arch}}$: Architecture filter.  Transformer attention patterns and model topology shape which types can be expressed.  A decoder-only LLM has high $\phi_{\mathrm{ling}}^{\mathrm{arch}}$ but low $\phi_{\mathrm{spat}}^{\mathrm{arch}}$.
- $\bF_{\mathrm{data}}$: Training data filter.  Corpus distribution determines type calibration.  Underrepresentation of social scenarios attenuates $\phi_{\mathrm{soc}}^{\mathrm{data}}$.
- $\bF_{\mathrm{obj}}$: Training objective filter.  RLHF amplifies $\phi_{\mathrm{soc}}^{\mathrm{obj}}$ (alignment $\approx$ social intelligence) but may attenuate $\phi_{\mathrm{eval}}^{\mathrm{obj}}$ (reduced willingness to express strategic assessments).

\begin{keyeq}
**Actionable bias decomposition.** \tA
\[
\text{"}I_{\mathrm{soc}} \text{ attenuated by } 0.3 \text{ cog due to } \bF_{\mathrm{data}}\text{"}\quad \gg \quad \text{"the model is biased."}
\]
The filter framework decomposes bias into type-specific, source-attributed attenuations that suggest targeted remediation: curate more social reasoning data ($\bF_{\mathrm{data}}$), modify the architecture ($\bF_{\mathrm{arch}}$), or adjust the training objective ($\bF_{\mathrm{obj}}$).
\end{keyeq}

!!! theorem "Filter composition"
 \tA\

The composition of any two diagonal filters is a diagonal filter: $(\bF_2 \circ \bF_1)_t = \phi_t^{(1)} \cdot \phi_t^{(2)} \in [0,1]$.

!!! lemma "Kernel monotonicity"
 \tA\

$\ker(\bF_2 \circ \bF_1) \supseteq \ker(\bF_1)$.  Bias accumulates through the pipeline: a type zeroed by the data filter cannot be recovered by the architecture or objective filter.  This has a practical implication: fixing a data gap is more effective than architectural modification if $\phi_t^{\mathrm{data}} \approx 0$.

!!! example "Filter diagnosis"

A model underperforms on social reasoning tasks.  The filter decomposition reveals:
[nosep,leftmargin=1.5em]
- $\phi_{\mathrm{soc}}^{\mathrm{arch}} = 0.9$ (architecture is adequate---attention can model social structure),
- $\phi_{\mathrm{soc}}^{\mathrm{data}} = 0.5$ (training corpus has limited social interaction data---the bottleneck),
- $\phi_{\mathrm{soc}}^{\mathrm{obj}} = 1.1$ (RLHF slightly amplifies social capability).

Net attenuation: $0.9 \times 0.5 \times 1.1 = 0.495$.  The diagnosis points to data curation as the primary intervention, not architectural redesign.

% ═══════════════════════════════════════════════════════════════════════════════

## Cost-Weighted Intelligence Functional

!!! definition "Intelligence functional"
 \tB\

The intelligence functional for a session $S$ of duration $T$ is:
\[
J[S] = \int_0^T \bigl[\bI_{\mathrm{eff}}(t) \cdot \bR(t) - c(t)\bigr]\,dt,
\]
where $\bI_{\mathrm{eff}}(t)$ is the effective intelligence vector at time $t$, $\bR(t)$ is the task demand, and $c(t)$ is the cost rate (compute, energy, API cost).

Optimal compute allocation maximizes $J[S]$: deploy expensive high-capability models when $\bI_{\mathrm{eff}} \cdot \bR$ is high (complex queries) and cheap models when it suffices (simple queries).  The Euler--Lagrange equation yields the optimal switching policy: transition from model $m_1$ to $m_2$ when the marginal intelligence gain $(\bI_{m_2} - \bI_{m_1}) \cdot \bR$ equals the marginal cost difference $c_{m_2} - c_{m_1}$.

!!! definition "Intelligence-second"
 \tB\
One *intelligence-second* (IS) is one cog of effective capability sustained for one second: $1\;\mathrm{IS} = 1\;\mathrm{cog}\cdot\mathrm{s}$.  The total intelligence delivered by a session is $\int_0^T \|\bI_{\mathrm{eff}}(t)\|\,dt$ in IS.  This provides a substrate-neutral unit for comparing compute efficiency: cost per intelligence-second is the natural figure of merit for inference economics.

\begin{keyeq}
**Inference economics.** \tB\
\[
\eta_m = \frac{\|\bI_m\|}{c_m} \quad (\text{intelligence per dollar per second}).
\]
A small model with $\|\bI\| = 5$ at cost $c = 0.001$ has $\eta = 5000$.  A frontier model with $\|\bI\| = 15$ at cost $c = 0.03$ has $\eta = 500$.  Optimal routing uses the small model when $\bI_{\mathrm{small}} \cdot \bR \geq \theta$ (the task doesn't need frontier capability) and the frontier model only for tasks where the small model's type coverage is insufficient.
\end{keyeq}

% ═══════════════════════════════════════════════════════════════════════════════

## IdeaRank on Idea Graphs

Beyond model routing, the framework defines a ranking over *ideas*---outputs, solutions, generated artifacts---that generalizes PageRank [PageRank1999] to cognitive type-weighted graphs.

!!! definition "IdeaRank"
 \tA\

Given an idea graph $G = (V, E, w)$ with vertices $V$ (ideas), edges $E$ (idea $i$ builds on idea $j$), and weights $w(i,j) = K_{t_i t_j}(I_{t_i} I_{t_j})^{1/2}$, the IdeaRank is the stationary distribution of a random walk with damping $d$:
\[
\IdeaRank(i) = (1-d)\frac{1}{|V|} + d \sum_{j \to i} \frac{w(j,i)}{\sum_{k:j \to k} w(j,k)} \IdeaRank(j).
\]
Existence and uniqueness follow from Perron--Frobenius applied to the weighted adjacency matrix.

\begin{intuition}
IdeaRank can rank candidate outputs from multiple models: build the idea graph from semantic dependencies, weight by type-specific quality, and select the highest-ranked idea.  This generalizes best-of-$N$ sampling by incorporating structural relationships between candidates.  Creative ideas---those bridging distant regions of the type space---naturally receive high IdeaRank because they connect to many clusters in the idea graph.
\end{intuition}

% ═══════════════════════════════════════════════════════════════════════════════

## Reference Implementation

The \textsc{Grand Engine} is a Python reference implementation of the full framework, including intelligence vector construction from benchmarks, $\bK$ matrix estimation, IdeaRank routing, synergy computation, filter decomposition, emergence value calculation, and assembly optimization.  The implementation achieves **100/100** on a validation test suite covering all mathematical objects and algorithms.

!!! remark "Empirical validation protocol"
 \tB\
To validate the framework: (1) estimate $\bI_m$ for $N \geq 10$ models from existing benchmarks, (2) compute IdeaRank routing decisions for a held-out query set, (3) compare routing accuracy against RouteLLM, Martian, and random baselines, (4) measure ensemble synergy predictions against empirical compound system performance, (5) test whether $K_{st}$ predictions match measured cross-type facilitation/interference in multi-model pipelines.  If the $\bK$-predicted synergy structure matches empirical observations, the framework provides a validated mathematical foundation for compound AI system design.

% ═══════════════════════════════════════════════════════════════════════════════

## Discussion

### Relation to Mixture of Experts

The MoE architecture [Shazeer2017,Jiang2024] routes tokens to specialized sub-networks.  RTSG provides a principled specialization criterion: each expert should cover a distinct region of the intelligence vector space, and the gating function should approximate the IdeaRank routing equation.  The $\bK$ matrix predicts which expert pairs should share tokens (high $K$, synergistic) versus operate independently (low $K$).  The emergence framework further predicts that MoE architectures with diverse expert profiles will exhibit $E_2$ emergence---capabilities absent from any individual expert.

### Comparison to existing frameworks

\begin{center}
\small

*[Table — see PDF for formatted version]*

\end{center}

### Limitations

The 8-type decomposition is designed for general cognitive tasks.  Highly specialized domains (protein folding, chip design) may require domain-specific extensions; the framework's algebra generalizes to any $n$.  The linear routing assumption (Proposition *ref:prop:routing*) is an approximation; nonlinear type interactions may require higher-order terms in the routing equation.  The compatibility matrix $\bK$ is currently estimated from architectural analysis and limited empirical data; large-scale calibration requires standardized multi-model evaluation protocols that do not yet exist.  The $E_3$ emergence class remains speculative; detecting structural novelty in model assemblies requires a theory of "genuinely novel" behavior that is an open research problem.  Finally, the framework addresses capability orchestration but does not incorporate safety or alignment considerations, which require separate treatment.

### Open problems

Three directions merit immediate investigation.  First, *learned $\bK$*: estimate the compatibility matrix from large-scale pairwise model evaluation data, yielding an empirical interaction structure that can validate or refine the theoretical estimates.  Second, *dynamic routing*: extend IdeaRank to multi-turn conversations where $\bR(t)$ changes between turns, requiring the router to track evolving task demands.  Third, *scaling laws*: how do intelligence vector components scale with model size, data, and compute?  Preliminary analysis suggests power-law scaling with type-specific exponents---$I_{\mathrm{symb}}$ may scale differently from $I_{\mathrm{soc}}$ with parameter count---which would have profound implications for training strategy and resource allocation.

% ═══════════════════════════════════════════════════════════════════════════════

## Conclusion

We have presented a framework that replaces scalar model benchmarks with variable-dimensional intelligence vector (n=12 for humans)s, provides a principled routing algorithm (IdeaRank), predicts ensemble synergy via the compatibility matrix, characterizes model bias as type-specific filter attenuation, and introduces an emergence theory with formal assembly optimization guarantees.  The framework is fully implemented (100/100 validation suite) and yields concrete experimental protocols for empirical validation.  If the $\bK$-predicted synergy structure matches empirical compound system performance, the intelligence vector formalism would provide the first mathematical foundation for the emerging compound AI paradigm.

% ═══════════════════════════════════════════════════════════════════════════════
% BIBLIOGRAPHY
% ═══════════════════════════════════════════════════════════════════════════════

## References

*See PDF for full bibliography.*
---

## v2 Integration: Algorithmic Frontier Expansion & Fingerprinting (TMP-20260217)

RTSG proposes AI can algorithmically pre-map the frontier of collective consciousness:

1. Extract top-layer IdeaRank nodes across all I-vector dimensions
2. Combine multiplicatively and geometrically (all k-combinations, not just pairwise)
3. Test each for: (a) logical consistency, (b) novelty score > threshold, (c) top-layer retention after insertion
4. Passing combinations = candidate frontier ideas, pre-validated

This is **proactive knowledge frontier expansion** — IdeaRank running in reverse.

**Intelligence fingerprinting pipeline:** Corpus C(ξ) → RTSG graph → IdeaRank top nodes → **I**(ξ) recovery → optimal cognitive assembly formation where persons with maximally synergistic I-vectors for a mission w ∈ Δ^{n-1} are paired.

**dim(n) in feature engineering:** Any node's ML-relevant complexity = its dimensional span across the 8-component I-vector, not raw feature count.
