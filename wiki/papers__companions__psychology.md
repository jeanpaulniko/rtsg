---
title: "Psychology Companion Paper"
version: "2.0.0"
last_updated: "2026-03-05"
status: ARXIV-READY
arxiv_category: "q-bio.NC"
---

# Psychology Companion Paper

**Jean-Paul Niko** · February 2026

\begin{center}
{\LARGE\bfseries\color{sectionblue} Beyond $g$: Intelligence Vectors,  [3pt]
Compatibility Dynamics, and the  [3pt]
Geometry of Cognitive Profiles}

{\large Jean-Paul Niko}  [4pt]
{}  [2pt]
{\small`niko@triptomean.com`}  [12pt]
{\small February 2026}
\end{center}

!!! abstract "Abstract"
    
We present a geometric framework for intelligence that subsumes both factor-analytic models (CHC, Cattell) and multiple intelligences theory (Gardner) while adding algebraic structure that neither provides. Each individual's cognitive profile is an variable-dimensional vector $\bI \in \\mathbb{R}^{n(e)}$, where components represent capacities in symbolic-logical, spatial, linguistic, social, mnemonic, auditory, kinesthetic, and evaluative domains. The scalar $g$ is recovered as $\|\bI\|$ but discards the profile information that determines comparative advantage, cross-domain transfer, and team composition. The compatibility matrix $\bK \in \R^{8 \times 8}$ encodes pairwise interactions between types, predicting that training in type $s$ transfers to type $t$ when $K_{st} > 1$ and interferes when $K_{st} < 1$---a quantitative prediction testable with any cognitive training study. Filter operators formalize personality traits as stable components of developmental and genetic filters on the intelligence vector, unifying personality psychology and ability research within a single formalism. The framework provides a mathematical foundation for attention dynamics (the Kahneman System 1/2 distinction as simplex trajectories), expertise research (the Gap Monotonicity theorem proves that experts *cannot* losslessly communicate their understanding to novices), team composition (the synergy formula predicts which teams will be superadditive), and creativity (IdeaRank identifies ideas that bridge distant regions of conceptual space). We derive testable predictions for cognitive training transfer, curriculum sequencing, team performance, and the curse of expertise.

% ═══════════════════════════════════════════════════════════════════════════════

## Introduction: The Poverty of Scalar Intelligence

% ═══════════════════════════════════════════════════════════════════════════════

This paper presents a geometric framework for intelligence that resolves the century-old tension between unitary and pluralistic models. The tension is familiar: Spearman's $g$ [spearman1904] captures the well-documented positive manifold (all cognitive tests correlate positively), but a single number cannot explain why individuals with identical $g$ can have dramatically different cognitive profiles. Gardner's multiple intelligences [gardner1983] captures the intuition that cognition is multifaceted, but lacks the mathematical structure needed to make quantitative predictions.

The resolution is geometric. We model intelligence as a *vector* $\bI \in \\mathbb{R}^{n(e)}$ rather than a scalar. This preserves Spearman's $g$ as the norm $\|\bI\|$ (the positive manifold is a natural consequence of a shared scaling factor) while retaining the profile information that $g$ discards. But the key advance is not the vector itself---it is the *compatibility matrix* $\bK$ that encodes interactions between intelligence types. This matrix predicts cross-domain transfer effects, team synergies, and treatment interactions that no factor-analytic model can express.

The framework subsumes existing models:
[nosep]
- **CHC theory** [carroll1993,mcgrew2009]: The eight types map to CHC broad abilities (Gf $\approx I_{\mathrm{symb}}$, Gv $\approx I_{\mathrm{spat}}$, Gc $\approx I_{\mathrm{ling}}$, etc.) but adds the interaction structure that factor analysis cannot capture.
- **Gardner** [gardner1983]: Formalizes "multiple intelligences" with actual algebra---addition, scalar multiplication, inner products, and matrix operations.
- **Cattell** [cattell1963]: Fluid intelligence maps to the ceiling-filtered component $\Fceil(\bI)$; crystallized intelligence to the culturally-filtered component $\Fcult(\bI)$. The Gf/Gc distinction is a filter decomposition, not a type distinction.
- **Sternberg** [sternberg2020]: Analytical, creative, and practical intelligence correspond to different attention simplex configurations, not different types.

