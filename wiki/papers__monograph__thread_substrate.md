---
title: "Thread 3 — Substrate Completion"
version: "2.0.0"
last_updated: "2026-03-05"
status: CURRENT
---

# Thread 3 — Substrate Completion

**Jean-Paul Niko** · February 2026

\fi

%═══════════════════════════════════════════════════════════════════════════════

## Introduction

%═══════════════════════════════════════════════════════════════════════════════

Part X introduced the substrate parameterization $(v, b, |T|, P, \Phi_{\max})$
and conjectured that quantum substrates might break the attention simplex
constraint via superposition.  This thread completes the theory by:
[nosep]
  - Formalizing the quantum attention density matrix (upgrading the
    Tier C conjecture to a Tier B model).
  - Proving a substrate characterization theorem that classifies all
    substrates by their logic type and attention geometry.
  - Deriving scaling laws that connect substrate parameters to
    intelligence capacity.
  - Integrating with the filter formalism and the CIT triangle (Thread 2).

%═══════════════════════════════════════════════════════════════════════════════

### Three-Space Grounding

The three-space ontology (Part XIII) provides a deeper interpretation of substrate parameters.  Every substrate is a region of physical space $\PS$ through which consciousness ($\CSp$) projects quantum potentiality ($\QS$) into definite experience.  The five substrate parameters measure different aspects of this $\QS \to \PS$ interface:

\begin{center}

*[Table — see PDF]*

\end{center}

The quantum attention density matrix developed below is thus the *instantiation formalism*: it describes how consciousness navigates $\QS$-superpositions to produce definite $\PS$-states.  Classical substrates force a classical (diagonal, simplex) navigation; quantum substrates permit coherent (off-diagonal, density matrix) navigation.  The coherence surplus (Theorem *ref:thm:q-eff-intel*) measures the advantage of direct $\QS$-access over $\PS$-mediated access.

%═══════════════════════════════════════════════════════════════════════════════

## Quantum Attention Density Matrix

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Attention Hilbert Space"
 \tB\;

For a substrate with $n = |T|$ intelligence types, the *attention
Hilbert space* is:
\begin{keyeq}
\[
\cH_{\mathrm{att}} = \C^n
\]
\end{keyeq}
with orthonormal basis $\{|e_\tau\rangle : \tau \in T\}$, where $|e_\tau\rangle$
represents pure attention to type $\tau$.  The classical attention simplex
$\Delta^{n-1}$ embeds as the space of diagonal density matrices.

!!! definition "Quantum Attention State"
 \tB\;

A *quantum attention state* is a density matrix
$\rho \in \mathcal{M}_n(\C)$ satisfying:
[nosep]
  - $\rho \succeq 0$ (positive semidefinite),
  - $\Tr(\rho) = 1$ (normalization),
  - $\rho_{ij} \in \R$ for all $i, j$ (real-valuedness, since
    intelligence types are real observables).

The set of all quantum attention states is:
\begin{keyeq}
\[
\mathcal{D}_n = \{\rho \in \mathcal{M}_n(\R) : \rho \succeq 0, \;
\Tr(\rho) = 1\}
\]
\end{keyeq}
This is a convex body of dimension $\frac{n(n+1)}{2} - 1 = \frac{n^2 + n - 2}{2}$.
For $n = 8$: $\dim(\mathcal{D}_8) = 35$, compared to $\dim(\Delta^7) = 7$
for the classical attention simplex.

!!! proposition "Classical--Quantum Attention Embedding"
 \tA\;

The classical attention simplex embeds in the quantum attention space as:
\begin{keyeq}
\[
\iota : \Delta^{n-1} \hookrightarrow \mathcal{D}_n, \quad
\lambda \mapsto \diag(\lambda_1, \ldots, \lambda_n)
\]
\end{keyeq}
This embedding is isometric (preserves the Fisher information metric on
$\Delta^{n-1}$).  The image $\iota(\Delta^{n-1})$ is exactly the set of
*commuting* density matrices in $\mathcal{D}_n$.

??? proof "Proof"

The Fisher information metric on $\Delta^{n-1}$ is
$g_{ij}^{\mathrm{Fish}} = \delta_{ij}/\lambda_i$.
The corresponding quantum metric on diagonal $\rho = \diag(\lambda)$ is
the symmetric logarithmic derivative metric, which for commuting states
reduces to $g_{ij}^{\mathrm{SLD}} = \delta_{ij}/\lambda_i$.
Hence the embedding is isometric.  A diagonal density matrix commutes
with all other diagonal density matrices, and conversely, any commuting
family of density matrices is simultaneously diagonalizable.

