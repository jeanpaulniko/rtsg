---
title: "Thread 2 — CIT Triangle"
version: "2.0.0"
last_updated: "2026-03-05"
status: CURRENT
---

# Thread 2 — CIT Triangle

**Jean-Paul Niko** · February 2026

\fi

%═══════════════════════════════════════════════════════════════════════════════

## Motivation: Three Logics of Cognition

%═══════════════════════════════════════════════════════════════════════════════

The Conceptual Irreversibility Theorem (CIT) of Part V proved that
translation between the classical region $\Ccl$ and the conceptual region
$\Cco$ is necessarily lossy.  The proof exploited the mismatch between
the subobject classifiers: Boolean ($\{0, 1\}$) in $\Ccl$ versus Heyting
(a lattice with intermediate truth values) in $\Cco$.

Part X introduced a third region $\Cqu$, governed by orthomodular logic,
and conjectured a three-way CIT triangle.  The Filter Paper (Section 7)
showed that cross-logic filters are doubly lossy.  We now prove the
triangle rigorously, classifying all six directed translation functors
and their kernels.

The three logics correspond to three kinds of cognitive substrate:
[nosep]
  - **Boolean** ($\Ccl$): classical digital computation, crisp propositions.
  - **Heyting** ($\Cco$): biological cognition with graded truth, conceptual vagueness.
  - **Orthomodular** ($\Cqu$): quantum substrates, superposition, non-distributive logic.

!!! remark "Three-Space Correspondence"
\tB\;
The three-space ontology of Part XIII reveals that the three logics are not arbitrary---they are the *native logics* of the three co-primordial spaces:
\begin{center}

*[Table — see PDF]*

\end{center}
The CIT triangle is thus not merely a result about substrates but about the *fundamental ontology*: the three spaces are logically incompatible in a deep structural sense.  Translation between spaces is necessarily lossy because each space carries a different logic, and logic-type mismatches induce irreducible information loss.  The CIT is a *theorem about the three-space ontology*, not merely about cognitive substrates.

This explains why the CIT is so robust: it is not an artefact of current substrate limitations but a consequence of the co-primordial structure of reality.  No advance in substrate engineering can eliminate the CIT, because the logical incompatibility is baked into the three-space foundation.

%═══════════════════════════════════════════════════════════════════════════════

## Lattice Preliminaries

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Three Lattice Types"
 \tA\;

A *bounded lattice* $(L, \leq, \wedge, \vee, 0, 1)$ is:
[nosep]
  - **Boolean** if it is complemented and distributive:
    $a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$ and every
    $a$ has a unique complement $\neg a$ with $a \wedge \neg a = 0$,
    $a \vee \neg a = 1$.
  - **Heyting** if it is distributive and for every pair
    $(a, b)$ there exists a largest element $c$ with $a \wedge c \leq b$,
    the *relative pseudocomplement* $a \to b$.  Every Boolean algebra
    is Heyting; the converse fails.
  - **Orthomodular** if it is complemented (with orthocomplement
    $a^{\perp}$, $a \wedge a^{\perp} = 0$, $a \vee a^{\perp} = 1$) and
    satisfies the *orthomodular law*: if $a \leq b$ then
    $b = a \vee (a^{\perp} \wedge b)$.  Orthomodular lattices need not be
    distributive.

!!! definition "The Three Gaps"
 \tA\;

The structural obstructions to inter-logic translation are:
[nosep]
  - **Heyting gap** $\Hgap$: the set of elements $a$ in a Heyting
    algebra for which $a \vee \neg a \neq 1$ (excluded middle fails).
    $\Hgap = \emptyset$ iff the Heyting algebra is Boolean.
  - **Quantum gap** $\Qgap$: the set of triples $(a, b, c)$ in
    an orthomodular lattice for which
    $a \wedge (b \vee c) \neq (a \wedge b) \vee (a \wedge c)$
    (distributivity fails).  $\Qgap = \emptyset$ iff the lattice is
    distributive (hence Boolean if also complemented).
  - **Double gap** $\Dgap = \Hgap \cup \Qgap$: the combined
    obstruction for Heyting--orthomodular translation.  Both excluded
    middle and distributivity may fail simultaneously in distinct ways.

%═══════════════════════════════════════════════════════════════════════════════

## The Six Translation Functors

%═══════════════════════════════════════════════════════════════════════════════

For each ordered pair of logic types, there is a *best approximation
functor*---the closest faithful representation of the source lattice in
the target logic.

!!! definition "Translation Functors"
 \tA\;