In the following sections, we develop the intelligence vector, compatibility matrix, filter formalism, attention dynamics, and applications to expertise, team composition, and creativity research, deriving testable predictions throughout.

% ═══════════════════════════════════════════════════════════════════════════════

## The Intelligence Vector

% ═══════════════════════════════════════════════════════════════════════════════

!!! definition "Intelligence Vector"
 \tA

An individual's cognitive profile is an variable-dimensional vector:
\begin{keyeq}
\[
\bI = (I_{\mathrm{symb}},\; I_{\mathrm{spat}},\; I_{\mathrm{ling}},\; I_{\mathrm{soc}},\; I_{\mathrm{mnem}},\; I_{\mathrm{aud}},\; I_{\mathrm{kin}},\; I_{\mathrm{eval}}) \in \\mathbb{R}^{n(e)}
\]
\end{keyeq}
Each component $I_t \geq 0$ represents capacity in a cognitive type, measured in standardized units ("cogs") calibrated via pairwise ELO tournaments on type-specific tasks.

The eight types are proposed as a basis for the human cognitive type space. The claim is not that exactly eight types exist (factor analysis might reveal a different optimal dimensionality) but that the framework's algebra works for any $n \geq 2$ and that eight provides the right granularity for most applications---fine enough to capture clinically and educationally meaningful distinctions, coarse enough to be estimable from realistic test batteries.

\begin{center}
\small

*[Table — see PDF for formatted version]*

\end{center}

!!! remark "Recovery of $g$"

The general intelligence factor is recovered as $g = \|\bI\| = \sqrt{\sum_t I_t^2}$. The positive manifold---the empirical finding that all cognitive tests correlate positively---follows from a shared scaling factor: individuals with larger $\|\bI\|$ tend to score higher on all type-specific tests. But two individuals with identical $g$ can have very different profiles: a mathematician with $\bI = (3, 2.5, 1.5, 1, 2, 1, 0.5, 1.5)$ and a diplomat with $\bI = (1.5, 1, 2.5, 3, 2, 1.5, 0.5, 2.5)$ have similar $\|\bI\|$ but very different comparative advantages.

% ═══════════════════════════════════════════════════════════════════════════════

## The Compatibility Matrix

% ═══════════════════════════════════════════════════════════════════════════════

The compatibility matrix is the central innovation beyond existing psychometric models. Factor analysis reveals correlations between abilities but cannot distinguish correlation due to shared variance from causal interaction. The $\bK$ matrix models the *causal* coupling between intelligence types.

!!! definition "Compatibility Matrix"
 \tA

The symmetric matrix $\bK \in \R^{8 \times 8}$ with $K_{tt} = 1$ encodes pairwise interactions:
\begin{keyeq}
\[
K_{st} \begin{cases}
> 1 & \text{types $s$ and $t$ amplify each other (training transfer, facilitation)}   
= 1 & \text{independent (no interaction)}   
< 1 & \text{types $s$ and $t$ interfere (inhibition, competition for resources)}
\end{cases}
\]
\end{keyeq}

Representative values (informed estimates; calibration from empirical data is an open research program):

\begin{center}
\small

*[Table — see PDF for formatted version]*

\end{center}

\begin{prediction}
The $\bK$ matrix generates quantitative predictions for cognitive training transfer studies. If $K_{\mathrm{spat},\mathrm{symb}} = 1.3$, then 20 hours of spatial training (mental rotation, spatial visualization) should produce measurable improvement in algebraic reasoning, with an effect size of approximately $d = 0.3 \times K_{\mathrm{spat},\mathrm{symb}} \times (\text{training gain in } I_{\mathrm{spat}})$. Conversely, if $K_{\mathrm{spat},\mathrm{soc}} = 0.7$, the same spatial training should produce a *negative* transfer to social cognition tasks. This is testable via a randomized training study with pre/post assessment on all eight type-specific task batteries.
\end{prediction}

### The $\bK$ Matrix vs.\ Factor Loadings

