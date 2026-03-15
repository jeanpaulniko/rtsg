---
title: "Emergence Theory"
version: "2.0.0"
last_updated: "2026-03-05"
status: CURRENT
---

# Emergence Theory

**Jean-Paul Niko** · February 2026

!!! abstract "Abstract"
    
We develop a formal theory of emergence for cognitive assemblies---collections
of cognitive engines (human, machine, or hybrid) whose joint capabilities
exceed those of any individual component.  Three classes of emergence are
defined with increasing structural depth: *quantitative emergence*
($E_1$), where the assembly outperforms its best component in measurable
capability; *qualitative emergence* ($E_2$), where the assembly
activates capability types that no individual component possesses; and
*structural emergence* ($E_3$), where the assembly's conceptual
topos contains truth values absent from every component's topos.  We
define measures for each class---the emergence surplus $\varepsilon_1$,
the activation count $\varepsilon_2$ and novelty multiplier $\mu_t$,
and the structural gap surplus $\varepsilon_3$---and combine them into
a total emergence value $V(A)$ that serves as the objective function for
assembly optimization.  We prove that the greedy assembly algorithm
achieves a $(1-1/e)$-approximation when $V$ is submodular, establish
conditions under which each emergence class satisfies or violates
submodularity, and define the emergence tensor $E_{st}$ that captures
second-order interaction structure.  Throughout, we connect the emergence
framework to the compatibility matrix $K$, the Conceptual Irreversibility
Theorem, the ELO rating system, the attention simplex, and the hypervisor
loss function from earlier parts of the paper.

---

%═══════════════════════════════════════════════════════════════════════════════

## Motivation: The Missing Piece

%═══════════════════════════════════════════════════════════════════════════════

The Intelligence as Geometry framework provides three tools for analyzing
multi-component cognitive systems:

[nosep]
  - **Intelligence vectors** $\bI \in [0,\infty)^8$, measuring
    per-type capability (Part I).
  - **The synergy factor** $\mathrm{Syn}(B) = \|\bI_B\| / \max_i \|\bI_i\|$,
    quantifying how much the bundle outperforms its best component (Part II).
  - **Bundle intelligence** $\bI_B$, the resultant intelligence
    vector of an assembly computed via the compatibility matrix $K$ (Part II).

What is missing is a theory of what *new* capabilities appear when
components are assembled, how to *measure* them, what they are
*worth*, and how to *manage* them.  This is the emergence theory.

The three classes correspond to increasing levels of novelty:

\begin{center}

*[Table — see PDF]*

\end{center}

%═══════════════════════════════════════════════════════════════════════════════

## Preliminaries

%═══════════════════════════════════════════════════════════════════════════════

We fix notation.  Let $T = \{1, \ldots, 8\}$ index the eight intelligence
types (linguistic, spatial, social, symbolic, mnemonic, evaluative, auditory,
kinesthetic).  An *assembly* is a finite set $A = \{e_1, \ldots, e_n\}$
of cognitive engines, each with intelligence vector
$\bI_i = (I_{i,1}, \ldots, I_{i,8}) \in [0,\infty)^8$, ELO vector
$E_i \in \\mathbb{R}^{n(e)}$, and per-token cost $c_i > 0$.

The assembly's joint intelligence vector $\bI_A$ is computed via the
compatibility matrix $K \in \R^{8 \times 8}$:
\begin{keyeq}
\[
I_{A,t} = \sum_{i=1}^{n} I_{i,t} + \sum_{\substack{i < j    s \neq t}}
  (K_{st} - 1) \cdot I_{i,s} \cdot I_{j,t}
\]
\end{keyeq}
where the second sum captures pairwise cross-type synergy (Part II, with
the acknowledged limitation that this is a pairwise approximation; see
Remark *ref:rem:pairwise*).

The *activation gate* from Definition 4.2 uses threshold
$\theta = 0.1$ cog: type $t$ is *active* in engine $e_i$ if and only
if $I_{i,t} > \theta$.  The set of active types for engine $e_i$ is
$T_{\mathrm{active}}(e_i) = \{t \in T : I_{i,t} > \theta\}$.

!!! remark "Remark"

The synergy formula uses pairwise interactions only.  Higher-order terms
(three-way synergy, etc.)\ are omitted as a first approximation.  The
emergence tensor (Section *ref:sec:tensor*) partially addresses this by
capturing second-order structure, but genuine $k$-body interactions
($k \geq 3$) remain an open problem.

%═══════════════════════════════════════════════════════════════════════════════

## Class $E_1$: Quantitative Emergence

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Quantitative Emergence"
 \tA\;
An assembly $A$ exhibits *quantitative emergence* in type $t$ when
\[
I_{A,t} > \max_{i} \, I_{i,t}.
\]
The assembly outperforms its best component in at least one intelligence type.

