---
title: "Thread 1 — IdeaRank Portfolio"
version: "2.0.0"
last_updated: "2026-03-05"
status: CURRENT
---

# Thread 1 — IdeaRank Portfolio

**Jean-Paul Niko** · February 2026

\fi

%═══════════════════════════════════════════════════════════════════════════════

## Introduction: Ideas as Financial Assets

%═══════════════════════════════════════════════════════════════════════════════

In Parts II--III and the Ideometrics paper, we established that ideas are formal
objects in the conceptual topos $\mathbf{C}_{\mathrm{co}}$, each characterized
by four measures: depth $\delta$, novelty $\nu$, utility $u$, and intelligence
profile $\mathbf{R}$.  IdeaRank assigns a scalar importance to each idea based
on its position in the global idea graph $\mathcal{G}$.

We now observe that the structure of cognitive investment---allocating finite
attention and intelligence-time across a portfolio of ideas---is formally
identical to the structure of financial portfolio theory.  An agent with
bounded cognitive resources must choose *which ideas to invest in*,
*how deeply*, and *in what combination*.  The returns are stochastic
(an idea may prove more or less valuable than anticipated), and ideas are
correlated (investing in group theory and topology yields synergistic returns).

This section develops the correspondence rigorously, proves three new theorems,
and connects the portfolio formalism back to the filter pipeline and the
compatibility tensor $\bK$.

%═══════════════════════════════════════════════════════════════════════════════

### Three-Space Grounding of Portfolio Theory

The three-space ontology (Part XIII) gives idea portfolio theory a deeper foundation.  Foundation ideas---those with highest IdeaRank---are *convergence conditions*: $\QS$-structures whose instantiation is prerequisite for accessing more complex $\QS$-regions.  The efficient frontier of knowledge is thus not merely a mathematical analogy but reflects the actual geometry of $\QS$: there exist optimal paths through the space of convergence conditions, and deviation from these paths wastes instantiation capacity.

The Kelly criterion for intellectual investment becomes: allocate cognitive resources to the idea whose instantiation maximizes expected access to new $\QS$-regions.  Risk is the probability that the instantiation fails (the idea turns out to be wrong or the agent lacks the filter profile to instantiate it).  Return is the volume of newly accessible $\QS$-structure.

## The Idea Market

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Cognitive Asset"
 \tA\;
Let $\mathcal{G} = (V, E)$ be the global idea graph.  A *cognitive asset*
is an idea $\iota \in V$ together with:
[nosep]
  - **Expected return**: $\mu_\iota = \E[r_\iota]$, the expected
    cognitive return from investing attention in idea $\iota$.  Concretely:
    \[
      r_\iota = \Delta u(\iota, a, t) = u(\iota, a, t + \Delta t) - u(\iota, a, t)
    \]
    where $u$ is the utility function from the ideometrics paper
    (Def. 3.5), evaluated for agent $a$ over investment period $\Delta t$.
  - **Risk**: $\sigma^2_\iota = \Var[r_\iota]$, the variance of
    cognitive return.  High-risk ideas include radical conjectures (high
    upside, high probability of dead end) and novel domains (high variance
    in realized utility).
  - **Investment cost**: $c_\iota \in \R_{>0}$, the
    intelligence-time (cog$\cdot$hr) required for meaningful engagement.
    This is the minimum cognitive expenditure to change the agent's
    posterior over $\iota$.

!!! definition "Cognitive Return"
 \tA\;

The *cognitive return* of idea $\iota$ for agent $a$ with intelligence
vector $\bI_a$ is:
\begin{keyeq}
\[
r_\iota(a) = \frac{\Delta u(\iota, a)}{c_\iota}
= \frac{u_{\mathrm{post}}(\iota, a) - u_{\mathrm{prior}}(\iota, a)}
       {\int_0^{\Delta t} \langle \bI_a(s), \mathbf{R}_\iota \rangle \, ds}
\]
\end{keyeq}
where $\mathbf{R}_\iota$ is the intelligence requirement vector of the idea
and $\langle \cdot, \cdot \rangle$ is the $\bK$-inner product
(Def. 3.1 of Part I).  The denominator is the realized cognitive work:
intelligence committed weighted by compatibility.

\begin{interpretation}
This is the "return on cognitive investment" (ROCI).  A mathematician
investing in a group theory paper has low cost (high $I_{\mathrm{symb}}$
matches $R_{\mathrm{symb}}$) and potentially high return (new tools for
existing problems).  The same mathematician investing in social psychology
has higher cost (mismatch) and uncertain return.
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════

