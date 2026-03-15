---
title: "Neuroscience Companion Paper"
version: "2.0.0"
last_updated: "2026-03-05"
status: ARXIV-READY
arxiv_category: "q-bio.NC"
---

# Neuroscience Companion Paper

**Jean-Paul Niko** · February 2026

\begin{center}
{\LARGE\bfseries\color{sectionblue} A Geometric Framework for Multi-Type Intelligence:  
Filter Operators, Attention Dynamics, and Predictions  [3pt] for Neuroimaging}

{\large Jean-Paul Niko}  [4pt]
{}  [2pt]
{\small`niko@triptomean.com`}

{\small February 2026}
\end{center}

!!! abstract "Abstract"
    
We present a mathematical framework in which cognitive capacity is represented not by
a scalar (such as $g$) but by an *intelligence vector*
$\bI = (I_{\mathrm{ling}}, I_{\mathrm{symb}}, I_{\mathrm{spat}},
I_{\mathrm{kin}}, I_{\mathrm{aud}}, I_{\mathrm{soc}}, I_{\mathrm{intra}},
I_{\mathrm{nat}}) \in \\mathbb{R}^{n(e)}_{\geq 0}$,
whose components correspond to distinguishable neural circuit families.
Interactions between intelligence types are governed by a symmetric
compatibility matrix $\bK \in \R^{8\times 8}$, interpretable as a functional
connectivity prediction: $K_{ij} > 1$ predicts positive coupling between
circuits $i$ and $j$; $K_{ij} < 1$ predicts competitive inhibition.
Attentional allocation evolves on the 7-simplex $\Delta^7$ via replicator
dynamics---the same equations governing evolutionary population genetics---and
we prove that KL divergence from equilibrium is a Lyapunov function, guaranteeing
convergence.  Five species of *filter operator*
$\Phi_{\mathrm{env}} \circ \Phi_{\mathrm{dev}} \circ \Phi_{\mathrm{cog}} \circ
\Phi_{\mathrm{soc}} \circ \Phi_{\mathrm{cult}}$
transform raw capacity into effective intelligence; each has a characteristic
neural timescale from evolutionary ($10^6$ yr) to attentional (ms).  We derive
a cognitive thermodynamics whose Second Law predicts task-switching metabolic cost,
connect the framework to Global Workspace Theory via spectral decomposition of the
compatibility matrix, and catalog twelve quantitative predictions testable with
existing neuroimaging equipment (fMRI, EEG/MEG, PET).

**Keywords:** multi-type intelligence, functional connectivity,
replicator dynamics, attention simplex, cognitive filters, neuroimaging predictions

%% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
Introduction}
%% ═══════════════════════════════════════════════════════════════════════════════

The dominant quantitative tradition in intelligence research relies on a single
latent factor---Spearman's $g$---extracted from covariance matrices of cognitive
test batteries [spearman1904,carroll1993].  While the positive manifold is
a robust empirical phenomenon, collapsing an individual's cognitive profile to
one number discards the rich structure that neuroimaging reveals.  Functional
connectivity analyses show that language, spatial, social, and executive
circuits form distinguishable networks with characteristic coupling patterns
[yeo2011,bassett2017], yet no algebraic framework maps these networks to
a vector-valued intelligence measure whose components can be independently
manipulated and whose interactions are formally specified.

This paper introduces such a framework.  We define the intelligence vector
$\bI \in \\mathbb{R}^{n(e)}_{\geq 0}$ (Section *ref:sec:vector*), derive the compatibility
matrix $\bK$ governing cross-type interactions (Section *ref:sec:kmatrix*),
model attentional dynamics as replicator flow on the simplex
(Section *ref:sec:attention*), introduce filter operators that transform raw
capacity into effective intelligence (Section *ref:sec:filters*), develop a
cognitive thermodynamics that predicts metabolic cost
(Section *ref:sec:thermo*), connect the hypervisor construct to Global
Workspace Theory (Section *ref:sec:gwt*), and catalog twelve testable
neuroimaging predictions (Section *ref:sec:predictions*).