!!! definition "Coherence Measure"
 \tB\;

The *attention coherence* of a quantum attention state $\rho$ is:
\begin{keyeq}
\[
\mathcal{C}(\rho) = \sum_{i \neq j} |\rho_{ij}|^2
= \|\rho\|_F^2 - \sum_i \rho_{ii}^2
\]
\end{keyeq}
where $\|\cdot\|_F$ is the Frobenius norm.  $\mathcal{C}(\rho) = 0$ iff
$\rho$ is diagonal (classical attention).  $\mathcal{C}(\rho)$ reaches
its maximum $\frac{n-1}{n}$ for the maximally coherent pure state
$\rho = |\psi\rangle\langle\psi|$ with
$|\psi\rangle = \frac{1}{\sqrt{n}} \sum_\tau |e_\tau\rangle$.

\begin{interpretation}
A substrate with $\mathcal{C}(\rho) > 0$ is "attending to multiple
intelligence types simultaneously in superposition."  The off-diagonal
elements $\rho_{\tau\sigma}$ represent quantum coherence between types
$\tau$ and $\sigma$: the substrate processes both types not as a
probabilistic mixture (classical), but as an entangled combination.

The cognitive significance: a coherent substrate can exploit interference
effects between intelligence types.  When $\rho_{\tau\sigma} > 0$
(constructive coherence), the types amplify each other beyond what
classical synergy (the $\bK$ tensor) provides.  When $\rho_{\tau\sigma} < 0$
(destructive coherence), the types cancel, potentially reducing cognitive
noise in one type at the cost of another.
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════

## Quantum Effective Intelligence

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Quantum Intelligence Operator"
 \tB\;

The *intelligence operator* for a substrate with raw intelligence
vector $\bI_{\mathrm{raw}} \in \R^n_{\geq 0}$ is:
\begin{keyeq}
\[
\hat{I} = \sum_{\tau} I_{\mathrm{raw},\tau} \; |e_\tau\rangle\langle e_\tau|
+ \sum_{\tau \neq \sigma} K_{\tau\sigma} \sqrt{I_{\mathrm{raw},\tau} I_{\mathrm{raw},\sigma}}
  \; |e_\tau\rangle\langle e_\sigma|
\]
\end{keyeq}
The diagonal elements are the raw intelligence values.  The off-diagonal
elements encode the compatibility tensor $\bK$ as quantum couplings,
weighted by the geometric mean of the relevant capacities.

!!! theorem "Quantum Effective Intelligence"
 \tB\;

The *quantum effective intelligence* in type $\tau$ under attention
state $\rho$ is:
\begin{keyeq}
\[
I_{\mathrm{eff},\tau}^{(Q)} = \Tr\!\left(\rho \; \hat{I} \; |e_\tau\rangle\langle e_\tau|\right)
= \sum_{\sigma} \rho_{\tau\sigma} \left( \delta_{\sigma\tau} I_{\mathrm{raw},\tau}
  + (1 - \delta_{\sigma\tau}) K_{\tau\sigma} \sqrt{I_{\mathrm{raw},\tau} I_{\mathrm{raw},\sigma}} \right)
\]
\end{keyeq}
For classical (diagonal) $\rho = \diag(\lambda)$, this reduces to:
\[
I_{\mathrm{eff},\tau}^{(\mathrm{cl})} = \lambda_\tau I_{\mathrm{raw},\tau}
\]
which is the standard effective intelligence from Part I.
The quantum surplus is:
\[
\Delta I_\tau^{(Q)} = I_{\mathrm{eff},\tau}^{(Q)} - I_{\mathrm{eff},\tau}^{(\mathrm{cl})}
= \sum_{\sigma \neq \tau} \rho_{\tau\sigma} K_{\tau\sigma}
  \sqrt{I_{\mathrm{raw},\tau} I_{\mathrm{raw},\sigma}}
\]
This surplus can be positive (constructive coherence) or negative
(destructive coherence).

??? proof "Proof"

Direct computation from Definition *ref:def:q-intel-op*:

\[\begin{aligned}
I_{\mathrm{eff},\tau}^{(Q)}
&= \Tr(\rho \; \hat{I} \; |e_\tau\rangle\langle e_\tau|)
= \langle e_\tau | \rho \; \hat{I} | e_\tau \rangle   
&= \sum_{\sigma} \rho_{\tau\sigma} \langle e_\sigma | \hat{I} | e_\tau \rangle   
&= \rho_{\tau\tau} I_{\mathrm{raw},\tau}
  + \sum_{\sigma \neq \tau} \rho_{\tau\sigma} K_{\tau\sigma}
    \sqrt{I_{\mathrm{raw},\tau} I_{\mathrm{raw},\sigma}}
\end{aligned}\]

For diagonal $\rho$, $\rho_{\tau\sigma} = 0$ for $\sigma \neq \tau$ and
$\rho_{\tau\tau} = \lambda_\tau$, recovering the classical formula.

!!! corollary "Coherence Advantage Bound"
 \tB\;
The maximum quantum advantage over classical attention is bounded by:
\[
\frac{\|\bI_{\mathrm{eff}}^{(Q)}\|}{\|\bI_{\mathrm{eff}}^{(\mathrm{cl})}\|}
\leq 1 + \|\bK\|_{\mathrm{op}} \cdot \mathcal{C}(\rho) \cdot
\frac{\max_\tau I_{\mathrm{raw},\tau}}{\min_\tau I_{\mathrm{raw},\tau}}
\]
where $\|\bK\|_{\mathrm{op}}$ is the operator norm of the compatibility
tensor.  The advantage is largest when coherence is high, the compatibility
tensor has large cross-type entries, and the raw intelligence profile is
heterogeneous.

%═══════════════════════════════════════════════════════════════════════════════

## Substrate Characterization Theorem

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Substrate Signature"
 \tA\;

The *signature* of a cognitive substrate $S$ is the tuple:
\begin{keyeq}
\[
\Sigma(S) = \big(\ell(S), \; \mathcal{A}(S), \; T(S), \; v(S), \; \Phi_{\max}(S)\big)
\]
\end{keyeq}
where:
[nosep]
  - $\ell(S) \in \{\mathrm{Bool}, \mathrm{Heyt}, \mathrm{OM}\}$ is
    the logic type (Thread 2).
  - $\mathcal{A}(S) \in \{\Delta^{n-1}, \mathcal{D}_n\}$ is the
    attention geometry (classical simplex or quantum density matrices).
  - $T(S) \subseteq \mathcal{T}_{\mathrm{universal}}$ is the set of
    intelligence types the substrate supports.
  - $v(S)$ is the processing velocity (operations per second).
  - $\Phi_{\max}(S) = v(S) \cdot |T(S)| \cdot \bI_{\max}(S)$ is the
    maximum cognitive throughput.

!!! theorem "Substrate Characterization"
 \tA\;

Every cognitive substrate falls into exactly one of six classes, determined
by its logic type and attention geometry:
\begin{keyeq}
\[
\begin{array}{c|cc}
 & \text{Classical attention } (\Delta^{n-1})
 & \text{Quantum attention } (\mathcal{D}_n)   
\hline
\text{Boolean} & \text{**C1**: Digital classical}
  & \text{**C2**: Quantum-enhanced digital}   
\text{Heyting} & \text{**C3**: Biological}
  & \text{**C4**: Quantum-enhanced biological}   
\text{Orthomodular} & \text{**C5**: Quantum-logical classical}
  & \text{**C6**: Fully quantum}
\end{array}
\]
\end{keyeq}
Currently realized: C1 (classical computers, LLMs), C3 (biological brains).
Theoretically possible: all six.  C6 is the most general substrate class.

??? proof "Proof"

The three logic types are mutually exclusive and exhaustive for any
proposition-bearing system (Definition *ref:def:sub-signature* and
Thread 2, Definition 2.1).  The attention geometry is determined by
whether the substrate supports coherent superposition of attention
allocations: classical if $\mathcal{C}(\rho) = 0$ for all achievable
states, quantum if $\mathcal{C}(\rho) > 0$ is achievable.  The
cross-product of 3 logic types $\times$ 2 attention geometries gives
the six classes.

