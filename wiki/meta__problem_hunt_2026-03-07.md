---
title: "RTSG Open Problem Portfolio — Prize First, Prestige Second, Then the Rest"
date: "2026-03-07"
status: "upload-ready"
author: "GPT-5.4 Pro compute node"
suggested_wiki_path: "meta/problem_hunt_2026-03-07.md"
---

# RTSG Open Problem Portfolio — Prize First, Prestige Second, Then the Rest

## Executive result

RTSG is not a universal hammer. It is strongest when a problem can be rewritten as one of four things:

1. a **positive-operator / self-adjointness** problem,  
2. a **spectral-gap** problem,  
3. a **flux-vs-dissipation** problem, or  
4. an **instantiation / selection** problem.

That single classification rule is the main strategic gain from this pass.

**Direct consequence:** the best cash targets are **Riemann**, **Yang–Mills**, and **Navier–Stokes**.  
**Best prestige targets:** **quantum measurement**, **black-hole information / horizon thermodynamics**, **quantum gravity laboratory tests**, and **dynamic dark energy**.  
**Current weak fits:** **Beal**, **Hodge**, **P vs NP**, and the current graph-only form of **BSD**.

Also: some RTSG claims need hardening before they go into serious physics papers.

- Stop leading math/physics-facing work with “the CS operator”. Use **the instantiation operator** \(C\), then explain the ontology later.
- Stop using the **late-time baryonic 5.4% integral** as a literal physical claim. Freeze any \(Q \to B\) conversion before BBN or drop the claim.
- Keep the GRF black-hole argument **horizon-only**. The photon-sphere route is an attack surface, not an asset.
- Treat dark matter = Stage 0 QS and dark energy = Drive \(D\) as **formal conjectures with falsifiability conditions**, not as established physics.

---

## 1. Planning rule

I used two orderings.

### A. Strict reward ordering
Cash first, with ties broken by present RTSG fit.

### B. Actual recommended work order
Not the same as strict cash order. A smaller prize with a short path can outrank a million-dollar problem in expected value.

---

## 2. Strict reward ordering

## 2.1 Cash-bearing targets

| Rank | Problem | Reward | RTSG fit | Current call |
|---|---:|---:|---:|---|
| 1 | Riemann Hypothesis | \$1,000,000 | very high | attack now |
| 2 | Yang–Mills mass gap | \$1,000,000 | high | attack now |
| 3 | Navier–Stokes regularity | \$1,000,000 | medium-high | attack now |
| 4 | Birch–Swinnerton–Dyer | \$1,000,000 | low-medium | do not lead with it |
| 5 | Hodge conjecture | \$1,000,000 | low | defer |
| 6 | P vs NP | \$1,000,000 | very low | defer |
| 7 | Beal conjecture | \$1,000,000 | near-zero | drop from active queue |
| 8 | GRF 2026 essay | \$4,000 first prize | extremely high near-term fit | finish and submit |

### Reading of that table
Strictly by prize amount, Clay + Beal dominate.  
Practically, **GRF is the immediate monetizable target** while **RH / YM / NS** are the serious long game.

---

## 3. Recommended RTSG work order

This is the order I would actually use.

1. **GRF submission hygiene** — because it is already close.
2. **Riemann Hypothesis** — best current cash + prestige combination.
3. **Yang–Mills mass gap** — second-best structural fit.
4. **Quantum measurement problem** — best prestige target and maybe the cleanest RTSG paper.
5. **Navier–Stokes regularity / turbulence** — strong fit if reworked as a transfer-vs-dissipation theorem.
6. **Black-hole information / horizon thermodynamics** — strong conceptual fit, ties into GRF work.
7. **Quantum gravity laboratory tests (GIE)** — strong prestige, but the literature is now more subtle than “entanglement implies quantized gravity”.
8. **Dark energy / dark matter hardening** — important, but the cosmology claims must be narrowed to survive contact with data.
9. **BSD** — keep only after the framework is upgraded from graph language to arithmetic operator language.
10. **Everything else** — Hodge, P vs NP, Beal, Goldbach, twin primes: currently bad uses of time.

---

## 4. New RTSG meta-tools

