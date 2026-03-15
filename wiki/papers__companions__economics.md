---
title: "Economics Companion Paper"
version: "2.0.0"
last_updated: "2026-03-05"
status: ARXIV-READY
arxiv_category: "physics.soc-ph"
---

# Economics Companion Paper

**Jean-Paul Niko** · February 2026

% ═══════════════════════════════════════════════════════════════════════════════

% ═══ Three-Space Notation ═══
\newcommand{\QS}{\mathcal{Q}}
\newcommand{\PS}{\mathcal{P}}
\newcommand{\CSp}{\mathcal{C}_S}
\newcommand{\Inst}{\mathfrak{I}}
\newcommand{\Qp}{\mathbb{Q}_p}

\title{\textcolor{sectionblue}{**Cognitive Capital, Synergistic Firms, and the IdeaRank Market:  [0.3em]
A Mathematical Framework for Knowledge Economics**}}
\author{Jean-Paul Niko}
\date{2026}

!!! abstract "Abstract"
    
Human capital theory has long recognized that education and skill acquisition drive economic growth, yet the standard formalization---a scalar measure of "human capital"---discards the dimensional structure that determines comparative advantage, team complementarity, and the economics of innovation. This paper introduces a vector-valued theory of cognitive capital drawn from the Intelligence as Geometry (RTSG) framework. Each economic agent carries an eight-dimensional *intelligence vector* $\bI \in [0,\infty)^8$ capturing the profile of cognitive capacities across linguistic-analytical, spatial-mechanical, social-relational, symbolic-abstract, mnemonic-archival, evaluative-strategic, auditory-musical, and kinesthetic-somatic types. A symmetric *compatibility matrix* $\bK \in \R^{8 \times 8}$ encodes pairwise cross-type interactions: when $K_{st} > 1$, exercising type $s$ amplifies type $t$ (synergy); when $K_{st} < 1$, it creates interference. Teams are modeled as *cognitive bundles* whose collective output depends on diversity of profiles and the $\bK$-weighted synergy between them, not merely the sum of individual productivities. The *IdeaRank assignment market* matches agents to tasks via inner products of intelligence vectors and requirement vectors, with ELO-calibrated confidence weights. A *filter formalism* models how institutional, cultural, and developmental environments transform raw cognitive profiles into observed economic productivity, providing a mathematical framework for discrimination, misallocation, and inequality. We derive testable predictions for optimal team composition, firm boundaries, R&D portfolio diversification, and the economic cost of discrimination measured as synergy loss. The framework extends Becker's human capital, Romer's endogenous growth, and Coase's theory of the firm with algebraic structure that was previously absent.
The three-space ontology grounds cognitive capital in instantiation capacity and reveals discrimination as a waste of the economy's projection resources.

**Keywords:** intelligence vector, cognitive capital, bundle synergy, compatibility matrix, IdeaRank, filter operators, team composition, knowledge economics, endogenous growth, discrimination

---

% ═══════════════════════════════════════════════════════════════════════════════

## Introduction

% ═══════════════════════════════════════════════════════════════════════════════

The economics of knowledge production rests on a paradox. Every major theoretical framework acknowledges that human cognition is the fundamental input to the knowledge economy, yet every standard model collapses that cognition into a scalar: Becker's "human capital" $h$, Romer's "human capital stock" $H$, Mincer's "years of schooling" $s$. These scalars compress multidimensional cognitive reality into a single number, discarding exactly the dimensional structure that determines who should work with whom, which teams produce breakthrough innovations, and why markets systematically misallocate talent.

Consider a concrete example. A biotechnology startup must assemble a founding team. It has access to two candidates with identical scalar human capital (same education level, same years of experience, same IQ score). Candidate A has exceptional spatial-mechanical and symbolic-abstract reasoning but limited social-relational skill. Candidate B has exceptional social-relational and evaluative-strategic ability but weaker formal reasoning. Standard human capital theory assigns them equal productive capacity. Any experienced hiring manager recognizes this is absurd: the *combination* of A and B may be far more productive than either alone, or far less, depending on how their cognitive types interact in the specific task environment.

The Intelligence as Geometry (RTSG) framework, developed in the full monograph  [Niko2026], provides the algebraic structure that human capital theory lacks. This paper extracts the components most relevant to economics and organizational science, translating the framework into the language of production functions, market mechanisms, firm theory, and growth models. We make five contributions.

First, we replace scalar human capital with a vector-valued *cognitive capital* $\bI_{\mathrm{eff}} = \bF(\bI_{\mathrm{raw}})$, where the filter operator $\bF$ captures the institutional, cultural, and developmental transformations that convert raw cognitive endowment into observed economic productivity. This preserves the dimensional information that determines comparative advantage.

Second, we formalize team production as *bundle synergy*. A firm or team is a cognitive bundle $B = \{\bI_1, \ldots, \bI_n\}$ whose collective output depends on the $\bK$-weighted interactions between member profiles, not merely the sum of individual productivities. We prove conditions under which diverse teams outperform homogeneous ones and derive the optimal team composition problem as a submodular optimization.

Third, we introduce the *IdeaRank assignment market*, a mechanism that matches agents to tasks (or workers to jobs) via the inner product of intelligence vectors and task requirement vectors, weighted by ELO-calibrated confidence. This provides a formal model of labor market efficiency and a precise measure of misallocation.

Fourth, we develop a *portfolio theory for R&D investment*, treating ideas as assets with IdeaRank-derived returns and using Markowitz-style diversification across cognitive dimensions.

Fifth, we formalize labor market discrimination as a filter distortion: prejudice applies a cultural filter $\bF_{\mathrm{bias}}$ that systematically attenuates the perceived intelligence vector of certain groups, producing suboptimal team compositions whose synergy loss constitutes the quantifiable economic cost of discrimination.

\begin{intuition}
**Central metaphor.** Standard economics treats workers as interchangeable units of "human capital" $h$---like homogeneous fuel. RTSG treats workers as elements with specific crystalline structures that bond differently depending on the partner. Carbon and iron are both valuable, but their value in combination depends on which alloy you are trying to forge. The $\bK$ matrix is the periodic table of cognitive bonding.
\end{intuition}

% ═══════════════════════════════════════════════════════════════════════════════

## The Intelligence Vector as Cognitive Capital

% ═══════════════════════════════════════════════════════════════════════════════

### From scalar to vector