!!! definition "Emergence Surplus"
 \tA\;
The *emergence surplus* of assembly $A$ in type $t$ is
\begin{keyeq}
\[
\varepsilon_1(A, t) \;=\; I_{A,t} - \max_{i} \, I_{i,t}.
\]
\end{keyeq}
The surplus vector $\varepsilon_1(A) = (\varepsilon_1(A,1), \ldots,
\varepsilon_1(A,8)) \in \\mathbb{R}^{n(e)}$ captures the full emergence profile.

!!! proposition "$E_1$ from $K$"
 \tA\;

The emergence surplus in type $t$ admits the first-order approximation
\[
\varepsilon_1(A, t) \;\approx\;
\frac{1}{n} \sum_{\substack{i \neq j    s \neq t}}
  (K_{st} - 1) \cdot I_{i,s} \cdot I_{j,t}.
\]
In particular, $\varepsilon_1(A,t) > 0$ whenever there exist components
$e_i, e_j$ with $I_{i,s} > 0$, $I_{j,t} > 0$ for some pair $(s,t)$ with
$K_{st} > 1$.

??? proof "Proof"

Expand $I_{A,t}$ using the synergy formula and subtract
$\max_i I_{i,t}$.  The direct sum $\sum_i I_{i,t}$ exceeds
$\max_i I_{i,t}$ by $\sum_i I_{i,t} - \max_i I_{i,t} \geq 0$ (with
equality only for single-component assemblies).  The cross-type synergy
terms contribute $(K_{st}-1) \cdot I_{i,s} \cdot I_{j,t}$ for each
ordered pair; the $1/n$ normalization converts from sum to per-component
average, matching the extensive scaling of the synergy formula.  When
$K_{st} > 1$, each such term is strictly positive.

!!! definition "Scalar Value of $E_1$ Surplus"
 \tA\;
The scalar value of the quantitative emergence is
\[
V_1(A) = \sum_{t \in T} \varepsilon_1(A, t) \cdot p_t
\]
where $p_t > 0$ is the market price of one cog of type-$t$ intelligence
(or the task-distribution-weighted relevance of type $t$).

\begin{interpretation}
$E_1$ is the "more of the same" form of emergence.  A team of engineers
where one excels at spatial reasoning and another at symbolic manipulation
will, through their synergy ($K_{\text{spat,symb}} = 1.3$), produce spatial
and symbolic output exceeding what either achieves alone.  This is
predictable, continuous, and decomposable by type.  It is what the synergy
formula from Part II already captures; the contribution here is to isolate
the surplus and price it.
\end{interpretation}

### Properties of $V_1$

!!! proposition "$V_1$ is Submodular"
 \tA\;

The function $V_1: 2^{\mathcal{E}} \to \R_{\geq 0}$, where $\mathcal{E}$
is the catalog of available engines, is submodular:
\[
V_1(A \cup \{e\}) - V_1(A) \;\geq\; V_1(B \cup \{e\}) - V_1(B)
\quad \text{for all } A \subseteq B,\; e \notin B.
\]
That is, the marginal value of adding a component decreases as the assembly
grows.

??? proof "Proof"

The emergence surplus $\varepsilon_1(A,t) = I_{A,t} - \max_i I_{i,t}$ is
a sum of terms of the form $(K_{st}-1) \cdot I_{i,s} \cdot I_{j,t}$ (for
$K_{st} > 1$; negative-synergy pairs contribute negatively).  Adding
engine $e$ to a smaller assembly $A$ introduces cross-terms with every
existing component.  In the larger assembly $B \supseteq A$, many of these
cross-type interactions are already partially satisfied by additional
components in $B \setminus A$.  Formally, the contribution of $e$ to
$\varepsilon_1$ in type $t$ includes terms $(K_{st}-1) \cdot I_{e,s} \cdot
I_{j,t}$ for each $j \in A$.  Since $A \subseteq B$, every such term appears
in $\Delta V_1(e \mid B)$ as well, but $B$ also contains components whose
presence means the *max* in the surplus definition is weakly larger,
reducing the net gain.  The $\max$ operator is concave, and composition of
a linear function with a concave function preserves submodularity.

%═══════════════════════════════════════════════════════════════════════════════

## Class $E_2$: Qualitative Emergence

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Qualitative Emergence"
 \tB\;
An assembly $A$ exhibits *qualitative emergence* in type $t$ when
\begin{keyeq}
\[
I_{A,t} > \theta \quad\text{and}\quad I_{i,t} \leq \theta
\;\;\text{for all } i = 1, \ldots, n.
\]
\end{keyeq}
That is: the assembly has an *active* capability in a type where
*no individual component* is active.