Factor analysis identifies shared variance but is silent on mechanism. The $\bK$ matrix specifies *directional interactions*: training type $s$ amplifies performance in type $t$ by a factor proportional to $K_{st}$. This makes different predictions from factor analysis in the critical case where two types share a factor loading (high correlation) but have $K_{st} < 1$ (causal interference). Such cases arise when correlation is due to a shared third variable (e.g., general arousal boosts both social and spatial performance, creating positive correlation, even though direct social-spatial interaction is inhibitory).

!!! proposition "Dissociation of Correlation and Causation"
 \tB

For any two types $s, t$, the observed correlation $r_{st}$ in cross-sectional psychometric data is:
\[
r_{st} = K_{st} + \sum_{u \neq s,t} \frac{K_{su} \cdot K_{tu}}{\sigma_s \sigma_t} \cdot \mathrm{Var}(I_u)
\]
The indirect pathways through shared connections inflate the observed correlation above the direct interaction $K_{st}$. Therefore $r_{st} > 0$ is consistent with $K_{st} < 1$.

This explains why factor analysis universally finds positive correlations (the positive manifold) even when some direct type interactions are inhibitory: the indirect pathways through shared connections dominate the signal.

% ═══════════════════════════════════════════════════════════════════════════════

## The Filter Formalism: Unifying Ability and Personality

% ═══════════════════════════════════════════════════════════════════════════════

The intelligence vector $\bI_{\mathrm{raw}}$ is never observed directly. What psychometric tests measure is the *effective* vector $\bI_{\mathrm{eff}} = \bF(\bI_{\mathrm{raw}})$, where $\bF$ is the composed filter cascade.

!!! definition "Filter Cascade"
 \tA

The effective intelligence vector is:
\begin{keyeq}
\[
\bI_{\mathrm{eff}} = F_{\mathrm{attn}} \circ \Fstate \circ \Fcult \circ \Fdev \circ \Fceil(\bI_{\mathrm{raw}})
\]
\end{keyeq}
Each filter operates at a different timescale: ceiling (evolutionary), developmental (years), cultural (months--years), state (seconds--hours), attention (milliseconds).

This formalism unifies several fields that have traditionally been studied separately:

### Personality as Stable Filter

!!! proposition "Personality--Filter Mapping"
 \tB

Personality traits are stable components of $F_{\mathrm{genetic}} \circ \Fdev$---the portion of the filter cascade that is relatively fixed in adulthood. The Big Five personality traits [costa1992] map to specific filter components:
\begin{keyeq}

\[\begin{aligned}
\text{Openness} &\approx \text{broadband gain on } I_{\mathrm{eval}} \text{ and } I_{\mathrm{symb}}   
\text{Conscientiousness} &\approx \text{attentional stability on } \Delta^7 \text{ (reduced } \Tcog\text{)}   
\text{Extraversion} &\approx \text{amplification of } I_{\mathrm{soc}} \text{ and } I_{\mathrm{kin}}   
\text{Agreeableness} &\approx \text{amplification of } I_{\mathrm{soc}} \text{ with } K_{\mathrm{soc},\mathrm{eval}} \text{ weighting}   
\text{Neuroticism} &\approx \text{instability of } \Fstate \text{ (high variance, rapid fluctuation)}
\end{aligned}\]

\end{keyeq}

\begin{intuition}
Personality psychology and ability psychology have been separate fields studying different aspects of the same architecture. Personality traits describe *how the filter is configured*; abilities describe *what gets through the filter*. The filter formalism reveals that these are not independent: an individual high in Openness (broadband evaluative-symbolic gain) will tend to score higher on creative tasks not because Openness "causes" creativity but because the same filter configuration that produces the Openness trait also amplifies the intelligence components relevant to creative performance.
\end{intuition}

### Cultural Psychology as Cultural Filter

!!! proposition "Culture as Filter"
 \tB

Cross-cultural differences in cognitive performance are modeled as different $\Fcult$ operators:
\[
\bI_{\mathrm{eff}}^{A} = \Fcult^{A}(\bI_{\mathrm{raw}}), \qquad \bI_{\mathrm{eff}}^{B} = \Fcult^{B}(\bI_{\mathrm{raw}})
\]
A test designed under $\Fcult^{A}$ measures $\bI_{\mathrm{eff}}^{A}$, not $\bI_{\mathrm{raw}}$. Students with different cultural filters score differently on the same raw ability.