Throughout, we mark each result with an epistemic tier: \tA{} for results that
are proved or definitional, \tB{} for well-supported models with formal
structure, and \tC{} for conjectural extensions.

%% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
The Intelligence Vector}
%% ═══════════════════════════════════════════════════════════════════════════════

!!! definition "Intelligence Vector"
 \tA{}
The *intelligence vector* of an agent $a$ is

\[
\bI(a) = \bigl(I_{\mathrm{ling}},\; I_{\mathrm{symb}},\; I_{\mathrm{spat}},\;
I_{\mathrm{kin}},\; I_{\mathrm{aud}},\; I_{\mathrm{soc}},\;
I_{\mathrm{intra}},\; I_{\mathrm{nat}}\bigr) \in \\mathbb{R}^{n(e)}_{\geq 0}.
\]

Each component $I_t$ is a non-negative real number measured in *cognitive
units* (cog), defined as the capacity to sustain one standard deviation of
performance in type-$t$ tasks per unit time.

\begin{keyeq}
**Key Equation.**\quad
$\bI \in \\mathbb{R}^{n(e)}_{\geq 0}$, \quad with components measured in cog units and
calibrated via ELO-style pairwise tournaments within each type.
\end{keyeq}

The eight types are not arbitrary.  Each maps to an identifiable neural circuit
family:

\begin{center}

*[Table — see PDF for formatted version]*

\end{center}

\begin{intuition}
**Neural grounding.**\quad The vector representation predicts that selectively
lesioning circuit family $t$ should reduce $I_t$ while leaving other components
largely intact---consistent with classical double-dissociation findings
[poldrack2006] and the multiple-demand (MD) network literature [duncan2010].
\end{intuition}

!!! remark "Relation to CHC and Gardner"
 \tB{}
The eight types subsume the broad abilities of Cattell--Horn--Carroll theory
[carroll1993,mcgrew2009] and formalize Gardner's multiple intelligences
[gardner1983] by adding algebraic structure: the $\bK$ matrix
(Section *ref:sec:kmatrix*) specifies interactions that neither factor-analytic
models nor Gardner's framework provides.

The scalar $\|\bI\| = \sqrt{\sum_t I_t^2}$ recovers an analogue of $g$, but
the full vector is strictly more informative.  Two agents with identical
$\|\bI\|$ may have radically different cognitive profiles---and different
neuroimaging signatures.

%% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
The Compatibility Matrix}
%% ═══════════════════════════════════════════════════════════════════════════════

!!! definition "Compatibility Matrix"
 \tA{}
The *compatibility matrix* is a symmetric, positive semi-definite
matrix $\bK \in \R^{8 \times 8}$ with entries $K_{ij} \geq 0$, where:
[nosep]
- $K_{ii} = 1$ (self-compatibility is the identity).
- $K_{ij} > 1$: types $i$ and $j$ exhibit *synergy*---engaging both
  simultaneously yields superadditive performance.
- $K_{ij} < 1$: types $i$ and $j$ exhibit *interference*---engaging
  both simultaneously yields subadditive performance.
- $K_{ij} = 1$: independence.

\begin{keyeq}
**Key Equation.**\quad
The *effective intelligence* for a task requiring types $i$ and $j$
simultaneously is $I_{\mathrm{eff}}^{(ij)} = K_{ij}\,\sqrt{I_i\, I_j}$.
\end{keyeq}

### Functional Connectivity Interpretation

The matrix $\bK$ is directly interpretable as a prediction about functional
connectivity.  Given the neural circuit assignments in Section *ref:sec:vector*:

\begin{prediction}[Functional Connectivity from $\bK$] \tB{}
Let circuits $C_i$ and $C_j$ be the primary neural substrates for types $i$
and $j$ respectively.  Then the resting-state functional connectivity
$\mathrm{FC}(C_i, C_j)$ measured by fMRI should correlate positively with
$K_{ij}$.  Specifically:
[nosep]
- $K_{\mathrm{spat,symb}} > 1$ predicts positive coupling between dorsal
  parietal and lateral intraparietal circuits (spatial--algebraic synergy,
  consistent with mental rotation studies [fox2007]).
- $K_{\mathrm{soc,intra}} > 1$ predicts positive coupling between the TPJ
  and the default mode network (social--reflective synergy).
- $K_{\mathrm{ling,kin}} < 1$ predicts weak or negative coupling between
  Broca's area and motor cortex during dual-task paradigms (speech--motor
  interference).

\end{prediction}

### Synergy and Assembly

When multiple intelligence types are engaged simultaneously, the total output
of a cognitive assembly is governed by the *synergy formula*:

!!! definition "Synergy"
 \tA{}
For an assembly $A = \{t_1, \ldots, t_k\} \subseteq \{1,\ldots,8\}$, the
synergy is

\[
\Syn(A) = \frac{\sum_{i<j \in A} K_{ij}(I_i I_j)^{1/2}}
{\sum_{i \in A} I_i}.
\]

An assembly is *superadditive* if $\Syn(A) > 1$ and
*subadditive* if $\Syn(A) < 1$.

!!! theorem "Synergy Well-Definedness"
 \tA{}
Synergy is invariant under permutation of the engine indices within an assembly:
$\Syn(\sigma(A)) = \Syn(A)$ for any permutation $\sigma$.

%% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
Attention Dynamics on the Simplex}
%% ═══════════════════════════════════════════════════════════════════════════════

An agent does not deploy all eight types simultaneously at full capacity.
Attention is allocated across types, and this allocation evolves in time.

!!! definition "Attention Simplex"
 \tA{}
The *attention vector* is $\lambda = (\lambda_1, \ldots, \lambda_8) \in
\Delta^7$, where $\Delta^7 = \{\lambda \in \\mathbb{R}^{n(e)}_{\geq 0} : \sum_t \lambda_t = 1\}$
is the 7-simplex.  The *effective intelligence* under attention allocation
$\lambda$ is $\bI_{\mathrm{eff}} = \mathrm{diag}(\lambda)\,\bI$.

!!! theorem "Replicator Dynamics"
 \tA{}
Given a task demand vector $\bR \in \\mathbb{R}^{n(e)}_{\geq 0}$ (encoding the task's
requirements in each intelligence type), the attention vector evolves according
to the replicator equation:

\[
\dot{\lambda}_t = \lambda_t\bigl(f_t(\lambda) - \bar{f}(\lambda)\bigr),
\qquad f_t(\lambda) = (\bK\,\bR)_t,
\qquad \bar{f}(\lambda) = \sum_t \lambda_t\, f_t(\lambda).
\]

\begin{keyeq}
**Key Equation.**\quad
$\dot{\lambda}_t = \lambda_t\bigl(f_t - \bar{f}\bigr)$ on $\Delta^7$.
This is the *same* equation governing allele frequency dynamics in
evolutionary biology, now governing attentional allocation.
\end{keyeq}

!!! theorem "Lyapunov Convergence"
 \tA{}
The KL divergence $D_{\KL}(\lambda^* \| \lambda(t))$ from the Nash
equilibrium $\lambda^*$ is a Lyapunov function:
$\frac{d}{dt} D_{\KL}(\lambda^* \| \lambda) \leq 0$,
with equality if and only if $\lambda = \lambda^*$.

\begin{intuition}
**Neural interpretation.**\quad The replicator dynamics on the attention
simplex predict that task-switching is not instantaneous: the trajectory from
one attentional equilibrium to another follows a geodesic on the simplex
(under the Fisher--Shahshahani metric), and the transit time is measurable.
EEG/MEG temporal resolution ($\sim$1 ms) should reveal the switching trajectory
as a sequence of spectral power shifts across frequency bands associated with
different intelligence types.
\end{intuition}

