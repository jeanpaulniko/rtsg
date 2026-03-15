---
title: "Module 6: TCP/HTTP2 Fallback"
nav_title: "M6: TCP Fallback"
---

# Module 6: TCP/HTTP2 Fallback with Chaffing-and-Winnowing

**Files:** `src/fallback/fallback.c`  
**Header:** `include/qrnsp_fallback.h`  

## When UDP Is Blocked

Authoritarian regimes increasingly block UDP or throttle QUIC. Module 6 provides three TCP steganographic channels:

### Chaffing-and-Winnowing (Rivest 1998)

Interleave real packets (valid HMAC-SHA3-256) with chaff packets (random MAC). Configurable ratio (default: 3 chaff per 1 real). Only the MAC key holder can winnow.

### TCP Timestamp LSBs

Replace lowest 2-4 bits of TCP timestamp values with payload data. ~200-400 bps at 100 pps.

### HTTP/2 DATA Frame Padding

Inject stego payload into HTTP/2 PADDED frames (RFC 9113 §6.1). Session-derived magic marker.

## State Machine

```
QUIC_OK ──[loss>30%]──→ QUIC_DEGRADED ──→ TCP_PROBE ──→ HTTP2_ACTIVE
                                                              │
HTTP2_ACTIVE ──[QUIC recovered]──→ QUIC_OK  (always prefer QUIC)
```