This provides a formal account of test bias: "culture-free" tests are impossible because every test is administered *through* a cultural filter. The honest approach is to model the filter explicitly---to say "this test measures $I_{\mathrm{symb}}$ as filtered through Western educational $\Fcult$"---rather than to pretend the filter does not exist.

\begin{prediction}
If test bias is a filter effect, then administering type-specific tasks in culturally matched formats (using local examples, materials, and modalities) should reduce cross-cultural performance gaps on types where the $\Fcult$ difference is largest (typically $I_{\mathrm{symb}}$ and $I_{\mathrm{ling}}$) while leaving gaps unchanged on types where $\Fcult$ is similar across groups (typically $I_{\mathrm{spat}}$ and $I_{\mathrm{kin}}$).
\end{prediction}

% ═══════════════════════════════════════════════════════════════════════════════

## Attention Dynamics and the Cognitive Simplex

% ═══════════════════════════════════════════════════════════════════════════════

At any instant, an individual's attention is distributed across the eight intelligence types according to a probability distribution.

!!! definition "Attention Simplex"
 \tA

The attention allocation is a point on the 7-simplex:
\begin{keyeq}
\[
\lambda = (\lambda_1, \ldots, \lambda_8) \in \Delta^7, \qquad \sum_{t=1}^{8} \lambda_t = 1, \quad \lambda_t \geq 0
\]
\end{keyeq}
The effective output at time $t$ is $\bI_{\mathrm{output}}(t) = \diag(\lambda(t)) \cdot \bI_{\mathrm{eff}}$: each type contributes in proportion to the attention allocated to it.

Attention dynamics on the simplex are governed by the *replicator equation*:
\begin{keyeq}
\[
\dot{\lambda}_t = \lambda_t \left( \pi_t(\lambda) - \bar{\pi}(\lambda) \right)
\]
\end{keyeq}
where $\pi_t(\lambda) = \sum_s K_{st} \lambda_s I_s$ is the fitness of type $t$ under the current allocation and $\bar{\pi} = \sum_t \lambda_t \pi_t$ is the mean fitness. Types that contribute more than average to the current task grow in allocation; those that contribute less shrink.

### Kahneman's System 1 and System 2

The attention simplex provides a precise formalization of the System 1/System 2 distinction [kahneman2011]:

!!! definition "System 1 and System 2 Trajectories"
 \tB

[nosep]
- **System 1** = low-friction, high-speed trajectories along well-worn paths on $\Delta^7$. These correspond to habitual attention allocations that have been reinforced through practice. The friction coefficient $F_{st}$ for transitions along these paths is near zero.
- **System 2** = high-friction, deliberate movement to unusual regions of $\Delta^7$. The system must override the replicator dynamics to allocate attention to types that are not naturally favored by the current task.

\begin{intuition}
Learning is the process of converting System 2 paths into System 1 paths. A beginning chess player uses high-friction System 2 processing to evaluate board positions (deliberately allocating attention to $I_{\mathrm{spat}}$ and $I_{\mathrm{symb}}$). A grandmaster has worn deep grooves in the simplex: the spatial-symbolic allocation is automatic, low-friction, and fast.
\end{intuition}

### Cognitive Development

!!! proposition "Development as Simplex Expansion"
 \tB

Child cognitive development corresponds to the expansion of the *accessible region* of $\Delta^7$:
[nosep]
- **Infancy**: Accessible region restricted to vertices and near-vertex allocations (only one type active at a time).
- **Early childhood**: Edges become accessible (two-type combinations: spatial-kinesthetic for object manipulation, linguistic-social for communication).
- **Middle childhood**: Interior of the simplex opens (multi-type integration for complex tasks).
- **Adolescence/adulthood**: Full simplex accessible; expertise involves deep grooves in specific regions.

This recasts Piaget's stages [piaget1952] as qualitative changes in simplex accessibility. The sensorimotor stage is restriction to kinesthetic-spatial edges; the concrete operational stage is access to the symbolic-spatial-mnemonic face; the formal operational stage is access to the full symbolic interior.

