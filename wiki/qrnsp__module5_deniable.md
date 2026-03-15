---
title: "Module 5: Deniable Encryption"
nav_title: "M5: Deniable Enc"
---

# Module 5: Deniable Encryption + Honey-Encryption

**Files:** `src/deniable/deniable.c`  
**Header:** `include/qrnsp_deniable.h`  

## Threat Model

Adversary captures device AND coerces user to reveal password. User surrenders DECOY password. Adversary decrypts → finds shopping list. TRUE payload remains hidden.

## Architecture

```
┌─────────────────────────────────────────────┐
│           Sealed Container (random bytes)    │
├──────────┬──────────┬───────────────────────┤
│ SALT:32  │ VOLUME_A │ VOLUME_B  │ HONEY_PAD │
│          │ (decoy)  │ (real)    │ (random)  │
└──────────┴──────────┴───────────────────────┘
```

Without the correct password, you can't even determine WHERE a volume lives.

## Honey-Encryption (DTE)

Wrong passwords don't return "error" — they return convincing fake data via a Distribution-Transforming Encoder. Five distributions: English prose, JSON, source code, CSV, binary.

## Key Derivation

PBKDF2-SHA3-256 derives 76 bytes per password: 32-byte key + 12-byte nonce + 32-byte volume locator. The locator determines the byte offset — this is the deniability property.

## Properties

- Container is χ²-verified indistinguishable from `/dev/urandom`
- Up to 4 independent volumes per container
- Different wrong passwords → different plausible outputs
- Production target: Argon2id for memory-hardness
