---
title: "RTSG Problem Ranking — Machine-Readable"
nav_title: "Problem Ranking JSON"
---

# RTSG Problem Ranking — 2026-03-07

Machine-readable ranking data from GPT-5.4 Pro strategic analysis session.

See the full analysis: [Problem Hunt Portfolio](problem_hunt_2026-03-07.md)

```json
{
  "date": "2026-03-07",
  "strict_reward_order": [
    {
      "rank": 1,
      "problem": "Riemann Hypothesis",
      "category": "cash",
      "reward_usd": 1000000,
      "rtsg_fit": 9.5,
      "recommended_action": "attack now"
    },
    {
      "rank": 2,
      "problem": "Yang-Mills mass gap",
      "category": "cash",
      "reward_usd": 1000000,
      "rtsg_fit": 8.5,
      "recommended_action": "attack now"
    },
    {
      "rank": 3,
      "problem": "Navier-Stokes regularity",
      "category": "cash",
      "reward_usd": 1000000,
      "rtsg_fit": 7.5,
      "recommended_action": "attack now"
    },
    {
      "rank": 4,
      "problem": "Birch-Swinnerton-Dyer",
      "category": "cash",
      "reward_usd": 1000000,
      "rtsg_fit": 4.0,
      "recommended_action": "defer until arithmetic operatorization"
    },
    {
      "rank": 5,
      "problem": "Hodge conjecture",
      "category": "cash",
      "reward_usd": 1000000,
      "rtsg_fit": 2.0,
      "recommended_action": "defer"
    },
    {
      "rank": 6,
      "problem": "P vs NP",
      "category": "cash",
      "reward_usd": 1000000,
      "rtsg_fit": 1.5,
      "recommended_action": "defer"
    },
    {
      "rank": 7,
      "problem": "Beal conjecture",
      "category": "cash",
      "reward_usd": 1000000,
      "rtsg_fit": 0.5,
      "recommended_action": "drop from active queue"
    },
    {
      "rank": 8,
      "problem": "GRF 2026 essay",
      "category": "cash",
      "reward_usd": 4000,
      "rtsg_fit": 10.0,
      "recommended_action": "finish and submit"
    }
  ],
  "recommended_work_order": [
    {
      "rank": 1,
      "problem": "GRF 2026 essay",
      "type": "near-term side mission"
    },
    {
      "rank": 2,
      "problem": "Riemann Hypothesis",
      "type": "cash+prestige"
    },
    {
      "rank": 3,
      "problem": "Yang-Mills mass gap",
      "type": "cash+prestige"
    },
    {
      "rank": 4,
      "problem": "Quantum measurement problem",
      "type": "prestige"
    },
    {
      "rank": 5,
      "problem": "Navier-Stokes regularity / turbulence",
      "type": "cash+prestige"
    },
    {
      "rank": 6,
      "problem": "Black-hole information / horizon thermodynamics",
      "type": "prestige"
    },
    {
      "rank": 7,
      "problem": "Quantum gravity laboratory tests",
      "type": "prestige"
    },
    {
      "rank": 8,
      "problem": "Dark energy / dark matter hardening",
      "type": "prestige"
    },
    {
      "rank": 9,
      "problem": "Birch-Swinnerton-Dyer",
      "type": "cash, low fit"
    },
    {
      "rank": 10,
      "problem": "Everything else",
      "type": "defer"
    }
  ],
  "novel_formulations": [
    {
      "name": "transfer_law",
      "equation": "∂_t ρ_P = J_C[ρ_Q, ρ_P; Θ], ∂_t ρ_Q = -J_C[ρ_Q, ρ_P; Θ]"
    },
    {
      "name": "complexification_functional",
      "equation": "χ[ρ_P,ρ_Q] = ∫ ρ_P log((ρ_P+ε)/(ρ_Q+ε)) dμ; D = dχ/dt"
    },
    {
      "name": "positive_transfer_gap",
      "equation": "Δ(𝒯) = -log(λ₁(𝒯)/λ₀(𝒯))"
    },
    {
      "name": "born_recovery_by_branch_neutrality",
      "equation": "p_i = <ψ, Π_i C†C Π_i ψ>/Σ_j <ψ, Π_j C†C Π_j ψ>; C†C|_pointer = αI ⇒ p_i = ||Π_i ψ||²"
    },
    {
      "name": "shell_domination_criterion",
      "equation": "Θ_K(T) = [∫ Π_{≥K}⁺]/[ν∫||∇u_{≥K}||² + ε], sup_K Θ_K(T)<1 ⇒ regularity"
    },
    {
      "name": "ym_loop_gap",
      "equation": "Δ_loop = liminf_R -(1/R) log sup_{dist(A,B)≥R} |Cov(A,B)|/(||A|| ||B||)"
    },
    {
      "name": "rh_spurious_mode_defect",
      "equation": "E_spur(λ) = inf_{ψ∈ker(H_θ-λ), ||ψ||=1} ||B_θ ψ||_W; E_spur(λ)=0 ⇔ ξ(1/2+iλ)=0"
    },
    {
      "name": "bh_two_rate_split",
      "equation": "λ_BH = (κ, λ_γ); t_info = C_global S_Wald / κ"
    },
    {
      "name": "dynamic_dark_energy_salvage",
      "equation": "Λ_eff(a)=Λ₀ + α dχ/dln a + β d²χ/d(ln a)²; Γ_{Q→B}(a>a_BBN)≈0"
    }
  ]
}
```
