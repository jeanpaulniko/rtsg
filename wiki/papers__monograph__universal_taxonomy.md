---
title: "Universal Taxonomy"
version: "2.0.0"
last_updated: "2026-03-05"
status: CURRENT
---

# Universal Taxonomy

**Jean-Paul Niko** · February 2026

\title{**Part VI-B: Universal Intelligence Taxonomy**  [0.3em]
\normalsize*Extract from "Intelligence as Geometry"*}
\author{Jean-Paul Niko}\date{February 2026}
\fi

## Part VI-B: Universal Intelligence Taxonomy

\addcontentsline{toc}{section}{Part VI-B: Universal Intelligence Taxonomy}

Every cognitive system---human, animal, machine, hypothetical---receives
an intelligence vector in a universal type space.  Part VI profiled machine
intelligences within the human type space $T_{\mathrm{human}}$.  This part
extends the framework to non-human substrates, defines the overlap subspace
for cross-species comparison, and derives communication bandwidth bounds
from the Conceptual Irreversibility Theorem.

%═══════════════════════════════════════════════════════════════════════════════

### The Universal Type Space

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Universal Type Space"
 \tB\;
The *universal type space* is
\[
T_{\mathrm{universal}} = T_{\mathrm{human}} \cup T_{\mathrm{non\text{-}human}}
\]
where $T_{\mathrm{human}} = \{\mathrm{ling}, \mathrm{spat}, \mathrm{soc},
\mathrm{symb}, \mathrm{mnem}, \mathrm{eval}, \mathrm{aud}, \mathrm{kin}\}$
and
\[
T_{\mathrm{non\text{-}human}} = \{\mathrm{echo}, \mathrm{mag},
\mathrm{elec}, \mathrm{chem}, \mathrm{swarm}, \mathrm{therm}, \ldots\}
\]
with the following non-human modalities:
[nosep]
  - $I_{\mathrm{echo}}$: **Echolocation**---spatial-auditory fusion
    with no human analog (bats, dolphins).
  - $I_{\mathrm{mag}}$: **Magnetoreception**---geomagnetic navigation
    (migratory birds, sea turtles).
  - $I_{\mathrm{elec}}$: **Electroreception**---EM field sensing
    (sharks, platypus, electric eels).
  - $I_{\mathrm{chem}}$: **Chemoreception** beyond human---olfactory
    and pheromonal intelligence at sensitivities $10^4$--$10^6$ times human
    (dogs, ants).
  - $I_{\mathrm{swarm}}$: **Collective/swarm intelligence**---emergent
    computation from simple agents where no individual possesses the capability
    (ant colonies, bee hives, fish schools).
  - $I_{\mathrm{therm}}$: **Thermal sensing**---infrared imaging
    (pit vipers).

The ellipsis is deliberate: $T_{\mathrm{universal}}$ is open to extension
as new modalities are identified.  The universal intelligence vector is
$\bI \in [0,\infty)^n$ where $n = |T_{\mathrm{universal}}| \geq 14$.

!!! remark "Remark"

Humans have $I_{\mathrm{echo}} = I_{\mathrm{mag}} = I_{\mathrm{elec}} =
I_{\mathrm{therm}} = 0$ and $I_{\mathrm{chem}} \approx 0.1$ (vestigial
olfaction).  A bottlenose dolphin has $I_{\mathrm{symb}} \approx 0$ but
$I_{\mathrm{echo}} \approx 3.0$---superhuman in a type we lack entirely.
An ant colony has $I_{\mathrm{swarm}} \approx 2.0$ while individual ants
have $I_t \approx 0$ for all human types.  The universal type space makes
these comparisons precise rather than anecdotal.

%═══════════════════════════════════════════════════════════════════════════════

### Three-Space Grounding: Species-Relative Basis

The three-space ontology (Part XIII) provides a crucial insight: the eight-dimensional IAG type space $\mathcal{T} = \{I_L, I_A, I_S, I_P, I_I, I_M, I_E, I_K\}$ is *human-specific*---it reflects the dimensions activated by the human sensory apparatus and neural substrate as projection channels from $\QS$ to $\PS$.