!!! definition "Intelligence Vector"
 \tA
An economic agent's cognitive endowment is described by a vector
\[
  \bI = (I_{\mathrm{ling}},\; I_{\mathrm{spat}},\; I_{\mathrm{soc}},\; I_{\mathrm{symb}},\; I_{\mathrm{mnem}},\; I_{\mathrm{eval}},\; I_{\mathrm{aud}},\; I_{\mathrm{kin}}) \;\in\; [0,\infty)^8,
\]
where each component measures capacity in a distinct cognitive type: linguistic-analytical, spatial-mechanical, social-relational, symbolic-abstract, mnemonic-archival, evaluative-strategic, auditory-musical, and kinesthetic-somatic respectively.

The eight types are chosen for empirical discriminability (they map onto established psychometric factors and identifiable neural circuit complexes) and algebraic completeness (they span the space of human cognitive variation at a resolution sufficient for organizational modeling while remaining tractable). The RTSG monograph provides the full justification, including the relationship to Cattell--Horn--Carroll factors and Gardner's multiple intelligences ([Niko2026], Part I).

The scalar models that dominate economics are projections of this vector onto a one-dimensional subspace. Becker's [Becker1964] human capital $h$ corresponds roughly to $\|\bI\|$, the Euclidean norm---total cognitive magnitude, direction discarded. Mincer's years-of-schooling proxy captures only the component of $\bI$ that formal education amplifies (primarily $I_{\mathrm{ling}}$, $I_{\mathrm{symb}}$, and $I_{\mathrm{mnem}}$), which explains why returns to education vary dramatically across occupations: a year of schooling amplifies the types relevant to academic work but may do little for $I_{\mathrm{soc}}$, $I_{\mathrm{kin}}$, or $I_{\mathrm{spat}}$.

\begin{keyeq}
**Scalar collapse.** All scalar human capital measures are projections:
\[
  h_{\mathrm{Becker}} = \|\bI_{\mathrm{eff}}\|, \qquad
  h_{\mathrm{Mincer}} \approx w_{\mathrm{ling}}\,I_{\mathrm{ling}} + w_{\mathrm{symb}}\,I_{\mathrm{symb}} + w_{\mathrm{mnem}}\,I_{\mathrm{mnem}}
\]
where the weights $w_t$ are implicit in the regression specification. The information destroyed by these projections is precisely what determines comparative advantage, team complementarity, and innovation potential.
\end{keyeq}

### Comparative advantage as vector geometry

Ricardo's comparative advantage, typically applied to nations trading goods, has a natural analog in the cognitive vector framework. An agent has comparative advantage in task $j$ over task $k$ relative to another agent when the ratio of their capability-to-requirement alignments favors that assignment.

!!! definition "Task Requirement Vector"
 \tA
Each economic task $j$ is characterized by a *requirement vector*
\[
  \bR_j = (R_{j,\mathrm{ling}},\; R_{j,\mathrm{spat}},\; \ldots,\; R_{j,\mathrm{kin}}) \;\in\; [0,\infty)^8,
\]
specifying the cognitive demands of the task across all eight types. A task requiring spatial visualization and symbolic manipulation would have high $R_{j,\mathrm{spat}}$ and $R_{j,\mathrm{symb}}$, with other components near zero.

The alignment between agent $i$ and task $j$ is the inner product $\langle \bI_i, \bR_j \rangle = \sum_t I_{i,t}\, R_{j,t}$. Agent $i$ has comparative advantage in task $j$ over task $k$ relative to agent $i'$ when
\[
  \frac{\langle \bI_i, \bR_j \rangle}{\langle \bI_i, \bR_k \rangle}
  > \frac{\langle \bI_{i'}, \bR_j \rangle}{\langle \bI_{i'}, \bR_k \rangle}.
\]
This is impossible to express when both agents have scalar $h$: equal $\|\bI\|$ implies equal alignment with every task. The dimensional structure of $\bI$ is exactly what generates comparative advantage.

!!! remark "Remark"

This formalization makes a prediction that departs from standard matching models: the optimal assignment of workers to jobs is NOT the one that maximizes total scalar output $\sum_i h_i$, but the one that maximizes the sum of alignments $\sum_{(i,j) \in M} \langle \bI_i, \bR_j \rangle$ across the matching $M$. These can differ substantially when workers have similar norms but different profiles.

### The filter formalism: from endowment to productivity

Raw cognitive endowment $\bI_{\mathrm{raw}}$ is never directly observed in economic activity. What an employer sees---what the labor market prices---is the *effective* intelligence vector after institutional, cultural, and developmental filters have been applied.

!!! definition "Filter Operator"
 \tA
A filter is a non-negative linear operator $\bF: [0,\infty)^8 \to [0,\infty)^8$ with bounded gain:
\[
  \bF \in \{M \in \R^{8 \times 8} : M_{ij} \geq 0,\; \|M\|_{\mathrm{op}} \leq c_{\max}\}.
\]
The effective intelligence vector is
\[
  \bI_{\mathrm{eff}} = \bF_{\mathrm{inst}} \circ \bF_{\mathrm{cult}} \circ \bF_{\mathrm{dev}} \circ \bF_{\mathrm{gen}}(\bI_{\mathrm{raw}}),
\]
where $\bF_{\mathrm{gen}}$ encodes genetic endowment variation, $\bF_{\mathrm{dev}}$ captures developmental and educational environment, $\bF_{\mathrm{cult}}$ encodes cultural values and practices, and $\bF_{\mathrm{inst}}$ captures institutional context (firm, industry, regulatory environment).

This decomposition reconceptualizes central questions in labor economics:

*Returns to education* are not a single number but depend on which components of $\bI$ the educational filter $\bF_{\mathrm{dev}}$ amplifies relative to the task requirements the graduate will face. A liberal arts education amplifies $I_{\mathrm{ling}}$ and $I_{\mathrm{soc}}$; an engineering degree amplifies $I_{\mathrm{spat}}$ and $I_{\mathrm{symb}}$. The "return" depends on the match between the amplified profile and downstream task requirements.

*Credential inflation* is the progressive narrowing of which filters employers will accept. When hiring requires a specific degree (a specific $\bF_{\mathrm{dev}}$ configuration), this excludes agents whose $\bI_{\mathrm{raw}}$ may be well-suited to the task but whose developmental filter applied different amplification.