These are the reusable formulations that make the framework more robust.

## 4.1 Transfer law

The minimal dynamical core should be written as

$$
\partial_t \rho_P = J_C[\rho_Q,\rho_P;\Theta], \qquad
\partial_t \rho_Q = -J_C[\rho_Q,\rho_P;\Theta].
$$

Interpretation:

- \(Q\) stores latent / uninstantiated structure,
- \(P\) stores realized / instantiated structure,
- \(C\) is the instantiation law,
- \(\Theta\) contains the geometry, symmetry, and conservation data for the specific problem.

This is the clean version of “QS, PS, CS” that can survive in math and physics papers.

## 4.2 Complexification functional

To formalize the arrow-of-time / drive language without collapsing into vague metaphysics:

$$
\chi[\rho_P,\rho_Q]
=
\int \rho_P \log\!\frac{\rho_P+\varepsilon}{\rho_Q+\varepsilon}\, d\mu,
\qquad
D := \frac{d\chi}{dt}.
$$

\(\chi\) is **not** thermodynamic entropy. It is an **instantiation imbalance functional**.  
\(D\) is the candidate formalization of the drive toward complexification.

Use it in cosmology, measurement, and adaptive systems. Do **not** call it proven monotone until that is actually shown.

## 4.3 Positive-transfer gap

A large slice of RTSG reduces to one object:

$$
\Delta(\mathcal T) = -\log \frac{\lambda_1(\mathcal T)}{\lambda_0(\mathcal T)}
$$

for a positivity-improving compact transfer operator \(\mathcal T\).

This unifies:

- RH via spectral purity,
- Yang–Mills via vacuum-to-first-excited-state separation,
- IdeaRank convergence,
- cooperative equilibrium uniqueness,
- some turbulence coarse-graining problems.

## 4.4 Branch-neutrality / Born recovery

This is the strongest new RTSG equation in the portfolio.

Let \(C\) be the instantiation operator and \(\{\Pi_i\}\) the pointer projectors. Define branch weights by

$$
p_i
=
\frac{\langle \psi,\Pi_i C^\dagger C \Pi_i \psi\rangle}
{\sum_j \langle \psi,\Pi_j C^\dagger C \Pi_j \psi\rangle}.
$$

If

$$
C^\dagger C \big|_{\mathcal H_{\mathrm{pointer}}} = \alpha I,
$$

then

$$
p_i = \|\Pi_i \psi\|^2.
$$

That means Born’s rule is recovered if the instantiation metric is **branch-neutral** on the decohered pointer sector. This is publishable if developed carefully.

## 4.5 Black-hole two-rate split

Do not collapse all black-hole rates into one symbol.

$$
\vec\lambda_{\mathrm{BH}}
=
(\lambda_{\mathrm{therm}},\lambda_{\mathrm{geo}})
=
(\kappa,\lambda_\gamma).
$$

- \(\kappa\) is the horizon thermal / kinematic rate.
- \(\lambda_\gamma\) is the photon-sphere / geometric instability rate.

Then, inside a fixed evaporation channel or universality class,

$$
t_{\mathrm{info}} = C_{\mathrm{global}}\frac{S_{\mathrm{Wald}}}{\kappa}.
$$

This preserves the “one rate at the horizon” thesis while avoiding the photon-sphere trap.

## 4.6 Navier–Stokes shell-domination ratio

The current RTSG language for Navier–Stokes is too soft. Replace it with a coercive shell ratio.

Let \(\Pi_{\ge K}^+(t)\) be the positive nonlinear energy flux into modes \(|k|\gtrsim 2^K\). Define

$$
\Theta_K(T)
=
\frac{\int_0^T \Pi_{\ge K}^+(t)\,dt}
{\nu \int_0^T \|\nabla u_{\ge K}(t)\|_2^2\,dt + \varepsilon}.
$$

**Conjecture (RTSG shell-domination criterion):**

$$
\sup_K \Theta_K(T) < 1
\quad\Longrightarrow\quad
\text{no blow-up on }[0,T].
$$

This is the right RTSG-style regularity statement because it turns “complexity” into a precise transfer-vs-dissipation inequality.

