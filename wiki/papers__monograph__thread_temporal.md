---
title: "Thread 4 — Temporal Dynamics"
version: "2.0.0"
last_updated: "2026-03-05"
status: CURRENT
---

# Thread 4 — Temporal Dynamics

**Jean-Paul Niko** · February 2026

\fi

%═══════════════════════════════════════════════════════════════════════════════

## Introduction: The Dynamics of Ideas

%═══════════════════════════════════════════════════════════════════════════════

The Ideometrics paper defined Dynamic IdeaRank with temporal decay
$\IdeaRank(i, t) \propto \sum_{j \to i} \IdeaRank(j, t) \cdot
e^{-\kappa(t - t_j)} / \mathrm{out}(j, t)$ and Thread 1 developed the
portfolio-theoretic treatment.  This thread builds the full temporal
theory: ideas as stochastic processes, the idea lifecycle (birth, growth,
maturity, obsolescence), cultural evolution as time-varying filters on the
idea graph, and the connection between temporal dynamics and the existing
mathematical apparatus.

The central claim: *the time-evolution of the idea graph is a
filtered diffusion process on a growing random graph, and the filter
pipeline determines which ideas survive.*

%═══════════════════════════════════════════════════════════════════════════════

### Three Temporal Structures

The three-space ontology (Part XIII) reveals that the single time parameter $t$ used throughout the IAG framework conceals three fundamentally different temporal structures:

\begin{interpretation}
**Quantum time** ($t_\QS$): reversible, symmetric under $t \to -t$.  The Schr\"odinger equation preserves inner products in both temporal directions.  In the idea graph, quantum time governs the *potentiality* of ideas---the space of possible future developments that exists in superposition before instantiation.

**Physical time** ($t_\mathbb{R}$): irreversible, carries the thermodynamic arrow.  In the idea graph, physical time is the clock on which the idea lifecycle (birth, growth, maturity, obsolescence) is measured.  The "age" of an idea is its $t_\mathbb{R}$-duration since instantiation.

**Consciousness time** ($t_\CSp = t_\mathbb{R} + i\,t_{\mathrm{lat}}$): complex-valued.  The real part is physical time; the imaginary part $t_{\mathrm{lat}}$ is *lateral time*---the freedom of consciousness to navigate outside the $t_\mathbb{R}$ direction.  Insight, creativity, and idea recombination correspond to movement in the $t_{\mathrm{lat}}$ direction: reaching across $t_\mathbb{R}$-separated ideas to forge new connections.

The arrow of time---the fact that $t_\mathbb{R}$ flows in one direction---is not fundamental but *accumulated*: each instantiation event is irreversible ($\Inst^{-1}$ does not exist), and the macroscopic arrow is the statistical accumulation of $\sim 10^{40}$ instantiation events per second across the physical universe.  Entropy increases because instantiation count increases, not the other way around.
\end{interpretation}

!!! remark "Remark"

The idea lifecycle equation (Section *ref:sec:lifecycle*) is a $t_\mathbb{R}$-equation: it tracks how ideas age in physical time.  The Idea Revival Theorem (Section *ref:sec:revival*) is a $t_\CSp$-theorem: revival occurs when a consciousness navigates laterally in $t_{\mathrm{lat}}$ to reconnect an obsolescent idea to a new context.  The distinction resolves a puzzle: how can "dead" ideas revive?  In $t_\mathbb{R}$, they cannot---obsolescence is irreversible.  In $t_\CSp$, they can---consciousness reaches laterally across physical time to re-instantiate the idea in a new configuration.

%═══════════════════════════════════════════════════════════════════════════════

## Idea Stochastic Processes

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Idea Price Process"
 \tB\;

The *price* of idea $\iota$ at time $t$ is:
\begin{keyeq}
\[
p(\iota, t) = \IdeaRank(\iota, t) \cdot \bar{u}(\iota, t)
\]
\end{keyeq}
where $\IdeaRank(\iota, t)$ is the Dynamic IdeaRank (network importance)
and $\bar{u}(\iota, t) = \E_a[u(\iota, a, t)]$ is the average utility
across the agent population.  The price is the "consensus value" of an
idea: network centrality $\times$ average usefulness.

!!! definition "Idea Dynamics SDE"
 \tB\;

