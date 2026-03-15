---
title: "Sociology Companion Paper"
version: "2.0.0"
last_updated: "2026-03-05"
status: ARXIV-READY
arxiv_category: "physics.soc-ph"
---

# Sociology Companion Paper

**Jean-Paul Niko** · February 2026

% ═══════════════════════════════════════════════════════════════════════════════

\title{\textcolor{sectionblue}{**Cognitive Bundles and Social Synergy:  [0.3em]
A Mathematical Framework for Collective Intelligence,  
Stratification, and Institutional Design**}}

\author{Jean-Paul Niko  
  
\small `triptomean.com`}

\date{February 2026}

!!! abstract "Abstract"
    
We introduce a mathematical framework for collective intelligence, social stratification, and institutional design grounded in the Intelligence as Geometry (RTSG) theory.  Every cognitive agent carries an *intelligence vector* $\bI \in \\mathbb{R}^{n(e)}_{\geq 0}$ measuring capacity across eight cognitive types.  A *compatibility matrix* $\bK \in \R^{8 \times 8}$ encodes cross-type interaction strengths, yielding a *synergy function* $\Syn(\bI_1, \bI_2) = \bI_1^\top \bK \, \bI_2$ that determines whether combining two agents amplifies or diminishes collective capacity.  Aggregating agents into *cognitive bundles* $B = \{\bI_1, \ldots, \bI_n\}$ formalizes social groups as algebraic objects whose collective intelligence is a non-trivial function of member profiles and institutional structure.  We show that Durkheim's mechanical and organic solidarity correspond to low-diversity and high-diversity bundle regimes, respectively.  A *filter formalism* models how social institutions transform raw intelligence through diagonal contractions $\Phi \in [0,1]^8$, formalizing Bourdieu's concepts of cultural capital, habitus, and misrecognition as specific filter configurations and compositions.  The Conceptual Irreversibility Theorem (CIT) proves that filter effects cannot be fully reversed, explaining why class mobility is structurally difficult even given equal raw ability.  We derive a continuous *polarization metric* $P_{\mathrm{cont}}$ that measures the shrinkage of shared conceptual space between subpopulations, predict a critical threshold below which democratic deliberation fails, and evaluate depolarization interventions by their effect on the overlap subspace.  The framework generates testable predictions for organizational design, inequality measurement, and institutional reform.

**Keywords:** collective intelligence, social stratification, cultural capital, synergy, polarization, institutional design, mathematical sociology

---

% ═══════════════════════════════════════════════════════════════════════════════

## Introduction

% ═══════════════════════════════════════════════════════════════════════════════

Sociology has long recognized that collective outcomes cannot be reduced to individual attributes.  Durkheim's distinction between mechanical and organic solidarity, Bourdieu's theory of capital and habitus, and Granovetter's analysis of network structure all point to the same insight: social organization mediates between individual capacity and collective performance in ways that are structurally consequential.  Yet the field lacks a unified mathematical language for expressing these insights---one that could connect individual cognition to institutional structure to macrosocial outcomes within a single formal system.

This paper presents such a framework, drawn from the Intelligence as Geometry (RTSG) theory developed in Niko [Niko2026].  The central move is to represent intelligence not as a scalar (IQ) but as a vector $\bI \in \\mathbb{R}^{n(e)}_{\geq 0}$ spanning eight cognitive types.  This seemingly simple shift has surprisingly deep consequences for social theory.  When agents combine into groups, their collective intelligence is not the sum of individual scores but a function of the *compatibility structure* between their profiles---and this compatibility is encoded in a symmetric positive semi-definite matrix $\bK$ whose entries determine whether cross-type interaction produces synergy or friction.

The framework contributes three things to sociology.  First, it formalizes collective intelligence as a *bundle synergy* computation, showing precisely when and why diverse groups outperform homogeneous ones.  Second, it models social stratification as a *filter distribution* problem, recasting Bourdieu's cultural capital as a specific mathematical operator that transforms raw cognitive capacity through institutional channels.  Third, it provides a quantitative *polarization metric* with a provable threshold below which communicative deliberation becomes structurally impossible, regardless of good faith.

We proceed as follows.  Section *ref:sec:algebra* introduces the intelligence algebra.  Section *ref:sec:bundles* develops bundle synergy theory.  Section *ref:sec:durkheim* maps the formalism to classical sociological theory.  Section *ref:sec:filters* presents the filter formalism and its connection to Bourdieu.  Section *ref:sec:inequality* reformulates inequality as filter dispersion.  Section *ref:sec:polarization* derives the polarization metric.  Section *ref:sec:institutions* applies the framework to institutional design.  Section *ref:sec:predictions* presents testable predictions, and Section *ref:sec:discussion* discusses implications and limitations.

% ═══════════════════════════════════════════════════════════════════════════════

## The Intelligence Algebra

% ═══════════════════════════════════════════════════════════════════════════════