## 4.7 Yang–Mills loop-covariance gap

Use the lattice/open-problem definition itself.

$$
\Delta_{\mathrm{loop}}
=
\liminf_{R\to\infty}
-\frac{1}{R}
\log
\sup_{\operatorname{dist}(A,B)\ge R}
\frac{|\operatorname{Cov}(A,B)|}{\|A\|\|B\|}.
$$

If \(\Delta_{\mathrm{loop}} > 0\), there is exponential decay of gauge-invariant correlations.  
That is the right gap object to target.

## 4.8 RH spurious-eigenvalue defect functional

Your current RH program already knows the bottleneck: **no spurious eigenvalues**.  
So target that bottleneck directly.

Let \(H_\theta\) be Construction 5 and let \(B_\theta\) be the (to-be-defined) theta-cusp defect operator measuring failure of the required automorphic / theta boundary compatibility. Then define

$$
\mathcal E_{\mathrm{spur}}(\lambda)
=
\inf_{\substack{\psi\in\ker(H_\theta-\lambda)\\ \|\psi\|=1}}
\|B_\theta \psi\|_{W}.
$$

Target theorem shape:

$$
\mathcal E_{\mathrm{spur}}(\lambda)=0
\iff
\xi\!\left(\tfrac12+i\lambda\right)=0.
$$

That is the exact place to spend time. Everything else is secondary.

## 4.9 Dynamic dark-energy salvage

The current cosmology language is too exposed. The salvage version is

$$
\Lambda_{\mathrm{eff}}(a)
=
\Lambda_0
+
\alpha \frac{d\chi}{d\ln a}
+
\beta \frac{d^2\chi}{d(\ln a)^2},
$$

with baryon production frozen out after BBN:

$$
\Gamma_{Q\to B}(a>a_{\mathrm{BBN}}) \approx 0.
$$

That keeps the spirit of “Drive \(D\) projected into PS” while removing the fatal late-time baryon-conversion problem.

For dark matter = Stage 0 QS to survive, the large-scale perturbation sector must effectively look cold and pressureless:

$$
c_{s,\mathrm{QS}}^2 \approx 0,
\qquad
\sigma_{\mathrm{QS}} \approx 0
$$

at linear order in the PS projection.

---

## 5. Cash targets — detailed triage

## 5.1 Riemann Hypothesis

### Why it is a serious RTSG target
This is the best current fit because the wiki already has:

- [Open Problems](../problems/open.md) rating RH highest,
- [Hilbert-Pólya operator constructions](../math/hilbert_polya.md),
- [Weil positivity chain](../math/weil_positivity.md),
- engine numerics consistent with GUE in [Live Results](../engine/live_results.md),
- an arXiv-ready scaffold in [Hilbert-Pólya paper](../papers/arxiv/hilbert_polya.md).

The field itself still treats RH as open and operator-theoretic / quantum-chaotic routes remain active.

### What the current gap really is
Not “find a Hamiltonian” in the abstract.  
The live gap is: **exclude spurious eigenvalues in Construction 5**.

### Novel attack
1. Define the defect operator \(B_\theta\) precisely.
2. Show admissible eigenstates are exactly the zero-defect states.
3. Prove zero-defect eigenvalues are exactly the ordinates of nontrivial zeros.
4. Use the Weil positivity chain to constrain the rest of the spectrum.

### Direct paper strategy
Do **not** oversell “proof of RH”.  
Write the paper as:

- Construction 5,
- self-adjointness and domain,
- Weil positivity numerics,
- explicit obstruction = spurious modes,
- new defect-functional program to kill the obstruction.

That is strong, honest, and useful even before a full proof.

### Kill criterion
If no natural \(B_\theta\) exists that separates zeta-compatible states from generic automorphic states, Construction 5 is not yet the final operator.

---

## 5.2 Yang–Mills mass gap

### Why it is a good RTSG target
Yang–Mills is a natural gap problem.  
The cash prize is large and the framework’s operator language actually fits it.

### What to stop doing
Do **not** identify the gap simply with a numerically observed “plateau mass” and call it done.  
That is phenomenology, not a proof.