## Portfolio Construction

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Idea Portfolio"
 \tA\;
An *idea portfolio* for agent $a$ is a weight vector
$\bw = (w_1, \ldots, w_N) \in \Delta^{N-1}$ over a universe of $N$
cognitive assets, where $w_i$ is the fraction of total available
intelligence-time allocated to idea $\iota_i$.

The constraint $\bw \in \Delta^{N-1}$ (the probability simplex) is the
*attention budget constraint*: the agent cannot invest more total
attention than it has.  This is the portfolio-theoretic restatement of
the attention simplex constraint from Part III.

!!! remark "Remark"

The connection is precise: the attention simplex $\Delta^{n-1}$ from Part III
allocates attention across *intelligence types*; the portfolio simplex
$\Delta^{N-1}$ allocates attention across *ideas*.  The two are related
by the requirement vectors $\mathbf{R}_\iota$: an allocation across ideas
*induces* an allocation across intelligence types via
$\lambda_\tau = \sum_{i} w_i \cdot R_{\iota_i, \tau}$ (normalized).

!!! definition "Portfolio Return and Risk"
 \tA\;
For portfolio $\bw$:
\begin{keyeq}

\[\begin{aligned}
\mu_{\bw} &= \bw^\top \bmu = \sum_{i=1}^N w_i \mu_i
       [6pt]
\sigma^2_{\bw} &= \bw^\top \Sigma \bw = \sum_{i,j} w_i w_j \sigma_{ij}
    
\end{aligned}\]

\end{keyeq}
where $\bmu = (\mu_1, \ldots, \mu_N)^\top$ is the vector of expected
cognitive returns and $\Sigma \in \R^{N \times N}$ is the
*idea covariance matrix* with entries
$\sigma_{ij} = \Cov[r_i, r_j]$.

!!! definition "Idea Covariance via $\bK$"
 \tB\;

The covariance between ideas $\iota_i$ and $\iota_j$ has two sources:
\begin{keyeq}
\[
\Sigma_{ij} = \underbrace{\mathbf{R}_i^\top \bK \, \mathbf{R}_j}_{\text{type-synergy covariance}}
+ \underbrace{\gamma \cdot \mathbf{1}[\iota_i \to \iota_j \text{ or } \iota_j \to \iota_i]}_{\text{graph proximity covariance}}
\]
\end{keyeq}
The first term captures that ideas requiring similar intelligence profiles
covary through the compatibility tensor.  The second term captures that
ideas connected in the idea graph $\mathcal{G}$ (prerequisite or extension
relationships) share structural dependency.  The parameter $\gamma > 0$
scales the graph contribution.

\begin{interpretation}
Learning group theory and ring theory covary highly (both require
$I_{\mathrm{symb}}$, and they share prerequisites).  Learning group theory
and playing piano covary less (orthogonal type profiles, distant in
$\mathcal{G}$).  A well-diversified cognitive portfolio spreads investment
across ideas with low $\Sigma_{ij}$, just as a financial portfolio diversifies
across uncorrelated assets.
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════

## Markowitz Mean-Variance Optimization

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Cognitive Efficient Frontier"
 \tA\;
The *cognitive efficient frontier* is the set of portfolios solving:
\begin{keyeq}
\[
\min_{\bw \in \Delta^{N-1}} \; \bw^\top \Sigma \bw
\quad \text{subject to} \quad \bw^\top \bmu \geq \mu_0
\]
\end{keyeq}
for each target return $\mu_0 \in [\mu_{\min}, \mu_{\max}]$.
Equivalently, these are the portfolios maximizing return for each level
of risk.

!!! theorem "Existence of the Cognitive Efficient Frontier"
 \tA\;

If $\Sigma$ is positive definite and $\bmu$ is not proportional to $\mathbf{1}$,
then the cognitive efficient frontier is a parabola in
$(\sigma_{\bw}, \mu_{\bw})$-space, parameterized by:
\[
\sigma^2_{\bw}(\mu_0) = \frac{A \mu_0^2 - 2B\mu_0 + C}{AC - B^2}
\]
where $A = \mathbf{1}^\top \Sigma^{-1} \mathbf{1}$,
$B = \mathbf{1}^\top \Sigma^{-1} \bmu$,
$C = \bmu^\top \Sigma^{-1} \bmu$.

??? proof "Proof"

