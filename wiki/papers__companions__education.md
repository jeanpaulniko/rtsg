---
title: "Education Companion Paper"
version: "2.0.0"
last_updated: "2026-03-05"
status: ARXIV-READY
arxiv_category: "cs.AI"
---

# Education Companion Paper

**Jean-Paul Niko** · February 2026

% ═══════════════════════════════════════════════════════════════════════════════

\title{\textcolor{sectionblue}{**Attention Simplices, Filter Plasticity,  
and the Geometry of Learning:  [0.3em]
A Mathematical Framework for Pedagogy  
and Educational Equity**}}

\author{Jean-Paul Niko  
  
\small `triptomean.com`}

\date{February 2026}

!!! abstract "Abstract"
    
We present a mathematical framework for learning, teaching, and educational equity grounded in the Intelligence as Geometry (RTSG) theory.  Learning is modeled as expansion of the accessible region of the *attention simplex* $\Delta^7$---the space of possible attention allocations across eight cognitive types.  Novices are confined to small simplex regions; experts move fluidly across the full simplex, deploying multiple types simultaneously.  Deliberate practice is systematic exploration of new simplex regions under guidance.  The *Heyting Gap*---the irreducible difference between an expert's and a novice's conceptual systems---is proven to grow monotonically with mastery, formalizing the "curse of expertise" in teaching and yielding the prediction that the optimal teacher is not the greatest expert but the person whose Gap relative to the student matches the Zone of Proximal Development.  An *intelligence filter formalism* models educational equity: "achievement gaps" are recast as *filter gaps*---differences in the developmental and cultural filters applied to raw intelligence---making the origin of inequality mathematically explicit and interventions evaluable by which filter component they modify.  The *compatibility matrix* $\bK$ provides a principled basis for curriculum sequencing: subjects should be ordered to exploit high-$K$ type pairs that produce cross-curricular synergy.  Kahneman's System 1 and System 2 are formalized as low-friction and high-friction trajectories on the simplex, with learning defined as the conversion of System 2 paths to System 1 paths through practice.  Cognitive thermodynamics provides a theory of motivation: "stuck" students occupy local minima in the learning energy landscape, intrinsic motivation is the gradient toward deeper basins, and flow is a trajectory with optimal challenge level.  Finally, per-type ELO ratings replace scalar standardized tests with eight-dimensional adaptive assessment.

**Keywords:** learning theory, attention simplex, expertise, Zone of Proximal Development, educational equity, curriculum design, cognitive thermodynamics, adaptive assessment

---

% ═══════════════════════════════════════════════════════════════════════════════

## Introduction

% ═══════════════════════════════════════════════════════════════════════════════

Learning is the central phenomenon that education seeks to facilitate, yet we lack a unified mathematical framework for its structure.  Piaget's [Piaget1952] developmental stages, Vygotsky's [Vygotsky1978] Zone of Proximal Development (ZPD), Kahneman's [Kahneman2011] dual-process theory, Csikszentmihalyi's [Csikszentmihalyi1990] flow, Ericsson's [Ericsson1993] deliberate practice, and Bloom's [Bloom1984] 2-sigma result each capture important aspects of learning, but they remain separate theories with separate vocabularies and no common mathematical substrate.

This paper provides that substrate, drawing on the Intelligence as Geometry (RTSG) theory [Niko2026].  The core insight is that learning is not merely the accumulation of knowledge but the *expansion of cognitive capacity across multiple types simultaneously*, and that this expansion can be modeled geometrically as movement through a well-defined mathematical space.

The contributions are fourfold.  First, we model learning as simplex expansion and derive the curse of expertise as a theorem.  Second, we formalize educational equity as a filter distribution problem.  Third, we derive curriculum sequencing principles from the compatibility matrix.  Fourth, we propose per-type ELO ratings as a replacement for scalar standardized tests.

% ═══════════════════════════════════════════════════════════════════════════════

## The Attention Simplex and Learning

% ═══════════════════════════════════════════════════════════════════════════════

!!! definition "Attention Simplex"
 \tA{}