Vygotsky's Zone of Proximal Development [vygotsky1978] corresponds to simplex regions that are adjacent to the child's current accessible set: regions they cannot reach alone but can reach with scaffolding (an external attention allocation provided by a teacher or peer).

% ═══════════════════════════════════════════════════════════════════════════════

## The ELO System for Psychometric Measurement

% ═══════════════════════════════════════════════════════════════════════════════

Traditional psychometric tests have fixed items, ceiling effects, and cultural loading. We propose an alternative measurement system based on pairwise ELO tournaments.

!!! definition "ELO Intelligence Profile"
 \tA

Each individual carries an ELO vector $\mathbf{E} \in \\mathbb{R}^{n(e)}$ alongside their intelligence vector $\bI$:
\begin{keyeq}
\[
\mathbf{E} = (E_{\mathrm{symb}},\; E_{\mathrm{spat}},\; E_{\mathrm{ling}},\; E_{\mathrm{soc}},\; E_{\mathrm{mnem}},\; E_{\mathrm{aud}},\; E_{\mathrm{kin}},\; E_{\mathrm{eval}})
\]
\end{keyeq}
Each $E_t$ is updated from observed pairwise performance on type-$t$-specific tasks:
\[
E_t^{\mathrm{new}} = E_t^{\mathrm{old}} + k\bigl(S_{t} - \mathbb{E}[S_{t}]\bigr)
\]
where $S_t \in \{0, 0.5, 1\}$ is the outcome, $\mathbb{E}[S_t] = 1/(1 + 10^{(E_t^{\mathrm{opp}} - E_t)/400})$ is the expected outcome from the logistic model, and $k$ is the update coefficient.

Advantages over traditional psychometrics:

[nosep]
- **No ceiling**: ELO scales indefinitely---there is no maximum score, so exceptional ability can be measured without item exhaustion.
- **Self-calibrating**: The rating system adjusts difficulty automatically through opponent matching.
- **Diagnostic**: Eight scores show *where* the individual is strong or weak, not just *whether*.
- **Less culturally loaded**: By modeling $\Fcult$ explicitly rather than pretending tests are culture-free, the ELO system separates filter effects from raw ability.
- **Continuous**: Ratings update continuously as new performance data arrives, unlike fixed-interval testing.

\begin{prediction}
An ELO-based variable-dimensional profile should predict academic and professional outcomes with higher fidelity than a single IQ score. Specifically: the profile-based prediction $\hat{y} = \bI \cdot \mathbf{w}$ (where $\mathbf{w}$ are type-specific weights for each outcome) should explain at least 15% more variance ($\Delta R^2 \geq 0.15$) than $g$ alone, with the improvement concentrated in outcomes that depend on specific type configurations (e.g., engineering success depends on $I_{\mathrm{spat}} \times I_{\mathrm{symb}}$, not on $g$).
\end{prediction}

% ═══════════════════════════════════════════════════════════════════════════════

## Expertise and the Curse of Knowledge

% ═══════════════════════════════════════════════════════════════════════════════

The framework provides a mathematical account of a well-documented phenomenon in expertise research: experts are poor at communicating their understanding to novices [hinds1999].

!!! theorem "Gap Monotonicity"
 \tB

Let $H(x)$ denote the Heyting Gap---the information lost when translating between experiential and descriptive representations. For any agent $x$ with expertise level $\mathcal{E}(x)$:
\begin{keyeq}
\[
\frac{\partial H}{\partial \mathcal{E}} > 0
\]
\end{keyeq}
The more you know, the harder it is to say what you know. This is a theorem, not a pedagogical failing.

\begin{intuition}
The expert chess player "sees" the board in a way that integrates spatial pattern recognition, strategic evaluation, and mnemonic retrieval into a seamless percept. To communicate this to a novice requires decomposing this integrated perception into sequential verbal descriptions---a translation from a high-dimensional experiential representation to a low-dimensional linguistic one. The Gap Monotonicity theorem proves that this translation is *increasingly* lossy as expertise grows, because the expert's internal representation becomes increasingly integrated and multi-type, while the communication channel remains fixed-bandwidth.
\end{intuition}