*Human capital externalities* (Lucas, [Lucas1988]; Moretti, [Moretti2004]) become interaction effects: an agent's filter environment depends on the profiles of surrounding agents. Living in a city with high average $I_{\mathrm{symb}}$ doesn't just raise the mean---it changes the $\bF_{\mathrm{inst}}$ filter available to all residents, through institutions, discourse norms, and ambient intellectual culture.

% ═══════════════════════════════════════════════════════════════════════════════

## The Compatibility Matrix and Team Production

% ═══════════════════════════════════════════════════════════════════════════════

### Cross-type interactions

The central algebraic object for organizational economics is the compatibility matrix.

!!! definition "Compatibility Matrix"
 \tA
The matrix $\bK \in \R^{8 \times 8}$ with $K_{st} > 0$ for all $s,t$ encodes pairwise cross-type interactions:
[nosep]
  - $K_{st} > 1$: exercising type $s$ amplifies performance in type $t$ (synergy)
  - $K_{st} = 1$: types are independent
  - $K_{st} < 1$: exercising type $s$ interferes with type $t$ (friction)

For organizational design, the critical insight is that $\bK$ governs not just intra-individual cognition but *inter-individual* team dynamics. When agent $A$ (high $I_{\mathrm{spat}}$) collaborates with agent $B$ (high $I_{\mathrm{symb}}$), and $K_{\mathrm{spat},\mathrm{symb}} = 1.3$, the team's effective output on tasks requiring both types exceeds what either agent could produce alone by a factor determined by the synergy coefficient. Conversely, two agents who both bring high $I_{\mathrm{eval}}$ experience diminishing returns (the same type competing for the same niche), and may even interfere if $K_{\mathrm{eval},\mathrm{eval}} < 1$ under attentional competition.

\begin{keyeq}
**Production function with $\bK$-structure.**
For a team of agents $\{\bI_1, \ldots, \bI_n\}$ executing a task with requirement $\bR$, the effective team output is:
\[
  Y(B, \bR) \;=\; \sum_{i=1}^n \langle \bI_i, \bR \rangle \;+\; \sum_{i < j}\sum_{s,t} (K_{st} - 1)\,I_{i,s}\,I_{j,t}\,R_s\,R_t
\]
The first term is the scalar-sum baseline (what standard human capital predicts). The second term is the *synergy surplus*---the additional output from cross-type interactions, positive when high-$K$ pairs are activated and negative when low-$K$ pairs interfere.
\end{keyeq}

This production function has immediate organizational implications. Holding total capability $\sum_i \|\bI_i\|$ constant, output $Y$ is maximized by allocating diversity across types with high $K_{st}$ and concentrating when $K_{st} < 1$. The standard economic intuition that "more is better" holds only for the first term; the synergy surplus depends on the *geometric arrangement* of profiles.

### Bundle synergy

!!! definition "Bundle Synergy"
 \tA
For a cognitive bundle $B = \{\bI_1, \ldots, \bI_n\}$, the synergy is
\[
  \Syn(B) = \frac{\bigl\|\sum_i \bK \bI_i\bigr\|}{\sum_i \|\bK \bI_i\|}
\]
where $\Syn(B) > 1$ indicates superadditivity (the whole exceeds the sum of parts), $\Syn(B) = 1$ indicates additivity, and $\Syn(B) < 1$ indicates subadditivity (coordination losses exceed complementarity gains).

!!! proposition "Diversity--Synergy Relationship"
 \tA
For agents drawn from a population with covariance $\Sigma$ over intelligence profiles, and a compatibility matrix $\bK$ with dominant eigenvalue $\lambda_1$ and spectral gap $\gamma = \lambda_1 - \lambda_2$:
[nosep]
  - Synergy increases with profile diversity (measured by the rank of the matrix $[\bI_1 | \cdots | \bI_n]$) when the diverse types occupy high-$K$ pairings.
  - Synergy decreases with diversity when diverse types occupy low-$K$ pairings (the coordination cost exceeds the complementarity benefit).
  - The optimal team composition balances diversity against $\bK$-compatibility.

This result formalizes the empirical findings of Woolley et al.\  [Woolley2010], who demonstrated a "collective intelligence factor" for groups. In our framework, this factor *is* $\Syn(B)$: teams with high $\Syn$ exhibit collective intelligence that exceeds individual contributions. The result also formalizes the core insight of Page [Page2007], who argued that diversity trumps ability---with a critical qualification that our framework provides: diversity trumps ability *only when the diverse types have favorable $\bK$-interactions*. Random diversity can reduce performance.

### Coordination costs and optimal firm size

Bundle synergy does not increase monotonically with team size. Adding agents introduces coordination costs: each new member must integrate with $n - 1$ existing members, and the attention required for coordination competes with productive cognitive work.

!!! definition "Coordination Cost"
 \tB
The coordination cost for a bundle of $n$ agents is
\[
  C_{\mathrm{coord}}(n) = c_0 \sum_{i < j} \frac{\max(0,\; 1 - K_{t_i^*, t_j^*})^2}{n^2}
\]
where $t_i^*$ denotes agent $i$'s dominant type and $c_0$ is a scale parameter calibrated to organizational data. The cost grows with the number of low-$K$ pairings and the severity of incompatibility.

Net effective output is then $Y_{\mathrm{net}} = Y(B, \bR) - C_{\mathrm{coord}}(n)$. The first-order condition $\partial Y_{\mathrm{net}}/\partial n = 0$ yields the optimal firm size $n^*$, which depends on:
[nosep]
  - The task requirement vector $\bR$: more dimensionally complex tasks justify larger teams.
  - The available talent pool's profile distribution: richer diversity expands $n^*$.
  - The $\bK$ structure: higher average $K_{st}$ across recruited pairs lowers coordination costs and raises $n^*$.

\begin{intuition}
**Coase's [Coase1937** theory of the firm, algebraically.] Firms exist because bundle synergy within a coordinated organization exceeds market-mediated synergy between independent agents. The firm boundary is the surface where marginal synergy gain from adding the next member equals marginal coordination cost. Transaction costs *are* low-$K$ friction costs: the difficulty of integrating cognitive types across organizational boundaries. The Coasean prediction that firms grow until internal coordination costs equal market transaction costs is a special case of $\partial Y_{\mathrm{net}}/\partial n = 0$.
\end{intuition}

% ═══════════════════════════════════════════════════════════════════════════════

## The IdeaRank Assignment Market