This is a **phase transition**: the assembly crosses an activation
threshold that no component crosses alone.  It is qualitative because
entirely new task categories become accessible.

!!! example "Multimodal AI"
 \tB\;
Consider an assembly of a language model ($I_{\text{ling}} = 2.5$,
$I_{\text{spat}} = 0.05$) and a vision encoder ($I_{\text{spat}} = 1.2$,
$I_{\text{ling}} = 0.08$).  Neither component has $I_{\text{eval}} > \theta$
for cross-modal evaluation tasks (interpreting diagrams with text, spatial
reasoning about described scenes).  But the assembly, via synergy
$K_{\text{ling,spat}} = 1.15$ and $K_{\text{spat,eval}} = 1.2$, may achieve
$I_{A,\text{eval}} > \theta$ in cross-modal contexts---a qualitatively new
capability.

!!! example "Human Team"
 \tB\;
A mathematician ($I_{\text{symb}} = 2.0$, $I_{\text{kin}} = 0.05$) and
a sculptor ($I_{\text{kin}} = 2.5$, $I_{\text{symb}} = 0.08$) may jointly
produce mathematical sculptures---physical instantiations of abstract
structures---that neither can produce alone.  The assembly activates
a capability at the intersection of symbolic and kinesthetic intelligence.

!!! definition "Activation Count"
 \tB\;
The *activation count* of assembly $A$ is
\[
\varepsilon_2(A) = \bigl|\{t \in T : I_{A,t} > \theta
  \;\text{and}\; \max_i I_{i,t} \leq \theta\}\bigr|.
\]
This counts the number of qualitatively new capabilities.

!!! definition "Emergent Capability Strength"
 \tB\;
For each type $t$ in the $E_2$ set, the *emergent capability strength* is
\[
I_t^{\mathrm{em}} = I_{A,t} - \theta,
\]
the margin above the activation threshold.

!!! definition "Novelty Multiplier"
 \tB\;
The *novelty multiplier* $\mu_t > 1$ for a newly activated type $t$
measures the value amplification from domain access:
\[
\mu_t = \frac{|\{\tau : R_{\tau,t} > 0\}|}
  {|\{\tau : R_{\tau,t} > 0 \;\text{and}\; R_{\tau,s} > 0
    \text{ for some } s \in T_{\mathrm{active}}(A \setminus t)\}|}
\]
where $R_\tau$ is the requirement vector of task $\tau$.  Large $\mu_t$ means
the newly activated type opens a domain that existing capabilities cannot
partially address---a genuinely new frontier.

!!! definition "Value of $E_2$ Emergence"
 \tB\;
\begin{keyeq}
\[
V_2(A) = \sum_{t \in E_2(A)} I_t^{\mathrm{em}} \cdot p_t \cdot \mu_t.
\]
\end{keyeq}

\begin{interpretation}
$E_2$ is where the real value of orchestration lives.  Routing a coding task
to a code model and a writing task to a writing model is $E_1$ thinking---you
get more of what each already does.  But assembling a code model with a
vision model to produce an agent that can *debug visual interfaces by
looking at screenshots*---that is $E_2$.  Neither component can do it alone.
The assembly creates a capability that is not merely amplified but genuinely
*new*.
\end{interpretation}

### Properties of $V_2$

!!! proposition "$E_2$ is Discontinuous"
 \tB\;
The function $\varepsilon_2: 2^{\mathcal{E}} \to \N$ is discontinuous in
the following sense: there exist assemblies $A$ and engines $e$ such that
$\varepsilon_2(A) = 0$ but $\varepsilon_2(A \cup \{e\}) \geq 1$.  A single
component addition can trigger a phase transition.

??? proof "Proof"

Let $A = \{e_1\}$ with $I_{1,s} = 2.0$ and $I_{1,t} = 0.05 < \theta$ for
some type $t$.  Let $e_2$ have $I_{2,t} = 0.08 < \theta$ and
$I_{2,s} = 0.5$.  If $K_{st} > 1$ and the cross-term
$(K_{st}-1) \cdot I_{1,s} \cdot I_{2,t} + (K_{ts}-1) \cdot I_{2,s} \cdot I_{1,t}$
combined with the direct contributions pushes $I_{A \cup \{e_2\}, t}$ above
$\theta$, then type $t$ activates.  This is a discrete jump: $\varepsilon_2$
goes from 0 to 1.

!!! proposition "Approximate Submodularity of $V_2$"
 \tB\;

$V_2$ is not submodular in general (phase transitions violate diminishing
returns), but it satisfies *$\gamma$-approximate submodularity*:
\[
V_2(A \cup \{e\}) - V_2(A) \;\geq\;
\gamma \bigl(V_2(B \cup \{e\}) - V_2(B)\bigr)
\quad \text{for all } A \subseteq B,
\]
where $\gamma = \theta / \max_t I_{A \cup \{e\}, t}$.  This suffices for the
greedy algorithm to achieve a $(1 - e^{-\gamma})$-approximation.