The price process follows a geometric Brownian motion with regime structure:
\begin{keyeq}
\[
\frac{dp(\iota, t)}{p(\iota, t)} = \mu_\iota(t) \, dt
  + \sigma_\iota(t) \, dW_\iota(t)
  + J_\iota(t) \, dN_\iota(t)
\]
\end{keyeq}
where:
[nosep]
  - $\mu_\iota(t)$ is the *drift* (expected rate of value change),
  - $\sigma_\iota(t)$ is the *volatility* (uncertainty in value),
  - $W_\iota(t)$ is a Wiener process (continuous random fluctuations),
  - $J_\iota(t)$ is the *jump size* and $N_\iota(t)$ is a Poisson
    process with intensity $\lambda_J$, capturing paradigm shifts (sudden
    revaluation of an idea due to a breakthrough or refutation).

!!! definition "Idea Liquidity"
 \tB\;

The *liquidity* of idea $\iota$ at time $t$ is:
\begin{keyeq}
\[
\ell(\iota, t) = \frac{\text{number of agents actively investing in } \iota \text{ at } t}
  {\text{total agent population at } t}
\]
\end{keyeq}
Liquidity measures how "tradeable" an idea is: how easily an agent can
find collaborators, mentors, or materials for engaging with the idea.
[nosep]
  - **High liquidity**: widely studied ideas (calculus, machine
    learning). Easy to enter, many resources available.
  - **Low liquidity**: niche ideas (non-associative algebraic
    geometry, medieval Icelandic poetry). Hard to enter, few collaborators.
  - **Zero liquidity**: ideas with no active participants.
    The idea exists in $\mathcal{G}$ but is "frozen": no agent allocates
    attention to it.

!!! definition "Idea Volatility Decomposition"
 \tB\;

The volatility of idea $\iota$ decomposes into:
\begin{keyeq}
\[
\sigma_\iota^2(t) = \underbrace{\beta_\iota^2 \sigma_M^2(t)}_{\text{systematic}}
  + \underbrace{\sigma_{\epsilon,\iota}^2(t)}_{\text{idiosyncratic}}
\]
\end{keyeq}
where $\sigma_M$ is the volatility of the "idea market" (aggregate
uncertainty about the value of knowledge), $\beta_\iota$ is the idea's
sensitivity to market-wide cognitive shocks (a "knowledge recession"
devalues all ideas), and $\sigma_{\epsilon,\iota}$ is the
idea-specific uncertainty.

%═══════════════════════════════════════════════════════════════════════════════

## The Idea Lifecycle

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Lifecycle Phases"
 \tA\;

Every idea passes through a canonical lifecycle with four phases,
characterized by their drift and volatility regime:
\begin{keyeq}
\[
\begin{array}{lcccl}
\text{Phase} & \mu_\iota & \sigma_\iota & \ell(\iota) & \text{Character}   
\hline
\text{I. Birth} & \text{high, uncertain} & \text{very high} & \text{very low}
  & \text{Radical novelty, few early adopters}   
\text{II. Growth} & \text{high, stabilizing} & \text{high} & \text{rising}
  & \text{Rapid adoption, connections multiply}   
\text{III. Maturity} & \text{low, stable} & \text{low} & \text{high}
  & \text{Canonical knowledge, widely taught}   
\text{IV. Obsolescence} & \text{negative} & \text{rising} & \text{falling}
  & \text{Superseded, declining relevance}
\end{array}
\]
\end{keyeq}

!!! theorem "Lifecycle--IdeaRank Correspondence"
 \tA\;

The four lifecycle phases correspond to distinct IdeaRank dynamics:
\begin{keyeq}

\[\begin{aligned}
\text{Birth:} \quad & \frac{d}{dt}\IdeaRank(\iota, t) > 0, \quad
  \frac{d^2}{dt^2}\IdeaRank(\iota, t) > 0
  \quad \text{(accelerating growth)}    
\text{Growth:} \quad & \frac{d}{dt}\IdeaRank(\iota, t) > 0, \quad
  \frac{d^2}{dt^2}\IdeaRank(\iota, t) < 0
  \quad \text{(decelerating growth)}    
\text{Maturity:} \quad & \frac{d}{dt}\IdeaRank(\iota, t) \approx 0
  \quad \text{(steady state)}    
\text{Obsolescence:} \quad & \frac{d}{dt}\IdeaRank(\iota, t) < 0
  \quad \text{(decay)} 
\end{aligned}\]