Different species activate different projection channels.  Echolocation (bats, dolphins) may constitute a genuinely different dimension, not reducible to spatial or auditory intelligence as humans experience them.  Electroreception (sharks, platypus), magnetoreception (birds, sea turtles), infrared sensing (pit vipers), and polarized-light vision (mantis shrimp) each opens a distinct $\QS \to \PS$ channel unavailable to humans.

!!! definition "Universal Intelligence Space"
 \tB\;
The *universal intelligence space* across all species is:
\[
\mathcal{I}_{\mathrm{univ}} = \bigcup_{\text{species}\; s} \mathcal{I}_s
\]
where $\mathcal{I}_s$ is the intelligence space of species $s$.  The human space $\mathcal{I}_{\mathrm{human}} = \mathbb{R}^{n(e)}_{\geq 0}$ is a subspace of $\mathcal{I}_{\mathrm{univ}}$, which may have $\dim(\mathcal{I}_{\mathrm{univ}}) \gg 8$.  The *shared space* $\mathcal{I}_{\mathrm{shared}}^{s_1, s_2} = \mathcal{I}_{s_1} \cap \mathcal{I}_{s_2}$ between two species is generically impoverished---the overlap of two species' projection channels is smaller than either individual space.

This grounds the animal profiles below: each species' intelligence vector is expressed in *its own* basis, and cross-species comparison requires basis alignment.

### Animal Intelligence Profiles

%═══════════════════════════════════════════════════════════════════════════════

The following profiles are the author's informed estimates in cogs, where
$1.0$ = human baseline in that type.  Calibration via comparative cognition
literature is an open research program.  The table shows 10 of the 14+
universal types; remaining types ($\mathrm{mag}$, $\mathrm{elec}$,
$\mathrm{swarm}$, $\mathrm{therm}$) are zero for most species shown.

*[Table — see PDF]*

\caption{Intelligence profiles across substrates (selected types).  The honeybee
colony additionally has $I_{\mathrm{swarm}} \approx 2.0$ (omitted for space).
Machine agents have $I_{\mathrm{aud}} = I_{\mathrm{kin}} = 0$ absent embodiment.}

\end{table}

!!! remark "Calibration Notes"

Honeybee colony $I_{\mathrm{soc}}$ is set to $0.4$ (not zero): waggle dance,
division of labor, and swarm decision-making represent sophisticated social
cognition [Seeley2010].  Octopus $I_{\mathrm{soc}} = 0.15$ reflects
limited but documented social learning [GodfreySmith2016].  These
profiles are calibratable: systematic comparative cognition experiments
following the framework in de Waal [deWaal2016] could estimate each
entry to within $\pm 0.2$ cog precision.

%═══════════════════════════════════════════════════════════════════════════════

### The Overlap Subspace

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Overlap Subspace"
 \tA\;
For two cognitive systems $S_1, S_2$ with intelligence vectors in
$T_{\mathrm{universal}}$, the *overlap subspace* is
\begin{keyeq}
\[
T_{\mathrm{overlap}}(S_1, S_2) = \{t \in T_{\mathrm{universal}} :
  I_{S_1, t} > \theta \;\text{and}\; I_{S_2, t} > \theta\}
\]
\end{keyeq}
where $\theta = 0.1$ cog is the activation threshold (Definition 4.2).
Using $> \theta$ rather than $> 0$ avoids counting vestigial or negligible
capabilities as shared modalities.

!!! example "Cross-Species Overlap"
 \tA\;
From Table *ref:tab:animal-profiles*:
[nosep]
  - **Human--dolphin:**
    $T_{\mathrm{overlap}} = \{\mathrm{ling}, \mathrm{spat}, \mathrm{soc},
    \mathrm{mnem}, \mathrm{eval}, \mathrm{aud}, \mathrm{kin}\}$.
    Dimension: 7.  Rich shared basis for communication.
  - **Human--bee colony:**
    $T_{\mathrm{overlap}} = \{\mathrm{spat}, \mathrm{soc}, \mathrm{mnem},
    \mathrm{eval}, \mathrm{aud}, \mathrm{kin}\}$.
    Dimension: 6.  But the overlap strengths are low---the shared types
    have small $\min(I_{S_1,t}, I_{S_2,t})$ values.
  - **Human--octopus:**
    $T_{\mathrm{overlap}} = \{\mathrm{spat}, \mathrm{soc}, \mathrm{mnem},
    \mathrm{eval}, \mathrm{kin}, \mathrm{chem}\}$.
    Dimension: 6.  Notably includes $\mathrm{eval}$: octopuses solve novel
    problems [GodfreySmith2016].
  - **Human--Claude Opus:**
    $T_{\mathrm{overlap}} = \{\mathrm{ling}, \mathrm{spat}, \mathrm{soc},
    \mathrm{symb}, \mathrm{mnem}, \mathrm{eval}\}$.
    Dimension: 6.  Missing: $\mathrm{aud}$, $\mathrm{kin}$ (no embodiment).