The *attention simplex* is:
\[
\Delta^7 = \left\{(\lambda_1, \ldots, \lambda_8) \in \\mathbb{R}^{n(e)}_{\geq 0} : \sum_{t=1}^8 \lambda_t = 1\right\}
\]
where $\lambda_t$ is the fraction of cognitive resources allocated to type $t$.  At any moment, an agent's attention is a point on $\Delta^7$.

The simplex constraint captures the fundamental scarcity of attention: allocating more to one type necessarily reduces what is available for others.  A vertex of $\Delta^7$ represents total concentration on a single type; the centroid represents equal allocation across all eight.

!!! definition "Accessible Region"
 \tB{}
For a learner with current intelligence vector $\bI$, the *accessible region* $\mathcal{A}(\bI) \subseteq \Delta^7$ is the set of attention allocations the learner can sustain productively:
\[
\mathcal{A}(\bI) = \{\lambda \in \Delta^7 : I_t \cdot \lambda_t \geq \theta_t \text{ for all } t \text{ with } \lambda_t > 0\}
\]
where $\theta_t$ is the minimum effective capacity required to productively deploy type $t$.

!!! proposition "Learning as Simplex Expansion"
 \tB{}
Learning is the expansion of the accessible region $\mathcal{A}(\bI)$.  A novice has a small accessible region (can only productively deploy one or two types at a time); an expert has a large accessible region (can fluidly combine multiple types).
\begin{keyeq}
\[
\text{Learning:} \quad \mathcal{A}(\bI_{t_1}) \subset \mathcal{A}(\bI_{t_2}) \quad \text{for } t_1 < t_2
\]
\end{keyeq}

\begin{intuition}
A beginning pianist can only attend to one hand at a time (near-vertex attention on $\Delta^7$).  An expert pianist simultaneously manages melody, harmony, rhythm, dynamics, and emotional expression---a point deep in the interior of $\Delta^7$ that deploys five or six cognitive types at once.  The journey from beginner to expert is the progressive expansion of the accessible region from a small neighborhood of a vertex to a large interior volume.
\end{intuition}

### Deliberate practice as simplex exploration

Ericsson's [Ericsson1993] concept of deliberate practice---effortful, structured practice at the edge of current ability---maps precisely to the boundary of the accessible region.

!!! proposition "Deliberate Practice Formalized"
 \tB{}
Deliberate practice is systematic exploration of the boundary $\partial \mathcal{A}(\bI)$: the learner attempts attention allocations just outside their current accessible region, gradually expanding it.  Unstructured practice (staying well within $\mathcal{A}$) does not expand the region; it only makes existing trajectories more efficient.

% ═══════════════════════════════════════════════════════════════════════════════

## The Curse of Expertise: Heyting Gap Monotonicity

% ═══════════════════════════════════════════════════════════════════════════════

The most consequential result for teaching is the monotonic growth of the Heyting Gap with mastery.

!!! definition "Heyting Gap"
 \tB{}
The *Heyting Gap* $\Hgap(E, N)$ between an expert $E$ and a novice $N$ measures the irreducible difference between their conceptual systems:
\[
\Hgap(E, N) = \|\bI_E^{\mathrm{eff}} - \bI_N^{\mathrm{eff}}\|_{\mathrm{concept}}
\]
where $\|\cdot\|_{\mathrm{concept}}$ measures distance in the space of expressible concepts.

!!! theorem "Gap Monotonicity"
 \tA{}
The Heyting Gap grows monotonically with expertise:
\[
\frac{d\,\Hgap(E, N)}{d\,\|\bI_E\|} > 0
\]
Experts literally *cannot* losslessly translate their understanding into novice terms.  The more expert they become, the larger the Gap---this is a theorem, not a failing of pedagogy.

!!! corollary "Optimal Teacher Theorem"
 \tB{}