This connects to:

[nosep]
- **Hinds' curse of expertise** [hinds1999]: Experts underestimate task difficulty for novices because they cannot "unsee" their integrated representation.
- **Dreyfus & Dreyfus skill acquisition** [dreyfus1986]: The progression from novice (rule-following) to expert (intuitive) corresponds to increasing integration across simplex dimensions---and increasing Heyting Gap.
- **Bloom's two-sigma problem** [bloom1984]: One-on-one tutoring produces a two-standard-deviation improvement over classroom instruction. The framework explains why: the tutor can dynamically adjust their Heyting Gap to match the student's level, while classroom instruction is fixed at one Gap setting.

!!! corollary "Optimal Teacher Gap"
 \tB

The most effective teacher for a student at expertise level $\mathcal{E}_s$ is not the greatest expert but the person whose Heyting Gap $H(\mathcal{E}_t)$ optimally matches the student's absorption capacity. Formally, the optimal teacher expertise is:
\[
\mathcal{E}_t^* = \arg\min_{\mathcal{E}_t > \mathcal{E}_s} \left[ H(\mathcal{E}_t) - H_{\mathrm{max}}(\mathcal{E}_s) \right]^2
\]
where $H_{\mathrm{max}}(\mathcal{E}_s)$ is the maximum Heyting Gap the student can bridge.

This provides a mathematical formulation of Vygotsky's Zone of Proximal Development: the ZPD width *is* $H_{\mathrm{max}}(\mathcal{E}_s)$.

% ═══════════════════════════════════════════════════════════════════════════════

## Team Composition and Collective Intelligence

% ═══════════════════════════════════════════════════════════════════════════════

The intelligence vector extends naturally from individuals to teams via the *bundle synergy* formula.

!!! definition "Cognitive Bundle"
 \tA

A team is a cognitive bundle $B = \{\bI_1, \ldots, \bI_n\}$---a collection of intelligence vectors with an orchestration mechanism.

!!! definition "Bundle Synergy"
 \tA

The synergy of a bundle is:
\begin{keyeq}
\[
\Syn(B) = \frac{I_{\mathrm{eff}}^{\mathrm{bundle}}}{\sum_{i} I_{\mathrm{eff}}^{(i)}} = 1 + \frac{1}{n}\sum_{i<j}\sum_{s \neq t} \frac{(K_{st} - 1) \cdot I_s^{(i)} \cdot I_t^{(j)}}{\sum_k I_k}
\]
\end{keyeq}
$\Syn(B) > 1$ means the team is *superadditive*: the whole exceeds the sum of parts.  
$\Syn(B) < 1$ means the team is *subadditive*: coordination costs exceed diversity benefits.

\begin{intuition}
A team with one spatial genius ($I_{\mathrm{spat}} = 3$) and one symbolic genius ($I_{\mathrm{symb}} = 3$) achieves $\Syn > 1$ when $K_{\mathrm{spat},\mathrm{symb}} > 1$: the spatial thinker's visualizations amplify the symbolic thinker's formal reasoning, and vice versa. A team of two identical profiles contributes no synergy---diversity is the source of superadditivity. This connects to Woolley et al.'s finding that collective intelligence depends more on social sensitivity and diversity than on maximum individual $g$ [woolley2010].
\end{intuition}

\begin{prediction}
Measure team member intelligence profiles via the 8D ELO system. The synergy formula should predict team performance on complex tasks with $R^2 > 0.4$, substantially outperforming the simpler model that uses only mean $g$ of team members ($R^2$ typically $\approx 0.1$--$0.2$ in existing literature). The improvement comes from the profile diversity and $\bK$ interaction terms.
\end{prediction}

### "Culture Fit" vs.\ "Culture Add"

The synergy formula formalizes the hiring debate between "culture fit" (hiring similar profiles to minimize coordination friction) and "culture add" (hiring diverse profiles to maximize synergy ceiling):