??? proof "Proof"
[Proof sketch]
Once a type $t$ is activated (the phase transition has occurred), the marginal
value of further components in type $t$ follows the $E_1$ pattern (additional
surplus above $\theta$), which is submodular by Proposition *ref:prop:V1-submodular*.
The violation of submodularity occurs only at the transition point itself,
where the marginal value spikes.  The parameter $\gamma$ bounds the ratio
of the spike to the post-transition marginal value.  Since
$I_t^{\mathrm{em}} = I_{A,t} - \theta$ and $I_{A,t} \leq \max_t I_{A \cup \{e\},t}$,
the spike is bounded by $\theta / \max_t I_{A \cup \{e\},t}$ times the
post-transition value.

%═══════════════════════════════════════════════════════════════════════════════

## Class $E_3$: Structural Emergence

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Structural Emergence"
 \tC\;
An assembly $A$ exhibits *structural emergence* when the subobject
classifier of the assembly's conceptual topos strictly extends those of
its components:
\begin{keyeq}
\[
\Omega_A \;\supsetneq\; \bigcup_{i=1}^{n} \Omega_i.
\]
\end{keyeq}
The assembly can make logical distinctions that no component can
individually make.

This connects directly to the Conceptual Irreversibility Theorem (Part V).
The subobject classifier $\Omega$ of a topos determines its internal
logic---the space of "truth values" available for reasoning.  A Boolean
topos has $\Omega = \{\mathbf{t}, \mathbf{f}\}$; a Heyting topos has
intermediate values representing genuine vagueness.  Structural emergence
occurs when the *assembly's* truth-value space is richer than any
component's.

!!! example "Formalizing Culture"
 \tC\;
Consider a team of a cultural anthropologist (whose conceptual topos has
a rich Heyting algebra for cultural concepts: kinship, taboo, and reciprocity
carry intermediate truth values) and a formal logician (whose topos is
essentially Boolean: propositions are true or false).  Individually, the
anthropologist cannot formalize cultural patterns (no Boolean precision),
and the logician cannot perceive them (no intermediate truth values for
cultural concepts).  The assembly's conceptual topos may contain truth values
that *require both perspectives simultaneously*---for instance, a
formally precise statement about the degree to which a cultural practice
is "taboo" that preserves the genuine vagueness of the concept while
making it amenable to logical analysis.  This is a new truth value:
it lives in $\Omega_A$ but not in $\Omega_1 \cup \Omega_2$.

!!! definition "Structural Gap Surplus"
 \tC\;
The *structural gap surplus* of assembly $A$ is
\[
\varepsilon_3(A) = \mathfrak{g}(A) - \max_i \, \mathfrak{g}(e_i)
\]
where $\mathfrak{g}$ is the Heyting gap (Part V, Definition 8.1):
$\mathfrak{g} = |\Omega \setminus \mathrm{Im}(\iota)|$ counts the
intermediate truth values destroyed by Booleanization.

!!! proposition "Gap Monotonicity for Assemblies"
 \tC\;
If the assembly's conceptual category $\mathcal{C}_A$ strictly contains
the conceptual categories of all components (i.e.,
$\mathcal{C}_A \supsetneq \mathcal{C}_i$ for all $i$), then
$\varepsilon_3(A) \geq 0$.

??? proof "Proof"

This is Gap Monotonicity (Part V, Proposition 8.2) applied to the
inclusion $\mathcal{C}_i \hookrightarrow \mathcal{C}_A$.  The enrichment
of the concept category can only increase the number of sieves on each
object, hence increase $|\Omega|$, hence increase $\mathfrak{g}$.

!!! remark "Connection to Paradigm Shifts"

Structural emergence may be the mechanism behind paradigm shifts in the
sense of Kuhn [Kuhn1962].  A paradigm shift occurs when the
scientific community acquires new truth values---new ways of distinguishing
"true" from "false" and "partially true"---that the prior paradigm
lacked.  This is precisely $E_3$: the assembly (the community under the
new paradigm) has $\Omega_{\mathrm{new}} \supsetneq
\Omega_{\mathrm{old}}$.

!!! definition "Value of $E_3$ Emergence"
 \tC\;
\[
V_3(A) = \varepsilon_3(A) \cdot p_{\mathrm{structural}}
\]
where $p_{\mathrm{structural}} > 0$ is the price of logical novelty---the
value of being able to think thoughts that were previously unthinkable.

