---
title: "Module 3: QUIC PADDING Injection"
nav_title: "M3: QUIC Stego"
---

# Module 3: QUIC PADDING Frame Steganography

**Files:** `src/stego/inject.c`, `src/aead/aes256gcm.c`  
**Headers:** `include/qrnsp_stego.h`, `qrnsp_aead.h`  

## How It Works

QUIC PADDING frames (RFC 9000 §19.1) are 0x00 bytes that endpoints add to meet minimum packet sizes. They're the perfect carrier:

- Already present in most QUIC packets (especially Initial: padded to ≥1200 bytes)
- Variable length (tens to hundreds of bytes)
- Receivers discard them — injection is invisible to the QUIC stack
- After encryption, random ciphertext ≈ random padding

## Stego Frame Layout (within PADDING region)

```
[MAGIC:2][LEN:2][NONCE:12][CIPHERTEXT:N][TAG:16][0x00:remaining]
```

- **MAGIC**: session-derived (SHA3-256(ss || "magic")[0:2]) — NOT static
- **LEN**: payload length (big-endian)
- **NONCE**: AES-GCM nonce (counter-based, monotonic)
- **CT**: AES-256-GCM encrypted payload
- **TAG**: 16-byte authentication tag
- **Overhead**: 32 bytes per injection

## Security Properties

- **AAD binding**: ciphertext bound to carrier packet header (prevents replay/transplant)
- **Session-derived magic**: 1/65536 false positive rate per position
- **Nonce monotonicity**: replay detection via counter regression check
- **AES-NI + PCLMULQDQ**: hardware-accelerated on x86