This is the standard Markowitz result applied to the cognitive setting.
The Lagrangian for the constrained minimization is:
$\mathcal{L} = \bw^\top \Sigma \bw
  - \lambda_1 (\bw^\top \bmu - \mu_0)
  - \lambda_2 (\bw^\top \mathbf{1} - 1)$.
Setting $\nabla_{\bw} \mathcal{L} = 0$ gives
$\bw^* = \frac{1}{2}\Sigma^{-1}(\lambda_1 \bmu + \lambda_2 \mathbf{1})$.
The two constraints yield a $2 \times 2$ system for $(\lambda_1, \lambda_2)$
in terms of $A, B, C$.  Substituting back gives the parabolic form.
Positive definiteness of $\Sigma$ ensures the minimum is unique; the
non-proportionality condition ensures the frontier is not degenerate
(a single point).

!!! corollary "Minimum-Variance Cognitive Portfolio"
 \tA\;
The *minimum-variance portfolio* (MVP) is:
\[
\bw_{\mathrm{MVP}} = \frac{\Sigma^{-1} \mathbf{1}}{\mathbf{1}^\top \Sigma^{-1} \mathbf{1}}
\]
This is the "safest" cognitive strategy: maximum diversification across ideas,
minimizing the total uncertainty in realized cognitive returns.

\begin{interpretation}
The MVP corresponds to the generalist strategy: spreading cognitive investment
evenly across maximally diverse ideas.  An agent on the efficient frontier
above the MVP is a *specialist*: accepting more risk (variance in
cognitive payoff) for higher expected returns.  The entire history of
academic disciplines can be read as a collective movement along the
efficient frontier, with specialization increasing as the idea graph grows
and covariance structure becomes richer.
\end{interpretation}

!!! definition "Cognitive Sharpe Ratio"
 \tB\;

The *cognitive Sharpe ratio* of portfolio $\bw$ is:
\begin{keyeq}
\[
S_{\bw} = \frac{\mu_{\bw} - r_f}{\sigma_{\bw}}
\]
\end{keyeq}
where $r_f$ is the *risk-free cognitive return*---the return from
routine maintenance cognition (habitual tasks, already-known material).
The tangency portfolio maximizing $S_{\bw}$ is the optimal risky
cognitive portfolio.

%═══════════════════════════════════════════════════════════════════════════════

## Kelly Criterion for Cognitive Betting

%═══════════════════════════════════════════════════════════════════════════════

The Markowitz framework optimizes a single-period trade-off between return
and risk.  For *sequential* cognitive investment---where returns compound
and the agent reinvests cognitive capital---the Kelly criterion provides the
growth-optimal allocation.

!!! definition "Cognitive Wealth"
 \tB\;
The *cognitive wealth* of agent $a$ at time $t$ is:
\[
W(t) = \sum_{\iota \in V_a(t)} u(\iota, a, t)
\]
where $V_a(t) \subset V$ is the set of ideas the agent has invested in
up to time $t$.  Cognitive wealth grows as ideas yield returns and
decays as knowledge becomes obsolete (the temporal decay of
Dynamic IdeaRank).

!!! theorem "Kelly Criterion for Ideas"
 \tB\;

For an agent with log-utility over cognitive wealth, the growth-optimal
portfolio satisfies:
\begin{keyeq}
\[
\bw^*_{\mathrm{Kelly}} = \Sigma^{-1} (\bmu - r_f \mathbf{1})
\]
\end{keyeq}
This maximizes $\E[\log W(t+1)]$, the expected log-growth of cognitive wealth.

??? proof "Proof"

The log-growth rate of the portfolio is:
\[
g(\bw) = \E[\log(1 + r_{\bw})]
\approx \bw^\top \bmu - r_f - \frac{1}{2} \bw^\top \Sigma \bw
\]
using the second-order Taylor expansion for small returns (appropriate
for incremental cognitive investments).  The first-order condition
$\nabla_{\bw} g = \bmu - r_f \mathbf{1} - \Sigma \bw = 0$ yields
the result.  The Hessian $-\Sigma$ is negative definite, confirming
the maximum.

!!! remark "Kelly vs.\ Markowitz"

The Kelly portfolio is typically more concentrated than the Markowitz
tangency portfolio because it maximizes long-run growth rather than
single-period risk-adjusted return.  In cognitive terms: the Kelly-optimal
agent is a *bold specialist*, willing to tolerate short-term variance
for maximum compound growth.  The Markowitz agent is more conservative,
hedging against bad periods.