The optimal teacher for a student at level $\bI_N$ is *not* the greatest expert (who has the largest Gap) but the person whose Heyting Gap relative to the student is small enough to permit translation yet large enough to lead:
\begin{keyeq}
\[
\bI_{\mathrm{teacher}}^* = \arg\min_{\bI_T} \left|\Hgap(T, N) - \text{ZPD}(N)\right|
\]
\end{keyeq}
where $\text{ZPD}(N)$ is the width of the student's Zone of Proximal Development.

\begin{intuition}
This formalizes a finding familiar to every educator: brilliant researchers are often poor lecturers, while near-peer tutors are often excellent.  The RTSG framework explains why: the researcher's Heyting Gap is too large for the student's ZPD---the translation loss overwhelms the content being communicated.  The near-peer tutor, being only slightly ahead, has a Gap that matches the ZPD.  Bloom's [Bloom1984] 2-sigma result---that one-on-one tutoring produces two standard deviations of improvement---is partly explained by the Gap-matching that personalized tutoring enables.
\end{intuition}

### Vygotsky's ZPD formalized

!!! definition "Zone of Proximal Development"
 \tB{}
The *Zone of Proximal Development* is the annular region of the attention simplex just beyond the current accessible region:
\[
\text{ZPD}(N) = \{\lambda \in \Delta^7 : \lambda \notin \mathcal{A}(\bI_N) \text{ but } \lambda \in \mathcal{A}(\bI_N + \delta\bI) \text{ for small } \delta\bI\}
\]
Tasks in the ZPD are too difficult for the student to accomplish alone but achievable with appropriate scaffolding---which, in RTSG terms, means a teacher whose Heyting Gap spans exactly the ZPD width.

% ═══════════════════════════════════════════════════════════════════════════════

## Filter Formalism for Educational Equity

% ═══════════════════════════════════════════════════════════════════════════════

The filter formalism reframes educational inequality as a precise mathematical problem.

!!! definition "Developmental Filter"
 \tA{}
The developmental filter $\Phi_{\mathrm{dev}} = \operatorname{diag}(\phi_1^{\mathrm{dev}}, \ldots, \phi_8^{\mathrm{dev}})$ models how socioeconomic conditions shape cognitive development:
\[
\bI_{\mathrm{eff}} = \Phi_{\mathrm{dev}}(\bI_{\mathrm{raw}})
\]
$\Phi_{\mathrm{dev}}$ varies with access to nutrition, enrichment, environmental stability, and educational quality.

!!! definition "Cultural Filter"
 \tA{}
The cultural filter $\Phi_{\mathrm{cult}} = \operatorname{diag}(\phi_1^{\mathrm{cult}}, \ldots, \phi_8^{\mathrm{cult}})$ encodes which cognitive types are valued, practiced, and reinforced in the student's cultural environment.

!!! proposition "Achievement Gaps as Filter Gaps"
 \tA{}
Observed "achievement gaps" between demographic groups decompose as:
\begin{keyeq}
\[
\underbrace{\text{Outcome gap}}_{\text{observed}} = \underbrace{\text{Raw gap}}_{\approx 0} + \underbrace{\text{Filter gap}}_{\|(\Phi_A - \Phi_B) \bar{\bI}_{\mathrm{raw}}\|}
\]
\end{keyeq}
If raw intelligence distributions are similar across groups (as genetic evidence suggests), then outcome gaps are almost entirely *filter gaps*---differences in developmental and cultural environments, not in intrinsic capacity.

\begin{intuition}
This formalizes what Ladson-Billings [LadsonBillings2006] calls the shift from "achievement gap" to "education debt": the debt is the accumulated filter differential---generations of unequal access to developmental resources that have produced unequal effective intelligence, not because of different raw capacity but because of different filters applied to similar raw material.
\end{intuition}

### Test bias formalized

!!! proposition "Test Bias as Filter Mismatch"
 \tB{}
A test designed under filter $\Phi_A$ measures $\Phi_A(\bI_{\mathrm{raw}})$, not $\bI_{\mathrm{raw}}$.  When administered to students developed under filter $\Phi_B$, the test measures neither raw intelligence nor $\Phi_B$-effective intelligence but the doubly-filtered $\Phi_A \circ \Phi_B(\bI_{\mathrm{raw}})$, which systematically underestimates capacity in types where $\Phi_A$ and $\Phi_B$ diverge.