The fundamental objects are the *intelligence vector* and the *compatibility matrix*.

!!! definition "Intelligence Vector"
 \tA{}
An agent's cognitive profile is a vector $\bI = (I_L, I_G, I_S, I_A, I_K, I_N, I_E, I_{\mathrm{Mu}}) \in \\mathbb{R}^{n(e)}_{\geq 0}$, where the eight components measure capacity in Linguistic ($L$), Symbolic-Algebraic ($G$), Spatial ($S$), Kinesthetic ($A$), Auditory ($K$), Social ($N$), Intrapersonal ($E$), and Naturalistic ($\mathrm{Mu}$) types.

The vector representation encodes the empirical observation that cognitive capacity is multidimensional and irreducible: an individual with high $I_N$ (social intelligence) and low $I_G$ (symbolic intelligence) is not "less intelligent" than the reverse---they are intelligent *differently*, in ways that are consequential for social role assignment, institutional fit, and collective outcomes.

!!! definition "Compatibility Matrix"
 \tA{}
The *compatibility matrix* $\bK \in \R^{8 \times 8}$ is symmetric and positive semi-definite, with $K_{ss} = 1$ for all $s$ and off-diagonal entries $K_{st} \in [-1, 1]$ encoding pairwise interaction between types $s$ and $t$.  When $K_{st} > 0$, deploying type $s$ facilitates type $t$ (synergy); when $K_{st} < 0$, it hinders type $t$ (interference).

!!! definition "Pairwise Synergy"
 \tA{}
The *synergy* between two agents is:
\begin{keyeq}
\[
\Syn(\bI_1, \bI_2) = \bI_1^\top \bK \, \bI_2
\]
\end{keyeq}
When $\Syn(\bI_1, \bI_2) > \|\bI_1\| \cdot \|\bI_2\|$, the combination is *superadditive*---the pair produces more than the sum of their individual capacities.

The key sociological insight is that $\bK$ is not merely a property of individuals but is *institutionally mediated*.  The same two individuals may exhibit high synergy in one organizational context and low synergy in another, because institutions shape which cross-type interactions are facilitated or suppressed.  We return to this in Section *ref:sec:institutions*.

!!! definition "Friction Tensor"
 \tA{}
The *friction tensor* $\bF \in \R^{8 \times 8}$ measures the cost of inter-type translation:
\[
F_{st} = c\,(1 - K_{st})
\]
where $c > 0$ is a calibration constant.  High compatibility implies low friction; orthogonal types impose maximal translation cost.

This friction is not merely metaphorical.  Context-switching between cognitive modes incurs measurable costs in time, effort, and accuracy---costs that compound at the organizational level when coordination requires frequent inter-type translation.

% ═══════════════════════════════════════════════════════════════════════════════

## Bundle Synergy: Groups as Algebraic Objects

% ═══════════════════════════════════════════════════════════════════════════════

A social group is, from the RTSG perspective, a *cognitive bundle*: a finite collection of intelligence vectors with an associated interaction structure.

!!! definition "Cognitive Bundle"
 \tB{}
A *cognitive bundle* is a set $B = \{\bI_1, \ldots, \bI_n\}$ of intelligence vectors together with a compatibility matrix $\bK$ governing inter-type interactions.

!!! definition "Bundle Synergy"
 \tB{}
The *total synergy* of a bundle $B$ is:
\begin{keyeq}
\[
\Syn(B) = \sum_{i < j} \bI_i^\top \bK \, \bI_j + \sum_i \|\bI_i\|^2
\]
\end{keyeq}
The *synergy ratio* $\sigma(B) = \Syn(B) / \sum_i \|\bI_i\|^2$ measures whether the group amplifies ($\sigma > 1$) or diminishes ($\sigma < 1$) total cognitive capacity.

The synergy ratio captures something that Woolley et al.\  [Woolley2010] measured empirically but could not formalize: the existence of a "collective intelligence factor" that is not reducible to average individual intelligence.  In our framework, this factor is precisely the off-diagonal contribution $\sum_{i < j} \bI_i^\top \bK \, \bI_j$, which depends on *profile diversity* weighted by *compatibility*.

!!! proposition "Diversity--Synergy Relationship"
 \tB{}
For a fixed total intelligence $\sum_i \|\bI_i\| = M$, bundle synergy is maximized when member profiles span orthogonal high-$K$ subspaces of $\\mathbb{R}^{n(e)}$.  That is, the optimal bundle combines agents with complementary strengths in types that interact synergistically.

\begin{intuition}
This formalizes Page's [Page2007] "diversity trumps ability" thesis: under the right compatibility conditions, a cognitively diverse group outperforms a homogeneous group of higher-ability members, because the off-diagonal synergy terms overwhelm the individual-capacity terms.  But the qualification "under the right compatibility conditions" is crucial---diversity without compatibility produces friction, not synergy.
\end{intuition}