% ═══════════════════════════════════════════════════════════════════════════════

### Assignment scores

The labor market is, at its core, a matching problem: agents with cognitive profiles must be assigned to tasks with cognitive requirements. IdeaRank provides the scoring function for this match.

!!! definition "IdeaRank Assignment Score"
 \tA
For agent $i$ with intelligence vector $\bI_i$, ELO vector $\mathbf{E}_i$, and task $j$ with requirement vector $\bR_j$:
\[
  \mathrm{score}(i,j) = \sum_t I_{i,t} \cdot R_{j,t} \cdot \sigma\!\left(\frac{E_{i,t} - \bar{E}_t}{s}\right)
\]
where $\sigma(x) = 1/(1 + e^{-x})$ is a sigmoid, $\bar{E}_t$ is the population mean ELO for type $t$, and $s$ is a scale parameter.

The ELO component serves as a calibration mechanism. Two agents with identical intelligence vectors $\bI_i = \bI_{i'}$ but different ELO ratings are distinguished by their demonstrated performance: the agent with higher $E_{i,t}$ receives greater confidence weight for type-$t$ tasks. This resolves a key measurement problem in labor economics---within-category heterogeneity---without requiring additional latent factors.

\begin{keyeq}
**Optimal assignment problem.**
\[
  M^* = \arg\max_M \;\sum_{(i,j) \in M} \mathrm{score}(i,j)
\]
subject to: each agent assigned to at most $\mathrm{cap}(i)$ tasks; each task assigned to exactly one agent. This is a linear assignment problem solvable in $O(n^3)$ by the Hungarian algorithm, or approximately by auction mechanisms (Bertsekas, [Bertsekas1988]).
\end{keyeq}

The optimal matching $M^*$ represents perfect labor market efficiency. The deviation of the actual matching from $M^*$ is a precise measure of misallocation:
\[
  \Delta_{\mathrm{misalloc}} = \sum_{(i,j) \in M^*} \mathrm{score}(i,j) - \sum_{(i,j) \in M_{\mathrm{actual}}} \mathrm{score}(i,j).
\]
This quantity has units (cognitive-type-weighted output), is always non-negative, and is directly interpretable as lost productivity from suboptimal assignment.

### Sources of misallocation

The framework identifies specific, distinguishable sources of labor market misallocation:

*Information failure.* The employer does not observe $\bI_i$ directly but only noisy proxies (credentials, interview performance, references). Each proxy is itself a filtered projection $\hat{\bI}_i = \bF_{\mathrm{signal}}(\bI_i)$, and the information loss in this filter drives matching error.

*Filter-induced bias.* The employer's evaluation filter $\bF_{\mathrm{eval}}$ may systematically attenuate certain components of perceived $\bI_i$ based on demographic characteristics unrelated to actual cognitive profile. This is the discrimination mechanism formalized in Section *ref:sec:discrimination*.

*Credential rigidity.* When hiring rules require specific credentials (specific $\bF_{\mathrm{dev}}$ configurations), agents with alternative developmental filters are excluded even when their effective profiles match the task requirements.

*Geographic mismatch.* Agents and tasks are spatially distributed, and relocation costs create friction that prevents optimal matching. The magnitude of this effect depends on the profile-space dispersion of the local talent pool versus the local task requirement distribution.

!!! example "Misallocation in technology hiring"
 \tB
A software company hires exclusively from elite computer science programs (filtering for $I_{\mathrm{symb}} > \theta_{\mathrm{high}}$ via credential proxy). The actual task requirement for most positions is a combination of $I_{\mathrm{symb}}$, $I_{\mathrm{soc}}$ (teamwork, communication), and $I_{\mathrm{eval}}$ (product judgment). By filtering on a single component, the company systematically under-weights $I_{\mathrm{soc}}$ and $I_{\mathrm{eval}}$, producing teams with suboptimal synergy despite high individual $I_{\mathrm{symb}}$. The misallocation cost is the difference between $\Syn(B_{\mathrm{actual}})$ and $\Syn(B_{\mathrm{optimal}})$, which can be substantial.

### Innovation as IdeaRank frontier

Ideas, like agents, have cognitive profiles. An idea's *requirement vector* $\bR_j$ specifies the cognitive types needed to develop, implement, and refine it. Innovation occurs when an agent (or team) with an intelligence profile matching $\bR_j$ encounters the idea and has sufficient capacity to execute.

!!! definition "Idea Price"
 \tB
The market price of an idea $j$ is proportional to the scarcity of agents capable of executing it:
\[
  p_j \propto \frac{1}{#\{i : \mathrm{score}(i,j) > \theta_j\}}.
\]
Ideas requiring rare profile combinations (high-dimensional $\bR_j$ with extreme component values) command premium prices because few agents can execute them.

This connects directly to Romer's [Romer1990] endogenous growth model. In Romer's framework, ideas are non-rival and partially excludable, and the stock of ideas drives growth. RTSG adds structure: ideas occupy a vector space indexed by their requirement profiles, and the *frontier* of innovation is the region of requirement space where capable agents are scarcest. Growth occurs when the population's profile distribution expands to cover new regions of requirement space---either through education (filter expansion), immigration (profile diversification), or AI (new cognitive types added to the accessible profile space).

% ═══════════════════════════════════════════════════════════════════════════════

## Portfolio Theory for R&D Investment

% ═══════════════════════════════════════════════════════════════════════════════

The IdeaRank framework extends naturally to a portfolio-theoretic model of R&D investment.

### Ideas as assets

Each idea $j$ in an R&D portfolio has:
[nosep]
  - An *expected return* $\mu_j = \mathbb{E}[\IdeaRank(j, t+\Delta t)] - \IdeaRank(j, t)$, the expected change in the idea's realized value.
  - A *variance* $\sigma_j^2$, the uncertainty in return due to technical risk, market uncertainty, and execution risk.
  - A *profile* $\bR_j$, the requirement vector determining which cognitive types drive the idea's success.

!!! proposition "Profile-Based Diversification"
 \tB
Two ideas $j, k$ with requirement vectors $\bR_j, \bR_k$ have return correlation bounded by
\[
  \rho_{jk} \leq \frac{\langle \bR_j, \bR_k \rangle}{\|\bR_j\| \cdot \|\bR_k\|}
\]
with equality when execution risk is purely profile-determined. Diversification benefit is maximized by investing in ideas with orthogonal requirement vectors.

This result provides a cognitive-profile interpretation of R&D diversification. A pharmaceutical company that invests only in molecule-design ideas (high $R_{\mathrm{symb}}$, $R_{\mathrm{spat}}$) has a concentrated cognitive portfolio; adding investments in patient-engagement innovation (high $R_{\mathrm{soc}}$, $R_{\mathrm{eval}}$) reduces portfolio variance by moving into orthogonal regions of requirement space.

\begin{keyeq}
**Efficient R&D frontier.**
The portfolio optimization is:
\[
  \max_{\{w_j\}} \;\sum_j w_j\,\mu_j - \frac{\gamma}{2}\sum_{j,k} w_j\,w_k\,\rho_{jk}\,\sigma_j\,\sigma_k
\]
subject to $\sum_j w_j = 1$, $w_j \geq 0$, where $\gamma$ is the risk-aversion parameter. The optimal weights $w^*_j$ trace out the efficient frontier in (expected IdeaRank return, portfolio variance) space.
\end{keyeq}

!!! remark "Remark"

Venture capital fund construction can be viewed through this lens. A fund invests in a bundle of ideas (startups), each with a requirement vector. The fund's performance depends not only on individual startup quality but on the portfolio's diversification across requirement space. Funds that concentrate in a single cognitive niche (e.g., all enterprise SaaS) bear correlated risk that profile-diversified funds avoid.

% ═══════════════════════════════════════════════════════════════════════════════

## Firm Design as Bundle Optimization

% ═══════════════════════════════════════════════════════════════════════════════

### The hiring problem

Firm assembly is a constrained bundle optimization. Given a task portfolio $\{\bR_1, \ldots, \bR_m\}$ and a labor market of available agents $\{\bI_1, \ldots, \bI_N\}$, the firm seeks the bundle $B \subset \{1, \ldots, N\}$ of size $n$ that maximizes net output:
\[
  B^* = \arg\max_{|B| = n} \left[\sum_j Y(B, \bR_j) - C_{\mathrm{coord}}(B) - C_{\mathrm{wage}}(B)\right]
\]
where $C_{\mathrm{wage}}(B) = \sum_{i \in B} w_i$ is the total wage bill. The key insight is that the synergy term in $Y$ makes this problem fundamentally different from hiring the $n$ highest-$\|\bI\|$ agents. The optimal bundle may include agents with lower individual capability if they provide high-$K$ complementarity with existing members.

!!! proposition "Submodularity of Bundle Synergy"
 \tB
Under mild regularity conditions on $\bK$ (positive semi-definiteness of the synergy matrix), the function $B \mapsto Y(B, \bR) - C_{\mathrm{coord}}(B)$ is submodular: the marginal value of adding an agent decreases as the bundle grows. Consequently, a greedy algorithm that iteratively adds the highest marginal-value agent achieves a $(1 - 1/e)$-approximation to the optimal bundle.

This result has practical implications for hiring algorithms and team assembly. It justifies a sequential hiring strategy where each new hire is evaluated not in isolation but in terms of their marginal contribution to the existing team's synergy.

### Culture fit versus culture add

The hiring debate between "culture fit" (hiring agents similar to existing team members) and "culture add" (hiring agents who bring different profiles) maps precisely onto a tension within the synergy formula.

*Culture fit* minimizes coordination cost $C_{\mathrm{coord}}$: agents with similar profiles have high pairwise $K$ and low friction. But it also limits type diversity, capping the synergy ceiling.

*Culture add* maximizes the synergy ceiling by expanding the team's profile span. But it may increase coordination costs if the new type occupies low-$K$ pairings with existing types.

\begin{modelingprinciple}[Optimal Diversity] \tB
The optimal team composition satisfies
\[
  \frac{\partial \Syn}{\partial \mathrm{diversity}} = \frac{\partial C_{\mathrm{coord}}}{\partial \mathrm{diversity}}
\]
at the margin. The answer to "fit vs.\ add" depends on the specific $\bK$ entries connecting the new type to existing types, not on a generic preference for homogeneity or diversity.
\end{modelingprinciple}

### Organizational architecture

Different organizational forms correspond to different strategies for managing the bundle synergy--coordination cost tradeoff.

*Startups* are small bundles ($n < 10$) with high type diversity relative to size, tolerating high coordination costs for maximal synergy. This predicts that startups should have higher variance in $\Syn$ than established firms: the small team amplifies both positive and negative $\bK$-interactions.

*Bureaucracies* are large bundles with low type diversity per team (high specialization), managing coordination costs through hierarchy and standardized processes. Each functional unit is approximately homogeneous in type profile, with inter-unit coordination managed by dedicated liaison roles (agents with high $I_{\mathrm{soc}}$ bridging specialist teams).

*Markets* are distributed bundles with no centralized coordination: agents self-select into tasks via price signals. The market mechanism approximates the optimal assignment $M^*$ when prices accurately reflect the $\mathrm{score}(i,j)$ function, but systematically deviates when filter-induced information asymmetries distort perceived profiles.

*Platform organizations* (e.g., Amazon, Alphabet) combine market-like internal task assignment with firm-level coordination of shared infrastructure. In RTSG terms, they maintain a large, diverse talent pool (high-dimensional bundle) with a sophisticated *hypervisor*---an allocation algorithm that routes agents to tasks based on real-time requirement vectors, reducing coordination costs below what hierarchy or pure market signals achieve.

% ═══════════════════════════════════════════════════════════════════════════════

## Discrimination as Filter Distortion

% ═══════════════════════════════════════════════════════════════════════════════

### The bias filter

Labor market discrimination takes a precise mathematical form in the filter framework.

!!! definition "Discriminatory Filter"
 \tA
A discriminatory filter $\bF_{\mathrm{bias}}$ is applied to the perceived intelligence vector of agents from a target group $G$:
\[
  \hat{\bI}_i = \bF_{\mathrm{bias}} \cdot \bI_{i,\mathrm{eff}}, \qquad i \in G,
\]
where $\bF_{\mathrm{bias}} \neq \mathbb{I}_{8 \times 8}$ is a filter that systematically attenuates certain components of the perceived profile. For agents outside group $G$, $\bF_{\mathrm{bias}} = \mathbb{I}$ (no distortion).

Several canonical forms of discrimination correspond to specific filter structures:

*Statistical discrimination* (Arrow, [Arrow1973]): The employer uses group-level priors $\bar{\bI}_G$ as a proxy for individual $\bI_i$, effectively applying a filter that shrinks individual variation toward the group mean: $\bF_{\mathrm{stat}} = (1 - \lambda)\mathbb{I} + \lambda \bar{\bI}_G \mathbf{1}^\top / \|\bar{\bI}_G\|^2$, where $\lambda \in (0,1)$ measures the degree of reliance on the group prior.

*Taste-based discrimination* (Becker, [Becker1957]): The employer applies an attenuation filter $\bF_{\mathrm{taste}} = \mathrm{diag}(d_1, \ldots, d_8)$ with some $d_t < 1$, systematically discounting the perceived capability of group $G$ members regardless of their actual profile.

*Stereotype-based filtering*: The employer applies a non-diagonal filter that not only attenuates but *redirects* perceived capability---for instance, perceiving high $I_{\mathrm{eval}}$ in a woman as $I_{\mathrm{soc}}$ ("she's good with people but not strategic"), a rotation of the perceived profile away from high-$\bK$ interactions with leadership task requirements.

\begin{keyeq}
**Economic cost of discrimination.**
The synergy loss from discriminatory filtering is:
\[
  \Delta\Syn = \Syn(B_{\mathrm{optimal}}) - \Syn(B_{\mathrm{biased}})
\]
where $B_{\mathrm{optimal}}$ is the team selected using true profiles $\bI_{\mathrm{eff}}$ and $B_{\mathrm{biased}}$ is the team selected using perceived profiles $\hat{\bI}$. This quantity is always $\geq 0$ and measures the firm-level productivity loss from discrimination in units of synergy.
\end{keyeq}

!!! proposition "Discrimination Is Costly"
 \tA
For any non-trivial discriminatory filter $\bF_{\mathrm{bias}} \neq \mathbb{I}$, the expected synergy loss satisfies $\mathbb{E}[\Delta\Syn] > 0$ whenever the excluded group contributes non-redundant profile diversity. The loss is proportional to the filter's deviation from identity and the excluded group's unique coverage of $\bK$-complementary types.

This result does not merely argue that discrimination is unfair (an ethical claim); it proves that discrimination is *economically irrational* for the discriminating firm, measured in terms of lost team synergy. The firm that discriminates systematically assembles suboptimal bundles, forgoing synergy that a meritocratic competitor would capture.

### Aggregate economic cost

At the economy level, discriminatory filters produce systematic misallocation. The aggregate cost is:
\[
  \Delta_{\mathrm{econ}} = \sum_{(i,j) \in M^*_{\mathrm{true}}} \mathrm{score}(i,j) - \sum_{(i,j) \in M^*_{\mathrm{biased}}} \mathrm{score}(i,j),
\]
the difference in total assignment quality between the optimal matching under true profiles and the optimal matching under filtered (distorted) profiles. This provides an aggregate welfare measure of discrimination that goes beyond individual wage gaps to capture the systemic synergy loss from suboptimal team formation economy-wide.

!!! example "Gender and STEM"
 \tB
If cultural filters systematically attenuate perceived $I_{\mathrm{symb}}$ and $I_{\mathrm{spat}}$ for women (stereotype-based filtering), STEM firms select teams with lower gender diversity than the optimal $B^*$ under true profiles. Since $K_{\mathrm{soc},\mathrm{symb}} > 1$ (social-symbolic synergy exists), excluding agents with high $I_{\mathrm{soc}}$ (which the diverse candidates would bring) reduces team synergy even on purely technical tasks. The misallocation cost compounds across firms to produce the aggregate welfare loss.

% ═══════════════════════════════════════════════════════════════════════════════

## Endogenous Growth with Cognitive Structure

% ═══════════════════════════════════════════════════════════════════════════════

Romer's [Romer1990] endogenous growth model treats ideas as the engine of long-run growth, with human capital $H$ determining the rate of idea production. Classical models of creative destruction [Aghion1992] emphasize the replacement of old ideas by new ones; RTSG provides micro-foundations for both processes by specifying *which* cognitive profiles produce *which* kinds of ideas.

### Structured idea production

In the standard Romer model, idea production is $\dot{A} = \delta H A^\phi$, where $H$ is aggregate human capital and $\phi$ captures knowledge spillovers. Replacing $H$ with the profile-structured aggregate:

\begin{keyeq}
**Profile-structured idea production.**
\[
  \dot{A}_j = \delta \left[\sum_i \mathrm{score}(i, j)\right] A_j^\phi, \qquad j = 1, \ldots, J,
\]
where $A_j$ indexes ideas by their requirement profile class $j$, and the effective human capital devoted to class-$j$ ideas depends on the alignment of the workforce's profile distribution with the requirement vectors in class $j$.
\end{keyeq}

This disaggregation reveals that growth is not limited by aggregate human capital but by the profile distribution's coverage of the requirement space. An economy with extremely high average $\|\bI\|$ but concentrated in a single type (e.g., all workers trained in symbolic-abstract reasoning) will have high idea production along the $I_{\mathrm{symb}}$ axis but low production in all other directions, limiting overall innovation to a narrow frontier.

### Immigration, education, and AI as profile interventions

The framework clarifies the growth effects of policy interventions:

*Education reform* modifies $\bF_{\mathrm{dev}}$ for the next generation. An educational system that emphasizes only $I_{\mathrm{ling}}$ and $I_{\mathrm{symb}}$ (the dominant Western model) produces a workforce with compressed profile diversity, constraining innovation to requirement-space regions dominated by those types.

*Immigration policy* directly modifies the population's profile distribution [Lazear1999]. Immigrants from different cultural backgrounds bring different $\bF_{\mathrm{cult}}$ configurations, expanding the profile space and enabling ideas in previously uncovered requirement regions. The RTSG framework predicts that immigration's growth contribution depends not on the average $\|\bI\|$ of immigrants (a scalar view) but on their *profile diversity* relative to the existing population.

*Artificial intelligence* adds entirely new profile configurations to the production function [Autor2015]. AI systems occupy regions of profile space inaccessible to biological agents (e.g., extremely high $I_{\mathrm{mnem}}$, high $I_{\mathrm{symb}}$ at machine scale). The growth implication is that AI does not merely substitute for human labor at lower cost---it *expands the accessible requirement space*, enabling ideas that no human team could execute regardless of size.

!!! proposition "AI Growth Contribution"
 \tB
The marginal growth contribution of an AI system with profile $\bI_{\mathrm{AI}}$ is proportional to the area of requirement space newly covered:
\[
  \Delta \dot{A} \propto \mathrm{vol}\!\left(\{\bR : \mathrm{score}(\mathrm{AI}, \bR) > \theta\} \setminus \{\bR : \max_i\, \mathrm{score}(i, \bR) > \theta\}\right),
\]
the volume of requirements satisfiable by the AI that no existing agent satisfies. AI that merely replicates existing human profiles has $\Delta\dot{A} \approx 0$ (it substitutes without expanding the frontier). AI with genuinely novel profiles has $\Delta\dot{A} > 0$ proportional to the novelty.

This provides a formal criterion for evaluating AI's economic impact: not "will AI replace jobs" (a scalar question) but "does AI expand the accessible requirement space" (a geometric question). The answer determines whether AI is substitutive (zero-sum, displacing workers) or frontier-expanding (positive-sum, enabling new categories of innovation).

% ═══════════════════════════════════════════════════════════════════════════════

## Inequality as Filter Dispersion

% ═══════════════════════════════════════════════════════════════════════════════

Income inequality in the RTSG framework is not merely a distributional outcome but a structural consequence of filter dispersion.

!!! definition "Filter Dispersion"
 \tB
The filter dispersion of a population is
\[
  D_F = \frac{1}{N^2}\sum_{i < j} \|\bF_i - \bF_j\|_F^2,
\]
where $\|\cdot\|_F$ is the Frobenius norm and $\bF_i$ is the effective filter applied to agent $i$. High $D_F$ indicates that agents face very different developmental, cultural, and institutional environments.

Two agents with identical $\bI_{\mathrm{raw}}$ but different filters $\bF_i \neq \bF_j$ produce different effective profiles and therefore receive different labor market outcomes. The income gap between them is not a "talent gap" but a *filter gap*---a structural consequence of different environmental transformations applied to the same raw endowment.

This reframes the equality-of-opportunity debate. Perfect equality of opportunity corresponds to $D_F = 0$: all agents face the same filter pipeline. The Rawlsian criterion becomes: minimize the worst-case filter attenuation across the population. Formally:
\[
  \bF^*_{\mathrm{Rawls}} = \arg\max_{\bF_{\mathrm{policy}}} \;\min_i\; \|\bF_i \circ \bF_{\mathrm{policy}}(\bI_i)\|.
\]
This is a max-min optimization over filter configurations, computable given estimates of the population's raw profile distribution and current filter environment.

% ═══════════════════════════════════════════════════════════════════════════════

## Testable Predictions

% ═══════════════════════════════════════════════════════════════════════════════

The framework generates specific, falsifiable predictions:

[nosep, label=(\arabic*)]
  - *Team composition*: Teams assembled to maximize $\Syn(B)$ given task requirements outperform teams assembled by total $\|\bI\|$ ranking, controlling for aggregate capability. Testable via randomized team assembly experiments in organizational settings.

  - *Hiring algorithms*: A matching algorithm using $\mathrm{score}(i,j) = \langle \bI_i, \bR_j \rangle \cdot \sigma(E_{i,t} - \bar{E}_t)$ should produce better job performance predictions than algorithms using scalar ability measures. Testable via A/B testing in recruitment platforms.

  - *Curriculum sequencing*: $\bK$ predicts which subject sequences facilitate learning transfer. Teaching spatial reasoning before abstract algebra ($K_{\mathrm{spat},\mathrm{symb}} > 1$) should produce better outcomes than the reverse. Testable via randomized curriculum ordering studies.

  - *Innovation diversity*: Firms and economies with greater workforce profile diversity (controlling for mean capability) should produce more patents in more diverse technology classes. Testable via patent data matched to workforce composition.

  - *Discrimination cost*: Firms with demographic hiring biases should have lower $\Syn(B)$ and lower innovation output than demographically balanced competitors, controlling for total compensation. Testable via matching firm diversity metrics to productivity and innovation data.

  - *R&D portfolios*: Venture capital funds whose portfolio companies span more diverse requirement-space regions should exhibit lower return variance and higher risk-adjusted returns. Testable via fund-level portfolio analysis.

  - *AI complementarity*: Human--AI teams should outperform either alone specifically when the AI profile occupies $\bK$-complementary types to the human team members' profiles. Testable via controlled human--AI collaboration experiments with profile-matched vs.\ profile-redundant AI assistants.

% ═══════════════════════════════════════════════════════════════════════════════

## Three-Space Economics

The three-space ontology (Part XIII) deepens the economic interpretation of cognitive capital.

**Ideas as instantiated $\QS$-structure.**  In the three-space framework, an idea is a $\QS$-configuration that has been instantiated into $\PS$ through conscious effort.  Economic value arises when instantiation produces $\PS$-structures that satisfy human needs or desires.  The "production function" of an economy is its aggregate instantiation capacity: how effectively its population can project $\QS$-potentiality into useful $\PS$-configurations.

**Innovation as novel instantiation.**  Schumpeterian creative destruction corresponds to $E_2$ emergence in the filter formalism: the assembly of cognitive profiles that jointly instantiate $\QS$-regions no individual member can access alone.  This explains why innovation clusters around diverse teams (Silicon Valley, Renaissance Florence): diversity of intelligence profiles expands the team's total instantiation capacity.

**Discrimination as instantiation waste.**  When bias filters exclude individuals from economic participation based on characteristics uncorrelated with their intelligence profile, the economy loses access to their instantiation capacity.  The aggregate cost of discrimination is the volume of $\QS$-structure that remains un-instantiated because the individuals who could have projected it were filtered out.  This provides a formal measure of the economic cost of discrimination that goes beyond wage gaps to the loss of potential ideas and innovations.

**Inequality as filter dispersion.**  Economic inequality maps to dispersion in developmental and cultural filter parameters across a population.  When filter chains are highly dispersed (some individuals have $d_t \approx 1$ across all types while others have $d_t \approx 0$ in several types), the economy underutilizes its cognitive capital.  The optimal policy minimizes unnecessary filter dispersion while preserving the cognitive diversity that expands collective instantiation capacity.

## Discussion

% ═══════════════════════════════════════════════════════════════════════════════

### Contributions

This paper introduces four structural enrichments to the economic theory of human capital and knowledge production. The intelligence vector replaces the scalar with an eight-dimensional profile that preserves the information determining comparative advantage, team complementarity, and innovation potential. The compatibility matrix provides the missing interaction structure for team production: whether diversity helps or hurts depends on $\bK$, not on a generic preference. The IdeaRank assignment market formalizes labor market efficiency as a matching problem with closed-form optimality conditions. And the filter formalism provides a unified mathematical language for discrimination, inequality, and institutional design.

### Relation to existing work

The framework builds on and extends several established research programs.

Becker's [Becker1964] human capital theory is recovered as the scalar projection $h = \|\bI_{\mathrm{eff}}\|$, preserving its insights while adding dimensional structure. Romer's [Romer1990] endogenous growth model is enriched with profile-structured idea production, explaining why aggregate human capital alone does not determine growth rates. Coase's [Coase1937] theory of the firm is given algebraic content: firm boundaries are the surfaces where marginal synergy equals marginal coordination cost. Page's [Page2007] diversity-trumps-ability theorem is formalized with the critical $\bK$-compatibility qualification.

The assignment market structure connects to Koopmans and Beckmann's [Koopmans1957] classical work on optimal assignment and to more recent developments in two-sided matching (Roth, [Roth2002]). The portfolio theory for R&D investment extends Markowitz [Markowitz1952] by providing cognitive-profile foundations for return correlation.

### Limitations

The framework's empirical applicability depends on solving two measurement problems. First, the intelligence vector $\bI$ must be estimable from observable data. The RTSG monograph proposes ELO tournaments as a calibration mechanism, but large-scale implementation in labor market settings remains an open challenge. Second, the compatibility matrix $\bK$ must be estimated from interaction data, which requires longitudinal observations of cross-type collaboration outcomes.

The pairwise approximation in the synergy formula captures first-order interactions but may miss higher-order effects (three-way or four-way cognitive interactions). The RTSG monograph addresses this via the full compatibility tensor $\boldsymbol{\Omega}$, but the economic applications in this paper use only the matrix $\bK$ for tractability.

The filter formalism assumes linearity, which is a modeling simplification. Real filters may have nonlinear effects---for instance, developmental deprivation may interact multiplicatively rather than additively with cultural filtering. The RTSG framework provides a deeper topological treatment (the Conceptual Irreversibility Theorem) that captures these nonlinearities, but the linear approximation suffices for the economic applications developed here.

### Implications for policy

The framework suggests several policy implications. Education policy should optimize for profile diversity across the population, not merely for aggregate $\|\bI\|$: a workforce with diverse profiles covers more of the idea requirement space and generates higher synergy potential. Immigration policy should be evaluated by the profile diversity immigrants contribute, not by scalar skill metrics. Anti-discrimination policy should be understood not only as an equity measure but as an efficiency intervention: removing bias filters allows the labor market to assemble higher-synergy teams.

Corporate governance should evaluate team composition using synergy metrics that account for $\bK$-compatibility, not merely individual performance scores. R&D investment should be diversified across cognitive-profile dimensions, not merely across industries or technologies.

Most fundamentally, the framework suggests that the central economic question is not "how much human capital does the economy have?" but "what is the geometric structure of the economy's cognitive profile distribution, and how well does the assignment market exploit that structure?" The answer determines innovation capacity, productivity growth, and the economic gains from diversity.

% ═══════════════════════════════════════════════════════════════════════════════
% BIBLIOGRAPHY
% ═══════════════════════════════════════════════════════════════════════════════

## References

*See PDF for full bibliography.*
---

## v2 Integration: GNEP Cooperative Nash & Federated Nodes (TMP-20260217)

**GNEP at societal scale:** Each economic agent = GNEP hypervisor node. Optimization variable = maximize total life force (cooperative Nash, not competitive). No agent can increase total life force by unilateral deviation.

The Id_extended equilibrium formally:
$$\text{Id}_{\text{extended}}: \max \sum_{\text{all agents } \alpha} \text{persistence}(\alpha)$$

**Federated node properties:** full information (shared ledger), equal vote weight, odd-number deciding bodies (no ties), minimal elliptic-curve cryptographic consensus. Conflict resolution: flag → isolate → re-integrate or exile from consensus network.

This is categorically distinct from classical game theory: life force is not partitioned per agent. It is one global quantity.

---

## Extended Formalizations *(v2 — 2026)*

### Coase's Theory of the Firm — Algebraically

Firms exist because bundle synergy within a coordinated organization exceeds market-mediated synergy between independent agents. The firm boundary is the surface where marginal synergy gain from adding the next member equals marginal coordination cost.

**Transaction costs are low-K friction costs** — the difficulty of integrating cognitive types across organizational boundaries. The Coasean prediction that firms grow until internal coordination costs equal market transaction costs is a special case of ∂Y_net/∂n = 0.

### Romer Growth Model + RTSG Frontier Expansion

Romer's (1990) endogenous growth model holds that ideas are non-rival and partially excludable, and the stock of ideas drives growth. RTSG adds structure: ideas occupy a vector space indexed by their requirement profiles. The *frontier* of innovation is the region of requirement space where capable agents are scarcest.

Growth occurs when the population's profile distribution expands to cover new regions of requirement space — through education (filter expansion), immigration (profile diversification), or AI (new cognitive types added to the accessible profile space). IdeaRank's frontier expansion algorithm formalizes this directly.

### Statistical Discrimination Formalized

Arrow's (1973) statistical discrimination — using group-level priors as proxy for individual capacity — maps to a filter shrinkage operator:

$$\mathbf{F}_{\text{stat}} = (1-\lambda)\mathbb{I} + \lambda\,\bar{\mathbf{I}}_G\,\mathbf{1}^\top / \|\bar{\mathbf{I}}_G\|^2$$

where λ ∈ (0,1) measures reliance on the group prior. At λ = 1, individuals are reduced to group means. At λ = 0, pure individual assessment. Statistical discrimination is the application of a non-identity filter to individual intelligence vectors — a measurable, correctable distortion.

### Human Capital Externalities as Filter Contagion

Human capital externalities (Lucas 1988; Moretti 2004) become interaction effects: an agent's filter environment depends on the profiles of surrounding agents. Living in a city with high average I_M (mathematical) doesn't just raise the mean — it changes the Φ_inst filter available to all residents through institutions, discourse norms, and ambient intellectual culture. The externality is filter transmission.
