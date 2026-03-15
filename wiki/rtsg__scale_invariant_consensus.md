# Scale-Invariant Consensus

## Core Theorem (Informal)

The hypervisor switching law is a **universal consensus mechanism** that operates identically at every scale of organization:

**P(leader = i) = exp(β · f_i) / Σⱼ exp(β · f_j)**

The only things that change between scales are:
1. What the agents are (dimensions, neurons, nodes, people)
2. What f_i measures (activation, fitness, reputation, competence)
3. What β is (neural temperature, network responsiveness, social inertia)

## Mathematical Properties

### Convergence
The gossip protocol guarantees that all nodes eventually share the same ledger state. From identical ledger state, all nodes compute identical softmax output. Therefore: **consensus is a mathematical consequence of data propagation**, not a separate protocol.

No voting. No rounds. No quorum. Just math on shared data.

### Hysteresis (Stability)
The current Agent Zero has inertia (hysteresis parameter h):

**f_current += h**

This prevents thrashing — the leader does not switch on every minor fluctuation. The same mechanism prevents consciousness from switching hypervisor dimensions on every minor stimulus. Stability is built into the equation.

### Threshold (Minimum Competence)
Nodes below a threshold θ are excluded from the softmax entirely:

**If f_i < θ, then P(leader = i) = 0**

This prevents incompetent or malicious nodes from ever becoming Agent Zero, regardless of how few competitors exist. In consciousness: this is why a fully traumatized dimension (f_i ≈ 0) never becomes hypervisor.

### Will Override (Emergency)
A meta-level override exists for crisis situations:

**If emergency(t) = true, then leader = argmax(crisis_competence_i)**

In consciousness: the fight-or-flight override that forces Kinesthetic to hypervisor status regardless of what was running. In the network: a protocol-level emergency that forces the most crisis-capable node to lead.

## Connection to Least Action

The softmax leader election minimizes total system energy:
- The most optimized node requires the least energy to lead
- Switching only when a clearly better leader emerges (hysteresis) minimizes switching cost
- The system naturally settles into the lowest-energy configuration

This IS the principle of least action applied to distributed consensus.

**S = ∫ (E_switching + E_leadership - V_coordination) dt → minimize**

---
*Source: @B_Niko, session v7, 2026-03-10*