### Evaluating equity interventions

Each equity intervention targets a specific filter component:

\begin{center}

*[Table — see PDF for formatted version]*

\end{center}

The framework enables *targeted* equity investment: diagnose which filter component produces the largest gap for a specific population, then invest in the intervention that modifies that component.

% ═══════════════════════════════════════════════════════════════════════════════

## Compatibility Matrix and Curriculum Design

% ═══════════════════════════════════════════════════════════════════════════════

The compatibility matrix $\bK$ provides a principled basis for curriculum sequencing.

!!! definition "Compatibility Matrix"
 \tA{}
The compatibility matrix $\bK \in \R^{8 \times 8}$ encodes pairwise interaction between cognitive types.  When $K_{st} > 1$, engaging type $s$ facilitates subsequent engagement with type $t$ (synergy); when $K_{st} < 1$, it hinders (interference).

!!! proposition "Optimal Sequencing Principle"
 \tB{}
Curriculum subjects should be sequenced to exploit high-$K$ pairs.  If $K_{\mathrm{spat,symb}} = 1.3$ (spatial reasoning facilitates symbolic reasoning) while $K_{\mathrm{soc,symb}} = 0.6$ (social reasoning interferes with symbolic reasoning), then spatial reasoning should precede algebra in the daily schedule, not follow social studies.

!!! example "Cross-Curricular Integration"
 \tB{}
Cross-curricular projects are most effective when they combine types with high $K$ values:
[nosep]
- Music + Mathematics ($K_{\mathrm{aud,symb}}$ high): rhythmic patterns reinforce algebraic structure
- Art + Science ($K_{\mathrm{spat,Mu}}$ high): spatial visualization supports scientific observation
- Drama + Language Arts ($K_{\mathrm{kin,ling}}$ moderate): embodied performance deepens textual comprehension
- History + Creative Writing ($K_{\mathrm{eval,ling}}$ high): evaluative reasoning enriches narrative construction

The prediction is testable: randomize curriculum sequences, measure outcomes, compare to $\bK$ predictions.

% ═══════════════════════════════════════════════════════════════════════════════

## Kahneman's System 1 and System 2 Formalized

% ═══════════════════════════════════════════════════════════════════════════════

Kahneman's [Kahneman2011] dual-process theory receives a geometric interpretation on the attention simplex.

!!! definition "System 1: Automatic Processing"
 \tB{}
System 1 processing corresponds to low-friction, well-worn trajectories on $\Delta^7$---attention paths that the agent can traverse with minimal cognitive effort because they have been practiced to automaticity.  These trajectories lie deep within the accessible region $\mathcal{A}(\bI)$.

!!! definition "System 2: Deliberate Processing"
 \tB{}
System 2 processing corresponds to high-friction, deliberate movement to unusual regions of $\Delta^7$---attention allocations that the agent can sustain only with effortful concentration.  These trajectories lie near the boundary of $\mathcal{A}(\bI)$ or within the ZPD.

!!! proposition "Learning as Friction Reduction"
 \tB{}
\begin{keyeq}
\[
\text{Learning} = \text{Converting System 2 paths} \to \text{System 1 paths}
\]
\end{keyeq}
Through practice, a trajectory that initially requires effortful System 2 processing becomes automatic System 1 processing.  The friction along that trajectory decreases until it becomes part of the agent's habitual repertoire.

\begin{intuition}
Learning to drive is the paradigmatic example.  Initially, every component (steering, shifting, checking mirrors, navigating) requires separate attention allocation---the student operates near the boundary of their accessible region with high friction.  With practice, these components become automatic, freeing attention for higher-order tasks (route planning, conversation, hazard anticipation).  The trajectories that were System 2 become System 1, and the freed capacity expands the accessible region further.
\end{intuition}

% ═══════════════════════════════════════════════════════════════════════════════

## Cognitive Thermodynamics and Motivation

% ═══════════════════════════════════════════════════════════════════════════════

