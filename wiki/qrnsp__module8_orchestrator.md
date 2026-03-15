---
title: "Module 8: Unified Orchestrator"
nav_title: "M8: Orchestrator"
---

# Module 8: Unified Pipeline Orchestrator

**Files:** `src/orchestrator/orchestrator.c`  
**Header:** `include/qrnsp_orchestrator.h`  

## Role

Single entry point tying modules 1-7 into a coherent pipeline.

## TX Pipeline

```
Application data
  → Message chunking [MSG_ID:4][CHUNK:2][TOTAL:2]
  → IF QUIC: PADDING injection (M3) + jitter (M4)
    ELSE IF TCP: chaff/timestamp/H2 padding (M6)
  → Traffic morphing (M7)
  → XDP packet send (M1)
```

## RX Pipeline

```
XDP packet receive (M1)
  → Probe for stego magic
  → IF QUIC: extract from PADDING (M3)
    ELSE: winnow/extract from TCP (M6)
  → Deserialize chunk header
  → Reassembly buffer (up to 4 concurrent messages)
  → Complete message delivery
```

## State Machine

```
INIT → HANDSHAKE → ACTIVE → [FALLBACK ↔ ACTIVE] → CLOSED
                          → JITTER_ONLY (both paths blocked)
                          → BLOCKED (nothing works)
```

## Session Lifecycle

1. `orch_init()` — generate keypair
2. `orch_handshake()` — KEM exchange, init all sub-modules
3. `orch_send()` / `orch_receive()` — data transfer
4. `orch_tick()` — periodic: cover traffic, fallback management
5. `orch_destroy()` — zeroize everything
