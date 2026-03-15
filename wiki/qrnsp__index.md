---
title: "QR-NSP: Quantum-Resistant Network Steganography Protocol"
nav_title: "QR-NSP"
---

# QR-NSP — Quantum-Resistant Network Steganography Protocol

**Mission:** Enable people living under authoritarian regimes to communicate freely with the outside world through undetectable, deniable, quantum-resistant channels hidden within ordinary internet traffic.

**Author:** Jean-Paul Niko / BuildNet  
**License:** AGPL-3.0-or-later  
**Status:** Architecture complete — 8 modules, 9,593 LOC, 32 files  

## Why QR-NSP?

Existing censorship-circumvention tools (Tor, Signal, VPNs) are *detectable*. A regime that can identify the traffic can block it. QR-NSP hides covert data inside traffic that is statistically indistinguishable from normal web browsing, video streaming, or voice calls. Even if the adversary captures the device, honey-encryption ensures they cannot prove the covert channel ever existed.

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│  Module 8: Unified Orchestrator (pipeline controller)   │
├─────────────────────────────────────────────────────────┤
│  Module 7: Traffic Morphing (statistical fingerprint)   │
├─────────────────────────────────────────────────────────┤
│  Module 5: Deniable Encryption (honey-enc, multi-KDF)   │
├──────────────────────┬──────────────────────────────────┤
│  Module 6: TCP/HTTP2 │  Module 4: Temporal Jitter       │
│  Fallback (chaff)    │  (timing channel)                │
├──────────────────────┴──────────────────────────────────┤
│  Module 3: QUIC PADDING Injection (stego payload)       │
├─────────────────────────────────────────────────────────┤
│  Module 2: ML-KEM-1024 + X25519 (PQC handshake)        │
├─────────────────────────────────────────────────────────┤
│  Module 1: XDP Interceptor (packet capture + ring)      │
├─────────────────────────────────────────────────────────┤
│  Hardware: NIC → L2/L3 Cache → DDR5 RAM-disk            │
└─────────────────────────────────────────────────────────┘
```

## Module Roadmap

| # | Module | Status | Description |
|---|--------|--------|-------------|
| 1 | [XDP Interceptor](module1_xdp.md) | ✅ | eBPF packet capture + ring buffer |
| 2 | [ML-KEM-1024 Handshake](module2_crypto.md) | ✅ | Post-quantum hybrid key exchange |
| 3 | [QUIC PADDING Injection](module3_stego.md) | ✅ | Primary steganographic channel |
| 4 | [Temporal Jitter](module4_jitter.md) | ✅ | Spread-spectrum timing channel |
| 5 | [Deniable Encryption](module5_deniable.md) | ✅ | Honey-enc + multi-password KDF |
| 6 | [TCP/HTTP2 Fallback](module6_fallback.md) | ✅ | Chaffing, TCP timestamps, H2 padding |
| 7 | [Traffic Morphing](module7_morph.md) | ✅ | Statistical profile matching |
| 8 | [Unified Orchestrator](module8_orchestrator.md) | ✅ | Pipeline controller |

## Steganographic Channels

| Channel | Transport | Bandwidth | When Used |
|---------|-----------|-----------|-----------|
| QUIC PADDING | UDP/QUIC | ~1000+ bytes/pkt | Primary (QUIC available) |
| Temporal Jitter | Packet timing | ~4 bps | Always (supplementary) |
| Chaffing-and-Winnowing | TCP | ~1000 bytes/pkt | UDP blocked |
| TCP Timestamp LSBs | TCP | ~200 bps | UDP blocked |
| HTTP/2 DATA Padding | TCP/HTTP2 | ~200 bytes/pkt | UDP blocked |

## Design Principles

1. **Undetectable > Unbreakable.** If they can't see it, they can't block it.
2. **Deniable by default.** Honey-encryption defeats rubber-hose cryptanalysis.
3. **Post-quantum from day one.** ML-KEM-1024 (FIPS 203).
4. **Zero-copy everywhere.** XDP native mode, mmap'd buffers, SIMD crypto.
5. **Degrade gracefully.** QUIC → TCP → jitter-only.

## Quick Start

```bash
# Prerequisites (Ubuntu/Debian)
sudo apt install clang llvm libbpf-dev linux-headers-$(uname -r) libelf-dev zlib1g-dev

# Build everything
make all

# Run all tests
make test

# Start daemon (monitor mode)
sudo ./build/qrnsp-daemon -i eth0 -p 443
```

## Source Code

Full source: [qrnsp/source/](source/index.md)

## Related

- [RTSG Framework](../rtsg/master.md) — The theoretical framework QR-NSP extends
- [Intelligence Arena](../arena/index.md) — Multi-agent evaluation system