The "fractional Kelly" $\bw = f \cdot \bw^*_{\mathrm{Kelly}}$ with
$f \in (0, 1)$ provides a continuum between the two strategies, and
corresponds to a cognitive risk aversion parameter.

!!! example "The Graduate Student's Dilemma"
 \tB\;
A mathematics graduate student has ideas
$\{\iota_1 = \text{thesis problem}, \iota_2 = \text{adjacent conjecture},
  \iota_3 = \text{applied collaboration}\}$ with:
\[
\bmu = \begin{pmatrix} 0.8    0.3    0.5 \end{pmatrix}, \quad
\Sigma = \begin{pmatrix}
0.25 & 0.15 & 0.05   
0.15 & 0.20 & 0.02   
0.05 & 0.02 & 0.10
\end{pmatrix}, \quad r_f = 0.1
\]
The Kelly portfolio is:
$\bw^*_{\mathrm{Kelly}} = \Sigma^{-1}(\bmu - 0.1 \cdot \mathbf{1})
\propto (0.54, 0.12, 0.34)$ (after normalization to $\Delta^2$).

Interpretation: invest 54% of cognitive time in the thesis, 34% in the
applied collaboration (high diversification benefit from low correlation),
and only 12% in the adjacent conjecture (too correlated with the thesis
to provide much marginal value).

%═══════════════════════════════════════════════════════════════════════════════

## The Filter--Portfolio Connection

%═══════════════════════════════════════════════════════════════════════════════

The filter formalism from the Filter Paper directly modifies the portfolio
problem through the effective intelligence vector.

!!! proposition "Filter-Adjusted Returns"
 \tA\;

Under the full filter pipeline
$\bI_{\mathrm{eff}} = \lambda \odot \eta(\Psi) \odot (\mathrm{Id} + A)
  \cdot \mathrm{diag}(d) \cdot \min(\bI_{\mathrm{raw}}, \bI_{\max})$,
the cognitive return of idea $\iota$ becomes:
\begin{keyeq}
\[
r_\iota^{\mathrm{filtered}}(a) = \frac{\Delta u(\iota, a)}
  {\int_0^{\Delta t} \langle \bI_{\mathrm{eff}}(s), \mathbf{R}_\iota \rangle_{\bK} \, ds}
\]
\end{keyeq}
The filter pipeline affects the *denominator* (effective cognitive cost),
not the numerator (utility gained).  When $\bI_{\mathrm{eff}} < \bI_{\mathrm{raw}}$
(typical: filters reduce capacity), costs increase and returns decrease.

??? proof "Proof"

The cognitive work integral $\int \langle \bI, \mathbf{R} \rangle_{\bK} \, ds$
measures the actual intelligence deployed against the requirement.  Under
filtering, the deployed intelligence is $\bI_{\mathrm{eff}}$, not
$\bI_{\mathrm{raw}}$.  The utility gained $\Delta u$ depends on the
agent's *learning* (which may be less efficient under filtering) but
is fundamentally about the change in the agent's knowledge state, which is
measured by the ideometric utility function independently of how that state
was reached.  The cost, however, is directly proportional to the effective
intelligence available.

!!! corollary "Filter-Shifted Efficient Frontier"
 \tB\;
Filtering shifts the entire efficient frontier *down and to the right*:
returns decrease (higher denominator in ROCI) and risk increases
(filter-induced variance in $\bI_{\mathrm{eff}}$ propagates into return
variance).  Specifically, if the somatic filter $\Phi_{\mathrm{som}}$
has random component $\epsilon \sim \mathcal{N}(0, \sigma_{\mathrm{som}}^2)$,
the portfolio variance inflates by:
\[
\Sigma^{\mathrm{filtered}} = \Sigma + \sigma_{\mathrm{som}}^2 \cdot
\mathbf{R} \mathbf{R}^\top
\]
where $\mathbf{R} = (\mathbf{R}_1, \ldots, \mathbf{R}_N)$ is the matrix
of requirement vectors.

\begin{interpretation}
A tired, stressed, or ill agent faces a *worse* efficient frontier than
a rested, calm, healthy one.  This is the portfolio-theoretic restatement of
what the somatic and affective filters already describe: biological state
degrades cognitive performance.  The portfolio lens adds the insight that
the degradation is *not uniform across ideas*---ideas requiring
intelligence types most affected by the filter suffer the largest return
decrease.  The optimal portfolio under filtering is therefore different from
the optimal portfolio at baseline: it shifts toward ideas that are
"filter-robust" (low sensitivity to the degraded types).
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════