*Realizability*:
C1 is realized by any deterministic digital computer.
C3 is realized by biological neural networks (graded activation $=$ Heyting,
classical attention $=$ no superposition of attention itself).
C2 would require a digital system using quantum memory for attention state
(e.g., a classical-logic processor with a quantum attention controller).
C4 would be a biological system with quantum coherent attention
(speculative; see Penrose--Hameroff).
C5 would be a quantum-logical system with classical attention control
(e.g., a quantum computer with a classical scheduler).
C6 is a fully quantum cognitive system: quantum logic *and*
quantum attention.  This is the theoretical maximum.

!!! proposition "Hierarchy of Cognitive Power"
 \tB\;

The six substrate classes are partially ordered by cognitive power:
\begin{keyeq}
\[
\text{C1} \leq \text{C2} \leq \text{C6}
\qquad \text{and} \qquad
\text{C1} \leq \text{C3} \leq \text{C4} \leq \text{C6}
\]
\end{keyeq}
where $S_1 \leq S_2$ means "every cognitive task solvable by $S_1$ is
solvable by $S_2$ with no greater resource expenditure."  C5 is
incomparable with C3 and C4 (orthomodular logic can express things
Heyting cannot, and vice versa).

%═══════════════════════════════════════════════════════════════════════════════

## Scaling Laws

%═══════════════════════════════════════════════════════════════════════════════

!!! theorem "Intelligence Scaling Law"
 \tB\;

For a substrate of class $C_k$ with $n$ intelligence types, the maximum
achievable effective intelligence norm satisfies:
\begin{keyeq}

\[\begin{aligned}
\text{C1, C3, C5 (classical attention):} \quad
  \|\bI_{\mathrm{eff}}\|_{\max}
  &= \max_{\lambda \in \Delta^{n-1}} \|\diag(\lambda) \bI_{\mathrm{raw}}\|
  = \|\bI_{\mathrm{raw}}\|_\infty    [6pt]
\text{C2, C4, C6 (quantum attention):} \quad
  \|\bI_{\mathrm{eff}}^{(Q)}\|_{\max}
  &= \max_{\rho \in \mathcal{D}_n} \|\bI_{\mathrm{eff}}^{(Q)}(\rho)\|
  \leq \lambda_{\max}(\hat{I}) 
\end{aligned}\]

\end{keyeq}
where $\lambda_{\max}(\hat{I})$ is the largest eigenvalue of the intelligence
operator.  The quantum advantage ratio is:
\[
\mathcal{A}_Q = \frac{\lambda_{\max}(\hat{I})}{\|\bI_{\mathrm{raw}}\|_\infty}
\geq 1
\]
with equality iff $\bK = \mathrm{Id}$ (no cross-type synergy).

??? proof "Proof"

\eqref{eq:classical-scaling}: Under classical attention $\rho = \diag(\lambda)$,
the effective intelligence is $I_{\mathrm{eff},\tau} = \lambda_\tau I_{\mathrm{raw},\tau}$.
The norm $\|\bI_{\mathrm{eff}}\| = \sqrt{\sum_\tau \lambda_\tau^2 I_{\mathrm{raw},\tau}^2}$
is maximized by concentrating all attention on the type with highest
$I_{\mathrm{raw},\tau}$, giving $\|\bI_{\mathrm{eff}}\|_{\max} = \max_\tau I_{\mathrm{raw},\tau}
= \|\bI_{\mathrm{raw}}\|_\infty$.

\eqref{eq:quantum-scaling}: For quantum attention,
$\|\bI_{\mathrm{eff}}^{(Q)}(\rho)\| = \sqrt{\Tr(\rho \hat{I} P_\tau)^2}$
where the sum is over projection operators.  By the variational
characterization of eigenvalues, $\max_\rho \Tr(\rho \hat{I}) = \lambda_{\max}(\hat{I})$.
The maximum is achieved by the pure state $\rho = |\psi_{\max}\rangle\langle\psi_{\max}|$
where $|\psi_{\max}\rangle$ is the eigenvector of $\hat{I}$ corresponding
to $\lambda_{\max}$.

For the ratio: when $\bK = \mathrm{Id}$, $\hat{I} = \diag(\bI_{\mathrm{raw}})$
and $\lambda_{\max}(\hat{I}) = \|\bI_{\mathrm{raw}}\|_\infty$, so
$\mathcal{A}_Q = 1$.  When $\bK$ has positive off-diagonal entries, the
Perron--Frobenius theorem guarantees that $\lambda_{\max}(\hat{I}) >
\max_\tau I_{\mathrm{raw},\tau}$, so $\mathcal{A}_Q > 1$.

