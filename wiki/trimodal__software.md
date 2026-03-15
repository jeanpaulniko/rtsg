# TRIMODAL — Software Architecture

Same codebase for X and C variants. HAL swaps at deploy time.

---

## Stack

```
Owner Interface (app / voice / Neurosity Crown)
  Intelligence Engine (RTSG P/C/A encoding, Drive D)
    Mission Planner | Damage Assessor | Quantum Planner
      Unified Compute API (e- | gamma | q | mech)
        Federated Node Layer (11 nodes, Raft consensus)
          CRDT memory | QUIC transport | Protobuf encoding
            HAL (Actuator | Sensor | Power | Comms drivers)
```

---

## Module Status

Built and tested: node, transport (photonic + QUIC), protocol.proto, unified API, HAL, mission planner, damage assessor, RTSG bridge, LLM engine, main loop, consensus/election, federated memory, power manager, locomotion optimizer, quantum planner, entangled QUBO, INS fusion, sensor stack, full integration test, cargo/solar analysis, pareto weight optimizer.

Planned: dashboard, leg IK solver, end effector controller, obstacle avoidance, sample collection, deploy manifest.

---

## Quantum Locomotion

Key innovation: power depletion is entangled across timesteps.

```python
# Greedy: sees only current step
# Quantum: sees full 8-step horizon simultaneously
# Entangled QUBO adds coupling terms:
# Q[vidx(t_early, m_expensive), vidx(t_late, m_needs_power)] += penalty

# Sim solver:
x, energy = QuantumAnnealingSim(n_reads=2000).solve(Q)
# Hardware swap (drop-in):
x, energy = dwave_sampler.sample_qubo(Q).first.sample
```

---

## RTSG Encoding Per Cycle

```python
enc = bridge.encode_state(world_state, system_status, mode, substrate)
# P_magnitude, synergy_score, total_obstruction, effective_capability, semantic
```

---

## Owner Interface

Voice: natural language → NLP → intent → Mission planner  
App: drag-and-drop waypoints + objectives  
Neurosity Crown: passive intent inference → RTSG I-vector → autonomous behavior adjustment  
API: full programmatic control, same interface as intelligence engine

---

## Inter-TRIMODAL Swarm

Peer-to-peer. No central server. Owner consent model. Emergent coordination from RTSG Drive D across multiple owner-intent vectors.