\end{keyeq}
Moreover, the transition from Phase II to Phase III occurs at the
*inflection time* $t^*$ where the second derivative changes sign,
and the transition from Phase III to Phase IV is triggered by a
*supersession event*: the birth of a new idea $\iota'$ with
$\iota' \to \iota$ in $\mathcal{G}$ (the new idea depends on and
generalizes the old one).

??? proof "Proof"

The Dynamic IdeaRank equation is:
\[
\IdeaRank(\iota, t) = \frac{1 - \alpha}{|V(t)|}
+ \alpha \sum_{j \to \iota} \frac{\IdeaRank(j, t)}{\mathrm{out}(j, t)}
  \cdot e^{-\kappa(t - t_j)}
\]
At birth ($t = t_{\iota}$), $\iota$ has few in-edges but they may be
high-value (radical ideas often build on deep prerequisites).  As the idea
gains citations (new edges $j \to \iota$), the sum grows, driving
$d\IdeaRank/dt > 0$.  The acceleration $d^2\IdeaRank/dt^2 > 0$ during
Phase I reflects network effects: each new adopter creates more edges.

The inflection point occurs when the marginal contribution of new edges
equals the decay of old edges: the growth rate starts decreasing even
though IdeaRank itself still increases.  This is the "S-curve" of
diffusion.

At maturity, the inflow (new edges) exactly compensates the temporal
decay $e^{-\kappa(t - t_j)}$, giving $d\IdeaRank/dt \approx 0$.

