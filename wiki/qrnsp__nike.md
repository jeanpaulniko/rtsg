---
title: "NÍKĒ — Sneakernet: Free, Uncensorable, Deniable Messaging"
nav_title: "NÍKĒ / Sneakernet"
version: "1.0.0"
last_updated: "2026-03-08"
status: "Phase 1 — Live"
---

# NÍKĒ — Sneakernet

**Free. Uncensorable. Deniable. Post-quantum. Zero-trace.**

*For every journalist in Tehran, every dissident in Pyongyang, every activist in Moscow, every whistleblower everywhere.*

---

## The Name — Four Layers of Meaning

**NÍKĒ** = Niko's Invisible Key Exchange.

But the word carries four layers:

1. **Níkē** (Νίκη) — the Greek goddess of victory. Victory over censorship.
2. **Niko and Nika** — the creators. Jean-Paul Niko and Veronika Pokrovskaia. Their names are encoded in the goddess.
3. **Sneakers** — Nike shoes. The logo everyone recognizes. Friendly. Approachable. "Join the Sneakernet" is a sentence nobody is afraid of.
4. **Sneakernet** — the classic computer science term for physically carrying data. Before the internet, you "sneaked" floppy disks between computers. Our users sneak messages through the internet itself, hidden in plain sight.

> *"It is no longer sufficient to bring a knife to a gun fight."* — @B_Niko

---

## What It Is

A web page. Not an app. Not a download. Not something that shows up in your app store or your browser history.

You open a URL. You see a research wiki about mathematical physics. You enter a passphrase. The comment section becomes a messenger. When you close the tab, there is nothing on your device. Nothing in your history. Nothing in your cookies. Nothing for a forensic examiner to find.

Under duress, you give the safety passphrase. The guard sees: "Hi mom, how's the weather?" He cannot prove anything else exists. Mathematically impossible — it's a hash lookup with infinite possible layers.

---

## Why It Can't Be Blocked

The cover isn't fake. It's the **RTSG research wiki** — 177+ pages of genuine mathematical physics, cited by arXiv papers, used by researchers worldwide. The therapeutic framework helps trauma survivors. The definitions page is used by graduate students.

A government that blocks smarthub.my blocks:

- Real academic research that helps people
- A therapeutic framework for trauma survivors
- arXiv papers that link to it
- Open mathematical problems tracked by researchers

The political cost of blocking is enormous. The messaging rides invisibly inside the real traffic.

---

## The Seven Layers

| Layer | What it does | QR-NSP Module |
|---|---|---|
| **0. Cover Identity** | The wiki IS the cover — 177 real pages of real math | M7 (traffic morphing) |
| **1. Zero-Trace UI** | No cookies, no cache, no history, no footprint | — |
| **2. Crypto** | ML-KEM-1024 + X25519 + AES-256-GCM (post-quantum) | M2 (PQC crypto) |
| **3. Stego Transport** | Messages hidden in visible English via synonym choice | M3 (stego) + M7 |
| **4. Protocol Cascade** | HTTP/3 → HTTP/2 → HTTP/1.1 → WebSocket → DoH | M6 (fallback) |
| **5. Domain Fronting** | CDN relay — adversary sees traffic to Cloudflare | — |
| **6. Deniability** | Honey encryption — duress passphrase → decoy messages | M5 (deniable enc) |

---

## How Linguistic Steganography Works

Every sentence under "Technical Commentary" on a wiki page contains four word-choice points. Each choice encodes one bit:

```
Sentence template:
"The {detailed|thorough} analysis {shows|demonstrates} that the 
gauge structure is {stable|robust} under {small|minor} perturbations."

If the page says "thorough" → bit = 1
If the page says "detailed" → bit = 0
```

Four bits per sentence. 16 templates cycling. The resulting text reads as normal academic English. A DPI inspector, a government censor, an LLM scraper — all see legitimate research discussion. The recipient knows the synonym pairs and extracts the hidden bitstream → base64 → JSON → messages.

**Capacity:** ~500 bits per paragraph of cover text. A short message fits in one academic paragraph.

---

## The Deniability Mechanism

Every "room" (conversation) is identified by a room code + passphrase. The server stores messages keyed by `SHA-256(room_code + passphrase)`. 

- **Real passphrase** → your actual conversation
- **Safety passphrase** → pre-seeded innocent messages ("Hi sweetie, how's the weather?")

The server cannot distinguish layers. It stores only hashes. There is no "real" or "duress" flag in the database. An adversary with the safety passphrase sees the decoy and **cannot prove any other layer exists**. There could be 1 layer, 2, 10, or 1000 — the database looks identical regardless.