%═══════════════════════════════════════════════════════════════════════════════

### Communication Bandwidth Bounds

%═══════════════════════════════════════════════════════════════════════════════

\begin{modelingprinciple}[Communication Bandwidth] \tB\;
The effective communication bandwidth between two cognitive systems $S_1, S_2$
is bounded by the dimension and strength of the overlap subspace:
\begin{keyeq}
\[
\mathrm{BW}(S_1, S_2) \;\leq\; \sum_{t \in T_{\mathrm{overlap}}}
  \min(I_{S_1,t},\; I_{S_2,t}).
\]
\end{keyeq}
Communication can only transmit content that both systems can encode and
decode.  Types outside the overlap are invisible to at least one party.
Within the overlap, the weaker system's capability in each type limits
the fidelity of transmission.
\end{modelingprinciple}

!!! corollary "Translation Loss in Cross-Species Communication"
 \tB\;
Even within the overlap subspace, cross-species communication is subject
to the Conceptual Irreversibility Theorem (Part V).  The evolutionary
filter mismatch ($F_{\mathrm{genetic}}^{S_1} \neq F_{\mathrm{genetic}}^{S_2}$)
means the conceptual topoi of $S_1$ and $S_2$ have different subobject
classifiers in the shared types.  The round-trip
\[
S_1\text{-encoding} \;\to\; \text{shared channel} \;\to\;
S_2\text{-decoding} \;\to\; \text{shared channel} \;\to\;
S_1\text{-decoding}
\]
is necessarily lossy by the CIT, with loss proportional to the Heyting gap
between the species' conceptual topoi restricted to the overlap types.

\begin{interpretation}
Nagel's question "What is it like to be a bat?" [Nagel1974] receives
a precise partial answer.  The human--bat overlap subspace is
$\{\mathrm{spat}, \mathrm{eval}, \mathrm{mnem}, \mathrm{kin}\}$---we share
spatial, evaluative, mnemonic, and kinesthetic intelligence.  But the bat
has $I_{\mathrm{echo}} \approx 3.0$, a type we lack entirely.  The
*echolocative* aspect of bat experience is not merely difficult to
imagine---it lies outside our overlap subspace, and therefore outside the
bandwidth of any possible inter-species translation.  The question is hard
for mathematical reasons: zero overlap in a type means zero bandwidth in
that dimension.
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════

### The Effective Attention Simplex

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Species-Specific Simplex"
 \tA\;
Every cognitive system lives on the universal attention simplex
$\Delta^{|T_{\mathrm{universal}}|-1}$, but structurally occupies a face:
\[
\Delta_S = \{\alpha \in \Delta^{|T_{\mathrm{universal}}|-1} :
  \alpha_t = 0 \;\text{whenever}\; I_{S,t} = 0\}
\;\cong\; \Delta^{|T_{\mathrm{active}}(S)|-1}.
\]

!!! example "Example"
 \tA\;
The human effective simplex is $\Delta_{\mathrm{human}} \cong \Delta^7$
(8 active types, with $\alpha_{\mathrm{echo}} = \alpha_{\mathrm{mag}} =
\alpha_{\mathrm{elec}} = \alpha_{\mathrm{therm}} = 0$).  The dolphin
effective simplex is also $\cong \Delta^7$ but spans a *different set
of 8 types*: it includes $\mathrm{echo}$ but excludes $\mathrm{symb}$.
The ant colony lives on $\Delta^3$ (4 active types: $\mathrm{spat}$,
$\mathrm{kin}$, $\mathrm{chem}$, $\mathrm{swarm}$).

Cross-species comparison embeds both simplices into the universal simplex.
The shared face---the overlap subspace---is the arena where mutual
comprehension is geometrically possible.