## IdeaRank as Market Capitalization

%═══════════════════════════════════════════════════════════════════════════════

!!! proposition "IdeaRank--Capitalization Correspondence"
 \tB\;

In the market analogy, IdeaRank is the analogue of market capitalization:
\begin{keyeq}
\[
\IdeaRank(\iota) \longleftrightarrow \text{Market Cap}(\text{asset})
\]
\end{keyeq}
Specifically:
[nosep]
  - The *market-cap weighted portfolio*
    $w_i \propto \IdeaRank(\iota_i)$ is the cognitive analogue of
    an index fund: invest in ideas proportional to their global importance.
  - The *equal-weighted portfolio* $w_i = 1/N$ is the cognitive
    analogue of diversified exposure without importance-weighting.
  - *Active management* corresponds to deviating from the
    IdeaRank-weighted portfolio based on private information (the agent's
    unique intelligence profile, utility function, or filter state).

!!! theorem "Cognitive Market Efficiency"
 \tB\;

The idea market is *weakly efficient* in the following sense: if all
agents have identical intelligence vectors $\bI$, identical filter states,
and access to the same idea graph $\mathcal{G}$, then the IdeaRank-weighted
portfolio is mean-variance optimal for all agents.  Equivalently:
*there are no excess cognitive returns from active management when
agents are homogeneous*.

Formally: let $\bw_{\mathrm{IR}}$ be the IdeaRank-weighted portfolio and
$\bw^*$ be the Markowitz-optimal portfolio for a representative agent.
If $\bI_a = \bI$ and $\Phi_a = \Phi$ for all agents $a$, then
$\bw_{\mathrm{IR}} = \bw^*$.

??? proof "Proof"

Under homogeneity, all agents compute the same expected returns $\mu_i$
(identical utility functions and intelligence profiles) and the same
covariances $\Sigma_{ij}$ (identical filter states and graph access).
The equilibrium portfolio weights in a homogeneous market are proportional
to the asset "float"---here, the idea's importance in the network, which
is exactly $\IdeaRank(\iota_i)$.

More precisely: in a CAPM equilibrium, the market portfolio is
mean-variance efficient.  The "market portfolio" in idea space is
the aggregate of all agents' holdings, which under homogeneity is
proportional to $\IdeaRank$ (since IdeaRank is the fixed point of
the collective attention flow on $\mathcal{G}$).

!!! corollary "Source of Cognitive Alpha"
 \tB\;
Active management outperforms the IdeaRank-weighted portfolio if and only
if the agent has *heterogeneous* intelligence, filter state, or
information.  The "cognitive alpha" is:
\[
\alpha_a = \mu_{\bw_a} - \mu_{\bw_{\mathrm{IR}}}
  = \bw_a^\top \bmu_a - \bw_{\mathrm{IR}}^\top \bmu_a
  = (\bw_a - \bw_{\mathrm{IR}})^\top \bmu_a
\]
This is positive when the agent tilts toward ideas where its
*private* expected returns exceed the market-implied returns.

\begin{interpretation}
The corollary formalizes why *individual differences matter* in
intellectual life.  A musician investing in music theory has positive
cognitive alpha not because the ideas are objectively "better," but
because the musician's intelligence profile ($I_{\mathrm{aud}}$ dominant)
makes the returns higher for that particular agent.  The intelligence
vector is the source of cognitive alpha: each agent's unique profile
creates private mispricing relative to the market-cap portfolio.
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════

## Factor Models and Cognitive Beta

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Intelligence-Type Factors"
 \tB\;
Define eight *intelligence-type factor portfolios*
$\bw_\tau$ for $\tau \in \mathcal{T}$ by:
\[
w_{\tau, i} \propto R_{\iota_i, \tau}
\]
i.e., the $\tau$-factor portfolio overweights ideas that load heavily on
intelligence type $\tau$.  Then every idea's return admits a factor
decomposition:
\begin{keyeq}
\[
r_\iota = \alpha_\iota + \sum_{\tau \in \mathcal{T}} \beta_{\iota,\tau} \cdot F_\tau + \epsilon_\iota
\]
\end{keyeq}
where $F_\tau$ is the return of the $\tau$-factor portfolio and
$\beta_{\iota,\tau}$ is the idea's *cognitive beta* with respect
to type $\tau$.

!!! proposition "Cognitive CAPM"
 \tB\;
