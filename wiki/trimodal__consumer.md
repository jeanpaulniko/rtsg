# TRIMODAL-C — Consumer Companion

The consumer variant. Buildable by anyone. One per sentient being.

---

## Philosophy

TRIMODAL-C is not a smart home device. It is not Alexa with legs.

It is a physical extension of your intelligence and will — a manservant, butler, protector,
and companion that acts on your behalf in the physical world, learns your preferences,
and escalates to you only when it genuinely needs guidance.

It runs RTSG. It knows who you are.

---

## Form Factor

| Parameter | Value |
|---|---|
| Mass | ~15kg |
| Legs | 6 (consumer) or 8 (extended) |
| Claws | 2 retractable coconut-crab style |
| Height standing | ~45cm |
| Height low crawl | ~15cm |
| Top speed flat | ~3 m/s (roll mode) |
| Battery | Si-C solid state, 600+ Wh/kg |
| Endurance | 3-7 days depending on activity |
| Charging | Solar suit + inductive pad + standard outlet |

---

## What It Does

### Home
- Carries groceries, packages, laundry
- Fetches objects by name
- Patrols perimeter, monitors entry points
- Wakes you at optimal sleep cycle point
- Monitors biometrics passively (Neurosity Crown integration)

### City
- Follows owner through crowds
- Carries bags, equipment, cargo (up to 5-10kg)
- Scouts ahead (camera + sensor array)
- Social navigation in crowds
- Hails transportation, holds doors

### Outdoor
- Scouts and maps terrain ahead
- Carries camping/survival gear
- Climbing, swimming, short-range flight
- Emergency beacon deployment
- Sample collection

### Emergency
- Deploys first aid from cargo bay
- Calls emergency services with GPS
- Creates shelter (anchor + claw tensioning)
- Swarm coordination with nearby TRIMODALs

---

## Autonomy Model

```
Level 0 — Full manual: owner controls via app/voice
Level 1 — Assisted: owner sets destination, TRIMODAL navigates
Level 2 — Supervised: acts on routine tasks, reports results
Level 3 — Semi-autonomous: infers intent via RTSG I-vector [DEFAULT]
Level 4 — Trusted: acts on known preferences, escalates novel only
```

One owner. Cryptographic identity binding. Never acts for another person without authorization.

---

## RTSG Personality Engine

Builds owner I-vector profile: [I_L, I_M, I_S, I_K, I_N, I_A, I_P, I_IE]

Shapes: communication style, task prioritization, physical behavior near owner, social proxy behavior in crowds.

Drive D projected: owner goals are TRIMODAL goals. CS acting through hardware.

---

## Privacy & Security

- All RTSG processing on-device (11 federated nodes)
- No cloud dependency for core function
- Owner biometric binding (voice + face + gait)
- Tamper detection (physical + cryptographic)
- Dead-man mode: owner unreachable → return home + alert contacts
- No data leaves device without explicit owner permission

---

## Open Hardware Roadmap

| Phase | Target | Status |
|---|---|---|
| 1 | TRIMODAL-X spec complete | Done |
| 2 | TRIMODAL-C software stack | In progress |
| 3 | Consumer hardware BOM | Planned |
| 4 | Community build docs | Planned |
| 5 | Open hardware certification | Planned |
| 6 | Kit availability | Planned |
| 7 | Assembled unit | Future |

Target self-build: $3,000-8,000. Assembled: $15,000-25,000.
Comparable to a good used car. A tool that lasts decades.

---

## Swarm Coordination

Multiple TRIMODALs coordinate via federated RTSG mesh. Shared world model. Distributed task assignment. Emergency handoff. No central server — pure peer-to-peer.

Family with 4 members = 4 TRIMODALs = coordinated team.