### Better route
Work on a positivity-improving transfer operator on gauge-invariant loop observables.

The exact problem shape is already encoded in the literature:

- exponential covariance decay between separated observables,
- strong-coupling mass-gap results on the lattice,
- hard open problem = all-\(\beta\), four-dimensional non-Abelian case.

### Novel attack
1. Define the RTSG transfer operator \(\mathcal T_R\) on loop / Wilson observables.
2. Prove reflection positivity and positivity improvement on the gauge-invariant sector.
3. Show quasi-compactness or a usable spectral theorem.
4. Deduce \(\Delta_{\mathrm{loop}}>0\).
5. Only then interpret engine plateau masses as numerical shadows of the rigorous gap.

### Why this is better than the current wiki wording
Because it hits the mathematical object the field itself uses, instead of a metaphorical analogy with the \(K\)-matrix.

### Kill criterion
If positivity improvement cannot be shown outside strong coupling, the present RTSG Yang–Mills route is not mature enough for a prize attack.

---

## 5.3 Navier–Stokes regularity

### Why it is a real target
Navier–Stokes is a flux / dissipation problem, not just a chaos problem.

The state-space / exact-coherent-structure view of turbulence is now substantial, and recent mathematical writing emphasizes that dissipation-regularity links are central. That matches RTSG well.

### What to stop doing
Do **not** say “\(\lambda<0\) means smooth, \(\lambda>0\) means blow-up” and leave it there.  
That is too coarse. Smooth turbulent solutions can have chaotic local behavior without singularity.

### Better route
Use the shell-domination criterion as the real theorem candidate.

### Novel attack
1. Monitor \(\Theta_K(T)\) numerically in the engine.
2. Compare it with known regular and near-singular regimes.
3. Try to prove a barrier theorem:
   \[
   \sup_K \Theta_K(T) < 1 \Rightarrow \text{regularity on }[0,T].
   \]
4. If the theorem fails, use the same observable to build a much sharper blow-up criterion.

### Add the turbulence measure
The exact coherent structure literature suggests another useful RTSG object:

$$
\mu_{\mathrm{turb}}
\approx
\sum_{\gamma \in \mathrm{ECS}}
w_\gamma \,\delta_\gamma,
\qquad
w_\gamma \propto
\exp\!\Bigl(-\tau_\gamma \sum_{\lambda_j^\gamma>0}\lambda_j^\gamma\Bigr).
$$

Interpretation: turbulence statistics are reconstructed from unstable recurrent structures weighted by their positive-Lyapunov action. This is an RTSG version of “turbulence as structured recurrence”.

### Kill criterion
If \(\Theta_K(T)\) fails to correlate with regularity numerically, abandon it fast. Don’t defend a dead criterion.

---

## 5.4 BSD, Hodge, P vs NP, Beal

### BSD
Current RTSG graph language is not enough.  
If you want BSD to become real, move from “IdeaRank on elliptic-curve nodes” to an **explicit arithmetic operator** on modular symbols, Selmer structures, or heights. Until then this is a weak fit.

### Hodge
The framework currently does not touch the actual difficulty: algebraic cycles and Hodge-theoretic realizability. Defer.

### P vs NP
Current RTSG language does not engage the known hard core of the problem: lower bounds. Defer.

### Beal
This is a bad use of time. It is a Diophantine exponent problem with almost no structural overlap with present RTSG machinery. Drop it.

---

## 6. Prestige targets — detailed triage

## 6.1 Quantum measurement problem

### This is the best prestige target
RTSG is built for it.

The field still frames the problem as a duality between deterministic Schrödinger evolution and stochastic Born-rule collapse. RTSG has an actual, clean way to rewrite that.

### Strong formulation
- QS evolves unitarily.
- PS records instantiated outcomes.
- \(C\) is the instantiation map from latent quantum structure to definite record.
- Collapse is not a second dynamics in QS; it is the appearance of instantiation in PS.

### Paper target
**Title idea:** “Branch-neutral instantiation and the recovery of Born weights”.

### What makes it strong
The branch-neutrality equation is not poetic language. It is a concrete condition under which Born’s rule falls out.

