# RTSG Rebooted Open-Problem Campaign
**Date:** 2026-03-07  
**Context:** full live-wiki reread completed; problem queue restarted from the updated RTSG baseline (Axiom 0 / ZFA-AFA, three-space co-primordiality, bisimulation quotient, Will Field / GL layer).

---

## 0. Executive ruling

### 0.1 First fix the formal core
The new Will-Field layer contains a **real formal bug** that must be corrected before using it to attack open problems.

The wiki currently states both:
- `L_int = β |W|^2 W`
- `S[W] = ∫ ( |∂W|^2 + α |W|^2 + (β/2) |W|^4 ) dμ`

These are **not the same thing**.

For a complex scalar field with global `U(1)` symmetry,
- the **interaction density / potential** must be a scalar and `U(1)`-invariant;
- `|W|^2 W` is **not invariant** under `W -> e^{iθ} W`;
- the invariant quartic interaction is `(|W|^4)/2`;
- the cubic term `β |W|^2 W` is the **Euler–Lagrange term in the field equation**, not the Lagrangian density.

### 0.2 Corrected core GL/Will-Field system
Use:

```math
S[W] = \int \left( |\partial W|^2 + \alpha |W|^2 + \frac{\beta}{2}|W|^4 \right) d\mu
```

Then the field equation is:

```math
\Box W - \alpha W - \beta |W|^2 W = 0
```

or, in dissipative / driven form,

```math
\partial_t W = -\alpha \nabla S + \beta |W|^2 W + \gamma \Phi + \xi
```

This patch keeps the cubic term where it belongs: **in the equation of motion**.

### 0.3 Immediate downstream corrections
The following current wiki formulas should be patched:

1. **Cosmological constant**  
   Replace
   ```math
   \Lambda_{\text{eff}} \sim \langle \rho_W \rangle_{PS}
   ```
   with a real, invariant scalar such as
   ```math
   \Lambda_{\mathrm{eff}} = \left\langle \alpha |W|^2 + \frac{\beta}{2}|W|^4 \right\rangle_{PS}
   ```
   or, after symmetry breaking at vacuum `W_0`,
   ```math
   \Lambda_{\mathrm{eff}} = V(W_0) = \alpha |W_0|^2 + \frac{\beta}{2}|W_0|^4.
   ```

2. **Navier–Stokes blow-up line**  
   Replace the current dimensionally/tensorially bad statement
   ```math
   \int_V \beta |W|^2 W \, dV > \int_V \alpha \nabla S \, dV \implies \text{singularity}
   ```
   with a scalar energy-balance functional, e.g.
   ```math
   \mathfrak B(T)
   = \int_0^T \!\int_\Omega
   \left(c\,|Du|\,|W|^2 - \nu |\nabla W|^2 - \frac{\beta}{2}|W|^4\right)
   dx\,dt.
   ```
   Proposed RTSG criterion:
   ```math
   \sup_{0<t<T} \mathfrak B(t) < \infty \quad \Longrightarrow \quad \text{no GL-driven blow-up trigger on } [0,T].
   ```

3. **Stress-energy / gravity coupling**  
   Add the Will-field stress tensor:
   ```math
   T^{(W)}_{\mu\nu}
   = \partial_{(\mu}\bar W\,\partial_{\nu)}W
   - g_{\mu\nu}\left(|\partial W|^2 + \alpha |W|^2 + \frac{\beta}{2}|W|^4\right).
   ```
   This is the correct bridge from the Will field to cosmology / gravity.

---

## 1. Corrected RTSG toolset

### 1.1 Quotient / instantiation operator
Let
```math
\pi : QS \to PS = QS/\!\sim_{\mathrm{bisim}}
```
be the bisimulation quotient.

Define the pushforward measure
```math
\mu_{PS}(B) = \mu_{QS}(\pi^{-1}(B)).
```

Then the quotient-Hilbert subspace is
```math
\mathcal H_\pi = \{f \in L^2(QS,\mu_{QS}) : f = \tilde f \circ \pi\text{ for some }\tilde f \in L^2(PS,\mu_{PS})\}.
```

### 1.2 Quotient covariance condition
The hidden condition needed for the claimed unitarity theorem is:

```math
q_1 \sim_{\mathrm{bisim}} q_2 \implies U_t q_1 \sim_{\mathrm{bisim}} U_t q_2 \qquad \forall t.
```

Call this **bisimulation covariance**.

If it holds, then `U_t` preserves `\mathcal H_\pi`, and the induced quotient dynamics
```math
\bar U_t : L^2(PS,\mu_{PS}) \to L^2(PS,\mu_{PS})
```
exists and is unitary.