### Coordination costs and optimal group size

Synergy is not free.  As group size $n$ grows, coordination costs grow with it.  Each new member adds $n-1$ pairwise interaction terms, each requiring inter-type translation at cost $F_{st}$.  The net value of the $k$-th member added to a bundle of size $k-1$ is:
\[
\Delta V_k = \sum_{i=1}^{k-1} \bI_i^\top \bK \, \bI_k - \sum_{i=1}^{k-1} \sum_{s,t} F_{st} \cdot \lambda_{s,i} \cdot \lambda_{t,k}
\]
where $\lambda_{s,i}$ is agent $i$'s attention allocation to type $s$.  Eventually $\Delta V_k < 0$: the group has grown past its optimal size.

!!! proposition "Optimal Bundle Size"
 \tB{}
For any fixed population of agents, there exists an optimal bundle size $n^*$ that maximizes net synergy.  Beyond $n^*$, coordination costs exceed marginal synergy gains.

This connects directly to Coase's [Coase1937] theory of the firm: firms exist because bundling agents under a shared governance structure reduces transaction costs, but they stop growing when the internal coordination costs exceed the synergy benefits.  Our framework makes this quantitative.

% ═══════════════════════════════════════════════════════════════════════════════

## Formalizing Durkheim: Solidarity as Synergy Regime

% ═══════════════════════════════════════════════════════════════════════════════

Durkheim's [Durkheim1893] distinction between mechanical and organic solidarity receives a precise mathematical interpretation.

!!! definition "Mechanical Solidarity"
 \tB{}
A bundle $B$ exhibits *mechanical solidarity* when member profiles are similar:
\[
\max_{i,j} \|\bI_i - \bI_j\| < \varepsilon \quad \text{for small } \varepsilon
\]
Synergy arises from *aggregation*: more of the same capacity.  The synergy ratio is close to 1 because the off-diagonal terms contribute little beyond what the diagonal terms already provide.

!!! definition "Organic Solidarity"
 \tB{}
A bundle $B$ exhibits *organic solidarity* when member profiles are diverse and compatibility is high:
\[
\text{Profile diversity} \gg \varepsilon, \qquad \text{mean}(K_{st}) \text{ high for covered type pairs}
\]
Synergy arises from *complementarity*: different capacities interact to produce outcomes no individual could achieve.  The synergy ratio $\sigma \gg 1$ when the $\bK$ matrix supports the specific diversity present.

\begin{intuition}
Durkheim's historical thesis---that societies transition from mechanical to organic solidarity as the division of labor deepens---translates to: as populations grow and specialize, individual $\bI$ vectors become sparser (more concentrated on fewer types), increasing profile diversity.  This creates the *potential* for organic solidarity, but only if institutional structures evolve to support high-$K$ cross-type interaction.  When institutions fail to keep pace with specialization, the result is anomie: high diversity with low compatibility, yielding $\sigma < 1$.
\end{intuition}

!!! proposition "Anomie as Compatibility Failure"
 \tB{}
*Anomie* in the RTSG framework is the condition $\sigma(B) < 1$ despite high profile diversity.  This occurs when the effective $\bK$ matrix (as mediated by institutions) has off-diagonal entries too low to compensate for the friction costs of coordination among diverse agents.

This formalization makes Durkheim's concept empirically testable: one can measure profile diversity (via psychometric instruments), estimate $\bK$ (via collaborative task performance), and compute $\sigma$ to determine whether a social unit is in mechanical solidarity, organic solidarity, or anomie.

% ═══════════════════════════════════════════════════════════════════════════════

## Filter Formalism: Bourdieu Mathematized

% ═══════════════════════════════════════════════════════════════════════════════

The filter formalism is the RTSG's tool for modeling how social structure transforms cognitive capacity.  A *filter* is a diagonal contraction that selectively attenuates components of the intelligence vector.

!!! definition "Intelligence Filter"
 \tA{}
A filter is a diagonal operator $\Phi = \operatorname{diag}(\phi_1, \ldots, \phi_8)$ with $\phi_t \in [0,1]$ for each type $t$.  Applied to a raw intelligence vector:
\[
\bI_{\mathrm{effective}} = \Phi(\bI_{\mathrm{raw}})
\]
The entry $\phi_t = 1$ means type $t$ passes unattenuated; $\phi_t = 0$ means type $t$ is completely suppressed.

Filters compose: a sequence of filters $\Phi_1, \Phi_2, \ldots, \Phi_k$ applied in order produces $\bI_{\mathrm{eff}} = \Phi_k \circ \cdots \circ \Phi_1(\bI_{\mathrm{raw}})$.  Crucially, composition can only *further attenuate*---it can never amplify a component beyond what remains after earlier filters.

!!! theorem "Kernel Lemma"
 \tA{}
For composed filters, $\ker(\Phi_2 \circ \Phi_1) \supseteq \ker(\Phi_1)$.  That is, filters can only destroy, never restore.