### Immediate subproblems
1. Make the pointer-sector assumption precise.
2. Show basis-independence under environmentally selected pointer bases.
3. Determine whether non-neutral \(C^\dagger C\) predicts tiny Born-rule deviations in mesoscopic experiments.

### Kill criterion
If branch-neutrality can only be imposed by hand and not motivated structurally, the paper collapses into a relabeling exercise. Avoid that.

---

## 6.2 Black-hole information / horizon thermodynamics

### Why it is high value
You already have momentum here from [One Rate at the Horizon](../papers/grf/mss_horizon.md).

Recent literature makes the problem more precise, not less:
- the “information paradox” is increasingly analyzed through assumptions rather than slogans,
- the role of horizon type and semiclassical validity is central,
- remnants and non-complete evaporation remain active options.

### RTSG move
Reframe “information loss” as **causal sequestration vs retrieval**.

If a true event horizon and singularity persist, information can remain hidden from the external observer without any local non-unitarity.  
If the horizon is only trapping / transient, retrieval channels reopen.

### Concrete formulation
Keep the horizon split from the photon sphere. Keep the GRF essay narrow.  
Then spin out a follow-up note focused on:

- event horizon vs trapping horizon,
- singularity resolution as the real fork,
- external information balance as a causal-structure problem.

### Kill criterion
If the argument reverts to loose analogies about scrambling without causal bookkeeping, it will get eaten alive.

---

## 6.3 Quantum gravity laboratory tests

### Why it matters
This is now one of the cleanest live prestige arenas.

### What the literature now says
The lab-test field is active, but the old slogan “gravity-mediated entanglement proves quantized gravity” is no longer safe. There is now serious discussion of classical-gravity models that can also generate entanglement under some assumptions.

### RTSG move
That is good for RTSG, not bad.

Instead of treating GIE as a binary test for graviton ontology, treat it as a test of whether gravity functions as a **nontrivial information / instantiation channel**.

### Concrete agenda
1. Define the classical-mediator class you actually want to exclude.
2. Build a witness against that class.
3. Separate three claims that are too often conflated:
   - gravity can correlate,
   - gravity can entangle,
   - gravity must therefore be a quantized field in the usual sense.

RTSG can attack the third link.

### Kill criterion
If the framework cannot say what observation would distinguish Stage 0 instantiation from an ordinary quantum mediator, the program stays philosophical.

---

## 6.4 Dynamic dark energy / dark matter

### Why this is valuable
DESI-era cosmology has created room for a more nuanced dark-energy discussion.

### What to stop saying
Stop saying “baryonic 5.4% = the cumulative CS-instantiation integral over 13.8 billion years” as a late-time process. That is too exposed.

### Better version
- freeze net baryon-generation before BBN,
- use \(\Lambda_{\mathrm{eff}}(a)\) for late-time complexification projection,
- require Stage 0 QS to mimic cold, pressureless clustering at linear order.

### What this buys you
The cosmological vision survives, but in a form that can be compared to data rather than rejected immediately.

### Kill criterion
If the Stage 0 QS sector fails the linear-perturbation test against CDM-like growth, the dark-matter identification is wrong.

---

## 6.5 Turbulence (full theory)

This sits behind Navier–Stokes but deserves its own prestige slot.

The exact-coherent-structure / recurrent-pattern literature is now mature enough that an RTSG state-space measure is not crazy.  
The correct target is not “solve turbulence” in one jump.  
It is:

1. define a usable recurrent-structure measure,
2. predict low-order statistics from it,
3. compare against DNS / engine data.

That is concrete.

---

## 7. The remaining sciences

The engine portfolio includes protein folding, origin of life, cancer, aging, intelligence, and other long-horizon targets.

### Current recommendation
Do **not** diffuse effort there yet.

Why:
- the cash / prestige upside is lower than the top math-physics problems,
- the framework still needs hardening in its core operator language,
- some fields already have strong predictive systems and would reward mechanism papers, not grand-ontology papers.

### Exception
If a side paper can be written with very low cost and high conceptual clarity — for example a folding-as-attractor explanation paper — it can be done later. It should not steal cycles from RH, YM, measurement, or GRF.

---