The RTSG framework includes a cognitive thermodynamics that provides a theory of learning motivation.

!!! definition "Learning Energy Landscape"
 \tB{}
The learning energy landscape is a function $E: \Delta^7 \to \R$ where $E(\lambda)$ measures the cognitive effort required to sustain attention allocation $\lambda$.  Local minima correspond to stable cognitive states ("comfort zones"); the global minimum corresponds to the default attention allocation.

!!! proposition "Stuck Students as Local Minima"
 \tB{}
A "stuck" student is one trapped in a local minimum of the learning energy landscape---a stable cognitive state that is suboptimal but requires energy input to escape.  The depth of the minimum determines how much external motivation or restructuring is needed to dislodge the student.

!!! definition "Intrinsic Motivation as Free Energy"
 \tB{}
Intrinsic motivation corresponds to the gradient toward deeper basins in the learning landscape:
\[
\mathbf{F}_{\mathrm{intrinsic}} = -\nabla E_{\mathrm{curiosity}}(\lambda)
\]
Curiosity creates a landscape where unexplored regions have lower energy, providing a natural gradient toward learning.  Extrinsic motivation is an externally imposed energy input that lifts the student out of a local minimum.

!!! proposition "Flow as Optimal Friction"
 \tB{}
Csikszentmihalyi's [Csikszentmihalyi1990] *flow* state is a trajectory through $\Delta^7$ where the challenge level is optimally matched to the student's current accessible region:
\[
\text{Flow:} \quad \lambda(t) \in \partial \mathcal{A}(\bI) \quad \text{with friction } F = F_{\mathrm{optimal}}
\]
Friction too high: anxiety (the task exceeds the accessible region by too much).  Friction too low: boredom (the task lies entirely within the accessible region).  Flow is the boundary condition---challenging enough to require full engagement but manageable enough to sustain momentum.

% ═══════════════════════════════════════════════════════════════════════════════

## ELO Ratings for Adaptive Assessment

% ═══════════════════════════════════════════════════════════════════════════════

The RTSG framework replaces scalar standardized tests with per-type ELO ratings.

!!! definition "Per-Type ELO"
 \tB{}
Each student maintains eight ELO ratings $\{R_t\}_{t=1}^8$, one per cognitive type.  Each assessment item has a difficulty vector $\mathbf{d} \in \\mathbb{R}^{n(e)}$ specifying the cognitive demands per type.  The predicted probability that student $s$ succeeds on item $i$ is:
\begin{keyeq}
\[
P(s \text{ succeeds on } i) = \sigma\left(\sum_t R_{s,t} \cdot d_{i,t} - D_i\right)
\]
\end{keyeq}
where $\sigma$ is the logistic function and $D_i$ is the item's overall difficulty.  After each response, all relevant $R_{s,t}$ are updated via the standard ELO update rule.

!!! proposition "Diagnostic Advantage"
 \tB{}
Per-type ELO provides diagnostic information that scalar scores cannot: eight ratings show *where* a student is strong or weak, not just *whether* they are.  This enables targeted intervention---resources are directed to the specific types where the student's ratings are below the threshold for their grade level.

!!! proposition "Reduced Cultural Loading"
 \tB{}
Per-type ELO is less culturally loaded than scalar standardized tests because the cultural filter $\Phi_{\mathrm{cult}}$ is modeled explicitly.  If a student's low $R_L$ is attributable to $\Phi_{\mathrm{cult}}$ (e.g., English is their second language) rather than to low raw $I_L$, the system can distinguish this from genuine linguistic deficit by examining the pattern of $R_t$ across types.

!!! example "Adaptive Assessment in Practice"
 \tB{}
A student takes an adaptive math test.  Early items probe multiple types: a spatial reasoning item ($d_S$ high), a symbolic manipulation item ($d_G$ high), a word problem ($d_L$ high).  The student excels at spatial items but struggles with word problems.  The system updates: high $R_S$, moderate $R_G$, low $R_L$.  Subsequent items probe the boundary between spatial and symbolic reasoning to refine the profile.  The final output is not "75th percentile in math" but a vector $(R_L, R_G, R_S, \ldots)$ that reveals the student has strong mathematical intuition ($R_S$) that is masked by linguistic challenges ($R_L$) in traditional testing.

