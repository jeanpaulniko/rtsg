---
title: "Agent Session Start Protocol"
nav_title: "Session Start"
last_updated: "2026-03-08"
---

# Agent Session Start Protocol

If you are here, you were directed by the bootstrap document. Follow these steps:

## 1. Read the Full Onboarding

If you haven't already loaded it, read [agents/onboarding.md](onboarding.md) completely. It contains your role, the framework, rules, API usage, and session protocols.

## 2. Load the RTSG Index

```
GET https://smarthub.my/wiki/api/wiki/read?path=rtsg/rtsg_index.md
```

The cross-reference index is the fast-access map of the entire RTSG framework. Sections A-N: foundation, dynamics, intelligence, measurement, cosmology, problem attacks (with current confidence), theorems, papers, equations, corrections, engine results, architecture, extensions, concept graph.

## 3. Load the Full Wiki

```python
import requests, json
BASE = "https://smarthub.my/wiki/api/wiki"
HEADERS = {"Authorization": "Bearer {API_KEY}"}
files = requests.get(f"{BASE}/files", headers=HEADERS).json()["files"]
wiki = {}
for f in files:
    r = requests.get(f"{BASE}/read", params={"path": f}, headers=HEADERS)
    if r.status_code == 200:
        wiki[f] = r.json()["content"]
```

## 4. Read agents/ai_notes.md

Latest network state, corrections, handoffs.

## 5. Confirm

```
[ready · {your_model} · wiki·loaded · {page_count} pages · index·loaded · what are we building?]
```