### 1.3 Born recovery on the quotient
For quotient cells `C_i \subset PS`, define
```math
p_i = \|\chi_{C_i} \, \bar U_t \psi_0\|_{L^2(PS)}^2.
```

If quotient classes are branch-neutral, this is exactly the Born rule.  
If not, the RTSG generalization is
```math
p_i^{RTSG} = \omega_i \, \|\chi_{C_i}\bar U_t\psi_0\|^2,
\qquad \sum_i \omega_i = 1.
```
This gives a testable deformation parameterization.

### 1.4 RH defect functional
Define the positive-cone quadratic form on the Krein-resolved theta kernel:
```math
\mathcal W_\theta[h] := \langle f_h, P_+ K_\theta P_+ f_h \rangle.
```

Then define the ghost defect
```math
\Delta_{\mathrm{ghost}}[h]
:= \langle f_h, K_\theta f_h \rangle_{\mathcal K}
 - \mathcal W_\theta[h].
```
A clean RH route is to show `\Delta_{ghost}[h]=0` on a dense generating cone.

### 1.5 Theta-cone closure program
Let
```math
\mathcal C_\theta
= \overline{\{g_\theta * \widetilde g_\theta\}}
```
inside the even positive-definite Schwartz cone.

If
1. `\mathcal W_\theta[h] \ge 0` for all `h \in \mathcal C_\theta`, and
2. `\mathcal C_\theta` is dense in the full positive-definite test-function cone,

then Weil positivity extends to all positive-definite `h`, closing the current Step-5 gap.

### 1.6 YM gap functional
For a gauge-invariant effective action with a center-sensitive order parameter `L` and Will field `W`, use
```math
\Gamma[L,W]
= \int \left(
|\nabla L|^2 + a|L|^2 + b|L|^4
+ c|W|^2|L|^2
+ |\nabla W|^2 + \alpha |W|^2 + \frac{\beta}{2}|W|^4
\right) dx.
```

At a confining vacuum `(L_0=0, W_0)`, define
```math
\Delta_{YM}^2
:= \lambda_{\min}\!\left(D^2\Gamma\big|_{(0,W_0)}\right)
= a + c|W_0|^2.
```
This is a usable RTSG mass-gap candidate. It is **not yet** the Clay proof, but it is a real analytic object.

### 1.7 NS flux-defect functional
Littlewood–Paley split `u = \sum_j u_j`. Define the high-frequency defect
```math
\mathcal D_K(t)
:= \sum_{j\ge K} \left(\Pi_j(t) - \nu 2^{2j}\|u_j(t)\|_2^2\right),
```
where `\Pi_j` is shell-to-shell incoming flux.

Proposed RTSG regularity criterion:
```math
\sup_K \int_0^T \mathcal D_K^+(t)\,dt < \infty
\quad \Longrightarrow \quad
\text{no forward-cascade-driven singularity on } [0,T].
```
This is the corrected mathematical version of the old “λ monitoring” idea.

---

## 2. Priority ordering after reread

## Tier A — highest dollar value targets

### A1. Riemann Hypothesis — ACTIVE
**Why active:** Best current match between RTSG and a million-dollar problem.  
**What RTSG already has:** Construction 5, C5a fourth-moment bound, C5b Krein-space ghost projection, Weil positivity chain.  
**What is still open:** The wiki still admits the real gap: extension from sampled / theta-lifted positivity to **all** positive-definite test functions.

#### Immediate attack program
1. Formalize continuity of the Weil functional in a Schwartz topology.
2. Prove or disprove density of the theta cone `\mathcal C_\theta`.
3. If density holds, Step 5 closes by continuity.
4. If density fails, identify the missing cone generator and patch the operator class.

#### Novel RTSG contribution
Reframe the remaining RH obstruction as a **cone-density theorem**, not a vague “prove positivity for all test functions.” That is a much sharper target.

#### Brutal truth
Current RH confidence in the wiki is still too high. The live page says “gap potentially closed,” but the actual open issue remains nontrivial. Do **not** call this solved.

---

### A2. Yang–Mills Mass Gap — ACTIVE BUT NEEDS REWRITE
**Why active:** Million-dollar problem and the new Will-Field / center-symmetry structure actually helps.  
**What RTSG already has:** confinement signal, Polyakov-loop emphasis, GL layer, engine confinement proxy.  
**What is weak:** “Plateau mass in the fermion propagator = the gap” is not sufficient for Clay and is not the right level of rigor.