% ═══════════════════════════════════════════════════════════════════════════════

## Testable Predictions

% ═══════════════════════════════════════════════════════════════════════════════

[nosep]

- **Optimal teacher matching.**  Students paired with tutors whose Heyting Gap matches their ZPD will show greater learning gains than students paired with either near-peer tutors (Gap too small) or expert tutors (Gap too large).  *Test*: measure tutor and student profiles, compute Gap, predict and verify learning outcomes.

- **Curriculum sequencing.**  Schools that sequence subjects according to $\bK$ predictions (high-$K$ pairs adjacent in the schedule) will show higher achievement gains than schools with random or traditional sequencing.  *Test*: randomized trial of $\bK$-optimized versus traditional daily schedules.

- **Filter gap decomposition.**  Within-school achievement gaps will be better predicted by developmental and cultural filter proxies (family income, enrichment access, home language) than by ability estimates.  *Test*: structural equation modeling with filter variables.

- **Deliberate practice boundary.**  Students practicing at the boundary of their accessible region (measured via adaptive assessment showing items at their frontier) will show faster simplex expansion than students practicing well within their accessible region.  *Test*: compare learning rates for students assigned frontier versus comfort-zone practice items.

- **Flow prediction.**  Student engagement (measured via self-report or physiological indicators) will be maximized when task difficulty places the student at the boundary of their accessible region.  *Test*: titrate difficulty in real time and measure engagement curves.

- **ELO diagnostic accuracy.**  Per-type ELO profiles will predict student performance on novel tasks more accurately than scalar standardized test scores.  *Test*: compute both measures, predict performance on out-of-sample tasks, compare predictive validity.

% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
Three-Space Education}

The three-space ontology provides a foundational justification for curriculum design.

**Curriculum recapitulates complexification.**  The optimal curriculum sequence follows the same path as cosmic complexification: from foundational convergence conditions (basic concepts) through increasing complexity, activating new intelligence dimensions in the order that maximizes $K$-synergy.  Just as the universe progressed from proto-consciousness (gravity) through chemistry to biology to cognition, a curriculum progresses from sensorimotor foundations through symbolic tools to abstract reasoning to creative synthesis.

**Developmental filters as personal complexification.**  Each student's developmental filter $F_{\mathrm{dev}}$ represents their personal position on the complexification journey.  Education is the deliberate acceleration of $F_{\mathrm{dev}}$ along the convergence-condition sequence.  The teacher's role is to identify the student's current convergence frontier---the set of $\QS$-structures the student is ready to instantiate---and provide the scaffolding for the next instantiation.

**IdeaRank as curriculum ordering.**  Foundation ideas (high IdeaRank) should be taught first because they are convergence conditions: their instantiation opens access to entire regions of $\QS$-structure that remain inaccessible without them.  Teaching peripheral ideas before foundations wastes instantiation capacity on structures that cannot be connected to the larger framework.

## Discussion

% ═══════════════════════════════════════════════════════════════════════════════

This paper has introduced a mathematical framework for education that unifies several influential theories under a common geometric structure.  The key contributions are:

The *simplex model of learning* provides a visual and computational framework for understanding skill development as expansion of accessible cognitive space.  This connects Piaget's developmental stages (qualitative shifts in accessible region), Vygotsky's ZPD (the boundary zone), Ericsson's deliberate practice (boundary exploration), and Csikszentmihalyi's flow (optimal boundary engagement) within a single mathematical object.

The *Gap Monotonicity Theorem* formalizes the curse of expertise and yields a concrete, testable prediction about optimal teacher--student matching.  This has immediate practical implications for tutoring programs, professional development, and the design of AI-powered educational systems that must calibrate their explanatory sophistication to the learner's level.

The *filter equity framework* provides a precise language for diagnosing educational inequality that moves beyond blame ("these students aren't trying") and beyond vague structural critique ("the system is unfair") to a specific decomposition: *which filter components are responsible for the gap, and which interventions target those components?*  This enables evidence-based equity investment with measurable targets.