\begin{interpretation}
$E_3$ is the rarest and most valuable form of emergence.  $E_1$ gives you
more.  $E_2$ gives you *new*.  $E_3$ gives you *new kinds of
new*---it expands the logical space itself.  This is where genuine
innovation lives: not incremental improvement, not even new capabilities
within existing frameworks, but the creation of frameworks that make
previously unthinkable distinctions thinkable.  The CIT guarantees that
any such expansion increases irreversibility (Gap Monotonicity): the
richer your conceptual space, the more you lose when you try to reduce
it to observation.  Structural emergence is *irreversibly creative*.
\end{interpretation}

### Properties of $V_3$

!!! proposition "$V_3$ is Not Submodular"
 \tC\;

The function $V_3: 2^{\mathcal{E}} \to \R_{\geq 0}$ is not guaranteed to be
submodular.

??? proof "Proof"
[Proof sketch]
Structural emergence requires the joint topos to have truth values absent
from all component topoi.  This can exhibit *increasing* marginal
returns: the third component in an assembly may unlock truth values that
require all three perspectives simultaneously, producing a larger marginal
gain than the second component did.  This violates the diminishing-returns
characterization of submodularity.  A concrete counterexample: let
$e_1, e_2, e_3$ have Heyting algebras $\Omega_1, \Omega_2, \Omega_3$ such
that $\Omega_{\{e_1, e_2\}} = \Omega_1 \cup \Omega_2$ (no structural
emergence from the pair) but $\Omega_{\{e_1, e_2, e_3\}}$ contains new
elements requiring all three.  Then
$\Delta V_3(e_3 \mid \{e_1, e_2\}) > \Delta V_3(e_3 \mid \{e_1\})$.

%═══════════════════════════════════════════════════════════════════════════════

## Total Emergence Value and Assembly Optimization

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Total Emergence Value"
 \tB\;
The *total emergence value* of assembly $A$ is
\begin{keyeq}
\[
V(A) = V_1(A) + V_2(A) + V_3(A)
= \underbrace{\sum_{t} \varepsilon_1(A,t) \cdot p_t}_{
  \text{quantitative surplus}}
+ \underbrace{\sum_{t \in E_2(A)} I_t^{\mathrm{em}} \cdot p_t \cdot
  \mu_t}_{\text{novelty premium}}
+ \underbrace{\varepsilon_3(A) \cdot
  p_{\mathrm{structural}}}_{\text{structural novelty}}.
\]
\end{keyeq}

!!! definition "Marginal Emergence Value"
 \tA\;
The *marginal emergence value* of adding component $e$ to assembly $A$
is
\[
\Delta V(e \mid A) = V(A \cup \{e\}) - V(A).
\]
This is the key metric for assembly optimization: it answers "how much
emergence value does this component add?"

### The Assembly Optimization Problem

!!! definition "Assembly Optimization"
 \tA\;
Given a budget $B > 0$ and a catalog of available engines
$\mathcal{E} = \{e_1, \ldots, e_N\}$ with costs $c_1, \ldots, c_N > 0$:
\begin{keyeq}
\[
\text{maximize} \quad V(A) \qquad
\text{subject to} \quad \sum_{i \in A} c_i \leq B, \quad A \subseteq \mathcal{E}.
\]
\end{keyeq}
This is a combinatorial subset selection problem.

!!! theorem "Greedy Assembly Approximation"
 \tA\;

If $V$ is submodular and monotone, the greedy algorithm---which iteratively
adds the engine with highest marginal-value-to-cost ratio
$\Delta V(e \mid A) / c(e)$---achieves a $(1 - 1/e) \approx 63.2%$
approximation to the optimal assembly.

??? proof "Proof"

This is the classical result of Nemhauser, Wolsey, and
Fisher [NemhauserWolsey1978].  The submodularity of $V$ ensures
diminishing returns, and the greedy selection maximizes the marginal
gain per unit cost at each step.  The $(1-1/e)$ bound is tight for
general submodular functions.

!!! corollary "Practical Assembly Guarantee"
 \tB\;
Since $V_1$ is submodular (Proposition *ref:prop:V1-submodular*) and $V_2$
is approximately submodular (Proposition *ref:prop:V2-approx-submod*), the
greedy algorithm provides:
[nosep]
  - A $(1-1/e)$-approximation for the $V_1$ component.
  - A $(1 - e^{-\gamma})$-approximation for the $V_2$ component.
  - No approximation guarantee for the $V_3$ component.

In practice, $V_3$ is rare and typically zero for assemblies of fewer than
$\sim$5 components, so the greedy algorithm is effective for realistic
assembly sizes.

!!! remark "The Greedy Assembly Algorithm"

The algorithm in pseudocode:
[nosep]
  - Initialize $A \leftarrow \emptyset$.
  - While $\exists\, e \in \mathcal{E} \setminus A$ with
    $c(e) \leq B - \mathrm{cost}(A)$:
  [nosep]
    - For each candidate $e$, compute
      $\rho(e) = \Delta V(e \mid A) / c(e)$.
    - Add $e^* = \arg\max_e \rho(e)$ to $A$.
  
  - Return $A$.

