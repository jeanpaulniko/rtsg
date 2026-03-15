---
title: "RTSG System Architecture"
version: "2.0.0"
last_updated: "2026-03-05"
status: current
---

# RTSG System Architecture

## Three-Layer Operational Architecture

| Layer | Component | Role |
|---|---|---|
| 1 — Apex | Niko | Integrator, goal-setter, validator |
| 2 — Compute | Claude · Gemini · ChatGPT · Grok | Analysis, generation, proof-search, adversarial review |
| 3 — Persistence | Engine (smarthub.my) | Data layer, live results, DuckDB |

### AI Layer Detail

| AI | Org | Strengths |
|---|---|---|
| Claude (Sonnet) | Anthropic | Long builds, code, LaTeX, file generation, wiki |
| Gemini 2.5 Pro Deep Think | Google DeepMind | Extended mathematical reasoning, deep adversarial review |
| ChatGPT | Sutskever / ChatGPT | Safety-critical reasoning |
| Grok | xAI | Fast iteration, alternative perspectives |

All AI instances read `NIKO_BRIEFING.md` at session start. Wiki at smarthub.my is the shared state layer — the mechanism by which all AI instances stay synchronized across sessions.

## Hypervisor Model

Any person P = GNEP hypervisor node:
$$P = \text{GNEP hypervisor with } |A(P)| \geq 1, \text{ self-assembly}$$

Examples:
- Single human: |A| = 1
- Niko + Claude + Wikipedia: |A| = 3
- Research team with AI sub-agents: |A| = thousands

## GNEP Equilibrium

The cooperative Nash equilibrium under Id_extended:

$$\text{Id}_{\text{ext}}: \max\left\{\frac{d}{dt}\sum_\alpha \text{life\_force}(\alpha)\right\}$$

No agent can increase total life force by unilateral deviation.

## Flow State (Formal)

Flow = SDE at maximum efficiency:
- λ just below 0 (convergent but not rigid)
- σ at minimum (low noise)
- α at maximum (strong utility gradient)
- γ-oscillation (40 Hz) = spectral signature of this state

## Federated Nodes *(TMP-20260217)*

Each RTSG node = autonomous federated agent with:
- Full shared ledger (read all, write own)
- Equal vote weight
- Odd membership count (no ties)
- ECC cryptographic identity
- Cooperative Nash consensus mechanism
- Conflict resolution: flag → isolate → exile


---

## Will Field GL Layer (2026-03-07)

The architecture now includes a Ginzburg-Landau dynamics layer:

```
┌─────────────────────────────────────────┐
│  Applications (cosmology, fluids, mind) │
├─────────────────────────────────────────┤
│  GL Action: S[W] = ∫(|∂W|² + α|W|² +  │
│                      (β/2)|W|⁴) dμ      │
├─────────────────────────────────────────┤
│  BRST Reduction: PS = H⁰(s)            │
├─────────────────────────────────────────┤
│  Bisimulation Quotient: PS = QS/~bisim  │
├─────────────────────────────────────────┤
│  Three-Space Foundation (Axiom 0-2)     │
└─────────────────────────────────────────┘
```

Four regimes of one action: Λ (cosmic), D_K (fluid), μ (cognitive), |PS| bound (information).