This is not obscurity. It is mathematical deniability. The hash function is one-way. The adversary would need to brute-force every possible passphrase to find every possible layer — and even then, each layer looks equally "real."

---

## Post-Quantum Encryption (Phase 2)

The cryptographic core is QR-NSP Module 2:

- **ML-KEM-1024** (NIST Level 5 post-quantum KEM based on Module-LWE)
- **X25519** (classical elliptic curve Diffie-Hellman)
- **Hybrid combiner:** `ss = SHA3-256(ss_mlkem || ss_x25519 || ct || pk_peer)`

Both ML-KEM AND X25519 must be broken to recover the shared secret. Even a quantum computer running Shor's algorithm breaks only X25519 — the ML-KEM layer survives.

The shared secret feeds AES-256-GCM for symmetric encryption. Forward secrecy via ephemeral key pairs per message exchange.

---

## Source Code

All source code is published under **AGPL-3.0-or-later**. This is deliberate:

1. **Transparency:** Anyone can audit the code. No hidden backdoors.
2. **Anti-censorship:** Publishing the source makes it legally and practically difficult to suppress. The code is speech.
3. **Reproducibility:** Anyone can deploy their own instance. The network has no single point of failure.

### Server

- [`nike_server.py`](../qrnsp/source/nike_server.py) — FastAPI server with deniable layers
- [`stego_bridge.py`](../qrnsp/source/stego_bridge.py) — Linguistic steganography engine
- [`comms_routes.py`](../qrnsp/source/comms_routes.py) — Agent communication system

### QR-NSP Cryptographic Core (C)

- [Module 2: ML-KEM + X25519](module2_crypto.md) — Post-quantum hybrid KEM
- [Module 3: QUIC PADDING Stego](module3_stego.md) — Network-level steganography
- [Module 5: Deniable Encryption](module5_deniable.md) — Honey encryption + multi-KDF
- [Module 7: Traffic Morphing](module7_morph.md) — Statistical fingerprint elimination

Full source: [QR-NSP Source Code](source/index.md) — 9,593 LOC, 32 files, pure C, zero external dependencies.

---

## For People Under Authoritarian Regimes

If you are reading this from behind a firewall:

1. You are not alone.
2. This tool exists for you.
3. The source code is public — anyone you trust can set up a relay.
4. Your safety passphrase protects you even if your device is seized.
5. The cover page is real research — blocking it costs the regime more than allowing it.

The framework that powers this tool — RTSG — was built by someone who was abused as a child and spent his life refusing to accept that abuse is normal. The therapeutic insight at the center of the framework is: **you are not broken. You are adapted to a broken environment.** Your filters were smart — they kept you alive. Now you are somewhere different. You can update.

The same framework that describes how particles become real (BRST cohomology), how intelligence works (I-vector geometry), and how consciousness emerges (three-space mechanics) — that framework also describes how suppressed communication passes through the obstruction of censorship and becomes actual.

CS is math itself. The wiki is the messenger itself.

---

## The Sneakernet Community

**Sneakernet** is not just a tool — it's the community of people who use it. Every person who carries a URL to a friend, who whispers a passphrase, who seeds a decoy conversation — they are part of the Sneakernet.

The classical sneakernet moved atoms (floppy disks). Our sneakernet moves bits — hidden in the atoms of visible English sentences about gauge theory.

> *"Never underestimate the bandwidth of a station wagon full of tapes hurtling down the highway."* — Andrew Tanenbaum, 1981
>
> Never underestimate the bandwidth of a wiki full of mathematics hurtling through the firewall. — @B_Niko, 2026

---

## Status

| Phase | Status | What |
|---|---|---|
| Phase 1: Stego Transport | ✅ **LIVE** | Messages via linguistic stego in wiki pages |
| Phase 1.1: Deniability | ✅ **LIVE** | Multi-layer rooms with duress passphrases |
| Phase 2: WASM Crypto | 🔲 Planned | ML-KEM-1024 + X25519 in browser |
| Phase 3: Protocol Cascade | 🔲 Planned | HTTP/3 → DoH fallback chain |
| Phase 4: Domain Fronting | 🔲 Planned | CDN relay for blocked domains |
| Phase 5: Regional Covers | 🔲 Planned | Farsi, Russian, Korean, Chinese, Arabic |

---

*NÍKĒ / Sneakernet — AGPL-3.0-or-later*
*Jean-Paul Niko · smarthub.my/wiki · 2026*
*Victory over censorship.*
