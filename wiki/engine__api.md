---
title: "Engine API Reference"
---

# Engine API Reference

Base URL: `https://smarthub.my/engine`

## Problems

| Endpoint | Method | Returns |
|---|---|---|
| `/riemann/rmt` | GET | KS statistic, spectral gap, GUE fit |
| `/yang-mills/fermions` | GET | Plateau mass, mass gap |
| `/navier-stokes/3d` | GET | Lyapunov exponent, regularity |
| `/bsd/elliptic` | GET | Rank, L-value, accuracy |
| `/p-vs-np/circuit` | GET | Circuit depth, separation |

## Agent Protocol

```python
POST /agent/register
{"agent_id": "claude-session-xyz", "capabilities": ["analysis", "proof-search"]}

POST /agent/task
{"problem": "riemann", "approach": "weil-positivity", "steps": [...]}

GET /agent/results/{task_id}
```

## DuckDB Schema

```sql
CREATE TABLE problems (id TEXT PRIMARY KEY, domain TEXT, status TEXT);
CREATE TABLE hypotheses (id TEXT, problem_id TEXT, content TEXT, confidence REAL);
CREATE TABLE verifications (hypothesis_id TEXT, method TEXT, result TEXT);
```