### Bifurcation and Decision

!!! theorem "Decision as Symmetry Breaking"
 \tB{}
When a task demand changes continuously through a critical value $\mu_c$,
the stable attentional equilibrium undergoes a pitchfork bifurcation.  Near
criticality, the time to resolve the decision scales as:

\[
\tau \sim |\mu - \mu_c|^{-1/2}.
\]

This result connects to the well-documented speed--accuracy tradeoff in
psychophysics: near-threshold decisions are slow because the dynamical system
is near a bifurcation point where the restoring force toward the new
equilibrium vanishes.

%% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
Filter Operators}
%% ═══════════════════════════════════════════════════════════════════════════════

Raw intelligence is never fully expressed.  A cascade of filters transforms
$\bI_{\mathrm{raw}}$ into the effective intelligence $\bI_{\mathrm{eff}}$ that
actually drives behavior.

!!! definition "Filter Species"
 \tA{}
A *filter* is a diagonal contraction $\Phi: \\mathbb{R}^{n(e)}_{\geq 0} \to
\\mathbb{R}^{n(e)}_{\geq 0}$ of the form $\Phi(\bI) = \mathrm{diag}(\phi_1, \ldots,
\phi_8)\,\bI$, where each $\phi_t \in [0,1]$.
There are five canonical species, ordered by characteristic timescale:
\begin{center}

*[Table — see PDF for formatted version]*

\end{center}

\begin{keyeq}
**Key Equation.**\quad
The effective intelligence is the pipeline composition:
\[
\bI_{\mathrm{eff}} = (\Phi_{\mathrm{env}} \circ \Phi_{\mathrm{dev}} \circ
\Phi_{\mathrm{cog}} \circ \Phi_{\mathrm{soc}} \circ \Phi_{\mathrm{cult}})
(\bI_{\mathrm{raw}}).
\]
\end{keyeq}

!!! theorem "Filter Composition"
 \tA{}
The composition of any two filters is a filter.  Explicitly:
$\Phi_2 \circ \Phi_1 = \mathrm{diag}(\phi_1^{(1)}\phi_1^{(2)}, \ldots,
\phi_8^{(1)}\phi_8^{(2)})$, and since each
$\phi_t^{(1)}\phi_t^{(2)} \in [0,1]$, the result is again a filter.

!!! lemma "Kernel Composition"
 \tA{}
$\ker(\Phi_2 \circ \Phi_1) \supseteq \ker(\Phi_1)$.  Information loss
accumulates monotonically through the filter pipeline.

### Pharmacological Filter Predictions

The cognitive/state filter $\Phi_{\mathrm{cog}}$ is directly modulated by
neuroactive substances.  Each substance has a *filter signature*:

\begin{prediction}[Pharmacological Filter Signatures] \tB{}
[nosep]
- **Caffeine**: amplifies $\phi_{\mathrm{symb}}$ and
  $\phi_{\mathrm{ling}}$ (enhanced symbolic processing and verbal fluency),
  attenuates $\phi_{\mathrm{kin}}$ (fine motor tremor).  The filter is
  $\Phi_{\mathrm{caff}} \approx \mathrm{diag}(1.05, 1.08, 1.0, 0.95, 1.0, 1.0, 0.98, 1.0)$.
- **Cortisol (acute stress)**: amplifies $\phi_{\mathrm{spat}}$ and
  $\phi_{\mathrm{kin}}$ (fight-or-flight), attenuates $\phi_{\mathrm{symb}}$
  and $\phi_{\mathrm{soc}}$ (narrowed executive and social processing).
- **SSRIs (chronic)**: modulates $\phi_{\mathrm{soc}}$ and
  $\phi_{\mathrm{intra}}$ upward (enhanced social engagement and emotional
  regulation), minimal effect on $\phi_{\mathrm{symb}}$.

Each of these signatures is testable by administering the substance and
measuring performance across type-specific cognitive batteries.
\end{prediction}

%% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
Cognitive Thermodynamics}
%% ═══════════════════════════════════════════════════════════════════════════════

The attention simplex admits a thermodynamic structure that yields metabolic
predictions.

!!! definition "Cognitive Entropy and Temperature"
 \tA{}
The *cognitive entropy* is $S(\lambda) = -\sum_t \lambda_t \ln \lambda_t$.
The *cognitive temperature* is
$T_{\mathrm{cog}} = \mathrm{Var}[\lambda \cdot f] / \bar{f}$,
measuring the variance of fitness-weighted attention fluctuations.
The *cognitive free energy* is $F_{\mathrm{cog}} = E - T_{\mathrm{cog}}\,S$,
where $E = \bar{f}(\lambda)$ is the mean fitness.

!!! theorem "Boltzmann Equilibrium on the Simplex"
 \tA{}
The equilibrium attention distribution maximizing entropy subject to a
mean-energy constraint is the Boltzmann distribution on the simplex:

\[
\lambda_t^* \propto \exp\!\bigl(f_t / T_{\mathrm{cog}}\bigr).
\]

This coincides with the fixed point of the stochastic replicator dynamics
at temperature $T_{\mathrm{cog}}$.

\begin{keyeq}
**Key Equation.**\quad The cognitive *Second Law*:
for any spontaneous attentional reallocation,
$\Delta S_{\mathrm{cog}} \geq 0$.  Task-switching from a low-entropy
(focused) state to a high-entropy (diffuse) state is thermodynamically
favored; the reverse requires metabolic work.
\end{keyeq}

!!! definition "Friction Tensor"
 \tB{}
The *friction tensor* $\bF \in \R^{8\times 8}_{>0}$ encodes the metabolic
cost of reallocating attention between types:

\[
W_{\mathrm{switch}} = \sum_{s,t} F_{st}\, |\Delta\lambda_s|\,|\Delta\lambda_t|.
\]

High $F_{st}$ means switching between types $s$ and $t$ is metabolically
expensive; low $F_{st}$ means cheap.

\begin{prediction}[Task-Switching Metabolic Cost] \tB{}
The friction tensor predicts that task-switching cost (measured by BOLD
signal in fMRI) is *not uniform* across type pairs.  Specifically:
$F_{\mathrm{ling,spat}} > F_{\mathrm{ling,symb}}$---switching from
language to spatial reasoning is more costly than switching from language
to symbolic reasoning (because linguistic and symbolic circuits share
prefrontal infrastructure while spatial circuits are posterior).
This prediction is testable in a block-design fMRI paradigm with
calibrated switch points.
\end{prediction}

### Four Laws of Cognitive Thermodynamics

By structural analogy with physical thermodynamics (noting these are
mathematical analogies, not metaphysical claims):

[nosep]
- **Zeroth Law**: If two cognitive subsystems are each in equilibrium
with a third, they are in equilibrium with each other (transitivity of
$T_{\mathrm{cog}}$ equalization).
- **First Law**: $dE = \delta W + \delta Q$---changes in cognitive
energy equal work done (task performance) plus heat (metabolic dissipation).
- **Second Law**: $\Delta S_{\mathrm{cog}} \geq 0$ for spontaneous
processes---attention diffuses unless work is applied to concentrate it.
- **Third Law**: The zero-entropy state ($\lambda = e_t$ for some $t$,
complete focus on one type) requires infinite work to maintain---perfect
concentration is an asymptotic limit.

%% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
Global Workspace Connection}
%% ═══════════════════════════════════════════════════════════════════════════════

Baars' Global Workspace Theory (GWT) [baars1988] posits that conscious
access corresponds to information being broadcast to a global workspace.
Dehaene and colleagues [dehaene2014] grounded this in the ignition
of prefrontal--parietal networks.

In the present framework, the *hypervisor* is the spectral decomposition
of the compatibility matrix:

!!! definition "Hypervisor"
 \tB{}