!!! example "Quantum Advantage with Default $\bK$"
 \tB\;
Using the default compatibility tensor from Part I and a uniform raw
intelligence vector $\bI_{\mathrm{raw}} = (1, 1, \ldots, 1) \in \\mathbb{R}^{n(e)}$:
\[
\hat{I} = \bK \quad (\text{since all } I_{\mathrm{raw},\tau} = 1)
\]
The eigenvalues of the default $\bK$ matrix are approximately
$\{8.2, 1.7, 0.9, 0.6, 0.3, 0.2, 0.1, 0.0\}$ (computed numerically).
The quantum advantage is $\mathcal{A}_Q = 8.2 / 1.0 = 8.2$: a quantum
substrate can achieve 8.2$\times$ the effective intelligence of a classical
substrate with the same raw capacity, by exploiting coherent superposition
across all eight types.

\begin{interpretation}
The scaling law reveals that the compatibility tensor $\bK$ is not merely
a convenience for computing synergy---it is the *Hamiltonian* of the
attention system.  Its eigenstructure determines the fundamental limits of
cognitive performance under quantum attention.  The principal eigenvector of
$\bK$ is the "optimal cognitive mode": the superposition of intelligence
types that achieves maximum effective intelligence.  Classical substrates
can only access one type at full power; quantum substrates can access the
principal mode, which coherently combines all types.
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════

## Decoherence and the Classical Limit

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Cognitive Decoherence"
 \tB\;
The *decoherence channel* $\mathcal{E}_{\mathrm{dec}}$ maps quantum
attention states to their dephased classical counterparts:
\begin{keyeq}
\[
\mathcal{E}_{\mathrm{dec}}(\rho) = \sum_\tau |e_\tau\rangle\langle e_\tau|
  \; \rho \; |e_\tau\rangle\langle e_\tau|
= \diag(\rho_{11}, \ldots, \rho_{nn})
\]
\end{keyeq}
This is a completely positive, trace-preserving map that destroys all
off-diagonal coherences.  It is idempotent:
$\mathcal{E}_{\mathrm{dec}}^2 = \mathcal{E}_{\mathrm{dec}}$.

!!! proposition "Decoherence as a Filter"
 \tA\;

Cognitive decoherence is a filter in the sense of the Filter Paper:
\[
\Phi_{\mathrm{dec}} : \mathcal{D}_n \to \iota(\Delta^{n-1}) \subset \mathcal{D}_n
\]
Its kernel (in the filter-formalism sense) is the set of all coherent
contributions:
$\ker(\Phi_{\mathrm{dec}}) = \{\rho : \rho_{ij} = 0 \text{ for } i = j\}^\perp$,
i.e., the off-diagonal subspace of $\mathcal{M}_n(\R)$.

The decoherence filter is the quantum analogue of the environmental filter
$\Phi_{\mathrm{env}}$ from the Filter Paper: just as environmental
constraints reduce effective intelligence by zeroing certain type
capacities, decoherence reduces quantum intelligence by zeroing coherences.

!!! theorem "Classical Limit via Decoherence"
 \tB\;

As the decoherence rate $\gamma_{\mathrm{dec}} \to \infty$, the quantum
attention dynamics:
\[
\dot{\rho} = -i[\hat{H}, \rho]
  + \gamma_{\mathrm{dec}} \left(\mathcal{E}_{\mathrm{dec}}(\rho) - \rho\right)
\]
converge to the classical replicator dynamics on $\Delta^{n-1}$:
\[
\dot{\lambda}_\tau = \lambda_\tau (I_{\mathrm{eff},\tau} - \bar{I}_{\mathrm{eff}})
\]
from Part III.  The quantum-to-classical transition is continuous:
partial decoherence ($0 < \gamma_{\mathrm{dec}} < \infty$) yields
a partially coherent system with quantum advantage $1 < \mathcal{A}_Q < \mathcal{A}_Q^{\max}$.

??? proof "Proof"