[nosep]
- **Culture fit**: Low friction (similar $\bI$ profiles → low coordination cost), but also low synergy ceiling (no diversity to exploit $\bK$-mediated amplification).
- **Culture add**: Higher potential synergy ($\Syn_{\max}$ increases with profile diversity), but higher coordination cost (the orchestration mechanism must manage a higher-dimensional attention simplex).

The optimal strategy depends on task type: routine tasks benefit from fit (low-friction execution), while novel or complex tasks benefit from add (diverse perspectives enable $\bK$-mediated amplification in new type combinations).

% ═══════════════════════════════════════════════════════════════════════════════

## Creativity and IdeaRank

% ═══════════════════════════════════════════════════════════════════════════════

!!! definition "IdeaRank"
 \tB

Each idea $x$ in a conceptual space has a relevance score with respect to each intelligence type. The IdeaRank of $x$ is:
\begin{keyeq}
\[
\IdeaRank(x) = \sum_{t=1}^{8} R_t(x) \cdot I_t \cdot w_t
\]
\end{keyeq}
where $R_t(x)$ is the relevance of idea $x$ to type $t$, $I_t$ is the agent's capacity in type $t$, and $w_t$ are context-dependent weights.

Creativity, in this framework, corresponds to generating ideas with high IdeaRank in *novel type combinations*---ideas that bridge distant regions of the conceptual space.

!!! proposition "Creativity as Remote Association"
 \tB

An idea $x$ is "creative" if $\IdeaRank(x)$ is high and $x$ has nonzero relevance in at least two types $s, t$ with low $K_{st}$ (i.e., types that normally *do not* interact). Formally:
\[
\text{Creativity}(x) \propto \IdeaRank(x) \times \sum_{s<t} R_s(x) R_t(x) (1 - K_{st})
\]

This connects to Mednick's remote associates theory [mednick1962]: creative ideas combine concepts from "remote" domains. In our framework, "remote" means types with low $K$---domains that normally inhibit rather than amplify each other. The creative act is bridging an inhibitory gap.

!!! example "Example"

A physicist who recognizes that the mathematics of fluid dynamics applies to traffic flow is connecting $I_{\mathrm{symb}}$ (differential equations) with $I_{\mathrm{spat}}$ (traffic patterns) through an unusual $I_{\mathrm{eval}}$ (recognizing the structural analogy). The high $K_{\mathrm{spat},\mathrm{symb}}$ makes this a natural but not especially creative connection. A poet who uses fluid dynamics as a metaphor for grief connects $I_{\mathrm{symb}}$ with $I_{\mathrm{eval}}$ through $I_{\mathrm{ling}}$---a much more "remote" association, hence more creative.

% ═══════════════════════════════════════════════════════════════════════════════

## Implications for Psychometric Practice

% ═══════════════════════════════════════════════════════════════════════════════

The framework has several practical implications:

**Assessment.** Replace single-score instruments with variable-dimensional profiles estimated via ELO tournaments. This is more diagnostic (shows *where* the individual excels or struggles), less culturally loaded (models $\Fcult$ explicitly), and has no ceiling effect.

**Cognitive training.** Design training programs that exploit $\bK$ amplification: pair spatial training with algebraic instruction ($K_{\mathrm{spat},\mathrm{symb}} = 1.3$) rather than administering them in isolation. Predict *negative* transfer when $K_{st} < 1$ and design accordingly.

**Educational placement.** Use profile matching: students with high $I_{\mathrm{spat}}$ but low $I_{\mathrm{symb}}$ may benefit from geometry-first curricula that exploit spatial strength to build symbolic competence via $K_{\mathrm{spat},\mathrm{symb}} > 1$.

**Team selection.** Use the synergy formula to predict which team compositions will be superadditive. Optimize for $\Syn(B) > 1$ rather than maximum mean $g$.

**Expertise development.** Use Gap Monotonicity to match mentors with mentees at the optimal expertise gap, rather than assigning the most senior expert as the default mentor.

% ═══════════════════════════════════════════════════════════════════════════════

## Limitations

% ═══════════════════════════════════════════════════════════════════════════════

**Dimensionality.** The claim of exactly 8 types is a working hypothesis. Factor analysis of comprehensive cognitive test batteries might reveal a different optimal number. The framework's algebra works for any $n \geq 2$.