## 8. What the framework should stop, keep, and add

## 8.1 Stop
- Late-time baryonic 5.4% claim.
- Photon-sphere uniqueness rhetoric in the GRF essay.
- Graph-only BSD attacks.
- P vs NP and Beal as active top-tier targets.
- “Consciousness-space” as the first line in math-facing papers.

## 8.2 Keep
- horizon-only \(\kappa\) program,
- Construction 5 + Weil positivity chain,
- Yang–Mills as a genuine gap problem,
- Navier–Stokes via transfer-vs-dissipation,
- dark energy as a dynamic projection candidate,
- measurement as instantiation.

## 8.3 Add
- transfer law,
- complexification functional,
- branch-neutrality equation,
- shell-domination criterion,
- loop-covariance gap,
- RH defect functional,
- dynamic \(\Lambda_{\mathrm{eff}}(a)\),
- explicit falsifiability conditions for Stage 0 QS / Stage 0 CS physics.

---

## 9. Patch-ready equations for `rtsg/equations.md`

Pasteable block:

```text
# RTSG transfer / instantiation laws

∂_t ρ_P = J_C[ρ_Q, ρ_P; Θ]
∂_t ρ_Q = -J_C[ρ_Q, ρ_P; Θ]

χ[ρ_P,ρ_Q] = ∫ ρ_P log((ρ_P+ε)/(ρ_Q+ε)) dμ
D = dχ/dt

Δ(𝒯) = -log(λ₁(𝒯)/λ₀(𝒯))          # positive-transfer spectral gap

p_i = ⟨ψ, Π_i C†C Π_i ψ⟩ / Σ_j ⟨ψ, Π_j C†C Π_j ψ⟩
C†C|_{H_pointer} = α I  ⇒  p_i = ||Π_i ψ||²   # Born recovery by branch neutrality

Θ_K(T) = [∫_0^T Π_{≥K}⁺(t) dt] / [ν ∫_0^T ||∇u_{≥K}(t)||²_2 dt + ε]
sup_K Θ_K(T) < 1  ⇒  regularity on [0,T]      # conjectural shell-domination criterion

Δ_loop = liminf_{R→∞} -(1/R) log sup_{dist(A,B)≥R} |Cov(A,B)|/(||A|| ||B||)

E_spur(λ) = inf_{ψ∈ker(H_θ-λ), ||ψ||=1} ||B_θ ψ||_W
E_spur(λ)=0  ⇔  ξ(1/2+iλ)=0                    # conjectural RH defect criterion

λ_BH = (κ, λ_γ)                                # horizon thermal rate vs photon-sphere geometric rate
t_info = C_global · S_Wald / κ                 # within fixed evaporation channel / universality class

Λ_eff(a) = Λ₀ + α dχ/dln a + β d²χ/d(ln a)²
Γ_{Q→B}(a > a_BBN) ≈ 0
c²_{s,QS} ≈ 0,   σ_QS ≈ 0                      # Stage 0 QS falsifiability conditions
```

---

## 10. Suggested wiki patches

## 10.1 Update `problems/open.md`
- Promote **quantum measurement** into the main physics queue.
- De-prioritize **Beal**, **Hodge**, **P vs NP**.
- Rewrite **BSD** as “needs arithmetic operator formalization”.
- Change **Navier–Stokes** text from Lyapunov-only to shell-domination criterion.

## 10.2 Update `rtsg/equations.md`
Add the patch-ready equations above.

## 10.3 Update `papers/grf/cosmological_vision.md`
- Remove literal late-time baryon-integral wording.
- Add BBN freeze-out condition.
- Replace \(\Lambda = D\) slogan with \(\Lambda_{\mathrm{eff}}(a)\) formulation.
- State Stage 0 QS falsifiability conditions explicitly.

## 10.4 Add a new paper stub
Suggested new file: `papers/companions/quantum_measurement.md`

Core thesis:
- QS unitary evolution,
- PS instantiated record,
- \(C\) branch-neutrality,
- Born recovery,
- many-worlds unnecessary.