Obsolescence begins when the decay of old edges exceeds the inflow of new
ones.  The supersession event (birth of a generalizing idea $\iota'$)
diverts edge formation from $\iota$ to $\iota'$, accelerating the decline.

!!! example "The Lifecycle of Newtonian Mechanics"
 \tA\;
[nosep]
  - **Birth** (1687): *Principia* published. Very few people
    can read it ($\ell \approx 0$), extremely high novelty ($\sigma$ huge),
    high expected return ($\mu$ high).
  - **Growth** (1700--1850): Widespread adoption, textbooks written,
    applications multiply. IdeaRank accelerates then decelerates.
  - **Maturity** (1850--1905): Canonical knowledge, taught
    universally, stable IdeaRank, low volatility.
  - **Partial Obsolescence** (1905--): Superseded by relativity
    and quantum mechanics for extreme regimes. IdeaRank declines but
    stabilizes at a high level (still taught, still useful for most
    engineering applications). This is *partial* obsolescence:
    the idea retains value in a restricted domain.

%═══════════════════════════════════════════════════════════════════════════════

## Cultural Evolution as Time-Varying Filters

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Cultural Filter"
 \tA\;

A *cultural filter* $\Phi_{\mathrm{cult}}(t)$ is a time-varying
cognitive filter that modulates the effective intelligence of all agents
in a population:
\begin{keyeq}
\[
\Phi_{\mathrm{cult}}(t) : \\mathbb{R}^{n(e)}_{\geq 0} \to \\mathbb{R}^{n(e)}_{\geq 0}, \quad
\Phi_{\mathrm{cult}}(t)(\bI) = D(t) \cdot \bI
\]
\end{keyeq}
where $D(t) = \mathrm{diag}(d_1(t), \ldots, d_8(t))$ with
$d_\tau(t) \in [0, 1]$ is the *cultural modulation vector*.
Each $d_\tau(t)$ represents the degree to which culture supports
intelligence type $\tau$ at time $t$: $d_\tau = 1$ means full support,
$d_\tau = 0$ means complete cultural suppression.

!!! example "Historical Cultural Filters"
 \tA\;
[nosep]
  - **Medieval Europe** (c.\ 1200):
    $d_{\mathrm{ling}} = 0.4$ (literacy restricted to clergy),
    $d_{\mathrm{symb}} = 0.3$ (mathematics suppressed outside monasteries),
    $d_{\mathrm{kin}} = 0.8$ (physical labor valued),
    $d_{\mathrm{soc}} = 0.5$ (rigid hierarchy).
  - **Renaissance Florence** (c.\ 1480):
    $d_{\mathrm{ling}} = 0.7$, $d_{\mathrm{spat}} = 0.9$ (visual arts
    flourishing), $d_{\mathrm{symb}} = 0.6$, $d_{\mathrm{soc}} = 0.7$
    (patronage networks).
  - **Modern research university** (c.\ 2024):
    $d_{\mathrm{ling}} = 0.9$, $d_{\mathrm{symb}} = 0.95$,
    $d_{\mathrm{kin}} = 0.3$ (sedentary culture),
    $d_{\mathrm{aud}} = 0.4$ (music de-emphasized in STEM).

!!! theorem "Cultural Selection Theorem"
 \tA\;

The cultural filter $\Phi_{\mathrm{cult}}(t)$ induces a time-varying
selection pressure on the idea graph: ideas whose intelligence requirement
profiles $\mathbf{R}_\iota$ are "compatible" with the cultural filter
survive; those that are "incompatible" decay.  Formally:
\begin{keyeq}
\[
\frac{d}{dt} \IdeaRank(\iota, t) \propto
\langle D(t) \cdot \bar{\bI}(t), \; \mathbf{R}_\iota \rangle_{\bK}
- \kappa \cdot \IdeaRank(\iota, t)
\]
\end{keyeq}
where $\bar{\bI}(t)$ is the population-average intelligence vector.
The first term is the *cultural fitness* of idea $\iota$: the
$\bK$-inner product of the culturally-filtered population intelligence
with the idea's requirement.  Ideas whose requirements match the
culturally-supported types grow; mismatched ideas decay.

??? proof "Proof"

The Dynamic IdeaRank of $\iota$ grows when agents invest in $\iota$ (creating
new edges $j \to \iota$).  An agent invests in $\iota$ when the expected
cognitive return is positive: $r_\iota(a) > 0$, which requires sufficient
effective intelligence $\langle \bI_{\mathrm{eff},a}, \mathbf{R}_\iota
\rangle_{\bK} > \theta$ (sufficiency threshold).  Under the cultural filter,
$\bI_{\mathrm{eff},a} = \Phi_{\mathrm{cult}}(t)(\bI_a) = D(t) \cdot \bI_a$.
The population-level investment rate in $\iota$ is proportional to the
fraction of agents meeting the threshold, which for a large population
approximates $\langle D(t) \cdot \bar{\bI}(t), \mathbf{R}_\iota \rangle_{\bK}$.
This drives edge creation, hence IdeaRank growth.  The $\kappa$ term is the
inherent temporal decay of Dynamic IdeaRank.

!!! corollary "Cultural Dark Ages as Filter Contraction"
 \tA\;
A "dark age" for intelligence type $\tau$ occurs when $d_\tau(t) \to 0$:
the cultural filter suppresses type $\tau$.  This causes:
[nosep]
  - All ideas with $R_{\iota,\tau} > 0$ lose cultural fitness,
    accelerating their decay.
  - The kernel of the cultural filter expands:
    $\ker(\Phi_{\mathrm{cult}}) \ni \tau$, in the filter-formalism sense.
  - The effective efficient frontier (Thread 1) contracts, reducing
    the space of viable cognitive portfolios.

Conversely, a "renaissance" for type $\tau$ ($d_\tau(t)$ increasing)
expands the frontier and revives ideas that load on type $\tau$.

%═══════════════════════════════════════════════════════════════════════════════

## The Idea Graph as a Growing Network

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Idea Birth Process"
 \tB\;

New ideas enter the graph $\mathcal{G}(t)$ via a marked Poisson process
with intensity:
\begin{keyeq}
\[
\Lambda(t) = \sum_a \lambda_a(t) \cdot \langle \bI_{\mathrm{eff},a}(t),
  \mathbf{1} \rangle
\]
\end{keyeq}
where $\lambda_a(t)$ is agent $a$'s "creativity rate" and
$\langle \bI_{\mathrm{eff},a}, \mathbf{1} \rangle = \sum_\tau I_{\mathrm{eff},a,\tau}$
is the total effective intelligence.  Each new idea $\iota'$ arrives with:
[nosep]
  - A random intelligence profile $\mathbf{R}_{\iota'}$ drawn from a
    distribution $\pi(t)$ that is itself shaped by the cultural filter.
  - A set of prerequisite edges from existing ideas, with edge
    probability proportional to $\IdeaRank(\iota, t)$ (preferential
    attachment: new ideas are more likely to build on important ideas).

!!! theorem "Preferential Attachment and Power Laws"
 \tB\;

Under the birth process of Definition *ref:def:birth-process*, the
steady-state IdeaRank distribution follows a power law:
\begin{keyeq}
\[
\Pr[\IdeaRank(\iota) \geq x] \sim x^{-\gamma}
\]
\end{keyeq}
with exponent $\gamma = 1 + 1/(\alpha \cdot \bar{m})$, where $\alpha$
is the IdeaRank damping factor and $\bar{m}$ is the average number of
prerequisite edges per new idea.

??? proof "Proof"

This follows from the standard Barab\'asi--Albert preferential attachment
model, adapted to the IdeaRank setting.  Each new idea creates $\bar{m}$
edges, each attaching to existing idea $\iota$ with probability
$\propto \IdeaRank(\iota, t)$.  The master equation for the degree
distribution is:
\[
\frac{\partial}{\partial t} n(k, t) = \bar{m} \frac{(k-1) n(k-1, t)
  - k \, n(k, t)}{2\bar{m} t} + \delta_{k, \bar{m}} \frac{1}{t}
\]
whose steady-state solution is a power law with exponent
$\gamma = 1 + 2\bar{m}/\bar{m} = 3$ in the basic model.  The IdeaRank
damping factor modifies this: with probability $(1-\alpha)/|V|$ each
node receives a "random teleportation" share, which flattens the tail.
The modified exponent is $\gamma = 1 + 1/(\alpha \bar{m})$.
For $\alpha = 0.85$ and $\bar{m} = 3$: $\gamma \approx 1.39$---a heavy
tail, consistent with the empirical observation that a few ideas
(calculus, evolution, electromagnetism) dominate the intellectual landscape.

\begin{interpretation}
The power-law distribution of IdeaRank means that the "idea market"
has extreme concentration: a few "blue-chip" ideas account for most
of the total IdeaRank in the graph.  This parallels the concentration of
financial markets (a few companies dominate market capitalization) and is
a direct consequence of preferential attachment: important ideas attract
more connections, which makes them more important.

The cultural filter shapes the power law by biasing which ideas receive
new connections.  A culture that suppresses type $\tau$ will have fewer
high-IdeaRank ideas loading on $\tau$---not because those ideas are
inherently less valuable, but because the cultural filter prevents agents
from investing in them.
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════

## Temporal Portfolio Optimization

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Dynamic Cognitive Portfolio"
 \tB\;

A *dynamic cognitive portfolio* is a stochastic process
$\bw(t) \in \Delta^{N(t)-1}$ adapted to the filtration generated by
the idea price processes and the idea birth process.  The agent
continuously rebalances as new ideas are born, existing ideas change
value, and the cultural filter evolves.

!!! theorem "Optimal Dynamic Allocation"
 \tB\;

The growth-optimal dynamic portfolio under the idea SDE
(Definition *ref:def:idea-sde*) and cultural filter
$\Phi_{\mathrm{cult}}(t)$ satisfies:
\begin{keyeq}
\[
w_i^*(t) = \frac{[\Sigma^{-1}(t) (\bmu(t) - r_f \mathbf{1})]_i^+}
  {\sum_j [\Sigma^{-1}(t) (\bmu(t) - r_f \mathbf{1})]_j^+}
\]
\end{keyeq}
where $[\cdot]^+$ denotes the positive part (no short-selling of
cognitive attention), $\bmu(t)$ is the vector of instantaneous expected
returns filtered through $\Phi_{\mathrm{cult}}(t)$:
\[
\mu_i(t) = \mu_i^{\mathrm{raw}} \cdot
  \frac{\langle D(t) \bar{\bI}(t), \mathbf{R}_i \rangle_{\bK}}
       {\langle \bar{\bI}(t), \mathbf{R}_i \rangle_{\bK}}
\]
and $\Sigma(t)$ is the time-varying covariance matrix.

??? proof "Proof"

This extends the Kelly criterion (Thread 1, Theorem 4.2) to the
continuous-time setting with time-varying parameters.  The log-growth rate
at time $t$ is:
\[
g(\bw, t) = \bw^\top \bmu(t) - r_f - \frac{1}{2} \bw^\top \Sigma(t) \bw
\]
Maximizing pointwise in $\bw$ (myopic optimization, valid under
log-utility by the separation theorem of Merton):
$\bw^*(t) = \Sigma^{-1}(t) (\bmu(t) - r_f \mathbf{1})$, projected onto
the simplex.  The cultural filter enters through $\bmu(t)$: it modulates
the expected returns by the ratio of culturally-filtered to raw cultural
fitness.

%═══════════════════════════════════════════════════════════════════════════════

## Idea Extinction and Revival

%═══════════════════════════════════════════════════════════════════════════════

!!! definition "Idea Extinction"
 \tA\;
An idea $\iota$ is *extinct at time $t$* if:
\[
\ell(\iota, t) = 0 \quad \text{and} \quad
\IdeaRank(\iota, t) < \theta_{\mathrm{ext}}
\]
where $\theta_{\mathrm{ext}}$ is the extinction threshold.  An extinct idea
has no active participants and negligible network importance.  The idea
still exists as a vertex in $\mathcal{G}$ but is effectively invisible.

!!! theorem "Conditions for Idea Revival"
 \tA\;

An extinct idea $\iota$ can be revived at time $t' > t$ if and only if:
\begin{keyeq}
\[
\exists \, a : \quad
\langle D(t') \cdot \bI_a, \; \mathbf{R}_\iota \rangle_{\bK} > \theta
\quad \text{and} \quad
\nu(\iota, t') > \nu_0
\]
\end{keyeq}
where the first condition requires at least one agent with sufficient
culturally-filtered intelligence to engage with the idea, and the second
requires that the idea has become "novel again" ($\nu(\iota, t')$ exceeds
a novelty threshold $\nu_0$) by virtue of being forgotten.

??? proof "Proof"

Revival requires an agent to invest in $\iota$, creating new edges.  The
sufficiency condition $\langle D(t') \cdot \bI_a, \mathbf{R}_\iota
\rangle_{\bK} > \theta$ ensures the agent has the cognitive capacity
(under the current cultural filter) to engage.  The novelty condition
ensures the idea offers positive expected return: if $\iota$ is well-known
(high $\bar{u}$, low $\nu$), re-engagement yields no new utility.
But an idea that has been forgotten ($\nu$ increases as collective
knowledge of $\iota$ decays) becomes "novel" to the current population,
making re-discovery worthwhile.

\begin{interpretation}
This formalizes the phenomenon of "rediscovery": ideas that were known
to a previous civilization, lost during a cultural dark age (filter
contraction), and rediscovered when the cultural filter re-expands.
Classical examples include the rediscovery of Aristotelian logic in
medieval Europe via Arabic translations, and the revival of ancient
Greek mathematics during the Renaissance.

The novelty-through-forgetting mechanism is a deep feature: the
temporal decay of IdeaRank and the mortality of agents ensure that
extinct ideas *become novel again* after sufficient time.  The
idea graph has a memory horizon beyond which all ideas are effectively
new.  This creates a cyclic structure in cultural evolution:
birth $\to$ growth $\to$ maturity $\to$ obsolescence $\to$ extinction
$\to$ (potential) revival $\to$ growth $\to \cdots$
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════

## Unification: The Master Temporal Equation

%═══════════════════════════════════════════════════════════════════════════════

!!! theorem "Master Temporal Equation for the Idea Graph"
 \tA\;

The complete temporal dynamics of the idea graph are governed by:
\begin{keyeq}
\[
\frac{d}{dt} \mathbf{p}(t) = \mathcal{M}(t) \cdot \mathbf{p}(t)
  + \mathbf{b}(t)
\]
\end{keyeq}
where $\mathbf{p}(t) = (p(\iota_1, t), \ldots, p(\iota_{|V(t)|}, t))^\top$
is the vector of idea prices, $\mathcal{M}(t)$ is the
*master evolution operator*:
\begin{keyeq}
\[
\mathcal{M}(t) = \underbrace{\alpha \, A_{\mathcal{G}}(t)}_{\text{IdeaRank propagation}}
  - \underbrace{\kappa \, \mathrm{Id}}_{\text{temporal decay}}
  + \underbrace{P_{\mathrm{cult}}(t)}_{\text{cultural selection}}
  + \underbrace{S_{\bK}(t)}_{\text{synergy coupling}}
\]
\end{keyeq}
and $\mathbf{b}(t)$ is the birth term (new ideas entering the graph).

Here:
[nosep]
  - $A_{\mathcal{G}}(t)$ is the column-normalized adjacency matrix of
    the idea graph (IdeaRank transition matrix).
  - $P_{\mathrm{cult}}(t) = \mathrm{diag}(\langle D(t) \bar{\bI}(t),
    \mathbf{R}_{\iota_i} \rangle_{\bK})$ is the cultural fitness diagonal.
  - $S_{\bK}(t)$ encodes cross-idea synergy through shared intelligence
    type requirements and the compatibility tensor.

The eigenvalues of $\mathcal{M}(t)$ determine the idea graph's
"cognitive temperature": the rate at which the graph reorganizes.

??? proof "Proof"

The price $p(\iota, t) = \IdeaRank(\iota, t) \cdot \bar{u}(\iota, t)$
evolves as:
\[
\dot{p}_i = \dot{\IdeaRank}_i \cdot \bar{u}_i + \IdeaRank_i \cdot \dot{\bar{u}}_i
\]
The IdeaRank dynamics are the Dynamic IdeaRank equation (matrix form):
$\dot{\IdeaRank} = (\alpha A_{\mathcal{G}} - \kappa \mathrm{Id})
\cdot \IdeaRank + \frac{1-\alpha}{|V|} \mathbf{1}$.
The utility dynamics are driven by the cultural selection equation
(Theorem *ref:thm:cultural-selection*):
$\dot{\bar{u}}_i \propto \langle D(t) \bar{\bI}(t), \mathbf{R}_i
\rangle_{\bK}$.
Combining (using the product rule and linearizing):
$\dot{\mathbf{p}} \approx \mathcal{M}(t) \mathbf{p}(t) + \mathbf{b}(t)$
where $\mathcal{M}$ collects all the linear terms and $\mathbf{b}$
captures the constant birth-rate injection.

\begin{interpretation}
The Master Temporal Equation unifies four previously separate dynamics:
IdeaRank propagation (Part II), temporal decay (Ideometrics paper),
cultural selection (this thread), and cross-idea synergy (via $\bK$ and
Thread 1).  The idea graph is a *driven dissipative system*:
driven by the birth process $\mathbf{b}(t)$, dissipated by temporal decay
$\kappa$, and organized by the interplay of IdeaRank propagation and
cultural selection.  The steady-state distribution (when it exists)
is the culturally-filtered power law of Theorem *ref:thm:power-law*.
\end{interpretation}

%═══════════════════════════════════════════════════════════════════════════════

## Summary of Results

%═══════════════════════════════════════════════════════════════════════════════

\begin{tempbox}[Thread 4: New Results]
[nosep,leftmargin=1.5em]
  - **Theorem *ref:thm:lifecycle-ir*** (Tier A): Lifecycle--IdeaRank
    correspondence; four phases characterized by derivatives of IdeaRank.
  - **Theorem *ref:thm:cultural-selection*** (Tier A): Cultural
    selection equation; ideas grow/decay proportional to cultural fitness.
  - **Theorem *ref:thm:power-law*** (Tier B): Power-law
    IdeaRank distribution from preferential attachment,
    $\gamma = 1 + 1/(\alpha \bar{m})$.
  - **Theorem *ref:thm:revival*** (Tier A): Conditions for
    idea revival---novelty through forgetting.
  - **Theorem *ref:thm:dynamic-opt*** (Tier B): Optimal dynamic
    cognitive portfolio under cultural filter evolution.
  - **Theorem *ref:thm:master-temporal*** (Tier A): Master
    temporal equation unifying IdeaRank, decay, cultural selection,
    and synergy coupling.
  - **Definition *ref:def:cultural-filter*** (Tier A): Cultural
    filter as time-varying diagonal modulation, with historical examples.
  - **Definition *ref:def:liquidity*** (Tier B): Idea liquidity
    as fraction of active participants.
  - **Definition *ref:def:idea-sde*** (Tier B): Idea price SDE
    with jump-diffusion (paradigm shifts).

\end{tempbox}

\ifx\STANDALONE\undefined
\else