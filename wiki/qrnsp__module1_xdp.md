---
title: "Module 1: XDP QUIC Interceptor"
nav_title: "M1: XDP Interceptor"
---

# Module 1: XDP QUIC Interceptor

**Files:** `src/xdp/qrnsp_xdp.c`, `src/daemon/daemon.c`, `include/qrnsp.h`  
**Dependencies:** Linux kernel ≥ 5.8, libbpf  

## Overview

Kernel-side eBPF program attached to a NIC that classifies QUIC packets by inspecting the first byte (RFC 9000 Fixed Bit), filters by configurable IP/port, and copies payloads into a BPF ring buffer for userspace consumption.

## Architecture

- **XDP program** (`qrnsp_xdp.c`): eBPF verifier-safe, bounded access, classifies QUIC long/short headers
- **Ring buffer**: `BPF_MAP_TYPE_RINGBUF` (32 MiB), lock-free SPSC
- **Daemon** (`daemon.c`): Polls ring buffer via libbpf, decodes headers, scans for PADDING regions
- **Slot structure**: 64-byte cache-line aligned (2176 bytes = 34 cache lines per slot)

## Key Design

- `XDP_PASS` mode: non-destructive monitoring (packet continues through kernel)
- SKB mode for broad compatibility; one flag change to native/HW for volcanic performance
- Configurable via BPF maps: enable/disable, target IP, target port, monitor/intercept mode

## QUIC Detection

```
RFC 9000 §17.2:
  Bit 7 (0x80) = Long Header flag
  Bit 6 (0x40) = Fixed Bit (MUST be 1 for QUIC)

  Fixed Bit set → QUIC packet
  Long Header set → handshake (version extractable from bytes 1-4)
```