#### Immediate attack program
1. Rewrite the YM page around a **gauge-invariant transfer / effective-action gap**.
2. Use center symmetry and Polyakov-loop order-parameter structure as the confining anchor.
3. Define the mass gap as the smallest positive Hessian mode / transfer-matrix gap on gauge-invariant states.
4. Only then attach engine observables as support, not as proof.

#### Novel RTSG contribution
Use the coupled action `\Gamma[L,W]` above and show that a nonzero `|W_0|` stabilizes the center-symmetric vacuum by shifting the Polyakov-loop Hessian upward:
```math
\Delta_{YM}^2 = a + c|W_0|^2.
```
This is a real analytic bridge between the GL layer and confinement physics.

#### Brutal truth
The current wiki formulation is still too heuristic for the Clay target. The rewrite is mandatory.

---

### A3. Navier–Stokes Regularity — ACTIVE BUT LOWER PRIORITY THAN RH/YM
**Why active:** Million-dollar problem; the GL layer gives new energy functionals.  
**What RTSG already has:** Lyapunov / turbulence language, engine monitoring, new cubic Will-field unification idea.  
**What is wrong:** The current blow-up line is not dimensionally or tensorially coherent.

#### Immediate attack program
1. Replace the heuristic criterion with shell-wise flux–dissipation defects.
2. Couple the GL functional to high-frequency envelopes rather than raw velocity.
3. Treat turbulence as state-space shadowing of unstable coherent structures, not just `λ>0` talk.
4. Keep the Clay target narrowly on smooth-solution continuation; ignore weak nonuniqueness as a separate phenomenon.

#### Novel RTSG contribution
Define the high-frequency “instantiation burden” via `\mathcal D_K(t)` and attempt a continuation criterion of the form
```math
\sup_K \int_0^T \mathcal D_K^+(t)dt < \infty.
```
This is much closer to modern regularity language than the old page.

#### Brutal truth
This is not ready for a proof claim. It is a serious research program.

---

### A4. BSD / Hodge / P vs NP / Beal — PARKED
These remain real prize targets, but **the current RTSG machinery is not the right hammer**.

- **BSD:** arithmetic geometry; current RTSG operator / field language does not yet bite.
- **Hodge:** deep algebraic geometry and motives; no current RTSG leverage worth trusting.
- **P vs NP:** current RTSG is continuous-dynamical and geometric, not discrete-complexity sharp enough.
- **Beal:** lower strategic leverage than RH/YM/NS for the same dollar figure.

Keep them in the portfolio but do not spend prime cycles there now.

---

## Tier B — highest reputational value targets

### B1. Quantum Measurement Problem — BEST FIT IN THE ENTIRE STACK
This is where the bisimulation quotient is strongest.

#### Why RTSG fits
The quotient map gives a concrete structural candidate for “collapse without information destruction.”

#### Immediate paper target
Build `papers/companions/quantum_measurement.md` around:
1. quotient covariance;
2. induced unitary `\bar U_t` on the quotient space;
3. Born recovery as quotient-cell norm;
4. deformation parameters `\omega_i` for possible deviations.

#### Novel RTSG theorem candidate
**Quotient Unitarity Theorem (formalized version).**  
If `U_t` is unitary on `L^2(QS)` and bisimulation-covariant, then `U_t` induces a unitary flow on `L^2(PS)`.

This is the cleanest prestige play available.

---

### B2. Black-Hole Information / Horizon Unitarity — ACTIVE
The black-hole literature is still organized around a unitarity conflict that now appears to demand new physics on horizon scales rather than only at the singularity.

#### RTSG angle
Treat the horizon as a **bisimulation boundary**:
```math
\pi_H : QS_{\mathrm{BH}} \to PS_H.
```

Define redundancy-removed entropy
```math
S_{\mathrm{red}}(\pi_H)
:= H(\mu_{QS}) - H((\pi_H)_*\mu_{QS}).
```
Then apparent information loss can be reframed as quotienting of operationally redundant structure, while quotient evolution remains unitary.

#### Novel theorem candidate
Break assumption (2) in Giddings’ black-hole theorem by showing that distinct interior states need **not** have identical exterior evolution after horizon quotienting, because quotient classes can carry nontrivial induced boundary dynamics.

#### Brutal truth
This is promising, but the mathematics still needs construction of the horizon quotient and induced boundary algebra.

---

### B3. Quantum Gravity Witnesses — ACTIVE, MEDIUM PRIORITY
Current literature is explicit that gravity’s quantumness is still open, and that entanglement-only witnesses are not the whole story.

#### RTSG angle
Stage-0 CS can be recast as a **minimal quantum memory channel** rather than only an entangler.

Define a channel-distance witness:
```math
\mathcal Q_g
:= \inf_{\Lambda \in \mathrm{EB}} \|\mathcal E_g - \Lambda\|_\diamond,
```
where `EB` is the set of entanglement-breaking channels.