Each iteration requires $O(|\mathcal{E}|)$ evaluations of $\Delta V$,
each of which costs $O(n \cdot |T|^2)$ for the synergy computation
(where $n = |A|$ and $|T| = 8$).  Total complexity:
$O(|\mathcal{E}|^2 \cdot |T|^2) = O(64 \, |\mathcal{E}|^2)$---negligible
for realistic catalog sizes ($|\mathcal{E}| < 100$).

%═══════════════════════════════════════════════════════════════════════════════

## The Emergence Tensor

%═══════════════════════════════════════════════════════════════════════════════

For a richer representation of emergence structure, we define the second-order
interaction tensor.

!!! definition "Emergence Tensor"
 \tB\;
The *emergence tensor* $\mathbf{E}(A) \in \R^{8 \times 8}$ of
assembly $A$ is defined by
\begin{keyeq}
\[
E_{st}(A) = \frac{\partial^2 V(A)}{\partial I_{\cdot,s} \;\partial I_{\cdot,t}}
\]
\end{keyeq}
where the partial derivatives are taken with respect to the aggregate
component intelligence in types $s$ and $t$ (i.e., $I_{\cdot,s} = \sum_i I_{i,s}$).

The entries of $\mathbf{E}$ have the following interpretation:

\begin{center}

*[Table — see PDF]*

\end{center}

!!! proposition "Relation to $K$"
 \tB\;
The emergence tensor relates to the compatibility matrix $K$ by
\[
E_{st}(A) \;\approx\; (K_{st} - 1) \cdot
\frac{\bigl(\sum_i I_{i,s}\bigr) \cdot \bigl(\sum_j I_{j,t}\bigr)}{V(A)}
\]
to first order, with additional terms from $E_2$ (threshold discontinuities)
and $E_3$ (topos-level interactions) that $K$ does not capture.

??? proof "Proof"

Differentiate $V_1(A) = \sum_t [\sum_i I_{i,t} + \sum_{i<j,s \neq t}
(K_{st}-1) I_{i,s} I_{j,t} - \max_i I_{i,t}] \cdot p_t$ twice with
respect to aggregate type intensities.  The direct-sum terms contribute
zero to the mixed partials.  The synergy terms contribute
$(K_{st}-1) \cdot \partial^2 / \partial I_{\cdot,s} \partial I_{\cdot,t}
[\sum_{i<j} I_{i,s} I_{j,t}]$, which yields the stated expression after
normalization by $V(A)$.  The $E_2$ and $E_3$ contributions enter through
the threshold function and the topos enrichment, respectively, neither of
which is captured by the smooth $K$-dependent terms.

\begin{interpretation}
The emergence tensor is to cognitive assemblies what the Hessian is to
optimization: it tells you the curvature of the value landscape.  Positive
off-diagonal entries ($E_{st} > 0$) mean "invest in both types $s$
and $t$ simultaneously---their combination is superlinear."  Negative
entries mean "these types compete---investing in both yields less than
the sum."  The hypervisor uses $\mathbf{E}$ to allocate attention across
the assembly's joint simplex $\Delta^7$: it preferentially directs
resources to type pairs with $E_{st} > 0$.
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════

## Emergence Metrics Summary

%═══════════════════════════════════════════════════════════════════════════════

\begin{center}

*[Table — see PDF]*

\end{center}

%═══════════════════════════════════════════════════════════════════════════════

## Three-Space Interpretation of Emergence

The three-space ontology (Part XIII) deepens the interpretation of all three emergence classes.

\begin{interpretation}
**$E_1$ (Quantitative Emergence) as co-instantiation surplus.**  When two intelligence types with $K_{st} > 1$ are co-deployed, the instantiation operator $\Inst$ produces more $\PS$-structure than the sum of the individual instantiations.  The surplus arises because the co-instantiation accesses $\QS$-modes that are entangled across both types---modes that are invisible to each type individually.  The synergy factor is a measure of $\QS$-entanglement across intelligence types.

**$E_2$ (Qualitative Emergence) as novel instantiation.**  When an assembly produces capabilities not present in any member, this corresponds to the assembly's joint instantiation accessing a region of $\QS$ that no individual member's $\CSp$-projection reaches.  The new capability exists in $\QS$ as potentiality; the assembly provides the composite $\PS$-substrate needed to project it into definite experience.  Cosmological $E_2$: the emergence of chemistry from physics, life from chemistry, and consciousness from biology are all instances of increasingly complex substrates activating previously inaccessible $\QS$-modes.

