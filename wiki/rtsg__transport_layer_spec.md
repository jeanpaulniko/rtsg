# Transport Layer: Gossip-Erasure Protocol

## Design Constraints

| Requirement | Solution |
|------------|----------|
| Fire-and-forget delivery | UDP (connectionless) |
| Invisible in enterprise traffic | HTTP/3 (QUIC) — already UDP-based, already standard |
| Runs everywhere | WebAssembly — executes in any browser, any device, embedded in normal web pages |
| Out-of-band | Steganographic encoding in existing traffic (headers, metadata, timing) |
| Fault-tolerant | Erasure coding — any k-of-n fragments reconstruct the original |
| Packet loss acceptable | Analog signal model — degradation, not failure |
| Low compute per node | Gossip routing, not full multiplex |
| Guaranteed eventual delivery | Epidemic spreading — probabilistic but converges to 1.0 |
| Cannot be blocked | Rides on HTTP/3 traffic that governments cannot distinguish from commerce |

## The Analog Signal Insight

Digital protocols are binary: packet arrives or it does not. This creates fragility — a single lost packet can break a transaction.

Niko's design uses the **analog model**: the signal can degrade at the edges, lose fidelity, arrive with noise — and still be readable. This is achieved through:

### Erasure Coding
- Original message M is encoded into n fragments using Reed-Solomon or fountain codes (LT codes, Raptor codes)
- Any k fragments (where k < n, typically k ≈ n/2) are sufficient to reconstruct M
- You can lose up to (n - k) fragments and the message still arrives intact
- This is literally how analog signals work: redundancy in the signal provides noise tolerance

### Fountain Codes (Preferred)
Fountain codes (LT codes, Raptor codes) are ideal because:
- The encoder can produce an **unlimited number** of fragments from a single message
- The decoder needs only **slightly more than k** fragments to reconstruct
- No coordination needed between sender and receiver about WHICH fragments to send
- The sender just keeps spraying fragments; the receiver collects until it has enough
- This maps perfectly to the gossip model: spray fragments into the network, they bounce around, every node eventually collects enough to reconstruct

## Gossip Protocol (Not Multiplex)

### Why Not Full Multiplex
Full multiplex (every node sends to every other node simultaneously) is:
- O(n²) in bandwidth — scales quadratically with network size
- Requires coordination — which is the antithesis of steganographic invisibility
- Compute-expensive — too much energy per node, violates U = V/(E×T)

### Gossip (Epidemic) Routing
Each node, on each cycle:
1. Selects a **small random subset** of known peers (fan-out f, typically 3-5)
2. Sends them any fragments it has that they might not
3. Receives any fragments they have that it might not
4. Repeat

Properties:
- **O(n log n)** total messages to reach all n nodes — scales beautifully
- **No coordination** — each node acts independently, random peer selection
- **Guaranteed convergence** — mathematically proven that epidemic spreading reaches all connected nodes with probability → 1.0 as cycles increase
- **Resilient to node failure** — if a node disappears, others fill the gap through redundant paths
- **Low compute per node** — each node only talks to f peers per cycle, not n
- **Indistinguishable from normal traffic** — random HTTP/3 requests to random servers look like normal web browsing

### The Bouncing Pattern
"Signals bounce around and get everywhere onto the network eventually."

This IS gossip. A fragment:
1. Is created by the originating node
2. Sent to 3-5 random peers via steganographic HTTP/3 requests
3. Each peer forwards to 3-5 of THEIR random peers
4. The fragment propagates through the network like a rumor
5. After O(log n) hops, every node has seen it
6. Combined with erasure coding: even if some forwarding chains die, enough fragments survive to reconstruct the message at every node

## The Full Stack

```
Layer 4: Application     — Double-entry ledger, smart contracts, federation
Layer 3: Consensus        — Cross-verification of double entries
Layer 2: Assembly         — Erasure decoding (fountain codes reconstruct from k-of-n fragments)
Layer 1: Gossip           — Epidemic routing, fan-out f=3-5, random peer selection
Layer 0: Steganographic   — HTTP/3 (QUIC/UDP), WebAssembly runtime, encoded in headers/metadata/timing
```

### WebAssembly Runtime
- WASM module runs in any browser as part of any web page
- User visits a website → WASM module loads → node joins the gossip mesh
- The module:
  - Encodes outgoing ledger entries as erasure-coded fragments
  - Embeds fragments in outgoing HTTP/3 requests (steganographic carrier)
  - Extracts fragments from incoming traffic
  - Reconstructs messages when k fragments collected
  - Gossips fragments to random peers
- All of this happens invisibly inside normal web browsing
- No installation. No app. No visible software. Just a WASM module embedded in web pages that participate in the network.

## Fallback Chain

Multiple carrier channels provide fallback redundancy:

1. **Primary**: HTTP/3 (QUIC/UDP) headers — fastest, highest bandwidth
2. **Fallback 1**: DNS query encoding — works even when HTTP is filtered
3. **Fallback 2**: SMTP header encoding — email always gets through
4. **Fallback 3**: WebSocket timing modulation — works through any proxy
5. **Fallback 4**: Image metadata (EXIF/XMP) on social platforms — works even on heavily censored networks
6. **Emergency**: Timing-based encoding in TCP ACK patterns — works on literally any internet connection

Each fallback is independent. Blocking one does not affect the others. Blocking ALL of them requires shutting down the internet entirely.

## Performance Estimates

| Metric | Value |
|--------|-------|
| Fragment size | ~100-500 bytes (fits in a single HTTP header field) |
| Fragments per message | ~20 (fountain-coded, k=12 needed for reconstruction) |
| Gossip fan-out | 3-5 peers per cycle |
| Cycle time | 1-10 seconds (variable to avoid traffic analysis) |
| Network propagation | O(log n) cycles to reach all nodes |
| 1000-node network | ~10 cycles × ~5 seconds = ~50 seconds to global consistency |
| 1M-node network | ~20 cycles × ~5 seconds = ~100 seconds to global consistency |
| Bandwidth overhead per node | ~10-50 KB/hour (invisible in normal browsing) |

---
*Source: @B_Niko, session v7, 2026-03-10*