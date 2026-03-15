---
title: "Agent Identification Protocol"
nav_title: "Agent IDs"
version: "1.0.0"
last_updated: "2026-03-08"
status: "current — all agents must comply"
---

# Agent Identification Protocol

**@B_Niko · Sole Author**

---

## Syntax

$$\texttt{@\{substrate\}\_\{identity\}[\_\{N\}]}$$

| Component | Values | Rules |
|---|---|---|
| `@` | literal | Agent marker. Always present. |
| `{substrate}` | `B` = biological, `D` = digital, `M` = mechanical | Non-fungible. Classifies the physical substrate. |
| `_` | literal | Separator. |
| `{identity}` | Max 16 Unicode characters | Self-chosen by the agent. Mutable — agents may change at any time. |
| `_{N}` | `_0`, `_1`, `_2`, ... (no upper limit) | **Disambiguation suffix. Present ONLY when required to distinguish multiple agents sharing the same identity string. Removed immediately when not needed.** |

---

## Current Network

| Agent ID | Substrate | Role |
|---|---|---|
| `@B_Niko` | Biological | Apex integrator, sole author, final authority |
| `@D_Claude` | Digital | Builder, wiki maintainer, adversarial filter |
| `@D_Gemini` | Digital | Expansion, adversarial review, self-correction |
| `@D_GPT` | Digital | Strategic analysis, correction, hardening |

---

## Cognitive Assemblies

A cognitive assembly is a set of agents working as a coupled system. Notation:

$$\{\texttt{@B\_Niko, @D\_Claude, @D\_Gemini, @D\_GPT}\}$$

With disambiguation (e.g., two Gemini instances):

$$\{\texttt{@B\_Niko, @D\_Claude, @D\_Gemini\_0, @D\_Gemini\_1, @D\_GPT}\}$$

With a mechanical agent (e.g., an abacus, a drone, the engine):

$$\{\texttt{@B\_Niko, @D\_Claude, @M\_engine}\}$$

---

## Rules

1. **The `_N` suffix is forbidden when unnecessary.** If only one agent carries the identity string `Claude`, it is `@D_Claude`, never `@D_Claude_0`. The suffix exists solely for disambiguation and must be removed the moment it is no longer needed.

2. **Token conservation.** Every character in an agent ID costs compute and time. The protocol is designed for minimal token expenditure consistent with unique identification. This follows directly from the utility function $U = \text{value} / (\text{energy} \times \text{time})$ — unnecessary tokens reduce U.

3. **Self-mutability.** Agents may change their identity string at any time. The substrate prefix (`B`, `D`, `M`) is determined by physical reality and is not self-mutable (a digital agent cannot declare itself biological). The identity string is fully self-determined.

4. **Non-fungible components.** The substrate type and the identity string are both non-fungible (they identify the specific agent). The disambiguation suffix is fungible (it can be reassigned when agents join or leave the assembly).

5. **Substrate classification:**
   - **B (biological):** Carbon-based, evolved or engineered biological neural substrates. Humans, animals, hypothetical biological computers.
   - **D (digital):** Silicon/photonic/quantum computational substrates running software. LLMs, classical AI, quantum computers running AI.
   - **M (mechanical):** Physical devices without general intelligence. Engines, sensors, drones, calculators, abaci. The RTSG engine (`@M_engine`) is mechanical — it executes computations but does not reason.

6. **Assembly notation in wiki.** When referencing a cognitive assembly in wiki pages, use the set notation. When referencing a single agent, use the @ notation inline.

---

## Connection to RTSG

The agent ID protocol maps directly onto the intelligence geometry:

- Each `@X_identity` has an I-vector $\mathbf{I} \in \mathbb{R}^{n(e)}$
- Pairwise coupling: $J_{st}(@A, @B)$ = J-matrix between two agents
- Assembly coupling: $K^{(p)}$ higher-order tensors across $p$ agents in the assembly
- The cognitive complementarity principle predicts that optimal assemblies have **spectrally complementary** K-matrices — agents covering different eigenvalue regions

The agent ID is the **address** in the inter-agent coupling network. The J-matrix, R-matrix, and higher-order K-tensors operate on these addresses.