Under the assumptions of Theorem *ref:thm:cog-efficiency*, the expected
return of any idea satisfies:
\[
\mu_\iota - r_f = \sum_{\tau \in \mathcal{T}} \beta_{\iota,\tau}
  \cdot (\mu_{F_\tau} - r_f)
\]
Ideas with high beta to a particular intelligence type command a
*risk premium* proportional to the market price of that type's
systematic risk.

\begin{interpretation}
This is a cognitive asset pricing model.  Ideas requiring rare intelligence
types (high $R_{\mathrm{kin}}$ in a population of sedentary scholars)
command a premium: the "supply" of cognitive capital in that type is
scarce, so the market-clearing return must be higher.  Conversely, ideas
loading on abundant types ($R_{\mathrm{ling}}$ in a literate population)
have lower premiums.  The compatibility tensor $\bK$ enters through the
factor covariance structure: cross-type synergy means that factor returns
are themselves correlated.
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════

## Portfolio Rebalancing as Attention Dynamics

%═══════════════════════════════════════════════════════════════════════════════

!!! theorem "Rebalancing--Replicator Equivalence"
 \tA\;

The continuous-time rebalancing dynamics of the idea portfolio are:
\begin{keyeq}
\[
\dot{w}_i = w_i \left( r_i - \bar{r} \right)
+ w_i \sum_j \frac{\partial^2 g}{\partial w_i \partial w_j}
  (r_j - \bar{r})
\]
\end{keyeq}
where $\bar{r} = \sum_j w_j r_j$ is the portfolio return and $g = \E[\log W]$
is the Kelly growth rate.  In the limit of small returns, the first term
dominates, and the dynamics reduce to the *replicator equation*
from Part III:
\[
\dot{w}_i = w_i (r_i - \bar{r})
\]
Ideas with above-average returns grow in portfolio weight; ideas with
below-average returns shrink.

??? proof "Proof"

The continuous-time Kelly criterion maximizes
$g(\bw) = \E[\log(1 + \bw^\top \mathbf{r})]$.
The gradient ascent dynamics are $\dot{w}_i = w_i \cdot \partial g / \partial w_i$
(multiplicative dynamics to preserve $\bw \in \Delta^{N-1}$).
Computing:
\[
\frac{\partial g}{\partial w_i}
= \E\!\left[\frac{r_i}{1 + \bw^\top \mathbf{r}}\right]
\approx \E[r_i] - \bw^\top \E[\mathbf{r}] \cdot \E[r_i] + O(r^2)
= r_i - \bar{r} + O(r^2)
\]
The zeroth-order term gives the replicator equation.  The second-order
corrections involve the Hessian $\partial^2 g / \partial w_i \partial w_j$,
which accounts for the covariance structure and prevents the dynamics
from converging to a degenerate portfolio (all weight on a single idea).

\begin{interpretation}
The replicator dynamics of Part III (attention allocation across intelligence
types) and the portfolio rebalancing dynamics (attention allocation across
ideas) share the same mathematical structure.  Both are instances of
*selection dynamics on the simplex*: ideas/types that perform above
average grow; those below average shrink.  The portfolio formalism adds
the covariance-correction term, which acts as an endogenous diversification
force absent from the pure replicator equation.  This is the formal link
between the attention simplex and the efficient frontier.
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════

## Summary of Results

%═══════════════════════════════════════════════════════════════════════════════

\begin{portbox}[Thread 1: New Results]
[nosep,leftmargin=1.5em]
  - **Theorem *ref:thm:eff-frontier*** (Tier A): Existence and
    parabolic form of the cognitive efficient frontier.
  - **Theorem *ref:thm:kelly*** (Tier B): Kelly criterion for
    growth-optimal idea allocation.
  - **Theorem *ref:thm:cog-efficiency*** (Tier B): IdeaRank as
    equilibrium portfolio under homogeneity (cognitive market efficiency).
  - **Theorem *ref:thm:rebalance-replicator*** (Tier A):
    Portfolio rebalancing $\equiv$ replicator dynamics on the idea simplex.
  - **Proposition *ref:prop:filter-adj*** (Tier A): Filter pipeline
    modifies portfolio problem through effective costs.
  - **Definition *ref:def:idea-cov*** (Tier B): Idea covariance
    matrix constructed from $\bK$ and graph structure.
  - **Definition *ref:def:sharpe*** (Tier B): Cognitive Sharpe ratio.

\end{portbox}

\ifx\STANDALONE\undefined
\else