!!! theorem "Conceptual Irreversibility (CIT)"
 \tA{}
For any non-trivial filter $\Phi$, there exists no inverse filter $\Phi^{-1}$ such that $\Phi^{-1} \circ \Phi = \operatorname{Id}$.  Filter effects are structurally irreversible.

### Cultural capital as filter

Bourdieu's [Bourdieu1984,Bourdieu1986] concept of *cultural capital* maps directly to the filter formalism.  The cultural filter $\Phi_{\mathrm{cult}}$ encodes which cognitive types are valued, practiced, and reinforced within a given social stratum.

!!! definition "Cultural Filter"
 \tB{}
A *cultural filter* $\Phi_{\mathrm{cult}} = \operatorname{diag}(\phi_1^{\mathrm{cult}}, \ldots, \phi_8^{\mathrm{cult}})$ represents the transmission of cultural capital.  For the French bourgeoisie (Bourdieu's paradigmatic case):
\[
\Phi_{\mathrm{bourgeois}} \approx \operatorname{diag}(0.9, 0.8, 0.5, 0.3, 0.7, 0.8, 0.7, 0.3)
\]
emphasizing linguistic, symbolic, auditory (music appreciation), and social types while attenuating kinesthetic and naturalistic capacities.

The working-class cultural filter has a different profile:
\[
\Phi_{\mathrm{working}} \approx \operatorname{diag}(0.5, 0.3, 0.7, 0.9, 0.4, 0.7, 0.5, 0.6)
\]
emphasizing spatial, kinesthetic, and naturalistic capacities while attenuating symbolic and linguistic ones.

\begin{intuition}
The critical point is not that working-class individuals are less intelligent---they may have identical $\bI_{\mathrm{raw}}$---but that the filter applied by their social environment *develops different components* of their intelligence.  Since the educational system, credentialing institutions, and labor market evaluation criteria are calibrated to $\Phi_{\mathrm{bourgeois}}$, a working-class individual with equal raw capacity but different effective profile will systematically underperform on *those metrics*, creating the appearance of a capacity deficit where there is in fact a filter mismatch.
\end{intuition}

### Habitus as internalized filter

Bourdieu's *habitus*---the set of dispositions, tastes, and perceptual categories that agents internalize through socialization---is the subjective experience of living under a particular filter.  The filter is not merely imposed from outside; it becomes the agent's own cognitive architecture, shaping what they perceive as possible, desirable, and natural.

!!! proposition "Misrecognition as Filter Opacity"
 \tB{}
Bourdieu's *misrecognition*---the failure of agents to perceive social structures as contingent rather than natural---is formalized as the inability to observe one's own filter.  An agent operating under $\Phi_{\mathrm{cult}}$ perceives $\bI_{\mathrm{eff}} = \Phi_{\mathrm{cult}}(\bI_{\mathrm{raw}})$ as their "natural" capacity, because the filter is transparent to the filtered agent.

This connects to Willis's [Willis1977] ethnographic finding that working-class "lads" actively participate in reproducing their own subordination: they are not merely subjected to a filter but have internalized it as identity.  In RTSG terms, the filter has become part of their self-model, making it phenomenologically invisible.

### Economic capital as filter access

Bourdieu distinguishes economic capital from cultural capital, but in the RTSG framework they are connected: economic capital buys access to developmental filters.

!!! proposition "Economic-Developmental Filter Link"
 \tB{}
Economic capital $W$ determines access to the developmental filter $\Phi_{\mathrm{dev}}(W)$, which includes education, nutrition, enrichment, and environmental quality.  Higher $W$ produces a more permissive filter: $\phi_t^{\mathrm{dev}}(W) \geq \phi_t^{\mathrm{dev}}(W')$ for $W > W'$ across most types $t$.

Lareau's [Lareau2003] finding that middle-class "concerted cultivation" produces different cognitive outcomes than working-class "accomplishment of natural growth" is precisely the claim that $\Phi_{\mathrm{dev}}(W_{\mathrm{middle}}) \neq \Phi_{\mathrm{dev}}(W_{\mathrm{working}})$, with the middle-class filter being more permissive in the types that correlate with institutional success.

% ═══════════════════════════════════════════════════════════════════════════════

## Inequality as Filter Distribution

% ═══════════════════════════════════════════════════════════════════════════════

Traditional inequality measures (Gini coefficient, Theil index) operate on scalar quantities---income, wealth, years of education.  The RTSG framework suggests a richer measure grounded in the *distribution of filters* across the population.

!!! definition "Filter Dispersion"
 \tB{}
For a population with filter distribution $\{\Phi_1, \ldots, \Phi_n\}$, the *filter dispersion* is:
\[
D_\Phi = \frac{1}{n(n-1)} \sum_{i \neq j} \|\Phi_i - \Phi_j\|_F
\]
where $\|\cdot\|_F$ is the Frobenius norm.  High $D_\Phi$ indicates that different subpopulations experience very different filter regimes.

!!! definition "Overlap Subspace"
 \tB{}
For two subpopulations $A$ and $B$ with mean effective profiles $\bar{\bI}_A$ and $\bar{\bI}_B$, the *overlap subspace* is the set of types where both populations retain non-trivial capacity:
\[
T_{\mathrm{overlap}}(A,B) = \{t : \bar{I}_{A,t} > \epsilon \text{ and } \bar{I}_{B,t} > \epsilon\}
\]

The overlap subspace is the communicative common ground---the set of cognitive dimensions through which groups can translate meaning to one another.  When $|T_{\mathrm{overlap}}|$ is large, cross-group communication is possible (though lossy).  When it shrinks, translation becomes increasingly difficult, and below a critical threshold, structural mutual unintelligibility emerges.

!!! proposition "Structural Inequality Decomposition"
 \tB{}
Total inequality in cognitive outcomes can be decomposed as:
\[
\underbrace{\text{Outcome gap}}_{\|\bar{\bI}_{\mathrm{eff},A} - \bar{\bI}_{\mathrm{eff},B}\|} = \underbrace{\text{Raw gap}}_{\|\bar{\bI}_{\mathrm{raw},A} - \bar{\bI}_{\mathrm{raw},B}\|} + \underbrace{\text{Filter gap}}_{\|(\Phi_A - \Phi_B) \cdot \bar{\bI}_{\mathrm{raw}}\|}
\]
If raw intelligence distributions are similar across groups (a reasonable assumption given genetic evidence), then outcome gaps are almost entirely *filter gaps*---differences in the institutional environments that shape cognitive development.

\begin{intuition}
This formalization supports what critical sociologists have long argued qualitatively: "achievement gaps" are not capacity gaps but *opportunity gaps*, measurable as filter differential.  The RTSG framework makes this quantitative and testable: measure the filter profiles of different socioeconomic strata, compute the predicted effective intelligence distribution, and compare to observed outcomes.
\end{intuition}

### A Rawlsian filter criterion

The filter framework enables a precise formulation of distributive justice concerns.  Following Rawls, we can define a justice criterion that minimizes the worst-case filter attenuation:

!!! definition "Maximin Filter Justice"
 \tB{}
A society satisfies *maximin filter justice* when institutional design minimizes the worst-case filter attenuation across the population:
\[
\max_{\text{institutions}} \min_{i \in \text{population}} \min_t \phi_{t,i}
\]
That is, no individual should have any cognitive type completely suppressed by their social circumstances.

This is more demanding than traditional Rawlsian criteria because it operates in variable dimensions (12 for humans): it is not enough that the worst-off person has adequate *total* intelligence; they must have adequate capacity in *each* type, because filter-induced blindness in even one dimension can be structurally disabling.

% ═══════════════════════════════════════════════════════════════════════════════

## Polarization as Filter Bifurcation

% ═══════════════════════════════════════════════════════════════════════════════

The RTSG framework provides a mathematically grounded theory of political and social polarization that goes beyond attitudinal divergence to model the structural conditions under which communication between subpopulations becomes impossible.

!!! definition "Discrete Polarization"
 \tB{}
For two subpopulations $A$ and $B$:
\[
P = 1 - \frac{|T_{\mathrm{overlap}}(A,B)|}{|T_{\mathrm{universal}}|}
\]
where $|T_{\mathrm{universal}}| = 8$.  When $P = 0$, the groups share all cognitive dimensions; when $P = 1$, they share none.

The discrete measure is coarse.  A more informative continuous version weights each dimension by capacity:

!!! definition "Continuous Polarization Metric"
 \tB{}
\begin{keyeq}
\[
P_{\mathrm{cont}} = 1 - \frac{\displaystyle\sum_t \min(\bar{I}_{A,t}, \bar{I}_{B,t})}{\displaystyle\sum_t \max(\bar{I}_{A,t}, \bar{I}_{B,t})}
\]
\end{keyeq}
This weights overlap by magnitude: vestigial shared capability counts less than robust shared capability.  $P_{\mathrm{cont}} \in [0,1]$ with $P_{\mathrm{cont}} = 0$ indicating identical profiles and $P_{\mathrm{cont}} = 1$ indicating zero shared capacity.

!!! theorem "Communication Threshold"
 \tB{}
There exists a critical polarization $P_c > 0$ such that for $P_{\mathrm{cont}} > P_c$, the communication bandwidth between subpopulations drops below the minimum required for deliberative exchange.  When this threshold is exceeded, groups *cannot* understand each other in the strong sense: the Conceptual Irreversibility Theorem applies to inter-group translation, and meaning loss exceeds reconstructability.

\begin{intuition}
This is not a claim about bad faith.  Two groups beyond the polarization threshold may be entirely sincere in their desire to communicate, but the structural divergence of their cognitive filters means that the concepts available to one group literally *do not translate* into the conceptual repertoire of the other.  This is the RTSG formalization of what Sunstein [Sunstein2009] describes as "group polarization"---but with a precise mathematical criterion for when the phenomenon becomes irreversible.
\end{intuition}

### Media ecosystems as filter amplifiers

Partisan media narrows $\Phi_{\mathrm{cult}}$ for each subpopulation by reinforcing certain cognitive modes and atrophying others.  If group $A$ consumes media that emphasizes types $\{L, E\}$ while suppressing $\{N, \mathrm{Mu}\}$, and group $B$ consumes media with the reverse emphasis, then:
\[
\frac{dP_{\mathrm{cont}}}{dt} > 0 \quad \text{as long as filter divergence exceeds convergence}
\]

The polarization dynamics have a clear bifurcation structure.  Below a critical media fragmentation level, a shared public sphere maintains sufficient overlap for deliberation.  Above it, the two groups' filters diverge exponentially, and the overlap subspace collapses.

### Depolarization interventions

The framework evaluates depolarization strategies by their effect on $T_{\mathrm{overlap}}$:

[nosep]
- **Bridging institutions**: organizations that require members from both groups to collaborate across types, expanding the overlap subspace through shared practice.
- **Shared experiences**: activities that activate the same cognitive types in both groups simultaneously, creating common ground that is experiential rather than discursive.
- **Lingua franca concepts**: ideas that can be expressed in the conceptual vocabulary of both groups, serving as translation anchors.  These are the high-IdeaRank nodes in the shared portion of the idea graph.

!!! proposition "Depolarization Rate"
 \tB{}
The rate of depolarization is bounded by the capacity of bridging institutions:
\[
\left|\frac{dP_{\mathrm{cont}}}{dt}\right| \leq \frac{k \cdot |T_{\mathrm{overlap}}|}{|T_{\mathrm{universal}}|} \cdot r
\]
where $k$ is the number of active bridging institutions and $r$ is the interaction rate per institution.  Depolarization is faster when the existing overlap is larger---a "use it or lose it" dynamic.

% ═══════════════════════════════════════════════════════════════════════════════

## Institutional Design

% ═══════════════════════════════════════════════════════════════════════════════

Institutions, in the RTSG framework, are governance structures that mediate the effective $\bK$ matrix of the bundles they contain.  Different institutional forms optimize for different synergy regimes.

### Universities

Universities are high-diversity, high-$K_{\mathrm{symb},*}$ institutions.  They combine agents with diverse type profiles (humanists, scientists, artists, engineers) under governance structures designed to maximize cross-type interaction: shared campuses, interdisciplinary seminars, collaborative research.  The institutional $\bK$ amplifies the symbolic dimension's interaction with all other types, producing the distinctive knowledge-creation synergy of the academy.

### Bureaucracies

Bureaucracies are low-diversity, high-$K_{\mathrm{eval,mnem}}$ institutions.  They select for agents strong in evaluative and mnemonic types (rule-following, record-keeping, procedural execution) and suppress cross-type interaction to minimize coordination friction.  This produces high efficiency within a narrow band but brittleness when confronted with problems that require types outside the institutional profile.

### Markets

Markets are distributed bundles with self-organizing synergy.  No central governance mediates the $\bK$ matrix; instead, agents find interaction partners through price signals that encode comparative advantage.  The market's advantage is that it can coordinate a very large $n$ without the quadratic growth of coordination costs that centralized institutions face.  Its disadvantage is that it has no mechanism for investing in the $\bK$ infrastructure that enables synergy---this is a public good that markets tend to under-provide.

!!! proposition "Institutional Comparative Advantage"
 \tB{}
Each institutional form has a domain in which it maximizes net synergy:
[nosep]
- **Universities**: novel problems requiring diverse types with symbolic integration
- **Bureaucracies**: routine problems requiring reliable execution of known procedures
- **Markets**: matching problems with distributed information about agent profiles

Institutional failure occurs when organizations are applied outside their comparative advantage domain.

### Granovetter's weak ties

Granovetter's [Granovetter1973] insight that "weak ties" are disproportionately important for information flow receives a natural formalization.  A weak tie connects agents from different cognitive clusters---agents whose profiles span different regions of the type space.  The information that travels across weak ties is valuable precisely because it comes from outside the receiver's filter bubble, activating types that are underrepresented in their immediate network.

!!! proposition "Weak Ties as Overlap Expanders"
 \tB{}
Weak ties between cognitively distant agents expand the effective overlap subspace of the network.  A network's resilience to polarization is proportional to its density of cross-cluster weak ties.

% ═══════════════════════════════════════════════════════════════════════════════

## Testable Predictions

% ═══════════════════════════════════════════════════════════════════════════════

The framework generates specific, falsifiable predictions:

[nosep]

- **Collective intelligence prediction.**  For teams with measured $\bI$ vectors and estimated $\bK$, the synergy ratio $\sigma(B)$ predicts team performance on complex tasks beyond what average IQ, maximum IQ, or social sensitivity predict.  *Test*: administer psychometric battery to team members, measure $\bI$ vectors, compute $\sigma$, correlate with task performance.

- **Institutional synergy prediction.**  Organizations whose structure aligns with the $\bK$-optimal regime for their task domain will outperform those with misaligned structures.  *Test*: measure the effective $\bK$ of different organizational units (via inter-departmental collaboration rates), compare to the theoretical optimum for their task domain, predict performance differentials.

- **Polarization threshold.**  Track $P_{\mathrm{cont}}$ over time using congressional speech data, social media discourse, or survey instruments.  The framework predicts a phase transition: gradual divergence followed by rapid collapse of communication quality once $P_c$ is crossed.  *Test*: compute $P_{\mathrm{cont}}$ for each Congress since 1970; predict that legislative productivity drops discontinuously when $P_{\mathrm{cont}}$ crosses the threshold.

- **Filter gap prediction.**  Within-group variation in cognitive outcomes should be better predicted by filter variation (socioeconomic status, educational quality, cultural environment) than by raw ability estimates.  *Test*: longitudinal study measuring both filter proxies and cognitive outcomes, with structural equation modeling to decompose filter versus raw effects.

- **Depolarization prediction.**  Interventions that expand $T_{\mathrm{overlap}}$ (cross-partisan collaborative projects, shared experiential programs) will reduce $P_{\mathrm{cont}}$ more effectively than interventions that target attitudes directly (persuasion campaigns, fact-checking).  *Test*: randomized controlled trial comparing overlap-expansion versus attitude-change interventions, measuring $P_{\mathrm{cont}}$ pre and post.

- **Weak tie prediction.**  Networks with higher density of cognitively cross-cutting ties will show slower polarization growth and higher collective intelligence.  *Test*: map cognitive profiles onto social networks, measure cross-cluster tie density, predict polarization trajectory and group problem-solving performance.

% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
Three-Space Sociology}

The three-space ontology grounds social reality in shared instantiation.

**Social reality as convergent instantiation.**  A social fact (a norm, an institution, a shared belief) exists because multiple consciousnesses converge on the same instantiation: they project the same $\QS$-structure into compatible $\PS$-configurations.  The "social construction of reality" is literally the *shared construction of $\PS$* through convergent instantiation.  Money, marriage, national borders, and property rights are all $\PS$-structures that exist only because a community's instantiation operators agree on them.

**Cultural filters as shared convergence conditions.**  The cultural filter $F_{\mathrm{cult}}$ is a set of convergence conditions shared by a community---the $\QS$-structures that the community has collectively agreed to instantiate.  Cultural change is the slow modification of these shared convergence conditions.  Cultural conflict arises when two communities' convergence conditions are incompatible: they instantiate different $\PS$-structures from the same $\QS$-potentiality.

**Cognitive diversity as adaptive strategy.**  A society with diverse intelligence profiles (different members activating different $\QS \to \PS$ channels) has access to a larger collective region of $\mathcal{I}_{\mathrm{univ}}$ than a homogeneous society.  This is the three-space foundation for the value of cognitive diversity: it expands the community's total instantiation capacity.

## Discussion

% ═══════════════════════════════════════════════════════════════════════════════

### Contributions

This paper has introduced a mathematical framework for collective intelligence that unifies several strands of sociological theory under a common algebraic structure.  The contributions are threefold.

First, the bundle synergy formalism provides a quantitative theory of collective intelligence that explains when and why diverse groups outperform homogeneous ones---and, equally importantly, when they do not.  The key mediating variable is the compatibility matrix $\bK$, which encodes institutional structure.  Diversity without institutional support for cross-type interaction produces anomie, not organic solidarity.

Second, the filter formalism translates Bourdieu's theory of cultural capital, habitus, and misrecognition into precise mathematical operations.  The Conceptual Irreversibility Theorem proves what critical sociologists have long argued: the effects of social stratification on cognitive development are not merely contingent but structurally irreversible.  Filter effects compound across generations, and no amount of post-hoc intervention can fully restore what a restrictive developmental filter has suppressed.  This is not pessimism but a diagnosis that directs attention to *prevention* (widening developmental filters) rather than *remediation* (attempting to undo filter damage after the fact).

Third, the polarization metric provides a quantitative tool for tracking democratic resilience with a theoretically grounded threshold for institutional failure.  Unlike attitudinal measures of polarization that capture how much groups disagree, the overlap subspace measures whether groups *can communicate at all*---a more fundamental question for institutional survival.

### Limitations

Several limitations should be acknowledged.  The eight-type decomposition, while empirically motivated, is a modeling choice; the framework generalizes to any finite number of types.  The compatibility matrix $\bK$ is treated as exogenous in this paper, but it is itself a social construction that evolves with institutional change---a dynamic theory of $\bK$ formation is needed.  The filter formalism uses diagonal operators for tractability, but real social filters may have off-diagonal effects (e.g., suppressing one type may enhance another through compensatory development).  Finally, the empirical testing program outlined in Section *ref:sec:predictions* requires psychometric instruments that measure all eight types reliably---current instruments approximate this but do not fully capture the RTSG type space.

### Relation to existing work

The framework connects to several existing research programs.  Woolley et al.'s [Woolley2010] collective intelligence factor is the empirical shadow of bundle synergy.  Page's [Page2007] diversity theorems are special cases of our synergy proposition.  Putnam's [Putnam2000] social capital maps to the institutional $\bK$: communities with dense associational life have high effective cross-type compatibility.  Granovetter's [Granovetter1973] weak ties are overlap expanders.  The filter formalism is compatible with Lareau's [Lareau2003] ethnographic findings and Willis's [Willis1977] analysis of working-class cultural reproduction.

What the RTSG framework adds is not new empirical insights but a *mathematical language* that makes these diverse insights commensurable, reveals their logical relationships, and generates predictions that go beyond what any individual theory produces.

### Implications for social policy

The framework suggests that effective social policy must operate on three levels simultaneously: individual capacity development (widening developmental filters), institutional design (engineering $\bK$ matrices that support synergy), and communicative infrastructure (maintaining the overlap subspace that enables democratic deliberation).  Interventions that target only one level---individual education without institutional reform, or institutional reform without attention to filter distributions---will produce suboptimal results because the three levels are mathematically coupled.

% ═══════════════════════════════════════════════════════════════════════════════
% BIBLIOGRAPHY
% ═══════════════════════════════════════════════════════════════════════════════

## References

*See PDF for full bibliography.*
---

## v2 Integration: Federated Social Architecture & Cultural Fingerprinting (TMP-20260217)

**Confederate model (GNEP):** No elected will — consensus emerges from shared optimization of total life force. Nodes are self-sovereign; equilibrium is cooperative Nash.

**Societal intelligence fingerprinting:** Corpus C(institution or culture) → **I**(ξ) recovery via IdeaRank → placement in collective consciousness graph with measurable distances between cultures, institutions, and epochs.

**Language as sociocultural mind:** A living language is itself a sociocultural conscious entity — an RTSG graph G(L) with **I**(L) = aggregate intelligence vector of all speakers. This has direct implications for cultural preservation and linguistic diversity policy.

---

## Extended Formalizations *(v2 — 2026)*

### Durkheim — Mechanical vs Organic Solidarity

Durkheim's (1893) distinction between mechanical and organic solidarity receives precise mathematical interpretation:

- **Mechanical solidarity** — agents share nearly identical filter profiles: ||Φ_i - Φ_j|| ≈ 0 for all i,j. Synergy is low (no complementarity) but coordination cost is zero (perfect conceptual overlap). Homogeneous communities.
- **Organic solidarity** — agents have diverse profiles with high K-matrix compatibility: ||Φ_i - Φ_j|| large but K_ij > 1. High synergy, higher coordination cost. Complex division of cognitive labor.

The RTSG prediction: organic solidarity is fragile — it requires the K-matrix to remain compatible as filter divergence increases. Beyond the polarization threshold ||Φ_A - Φ_B|| > θ, organic solidarity collapses into factional mechanical solidarity.

### Bourdieu — Cultural Capital as Filter

Bourdieu's (1984, 1986) cultural capital maps directly to the filter formalism. The cultural filter Φ_cult encodes which cognitive types are valued, practiced, and reinforced within a given social stratum.

Willis's (1977) ethnographic finding that working-class "lads" actively participate in reproducing their own subordination receives formal explanation: the filter has become part of their self-model, making it phenomenologically invisible. They are not merely subjected to a filter — they have internalized it as identity.

Lareau's (2003) finding that "concerted cultivation" produces different cognitive outcomes than "accomplishment of natural growth" is precisely: Φ_dev(W_middle) ≠ Φ_dev(W_working), with the middle-class filter being more permissive in types that correlate with institutional success.

### The Synergy Ratio and Collective Intelligence

Woolley et al. (2010) measured a "collective intelligence factor" for groups empirically but could not formalize it. In RTSG, this factor is precisely the off-diagonal contribution:

$$\text{Syn}(B) = \sum_{i < j} \mathbf{I}_i^\top \mathbf{K}\, \mathbf{I}_j$$

Page's (2007) "diversity trumps ability" thesis follows: under favorable K-matrix conditions, a cognitively diverse group outperforms a homogeneous high-ability group because off-diagonal synergy terms overwhelm individual-capacity terms. The critical qualification RTSG adds: *diversity without K-matrix compatibility produces friction, not synergy*. This is the missing variable in the diversity literature.