**$\bK$ calibration.** The compatibility values are informed estimates. Systematic calibration requires large-scale cognitive training transfer studies. The framework predicts *that* $\bK$ exists and has the specified structure; the exact values are an empirical program.

**Linearity.** The filter formalism assumes linearity in first approximation. Actual cognitive dynamics likely involve threshold effects, saturation, and nonlinear interactions.

**Individual stability.** The framework assumes that $\bI_{\mathrm{raw}}$ and $\bK$ are relatively stable within individuals. Longitudinal studies are needed to assess this assumption.

**Pairwise limitation.** The synergy formula uses pairwise $\bK$ interactions. Higher-order (three-way, four-way) interactions may be significant for complex team compositions.

% ═══════════════════════════════════════════════════════════════════════════════

## Conclusion

% ═══════════════════════════════════════════════════════════════════════════════

We have presented a geometric framework for intelligence that resolves the scalar-vs.-plural debate by treating intelligence as a vector with algebraic structure. The framework subsumes CHC and Gardner, provides a formal account of cross-domain transfer via the compatibility matrix, unifies ability and personality through the filter formalism, and generates testable predictions for cognitive training, team composition, expertise development, and creativity research. The scalar $g$ is not wrong---it is a shadow of a richer structure. The goal is not to abandon $g$ but to see the full geometry that casts it.

*This paper is a companion extraction from "Intelligence as Geometry" (Niko, 2026). The full mathematical development is available in the parent document.*

% ═══════════════════════════════════════════════════════════════════════════════

## \color{sectionblue
Three-Space Psychology}

The three-space ontology (Part XIII) enriches the psychological interpretation of the IAG framework in three ways.

**The Id as pre-filter.**  The Id (Species 0 filter) anchors consciousness to physical time $t_\mathbb{R}$, overriding the lateral temporal freedom of $\CSp$ when survival demands it.  Anxiety is the Id's signal that the organism is drifting too far into $t_{\mathrm{lat}}$ (future-oriented rumination); depression is the signal of excessive backward $t_{\mathrm{lat}}$ navigation (past-focused dwelling).  Healthy psychological function requires a dynamic equilibrium between $t_\mathbb{R}$-anchoring (Id) and $t_{\mathrm{lat}}$-exploration (creativity, planning, reflection).

**Memory as multi-algebraic structure.**  The five memory types map to distinct algebras: episodic ($\mathbb{R}$, linear timeline), semantic ($\Qp$, ultrametric hierarchy), procedural ($K$-matrix sculpting), working ($\Delta^7$ simplex), short-term ($\mathbb{C}$ decay).  Psychological interventions target specific algebraic structures: cognitive-behavioral therapy restructures the $\Qp$-topology of semantic memory; exposure therapy sculpts the $K$-matrix of procedural fear responses; mindfulness training expands the $\Delta^7$ capacity of working memory.

**Transcendent states.**  Peak experiences, flow states, and mystical experiences correspond to temporary expansion of $t_{\mathrm{lat}}$ navigation: the Id filter relaxes, and consciousness accesses regions of $\CSp$ normally unavailable.  The "timelessness" reported in these states is the phenomenological signature of movement in the purely lateral temporal direction, where $t_\mathbb{R}$ appears to stop.

## References

*See PDF for full bibliography.*
---

## v2 Integration: Personal Language, Style as Identity, Fingerprinting (TMP-20260217)

**Personal language:** L(ξ) = f(G(ξ)_own, G(ξ)_absorbed). Formal account of the tension between authentic self-expression and socialized behavior — the central problem of personality psychology.

**Style = G(ξ)_own:** The irreducible personal RTSG subgraph after factoring out absorbed influences. Formal definition of psychological authenticity: degree to which expressed output reflects G_own rather than G_absorbed.

**Fingerprinting as assessment:** Corpus → **I**(ξ) pipeline replaces self-report personality instruments with direct I-vector recovery from behavioral output (written, spoken, artistic, movement). Robust to self-report bias.

**Flow state (formal):** SDE update loop at maximum efficiency: λ just below 0, σ at minimum, utility gradient α at maximum. The γ-oscillation correlate is the spectral signature of this SDE state.