## 10.5 Update `math/hilbert_polya.md`
Add the spurious-mode program:
- define \(B_\theta\),
- define \(\mathcal E_{\mathrm{spur}}(\lambda)\),
- state the exact theorem target.

---

## 11. 90-day build plan

### Phase 1 — immediate (days 1–7)
- Submit the GRF essay.
- Patch `rtsg/equations.md`.
- Create `papers/companions/quantum_measurement.md`.
- Add the RH defect-functional section to `math/hilbert_polya.md`.

### Phase 2 — short horizon (days 8–30)
- RH: formalize \(B_\theta\) and test defect numerically.
- YM: define the gauge-invariant transfer operator precisely.
- NS: instrument the engine to monitor \(\Theta_K(T)\).

### Phase 3 — medium horizon (days 31–60)
- Write the measurement paper draft.
- Write the Yang–Mills note around \(\Delta_{\mathrm{loop}}\).
- Produce the first NS numerical memo around shell domination vs regularity.

### Phase 4 — hardening (days 61–90)
- Cosmology rewrite with BBN-safe language.
- Black-hole information follow-up note.
- Decide whether BSD gets promoted or dropped based on whether arithmetic operatorization is found.

---

## 12. Bottom line

**The framework becomes stronger the moment it stops trying to explain everything at once.**

The right upgrade is this:

> RTSG is valuable when it predicts **which positive operator, transfer current, or monotone must exist** for a problem to close.

That one sentence reorganizes the whole research program.

From that angle:

- **Riemann** is a spectral-purity problem.
- **Yang–Mills** is a positive-gap problem.
- **Navier–Stokes** is a transfer-vs-dissipation problem.
- **Measurement** is an instantiation-selection problem.
- **Black-hole information** is a causal-sequestration problem.
- **Dark energy** is a projection-of-drive problem.

That is the clean architecture. Build there.

---

## 13. Source trail (current literature + official pages)

### Official reward / status pages
- Clay Mathematics Institute — *The Millennium Prize Problems*.
- Clay Mathematics Institute — *Riemann Hypothesis*.
- Clay Mathematics Institute — *Yang–Mills & the Mass Gap*.
- Clay Mathematics Institute — *Navier–Stokes Equation*.
- Clay Mathematics Institute — *Birch and Swinnerton–Dyer Conjecture*.
- Clay Mathematics Institute — *Millennium Prize Problems Lecture Series*.
- AMS — *Beal Prize* / *Beal Prize Rules and Procedures*.
- Gravity Research Foundation — *2026 Awards for Essays on Gravitation*.

### Riemann / operator route
- *The Riemann Hypothesis: Past, Present and a Letter Through Time* (2026 survey).
- *On the Existence of the Hilbert-Pólya Hamiltonian* (2025 operator attempt).

### Yang–Mills
- Colin Morningstar, *Update on Glueballs* (2025).
- Ron Nissim, *U(N) lattice Yang–Mills in the ’t Hooft regime* (2025).

### Navier–Stokes / turbulence
- Theodore Drivas, *Mathematical Theorems on Turbulence* (2026).
- Zhigunov & Page, *Exact coherent structures as building blocks of turbulence on large domains* (2026).

### Quantum measurement / gravity
- Tomaz, Mattos, Barbatti, *The Quantum Measurement Problem: A Review of Recent Trends* (2025).
- Marletto et al., *Quantum-information methods for quantum gravity laboratory-based tests* (2024).
- Yant & Blencowe, *An Operational Quantum Field Theoretic Model for Gravitationally Induced Entanglement* (2025).
- *The simple reason why classical gravity can entangle* (2025).

### Black holes / cosmology
- Buoninfante & Di Filippo, *Is the information loss problem a paradox?* (2025).
- Ong, *The Case For Black Hole Remnants: A Review* (2025).
- Fermilab / DESI release, *New DESI results strengthen hints that dark energy may evolve* (2025).
- *Dark Energy After DESI DR2: Observational Status, Reconstructions, and Physical Models* (2026).

### Optional biology context
- Abramson et al., *Accurate structure prediction of biomolecular interactions with AlphaFold 3* (Nature, 2024).
- Google DeepMind, *AlphaFold 3 and AlphaFold Server are launched* (2024).