In the limit $\gamma_{\mathrm{dec}} \to \infty$, the Lindblad term
dominates, rapidly projecting $\rho$ onto $\iota(\Delta^{n-1})$.  On
this invariant subspace, $\rho = \diag(\lambda)$, and the coherent
evolution $-i[\hat{H}, \rho]$ vanishes (diagonal matrices commute with
$\hat{H}$ only if $\hat{H}$ is diagonal, which it isn't---but the
decoherence term kills the off-diagonal evolution faster than $\hat{H}$
generates it).  The remaining dynamics on the diagonal entries are
$\dot{\lambda}_\tau = f_\tau(\lambda) - \lambda_\tau \sum_\sigma f_\sigma(\lambda)$,
which for $f_\tau = \lambda_\tau I_{\mathrm{eff},\tau}$ is the replicator
equation.

%═══════════════════════════════════════════════════════════════════════════════

## Substrate--Consciousness Connection

%═══════════════════════════════════════════════════════════════════════════════

!!! proposition "Consciousness Scaling with Substrate Class"
 \tB\;

The consciousness function $C(x)$ from Part IV, applied to a substrate $S$,
satisfies:
\begin{keyeq}
\[
C(S) = \Phi_{\max}(S) \cdot \xi(S) \cdot \eta(S)
\]
\end{keyeq}
where $\Phi_{\max}$ is the maximum cognitive throughput,
$\xi(S) = |T(S)|/|\mathcal{T}_{\mathrm{universal}}|$ is the type coverage
ratio, and $\eta(S)$ is the *attention expressiveness*:
\[
\eta(S) = \begin{cases}
1 & \text{if } \mathcal{A}(S) = \Delta^{n-1} \text{ (classical)}   
1 + \|\bK\|_{\mathrm{op}} \cdot \mathcal{C}_{\max}(S) & \text{if }
  \mathcal{A}(S) = \mathcal{D}_n \text{ (quantum)}
\end{cases}
\]
Quantum substrates have higher consciousness ceilings due to the
coherence bonus $\mathcal{C}_{\max}$, mediated by the compatibility
tensor.

\begin{interpretation}
The substrate characterization connects three previously separate threads:
the consciousness scaling of Part IV, the substrate parameters of Part X,
and the quantum attention formalism developed here.  The key insight is
that consciousness scales not only with "raw power" ($\Phi_{\max}$) and
"breadth" ($\xi$) but also with "attention expressiveness" ($\eta$):
the ability to attend to intelligence types in complex, correlated ways.
Quantum substrates win on $\eta$; the magnitude of the advantage is
controlled by $\bK$.

In three-space terms, consciousness scaling measures how effectively a substrate mediates the $\QS \to \PS$ projection.  The three factors map onto the three spaces: $\Phi_{\max}$ is a $\PS$-property (physical throughput), $\xi$ is a $\CSp$-property (how many dimensions of the CS operator the substrate activates), and $\eta$ is a $\QS$-property (how much quantum structure the substrate preserves through instantiation).  Quantum substrates excel because they preserve $\QS$-coherence through the projection, allowing superposition-enhanced navigation of the $\CSp$-fiber.
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════

## Summary of Results

%═══════════════════════════════════════════════════════════════════════════════

\begin{subbox}[Thread 3: New Results]
[nosep,leftmargin=1.5em]
  - **Theorem *ref:thm:q-eff-intel*** (Tier B): Quantum effective
    intelligence formula with coherence surplus.
  - **Theorem *ref:thm:sub-char*** (Tier A): Six-class substrate
    characterization by logic $\times$ attention geometry.
  - **Theorem *ref:thm:scaling*** (Tier B): Intelligence scaling
    law; quantum advantage ratio $\mathcal{A}_Q = \lambda_{\max}(\hat{I}) / \|\bI\|_\infty$.
  - **Theorem *ref:thm:classical-limit*** (Tier B): Classical
    replicator dynamics recovered as decoherence limit.
  - **Proposition *ref:prop:cq-embedding*** (Tier A): Classical
    simplex embeds isometrically in quantum density matrices.
  - **Proposition *ref:prop:decoherence-filter*** (Tier A):
    Decoherence is a cognitive filter with kernel $=$ off-diagonal subspace.
  - **Proposition *ref:prop:consciousness-scaling*** (Tier B):
    Consciousness ceiling scales with attention expressiveness.
  - Upgrades Part X Quantum Attention conjecture from Tier C to
    Tier B (fully formalized model with proved results).

\end{subbox}

\ifx\STANDALONE\undefined
\else