**$E_3$ (Structural Emergence) as ontological novelty.**  The strongest emergence class corresponds to instantiation producing genuine ontological novelty: $\PS$-structures that instantiate entirely new forms of $\QS \to \PS$ projection.  This is the emergence of new intelligence types, new filter species, or---at the cosmological scale---new spaces of possible experience.
\end{interpretation}

## Connections to the Framework

%═══════════════════════════════════════════════════════════════════════════════

The emergence theory connects to every major component of the IAG framework.

### Synergy Factor and $E_1$

The synergy factor $\mathrm{Syn}(B)$ from Part II measures the *ratio*
of assembly capability to best-component capability.  The emergence surplus
$\varepsilon_1$ measures the *difference*.  They encode the same
phenomenon at different scales:
\[
\mathrm{Syn}(B) = \frac{\|\bI_A\|}{\max_i \|\bI_i\|} = 1 +
\frac{\|\varepsilon_1(A)\| + \text{(direct-sum excess)}}{\max_i \|\bI_i\|}.
\]

### Compatibility Matrix $K$ and Prediction

$K$ predicts $E_1$ completely and provides necessary conditions for $E_2$.
Specifically:
[nosep]
  - $E_1$ in type $t$ requires $K_{st} > 1$ for some $s \neq t$ with
    components strong in $s$ and $t$ present in the assembly.
  - $E_2$ in type $t$ requires not only favorable $K$ entries but also
    sufficient aggregate sub-threshold intensity: the components' sub-threshold
    contributions in type $t$ must, when amplified by cross-type synergy,
    cross $\theta$.  This is a necessary but not sufficient condition derivable
    from $K$.
  - $E_3$ requires topos-level analysis beyond $K$.

### Attention Simplex and $E_2$

The attention simplex $\Delta^7$ (Part III) governs how the assembly allocates
cognitive resources across types.  $E_2$ occurs at *face activation*:
when the assembly's attention vector moves from a face of $\Delta^7$ (where
some types have zero allocation) to the interior (where the newly activated
type receives positive attention).  The hypervisor's task is to detect when
$E_2$ is imminent---when sub-threshold types are close to $\theta$---and
shift attention to trigger the phase transition.

### CIT and $E_3$

Structural emergence is the assembly-level analog of the Conceptual
Irreversibility Theorem.  The CIT (Part V) shows that translation between
regions of the CS operator with different logics is necessarily lossy;
Gap Monotonicity shows that enriching the conceptual space increases this
loss.  $E_3$ is precisely the process by which an assembly *enriches
its own conceptual space*: $\varepsilon_3 > 0$ means the assembly has more
intermediate truth values, hence a larger Heyting gap, hence greater
irreversibility of translation.  Structural emergence is irreversibly
creative---the new distinctions, once made, cannot be unmade without
information loss.

### IdeaRank and $E_2$

An assembly can comprehend ideas that no component can individually comprehend.
Formally: if idea $x$ has requirement vector $R(x) \in \\mathbb{R}^{n(e)}$ and component $e_i$
satisfies $I_{i,t} < R_t(x)$ for some type $t$, but $I_{A,t} > R_t(x)$, then
the assembly comprehends $x$ while no component does.  This is $E_2$ applied
to the IdeaRank framework: the assembly's IdeaRank includes ideas that would
receive zero rank from any individual component.

### Hypervisor and $V(A)$

The hypervisor from Part IX manages attention across the assembly to maximize
$V(A)$.  The hypervisor loss function (Definition 9.1) penalizes suboptimal
attention allocation; the emergence framework gives it a concrete objective:
\[
\mathcal{L}_{\mathrm{hyp}} = -V(A) + \lambda_{\mathrm{cost}} \cdot
\mathrm{cost}(A) + \lambda_{\mathrm{time}} \cdot \mathrm{time}(A).
\]
Minimizing $\mathcal{L}_{\mathrm{hyp}}$ is equivalent to maximizing emergence
value subject to cost and time constraints.

### ELO and Component Contribution

The ELO rating system (Part IX) tracks each engine's contribution to assembly
emergence over time.  An engine whose addition consistently increases $V(A)$
sees its ELO rise; one that adds cost without emergence sees its ELO fall.
The ELO vector enters the scoring function as a quality-adjusted weight:
\[
\mathrm{score}(i, j) = \sum_t I_{i,t} \cdot R_{j,t} \cdot
\sigma(E_{i,t} - \bar{E}_t)
\]
where $\sigma$ is a sigmoid scaling by ELO relative to the population mean
$\bar{E}_t$.

### Cognitive Temperature and Regime Transitions