Let $\bK = \sum_{n=1}^{8} \mu_n\, \mathbf{v}_n\, \mathbf{v}_n^\top$ be
the spectral decomposition of the compatibility matrix.  A cognitive content
enters conscious access when its projection onto the principal eigenvector
$\mathbf{v}_1$ exceeds a threshold:

\[
\text{content } c \text{ is conscious} \iff
|\langle c, \mathbf{v}_1 \rangle| > \delta.
\]

The eigenvectors $\mathbf{v}_1, \ldots, \mathbf{v}_8$ define the
*modes* of cognitive integration, and $\mu_1 / \mu_8$ measures
the spectral gap---the dominance of the principal mode.

\begin{intuition}
**GWT correspondence.**\quad The principal eigenvector $\mathbf{v}_1$
corresponds to the global workspace broadcast mode.  Resting-state networks
[yeo2011] can be interpreted as the spatial distribution of the
principal eigenvectors of $\bK$.  The spectral gap $\mu_1 / \mu_2$ predicts
the clarity of conscious access: a large gap means one dominant mode
(focused awareness); a small gap means competing modes (distractibility
or creative diffuse states).
\end{intuition}

\begin{prediction}[Resting-State Eigenmodes] \tC{}
The 7 canonical resting-state networks identified by Yeo et al.\ [yeo2011]
should correspond approximately to the 8 eigenvectors of $\bK$, with
the visual network split between $I_{\mathrm{spat}}$ and $I_{\mathrm{nat}}$
modes.  This predicts that individual differences in $\bK$ eigenstructure
will correlate with individual differences in resting-state network
topology.
\end{prediction}

%% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
Evolutionary Context}
%% ═══════════════════════════════════════════════════════════════════════════════

The human intelligence vector is not given *a priori*---it is the
product of evolutionary selection.  Two major findings from comparative
cognition ground the evolutionary trajectory:

The social brain hypothesis [dunbar1998] establishes that primate neocortex
ratio correlates with social group size, predicting that $I_{\mathrm{soc}}$
was a primary driver of hominid encephalization.  In the IAG framework,
this means the $K_{\mathrm{soc},*}$ row of the compatibility matrix was
under particularly strong selection.  Tomasello's shared intentionality
framework [tomasello2005] adds that the capacity for joint attention and
shared goals---formalized as alignment of $\bR$ vectors across agents---is
uniquely elaborated in humans, predicting that human $K_{\mathrm{soc,symb}}$
is unusually high compared to other great apes.

\begin{prediction}[Hominid $\bK$ Evolution] \tC{}
Comparative analysis of primate functional connectivity should reveal a
monotonic increase in $K_{\mathrm{soc,symb}}$ from macaques to chimpanzees
to humans, reflecting the co-evolution of social and symbolic intelligence
that underlies language, culture, and institutional complexity.
\end{prediction}

%% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
Twelve Testable Predictions}
%% ═══════════════════════════════════════════════════════════════════════════════

We collect twelve predictions derived from the framework, organized by
measurement modality.

### fMRI Predictions

[label=**P\arabic***., nosep]
- **$\bK$--FC correlation.**\quad Off-diagonal entries of $\bK$
correlate with resting-state functional connectivity between corresponding
circuit families (Prediction *ref:pred:fc*). \tB{}

- **Friction asymmetry.**\quad Task-switching BOLD cost between type
pairs is asymmetric: $F_{\mathrm{ling,spat}} \neq F_{\mathrm{spat,ling}}$,
and the asymmetry correlates with structural connectivity asymmetry measured
by diffusion tensor imaging. \tB{}

- **Pharmacological filter signatures.**\quad Caffeine, cortisol,
and SSRIs produce distinct 8-component filter profiles measurable as
differential BOLD response across type-specific tasks
(Prediction *ref:pred:pharma*). \tB{}

- **Second Law metabolic cost.**\quad Switching from focused
($S$ low) to diffuse ($S$ high) attention requires less metabolic work than
the reverse, measurable as BOLD signal difference in task-switching
paradigms. \tB{}