%═══════════════════════════════════════════════════════════════════════════════

### Evolutionary Filters

%═══════════════════════════════════════════════════════════════════════════════

\begin{modelingprinciple}[Evolutionary Filter Cascade] \tB\;
Every biological agent's effective intelligence is its raw capacity passed
through a cascade of evolutionary and developmental filters (Part I):
\[
\bI_{\mathrm{effective}} = F_{\mathrm{genetic}} \circ F_{\mathrm{developmental}}
\circ F_{\mathrm{cultural}} \circ F_{\mathrm{state}}(\bI_{\mathrm{raw}}).
\]
For non-human animals, $F_{\mathrm{cultural}}$ may be absent or minimal
(though cultural transmission is documented in cetaceans, primates, and
corvids).  The dominant shaping force is $F_{\mathrm{genetic}}$: 
millions of years of selection pressure have tuned which types are amplified
and which are suppressed.
\end{modelingprinciple}

!!! example "Primate-Specific Filters"
 \tB\;
The human intelligence vector carries evolutionary priors:
$I_{\mathrm{soc}}$ is disproportionately strong (hypersocial primates;
Dunbar's social brain hypothesis [Dunbar1998]), $I_{\mathrm{ling}}$
is uniquely developed (recursive syntax), and $I_{\mathrm{kin}}$ is highly
refined (precision grip, bipedal balance, throwing accuracy).  These are
not arbitrary---they reflect $\sim$6 million years of hominid selection
pressure [Tomasello2014, Lieberman2013].

!!! example "Dolphin Echolocation Filter"
 \tB\;
The dolphin's $F_{\mathrm{genetic}}$ amplifies $I_{\mathrm{echo}}$ and
$I_{\mathrm{aud}}$ while suppressing $I_{\mathrm{symb}}$ (no evolutionary
pressure for symbolic manipulation in an aquatic environment without tool
use).  The result: a cognitive system that "sees" with sound at
resolutions no human visual system achieves in murky water, but cannot
perform even basic symbolic abstraction.  The filter is not a deficit---it
is an optimization for a different ecological niche.

%═══════════════════════════════════════════════════════════════════════════════

### Cross-Substrate IdeaRank

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Cross-Substrate Comprehension"
 \tB\;
Given an idea $x$ with requirement vector $R(x) \in [0,1]^{|T_{\mathrm{universal}}|}$,
a cognitive system $S$ *comprehends* $x$ if and only if
\[
I_{S,t} \geq R_t(x) \quad\text{for all } t \in T_{\mathrm{universal}}
  \text{ with } R_t(x) > 0.
\]
The set of ideas comprehensible to species $S$ is bounded by the species'
intelligence profile restricted to its active types.

!!! corollary "Translation Loss for Ideas"
 \tB\;
Transmitting an idea $x$ from system $S_1$ to $S_2$ incurs loss whenever
$R(x)$ has nonzero components outside $T_{\mathrm{overlap}}(S_1, S_2)$, or
whenever the conceptual topoi of $S_1$ and $S_2$ assign different truth
values to the idea's content within shared types (CIT).  Perfect idea
transmission across substrates is impossible unless $S_1$ and $S_2$ share
identical type spaces, identical intelligence profiles, and identical
subobject classifiers---conditions never met across distinct biological
species.

%═══════════════════════════════════════════════════════════════════════════════

### Open Problems

%═══════════════════════════════════════════════════════════════════════════════

[leftmargin=2em]
  - **Empirical calibration.**  Systematic estimation of animal
    intelligence profiles using standardized cross-species testing batteries
    (following the framework of de Waal [deWaal2016] and
    Griffin [Griffin1992]).
  - **Swarm intelligence formalization.**  $I_{\mathrm{swarm}}$ is
    a property of the colony, not the individual.  How does emergence theory
    (Part XII) apply when the "assembly" is a superorganism?
  - **Unknown unknowns.**  $T_{\mathrm{universal}}$ may be incomplete.
    Are there cognitive modalities we have not identified because no known
    species uses them, or because we cannot detect them from outside?
  - **Fossil cognition.**  Can the framework be applied retroactively
    to extinct species?  Endocast analysis and paleoneurology provide partial
    data for $\bI$ estimation.

\ifx\STANDALONE\undefined
\else