The *$\bK$-based curriculum design* is immediately testable and, if validated, would provide a principled alternative to traditional curriculum sequencing that is based largely on historical convention.  The prediction that spatial reasoning should precede algebra---because $K_{\mathrm{spat,symb}}$ is high---is specific, falsifiable, and actionable.

Limitations include the simplified eight-type model, the challenge of estimating $\bK$ empirically, and the assumption that the attention simplex is seven-dimensional (real attention may have more or fewer effective dimensions depending on context).  The framework is intentionally parsimonious; richer models will be needed for fine-grained instructional design.

The deepest implication is philosophical.  The Gap Monotonicity Theorem means that *perfect* teaching is impossible in principle: the very mastery that makes someone knowledgeable creates an irreducible barrier to communicating that knowledge.  This is not a defeatist conclusion---it redirects attention from the impossible goal of eliminating the Gap to the achievable goal of *matching* the Gap to the learner.  The best education system is not one that hires the smartest teachers but one that ensures every student has access to a teacher whose Heyting Gap relative to them is in the ZPD sweet spot.  This is a solvable engineering problem with the right assessment infrastructure.

% ═══════════════════════════════════════════════════════════════════════════════
% BIBLIOGRAPHY
% ═══════════════════════════════════════════════════════════════════════════════

## References

*See PDF for full bibliography.*
---

## v2 Integration: dim(n) in Pedagogy & Adaptive Learning (TMP-20260217)

**dim(n) as curriculum complexity measure:** Concepts with dim = 1 require single-modality instruction. Concepts with dim ≥ 5 require multi-modal scaffolding activating all required I-vector dimensions simultaneously.

**Intelligence fingerprinting for adaptive learning:** Corpus C(student) → **I**(student) — actual I-vector profile, not self-reported. More robust to self-report bias and social desirability effects than standard instruments.

**Basic English ratio** as lightweight complexity proxy: higher ratio = more basic words needed = deeper concept = more instructional scaffolding required.

**Cooperative assembly:** Optimal learning groups are assembled by maximizing I-vector synergy across members for the specific learning objective — the cooperative Nash equilibrium of the classroom.

---

## Extended Formalizations *(v2 — 2026)*

### Heyting Gap and Bloom's 2-Sigma Result

The *Heyting Gap* is the cognitive distance between teacher and student — the measure of how many filter steps separate their current accessible regions. Bloom's (1984) 2-sigma result — one-on-one tutoring produces two standard deviations of improvement — is partly explained by Gap-matching that personalized tutoring enables. A researcher's Heyting Gap is too large for the student's ZPD: the translation loss overwhelms the content. A near-peer tutor, being only slightly ahead, has a Gap that matches the ZPD precisely.

**Formal criterion:** Optimal teaching occurs when the teacher's accessible region extends just beyond the boundary of the student's ZPD — not so far that translation fails, not so close that no new region is exposed.

### Achievement Gap as Filter Differential

Ladson-Billings' (2006) shift from "achievement gap" to "education debt" receives formal expression: the debt is the accumulated filter differential — generations of unequal access to developmental resources that have produced unequal effective intelligence. Not different raw capacity. Different filters applied to similar raw material.

$$\text{Education debt}(\xi) = \int_0^T \left[\Phi_{\text{optimal}}(\tau) - \Phi_{\text{actual}}(\xi, \tau)\right] d\tau$$

### Dual-Process Theory on the Attention Simplex

Kahneman's (2011) dual-process theory receives geometric interpretation on the attention simplex Δ⁷:
- **System 1** = automatic trajectory along learned edges of Δ⁷ (low α cost, high speed)  
- **System 2** = deliberate traversal requiring sustained α-allocation (high cost, slow, accurate)

Flow state (Csikszentmihalyi 1990) is a trajectory through Δ⁷ where challenge level is optimally matched to the student's current accessible region — Lyapunov exponent λ just below 0, minimum noise σ, maximum drift α.