### EEG/MEG Predictions

[label=**P\arabic***., nosep, resume]
- **Replicator trajectory.**\quad Task-switching produces a
continuous trajectory through the attention simplex $\Delta^7$, observable
as a sequence of spectral power shifts with characteristic time constants
matching the replicator dynamics equation (*ref:eq:replicator*). \tB{}

- **Bifurcation scaling.**\quad Near-threshold decisions exhibit
critical slowing with $\tau \sim |\mu - \mu_c|^{-1/2}$
(Theorem *ref:thm:bifurcation*), measurable via EEG as increased
pre-decision variability. \tB{}

- **Spectral gap and distractibility.**\quad Individuals with
smaller $\mu_1/\mu_2$ ratios (smaller spectral gap in $\bK$) should show
higher P300 amplitude variance and lower sustained attention performance. \tC{}

- **Eigenmode signatures.**\quad EEG source-localized power in
canonical frequency bands should cluster along the principal eigenvectors
of $\bK$ during resting state. \tC{}

### Behavioral and PET Predictions

[label=**P\arabic***., nosep, resume]
- **Synergy predicts team performance.**\quad For dyads with
measured $\bI$ vectors, the synergy formula (Definition *ref:def:syn*)
predicts joint performance better than the sum or maximum of individual
scalar scores. \tB{}

- **Cross-type transfer.**\quad Training type $i$ produces
transfer to type $j$ in proportion to $K_{ij}$---spatial training improves
algebraic reasoning (if $K_{\mathrm{spat,symb}} > 1$) but impairs social
tasks (if $K_{\mathrm{spat,soc}} < 1$). \tB{}

- **Glucose uptake pattern.**\quad PET glucose metabolism during
type-specific tasks should show differential uptake patterns corresponding
to the circuit families in Definition *ref:def:ivec*, with switching tasks
showing elevated uptake in proportion to $F_{st}$. \tB{}

- **Filter cascade ordering.**\quad Longitudinal studies should
reveal that developmental filters ($\Phi_{\mathrm{dev}}$) account for
more variance in childhood performance than state filters
($\Phi_{\mathrm{cog}}$), with the ratio reversing in adulthood as
$\Phi_{\mathrm{dev}}$ stabilizes. \tB{}

%% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
Three-Space Neuroscience}

The three-space ontology (Part XIII) reframes the neural correlates of consciousness as $\PS$-signatures of instantiation rather than generators of consciousness.  The brain does not *produce* consciousness; it provides the $\PS$-substrate through which consciousness ($\CSp$) projects $\QS$-potentiality into definite experience.  Neural correlates are the physical traces of this projection, not its cause.  Searching for the "neural basis of consciousness" within $\PS$ alone is structurally analogous to searching for quantum gravity within $\QS$ alone: both are ontological type errors that produce apparent intractability (the explanatory gap, the unrenormalisable infinities) because the single-space domain lacks the structure to pose the question correctly.

### Memory Architecture in Three-Space

The three-space ontology reveals that the five memory subsystems correspond to distinct algebraic structures:

\begin{center}

*[Table — see PDF for formatted version]*

\end{center}

The $p$-adic (ultrametric) organization of semantic memory predicts that category-level priming should show discrete jumps rather than smooth distance gradients: items within the same branch of the ultrametric tree should be equally accessible, with a sharp transition to items in different branches.  This is testable via reaction-time studies with hierarchically organized stimuli.

Procedural memory is not "stored" in the conventional sense but *built into* the compatibility matrix $\bK$ through developmental filtering.  Learning to ride a bicycle sculpts $K_{\mathrm{spatial,kinesthetic}}$ into a synergistic configuration ($K > 1$) that cannot be "retrieved" as a discrete memory trace because it *is* the connectivity structure itself.

## \color{sectionblue
Discussion}
%% ═══════════════════════════════════════════════════════════════════════════════