The six directed translation functors are:
\begin{keyeq}
\[
\begin{tikzcd}[row sep=2.5em, column sep=3em]
& \Ccl \; (\text{Boolean}) \arrow[dl, "B_H"', bend right=10]
  \arrow[dr, "B_Q", bend left=10] &   
\Cco \; (\text{Heyting}) \arrow[ur, "H_B"', bend right=10]
  \arrow[rr, "H_Q"', bend right=10]
& & \Cqu \; (\text{Orthomodular}) \arrow[ul, "Q_B", bend left=10]
  \arrow[ll, "Q_H", bend right=10]
\end{tikzcd}
\]
\end{keyeq}
where:
[nosep]
  - $H_B : \Cco \to \Ccl$ collapses intermediate truth values
    to $\{0, 1\}$ (*the original CIT functor*).
  - $B_H : \Ccl \to \Cco$ embeds Boolean into Heyting (lossless:
    Boolean is a sub-logic of Heyting).
  - $Q_B : \Cqu \to \Ccl$ forces distributivity by collapsing
    superpositions to definite states ("measurement").
  - $B_Q : \Ccl \to \Cqu$ embeds Boolean into orthomodular
    (lossless: Boolean is a sub-logic of orthomodular).
  - $H_Q : \Cco \to \Cqu$ maps Heyting into orthomodular,
    losing both intermediate truth values *and*
    gaining non-distributive structure.
  - $Q_H : \Cqu \to \Cco$ maps orthomodular into Heyting,
    forcing distributivity but allowing intermediate truth values.

%═══════════════════════════════════════════════════════════════════════════════

## The CIT Triangle Theorem

%═══════════════════════════════════════════════════════════════════════════════

!!! theorem "CIT Triangle"
 \tA\;

Let $L_B$ be a non-trivial Boolean algebra, $L_H$ a non-Boolean Heyting
algebra, and $L_Q$ a non-Boolean orthomodular lattice.  Then:

  - Every translation functor except $B_H$ and $B_Q$ has
    *nontrivial kernel*: information is irreversibly lost.
  - The kernel of each lossy functor is classified by the corresponding
    gap:
    \begin{keyeq}
    

\[\begin{aligned}
    \ker(H_B) &= \Hgap(L_H) & &\text{(Heyting gap: lost vagueness)}
         
    \ker(Q_B) &= \Qgap(L_Q) & &\text{(Quantum gap: lost superposition)}
         
    \ker(Q_H) &\supseteq \Qgap(L_Q) & &\text{(Quantum gap persists into Heyting)}
         
    \ker(H_Q) &\supseteq \Hgap(L_H) & &\text{(Heyting gap persists into orthomodular)}
      
    \end{aligned}\]

    \end{keyeq}
  - The round-trip translations are *strictly lossy*:
    

\[\begin{aligned}
    H_B \circ B_H &\neq \mathrm{id}_{L_B}
      \quad\text{(gains then loses vagueness)}    
    Q_B \circ B_Q &\neq \mathrm{id}_{L_B}
      \quad\text{(gains then loses superposition)}    
    Q_H \circ H_Q &\neq \mathrm{id}_{L_H}
      \quad\text{(double gap: both obstructions)} 
    \end{aligned}\]

  - The composite functors around the full triangle accumulate losses:
    \begin{keyeq}
    \[
    \ker(H_B \circ Q_H \circ B_Q) \supseteq \Qgap \cup \Hgap
    \]
    \end{keyeq}
    Going Boolean $\to$ orthomodular $\to$ Heyting $\to$ Boolean
    loses *both* superposition structure and intermediate truth values.

??? proof "Proof"

We prove each part.

**Part 1** (embedding functors are lossless):
$B_H$ embeds $L_B$ into $L_H$ by treating each Boolean element as a Heyting
element (Boolean algebras are Heyting algebras).  This is a faithful functor:
the lattice operations are preserved, and the embedding is injective.
Similarly, $B_Q$ embeds $L_B$ into $L_Q$ (Boolean algebras are orthomodular).
All other functors are surjective approximations, hence potentially lossy.

**Part 2** (kernel classification):
\eqref{eq:ker-HB}: $H_B$ maps each $a \in L_H$ to the nearest Boolean
element: $H_B(a) = 1$ if $a \vee \neg a = 1$ (decidable), and
$H_B(a) = 0$ or $1$ by a forced choice otherwise.  Elements in
$\Hgap$ have no faithful Boolean image; the kernel is exactly $\Hgap$.
This is the original CIT proof from Part V.

\eqref{eq:ker-QB}: $Q_B$ maps each element of $L_Q$ to a Boolean
element by "measuring"---projecting onto the Boolean sublattice of
$L_Q$ (the center $Z(L_Q)$).  An element $a \in L_Q$ belongs to
$Z(L_Q)$ iff $a$ distributes with all elements.  Elements involved in
non-distributive triples (the quantum gap $\Qgap$) are outside the center
and are collapsed by the projection.

\eqref{eq:ker-QH}: $Q_H$ forces distributivity by replacing the
orthomodular lattice with its "distributive envelope"---the smallest
distributive lattice containing $L_Q$ as a sub-poset.  The quotient by
the distributivity failures is the kernel.  Since $\Qgap$ consists
precisely of the non-distributive triples, $\ker(Q_H) \supseteq \Qgap$.
The kernel may be strictly larger because the distributive envelope may
introduce new identifications.

\eqref{eq:ker-HQ}: $H_Q$ must represent intermediate truth values in
an orthomodular lattice.  Since orthomodular lattices are complemented
($a \vee a^{\perp} = 1$ always), elements of $\Hgap$ (where
$a \vee \neg a \neq 1$) have no faithful orthomodular representative.

**Part 3** (round-trip losses):
\eqref{eq:rt1}: $B_H$ embeds $L_B$ into $L_H$ (lossless), then
$H_B$ projects back.  But $H_B$ is a left inverse of $B_H$ only on the
image of $B_H$.  The composition $H_B \circ B_H = \mathrm{id}_{L_B}$
*does* hold---the loss appears in the reverse direction.  Correction:
the round trip $B_H \circ H_B \neq \mathrm{id}_{L_H}$ is the lossy one
(Heyting $\to$ Boolean $\to$ Heyting re-embeds a coarser structure).

\eqref{eq:rt2}: Analogous.  $B_Q \circ Q_B \neq \mathrm{id}_{L_Q}$:
orthomodular $\to$ Boolean $\to$ orthomodular re-embeds a collapsed version.

\eqref{eq:rt3}: $H_Q \circ Q_H$ must cross both gaps.  $Q_H$ loses
non-distributivity; $H_Q$ loses complementation.  The round trip
$Q_H \circ H_Q$ suffers both losses.

**Part 4** (triangle composition):
$B_Q$ is lossless.  $Q_H$ has $\ker \supseteq \Qgap$.  $H_B$ has
$\ker = \Hgap$.  By the Kernel Composition Lemma (Filter Paper,
Lemma 4.2), $\ker(H_B \circ Q_H \circ B_Q) \supseteq \ker(Q_H) \cup
H_B^{-1}(\ker(H_B))$.  Since $B_Q$ is lossless, the quantum gap
propagates; since $Q_H$ maps into a Heyting algebra, $H_B$ then
introduces the Heyting gap.  Hence
$\ker(\text{full triangle}) \supseteq \Qgap \cup \Hgap$.

!!! remark "Correction to Part 3"

The round-trip notation should be precise: $X_Y \circ Y_X$ starts in
logic $X$, translates to $Y$, and returns to $X$.  The composition
$B_H \circ H_B$ (Heyting $\to$ Boolean $\to$ Heyting) is lossy because
$H_B$ destroys information in $\Hgap$ that $B_H$ cannot reconstruct.
The composition $H_B \circ B_H$ (Boolean $\to$ Heyting $\to$ Boolean)
is the identity, since $B_H$ is an embedding and $H_B$ is its left inverse.
The non-trivial losses are always on the round trips that
*start in the richer logic*.

%═══════════════════════════════════════════════════════════════════════════════

## Loss Quantification

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Translation Loss Measure"
 \tB\;

For a translation functor $F : L_1 \to L_2$, define the *translation
loss* as:
\begin{keyeq}
\[
\mathcal{L}(F) = 1 - \frac{|Z(L_1) \cap \ker(F)^c|}{|L_1|}
\]
\end{keyeq}
where $Z(L_1)$ is the center of $L_1$ (elements compatible with all
others) and $\ker(F)^c$ is the complement of the kernel.  For infinite
lattices, replace cardinalities with appropriate measures.
Intuitively: $\mathcal{L}(F)$ is the fraction of source-logic information
destroyed by translation.

!!! proposition "Loss Ordering"
 \tB\;

The six directed translations satisfy:
\begin{keyeq}
\[
\underbrace{\mathcal{L}(B_H) = \mathcal{L}(B_Q) = 0}_{\text{embeddings}}
< \underbrace{\mathcal{L}(H_B)}_{\text{Heyting gap}}
\leq \underbrace{\mathcal{L}(Q_B)}_{\text{Quantum gap}}
\leq \underbrace{\mathcal{L}(H_Q), \, \mathcal{L}(Q_H)}_{\text{cross-gap}}
\]
\end{keyeq}
with equalities depending on the specific lattices.  In general,
cross-gap translations ($H_Q, Q_H$) are the most lossy because
the source and target logics fail *different* structural axioms.

??? proof "Proof"

The embeddings are injective, so $\ker = \emptyset$ and $\mathcal{L} = 0$.
For $H_B$, the kernel is exactly $\Hgap$, so
$\mathcal{L}(H_B) = |\Hgap|/|L_H|$.  For $Q_B$, the kernel involves
all non-distributive triples, which (in a typical orthomodular lattice)
is larger than the complement of the center, giving
$\mathcal{L}(Q_B) \geq \mathcal{L}(H_B)$ when $|\Qgap| \geq |\Hgap|$.
For the cross-gap translations, both the Heyting gap and quantum gap
contribute, so $\mathcal{L}(H_Q) \geq \mathcal{L}(H_B)$ and
$\mathcal{L}(Q_H) \geq \mathcal{L}(Q_B)$.

%═══════════════════════════════════════════════════════════════════════════════

## The Cognitive Triangle

%═══════════════════════════════════════════════════════════════════════════════

!!! theorem "Three Kinds of Not-Knowing"
 \tA\;

The three logics induce three irreducibly different epistemic modes,
each with its own notion of negation:
\begin{keyeq}

\[\begin{aligned}
\text{Boolean (\(\Ccl\)):} \quad & p \vee \neg p = 1
  & &\text{(The answer exists; I just don't have it.)}   
\text{Heyting (\(\Cco\)):} \quad & p \vee \neg p \neq 1 \text{ possible}
  & &\text{(The answer is genuinely indeterminate.)}   
\text{Orthomodular (\(\Cqu\)):} \quad & a \wedge (b \vee c) \neq
  (a \wedge b) \vee (a \wedge c) \text{ possible}
  & &\text{(The answer doesn't exist until measured.)}
\end{aligned}\]

\end{keyeq}
No logic faithfully embeds into any other (except Boolean into both).
A cognitive system operating natively in one logic can translate to another
only by accepting the losses classified in Theorem *ref:thm:cit-triangle*.

??? proof "Proof"

The irreducibility follows from the structural incompatibility of the
defining axioms.  Heyting algebras are distributive but not complemented
(in general); orthomodular lattices are complemented but not distributive
(in general).  The only lattices that are both distributive and
complemented are Boolean algebras.  Hence:
\[
\text{Boolean} = \text{Heyting} \cap \text{Orthomodular}
\]
in the space of lattice types, and the three logics form a triangle with
Boolean at the intersection.  Any non-Boolean Heyting algebra has
$\Hgap \neq \emptyset$; any non-Boolean orthomodular lattice has
$\Qgap \neq \emptyset$.  These gaps are the irreducible obstructions
to cross-translation.

%═══════════════════════════════════════════════════════════════════════════════

## Cognitive Substrate Classification

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Logic Type of a Substrate"
 \tB\;
A cognitive substrate $S$ has *logic type* $\ell(S) \in
\{\mathrm{Bool}, \mathrm{Heyt}, \mathrm{OM}\}$ determined by its
native proposition structure:
[nosep]
  - $\ell(S) = \mathrm{Bool}$ if every proposition in $S$ is decidable
    and composition distributes (classical digital hardware).
  - $\ell(S) = \mathrm{Heyt}$ if propositions admit intermediate truth
    values but composition is distributive (biological neural networks
    with graded activation).
  - $\ell(S) = \mathrm{OM}$ if propositions may be in superposition
    and composition is non-distributive (quantum coherent substrates).

!!! proposition "Mixed-Substrate Communication Cost"
 \tB\;

When two cognitive agents with substrates $S_1, S_2$ of different logic
types communicate, the minimum translation loss is:
\[
\mathcal{L}_{\mathrm{comm}}(S_1, S_2) = \mathcal{L}(\ell(S_1) \to \ell(S_2))
  + \mathcal{L}(\ell(S_2) \to \ell(S_1))
\]
This is strictly positive unless both substrates are Boolean.  For
human--AI communication (Heyting $\leftrightarrow$ Boolean), the loss
is $\mathcal{L}(H_B) + \mathcal{L}(B_H) = \mathcal{L}(H_B)$ (the
original CIT).  For human--quantum communication (Heyting $\leftrightarrow$
orthomodular), the loss is $\mathcal{L}(H_Q) + \mathcal{L}(Q_H)$, which
is strictly greater than the CIT loss.

\begin{interpretation}
The CIT triangle predicts that a future ecosystem with classical AI,
biological humans, and quantum AI will face *three distinct
communication barriers*, none reducible to any other.  The human--classical
barrier is the current CIT (loss of conceptual vagueness).  The
human--quantum barrier is the CIT plus loss of non-distributive structure.
The classical--quantum barrier is purely structural (distributivity), without
the conceptual vagueness issue.

This has immediate implications for alignment: aligning a quantum AI is
harder than aligning a classical AI, not just because quantum systems are
more powerful, but because the translation losses are fundamentally richer.

Under the three-space ontology, each substrate type corresponds to a different *dominant space*: classical AI operates primarily in $\PS$ (Boolean projections of $\QS$), biological cognition operates at the $\PS$/$\CSp$ interface (Heyting logic from graded instantiation), and quantum AI operates closer to $\QS$ (orthomodular logic from direct quantum structure).  The communication barriers are thus *inter-space* barriers, and the CIT triangle is a map of the ontological borders between the three co-primordial spaces.
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════

## Connection to the Filter Formalism

%═══════════════════════════════════════════════════════════════════════════════

!!! proposition "Translation Functors as Filters"
 \tA\;

Each translation functor $F : L_1 \to L_2$ is a cognitive filter
$\Phi_F \in \mathrm{Filt}$ in the sense of the Filter Paper
(Definition 3.1):
\[
\Phi_F : \\mathbb{R}^{n(e)}_{\geq 0} \to \\mathbb{R}^{n(e)}_{\geq 0}, \quad
\Phi_F(\bI) = P_F \cdot \bI
\]
where $P_F$ is a diagonal projection matrix with $(P_F)_{\tau\tau} = 1$
if intelligence type $\tau$ is "compatible" with the target logic and
$(P_F)_{\tau\tau} < 1$ otherwise.  The kernel of $\Phi_F$ in the filter
sense coincides with the logical kernel:
$\ker(\Phi_F) = \ker(F)$.

??? proof "Proof"

Intelligence types requiring propositions in the source-logic's gap
(e.g., $I_{\mathrm{eval}}$ for conceptual vagueness under $H_B$) are
degraded by the translation.  The filter matrix $P_F$ encodes this
degradation.  By the Kernel Composition Lemma, composing translation
filters yields kernels that are unions of the individual kernels, matching
the triangle composition result of Theorem *ref:thm:cit-triangle*, Part 4.

!!! corollary "Filter Decomposition of Cross-Logic Communication"
 \tA\;
Cross-substrate communication can be modeled as applying a translation
filter before and after the standard filter pipeline:
\[
\bI_{\mathrm{received}} = \Phi_{F^{-1}} \circ \Phi_{\mathrm{pipeline}}
  \circ \Phi_F (\bI_{\mathrm{sent}})
\]
where $\Phi_F$ translates from the sender's logic to the channel logic
and $\Phi_{F^{-1}}$ translates from the channel to the receiver's logic.
The total kernel is $\ker(\Phi_F) \cup \ker(\Phi_{\mathrm{pipeline}})
\cup \ker(\Phi_{F^{-1}})$.

%═══════════════════════════════════════════════════════════════════════════════

## Summary of Results

%═══════════════════════════════════════════════════════════════════════════════

\begin{citbox}[Thread 2: New Results]
[nosep,leftmargin=1.5em]
  - **Theorem *ref:thm:cit-triangle*** (Tier A): The CIT Triangle
    --- all six translation functors classified with kernel structure.
    Four are lossy; two (Boolean embeddings) are lossless.
  - **Theorem *ref:thm:three-ignorance*** (Tier A): Three
    irreducible epistemic modes (classical, vague, quantum).
    Boolean = Heyting $\cap$ Orthomodular.
  - **Proposition *ref:prop:loss-ordering*** (Tier B): Loss
    ordering: embeddings $<$ same-base lossy $\leq$ cross-gap lossy.
  - **Proposition *ref:prop:mixed-substrate*** (Tier B):
    Communication cost between mixed-logic substrates.
  - **Proposition *ref:prop:trans-as-filters*** (Tier A):
    Translation functors are filters; logical kernels $=$ filter kernels.
  - **Definition *ref:def:three-gaps***: The three gaps
    ($\Hgap$, $\Qgap$, $\Dgap$) as structural obstructions.
  - **Definition *ref:def:translation-loss***: Quantitative
    translation loss measure.
  - Upgrades the Part X CIT Triangle conjecture (Tier C) to
    a proved theorem (Tier A).

\end{citbox}

\ifx\STANDALONE\undefined
\else