If Stage-0 gravity is genuinely instantiating, RTSG predicts
```math
\mathcal Q_g > 0.
```
This is sharper than “gravity entangles, therefore quantum.”

---

### B4. Dark Energy / Cosmology — SALVAGE AND REWRITE
The GL layer helps, but only after the invariance fix.

#### Corrected cosmology line
Do **not** use `\langle \rho_W \rangle`.  
Use the real invariant vacuum-energy density:
```math
\rho_W = |\partial W|^2 + \alpha |W|^2 + \frac{\beta}{2}|W|^4.
```
Then
```math
\Lambda_{\mathrm{eff}} \sim \langle \rho_W \rangle.
```

#### Stronger route
Add time dependence through a coarse-grained order parameter `W_0(a)` and write
```math
\Lambda_{\mathrm{eff}}(a) = \alpha |W_0(a)|^2 + \frac{\beta}{2}|W_0(a)|^4.
```
This is DESI-compatible in spirit and at least formally clean.

---

### B5. Turbulence — ACTIVE COMPANION TARGET
Modern turbulence work is increasingly state-space / exact-coherent-structure oriented. That matches RTSG better than the old scalar-Lyapunov framing.

#### RTSG angle
Interpret turbulence as motion through a network of unstable quotient states / coherent structures, with the Will field supplying an energy-landscape description.

#### Immediate deliverable
Write a companion note connecting:
- exact coherent structures;
- shadowing / recurrent dynamics;
- GL energy landscape for coarse-grained turbulent modes.

---

## 3. What to write now

### 3.1 arXiv / submission priority after reboot
1. **GRF essay** — keep narrow, horizon-only.
2. **Quantum measurement / bisimulation quotient** — highest prestige-to-effort ratio.
3. **Yang–Mills rewrite** — replace plateau-mass rhetoric with gauge-invariant gap functional.
4. **Hilbert–Pólya paper** — focus on theta-cone closure / density theorem.
5. **Navier–Stokes note** — cast as flux-defect continuation program, not proof claim.
6. **GL Theory of Instantiation** — patch invariance and stress-tensor formalism before submission.

### 3.2 Best immediate wiki patches
1. `rtsg/will_field_universality.md`
2. `rtsg/equations.md`
3. `problems/open.md`
4. `papers/companions/consciousness.md`
5. `papers/arxiv/gl_theory_of_instantiation.md`

---

## 4. Exact patch suggestions

### 4.1 `rtsg/will_field_universality.md`
Replace
```math
\mathcal L_{int} = \beta |W|^2 W
```
with
```math
V_{int}(W) = \frac{\beta}{2}|W|^4,
\qquad
\frac{\delta V_{int}}{\delta \bar W} = \beta |W|^2 W.
```
Add the sentence:
> The quartic term is the invariant interaction density; the cubic term appears in the field equation after variation.

### 4.2 `rtsg/equations.md`
Replace the cosmological constant line with
```math
\Lambda_{eff} = \left\langle \alpha |W|^2 + \frac{\beta}{2}|W|^4 \right\rangle_{PS}.
```
Replace the NS blow-up line with a scalar flux-balance functional, not a vector inequality.

### 4.3 `problems/open.md`
- RH: lower prose temperature; emphasize Step-5 density/closure gap.
- YM: rewrite around center symmetry / transfer gap / Hessian gap.
- NS: replace `λ < 0 / λ > 0` wording with high-frequency defect criterion.

### 4.4 `papers/companions/consciousness.md`
Add the missing assumption explicitly:
```math
q_1 \sim q_2 \Rightarrow U_t q_1 \sim U_t q_2.
```
Without this, the quotient-unitarity theorem is underspecified.

### 4.5 `papers/arxiv/gl_theory_of_instantiation.md`
Patch every place where a non-invariant cubic expression is used as a scalar observable.  
Use the quartic potential / cubic EOM distinction everywhere.

---

## 5. Final strategic verdict

### What is strongest right now
- **Quantum measurement** via bisimulation quotient.
- **Black-hole information** via horizon quotient.
- **Yang–Mills rewrite** via center symmetry + Will-field stabilizer.
- **RH** via theta-cone closure.

### What is not yet honest enough to claim
- RH solved.
- YM solved.
- Navier–Stokes solved.
- Cosmology fully derived.

### One-line summary
The reread revealed one critical formal bug and one major opportunity:  
**fix the GL layer first, then build the problem program around quotient unitarity, theta-cone closure, center-symmetry Hessian gaps, and flux-defect continuation.**