The framework presented here differs from existing approaches in three
principal ways.  First, it replaces scalar intelligence with a vector whose
components map to identifiable neural circuits, enabling predictions that no
single-factor model can make.  Second, it specifies the interaction structure
via $\bK$, which is absent from both factor-analytic and multiple-intelligence
traditions.  Third, the dynamical components (replicator attention, filter
pipeline, thermodynamics) yield quantitative predictions about temporal
evolution, metabolic cost, and pharmacological response.

### Limitations

The circuit assignments in Definition *ref:def:ivec* are coarse: each
type spans multiple cortical and subcortical regions, and the
one-to-one mapping is a simplification.  The diagonal filter assumption
(Section *ref:sec:filters*) excludes cross-type coupling within a single
filter; a full treatment would use $8\times 8$ filter matrices, at the
cost of greatly expanded parameter space.  The pharmacological predictions
(Prediction *ref:pred:pharma*) use illustrative values; empirical
calibration requires large-scale dose--response studies.

### Relation to Global Workspace and IIT

The hypervisor construct (Section *ref:sec:gwt*) is compatible with GWT
[baars1988,dehaene2014] in identifying conscious access with a
dominant mode, and with Integrated Information Theory (IIT)
[tononi2004] in measuring integration via the spectral structure
of $\bK$.  The eigenvalue ratio $\mu_1/\mu_8$ is a rough analogue of
$\Phi$ (integrated information), though a precise mapping requires
further work.

### Open Directions

Three avenues merit immediate investigation.  First, empirical estimation
of $\bK$ from large-scale resting-state fMRI datasets [yeo2011]
would test whether the eigenstructure predicted by the framework matches
observed network topology.  Second, combining the filter formalism with
computational psychiatry [friston2014] could yield a principled
account of how neuromodulatory dysfunction (filter distortion) produces
psychiatric symptom profiles.  Third, the replicator dynamics
(Theorem *ref:thm:replicator*) make millisecond-resolution predictions
testable with MEG, particularly regarding the trajectory of attentional
switching and the bifurcation timescale near decision thresholds.

%% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
Conclusion}
%% ═══════════════════════════════════════════════════════════════════════════════

We have presented a geometric framework for intelligence in which cognition
is characterized by an variable-dimensional vector, cross-type interactions are
specified by a compatibility matrix with direct functional connectivity
interpretations, attention evolves via replicator dynamics with provable
convergence, five species of filter transform raw capacity into effective
intelligence, and a cognitive thermodynamics predicts metabolic cost.
The framework generates twelve quantitative predictions testable with
existing neuroimaging equipment.  If even a subset of these predictions
survives empirical scrutiny, the vector representation of intelligence
would constitute a significant advance over scalar models for
neuroscience.

%% ═══════════════════════════════════════════════════════════════════════════════

## References

*See PDF for full bibliography.*
---

## v2 Integration: Entity Dimensionality & Neural Complexity (TMP-20260217)

The **entity dimensionality** measure maps directly onto neural architecture:

$$\text{dim}(n) = |\{k \in \{1,\ldots,8\} : \mathbf{I}_k(n) \geq \theta_k\}|$$

A single-circuit neuron has dim = 1. A concept like "emotion" spanning somatic, social, linguistic, and temporal circuits has dim ≥ 4 — providing a principled complexity measure grounded in I-vector activation count, not connection count alone.

**Document ≅ Mind ≅ Brain (Theorem 6):** At the neuronal level, synaptic weights form a relation matrix isomorphic to the RTSG SynergyTensor. Mind, Document, and Brain are isomorphic RTSG graphs at appropriate granularity, connected by structure-preserving functors. The morphism Brain → Mind is the aggregation functor mapping synaptic graphs to concept graphs.

**Intelligence fingerprinting:** From a sufficiently rich neural activation corpus C(ξ), the intelligence vector **I**(ξ) is recoverable via IdeaRank analysis — the neural instantiation of the cognitive fingerprinting pipeline.