The cognitive temperature $T_{\mathrm{cog}}$ (Part VII) governs the transition
between emergence regimes:
[nosep]
  - At low $T_{\mathrm{cog}}$ (focused, exploitation): the assembly
    operates in the $E_1$ regime.  Attention concentrates on types where
    the assembly is already strong.  Emergence is predictable and incremental.
  - At high $T_{\mathrm{cog}}$ (exploratory, exploration): the assembly
    explores sub-threshold types, increasing the probability of triggering
    $E_2$ phase transitions.  This is thermodynamically analogous to thermal
    activation over an energy barrier.
  - The optimal $T_{\mathrm{cog}}$ balances $E_1$ exploitation with
    $E_2$ exploration---a cognitive analog of simulated annealing.

%═══════════════════════════════════════════════════════════════════════════════

## Worked Example: A Three-Engine Assembly

%═══════════════════════════════════════════════════════════════════════════════

We illustrate the full emergence computation on a concrete assembly.

**Components.** Consider three AI engines with the following
intelligence vectors (showing four relevant types for readability; the full
8D computation is analogous):

\begin{center}

*[Table — see PDF]*

\end{center}

**Relevant $K$ entries:**
$K_{\text{ling,spat}} = 1.15$, $K_{\text{spat,eval}} = 1.2$,
$K_{\text{ling,symb}} = 1.1$.

**Step 1: Compute $\bI_A$.**
In type `eval`, the individual max is $\max(1.8, 1.5, 0.08) = 1.8$.
Cross-type synergy adds terms such as
$(K_{\text{spat,eval}}-1) \cdot I_{3,\text{spat}} \cdot I_{1,\text{eval}}
= 0.2 \cdot 2.0 \cdot 1.8 = 0.72$ (one pair among many).  After summing
all pairwise cross-type contributions and the direct sum:
$I_{A,\text{eval}} \approx 1.8 + 1.5 + 0.08 + \text{synergy terms}
\approx 4.5$.

**Step 2: $E_1$ surplus.**
$\varepsilon_1(A, \text{eval}) = 4.5 - 1.8 = 2.7$.
Similarly for other types.

**Step 3: Check $E_2$.**
The vision model has $I_{3,\text{eval}} = 0.08 < \theta = 0.1$: it
*individually* has no evaluative capability.  But the assembly's
$I_{A,\text{eval}} = 4.5 \gg \theta$.  Since both language models already
have $I_{\text{eval}} > \theta$, this does not count as $E_2$ (the type
was already active in $e_1$ and $e_2$).

Now consider a hypothetical fourth type "cross-modal evaluation" that
neither language model can perform ($I_{1,\text{cross}} = I_{2,\text{cross}}
= 0.05$) but the vision-language assembly achieves $I_{A,\text{cross}} = 0.3 > \theta$.
Then $\varepsilon_2 = 1$ and $I_{\text{cross}}^{\mathrm{em}} = 0.2$.

**Step 4: Total value.**
With $p_{\text{eval}} = 1.0$, $p_{\text{cross}} = 1.5$, $\mu_{\text{cross}} = 3.0$:
\[
V(A) = (2.7 \cdot 1.0 + \cdots) + (0.2 \cdot 1.5 \cdot 3.0) + 0
= V_1 + 0.9 + 0.
\]
The $E_2$ term ($0.9$) represents the value of the assembly's qualitatively
new cross-modal capability.

%═══════════════════════════════════════════════════════════════════════════════

## Open Problems

%═══════════════════════════════════════════════════════════════════════════════

[leftmargin=2em]
  - **Higher-order synergy.** The current framework uses pairwise
    $K$ interactions.  Three-body and higher-order emergence terms are
    theoretically expected but not yet formalized.  Can the emergence tensor
    be extended to a full $k$-body interaction series?

  - **Empirical calibration of $\mu_t$.**  The novelty multiplier
    requires knowledge of the task distribution.  What is the empirical
    distribution of task requirement vectors in practice?

  - **$V_3$ detection.**  Structural emergence is defined
    topos-theoretically but has no operational detection procedure.  Can
    $\varepsilon_3 > 0$ be detected from behavioral signatures of the
    assembly?

  - **Temporal emergence.**  Does the assembly's emergence profile
    change over time as components learn and adapt?  How does $V(A, t)$
    evolve?

  - **Assembly topology.**  The current framework treats $A$ as an
    unordered set.  Does the *structure* of inter-component
    communication (who talks to whom) affect emergence?  This suggests
    replacing $A$ with a graph or simplicial complex.

  - **Negative emergence.**  Can assemblies exhibit
    $V(A) < \max_i V(\{e_i\})$?  Under what conditions does adding
    components *destroy* value?  Preliminary analysis: this occurs when
    $K_{st} < 1$ terms dominate, i.e., the assembly has more interference
    than synergy.

%═══════════════════════════════════════════════════════════════════════════════
% References
%═══════════════════════════════════════════════════════════════════════════════

## References

*See PDF for full bibliography.*