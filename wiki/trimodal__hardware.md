# TRIMODAL — Hardware Specification

---

## Materials Stack (outside → inside)

| Layer | Material | X | C |
|---|---|---|---|
| 1 | TiC + diamond coating 1.5mm | Yes | Yes reduced |
| 2 | DU/WC/Ti cermet 2-3mm | Torso only | No |
| 3 | CF/Ti TPMS lattice 15mm fill=0.30 | Yes | CF only |
| 4 | Graphene-ceramic FGM 1mm | Yes | Yes |
| 5 | UHMWPE + graphene + B4C 2mm | Yes | Yes reduced |
| 6 | Mu-metal foil | Yes | Optional |
| 7 | Aerogel blanket 2mm | Yes | Yes |
| 8 | SiC ceramic 3mm | Yes | Yes reduced |
| 9 | PTFE + iridium 0.5mm | Yes | No |
| 10 | Borosilicate glass 1.5mm | Yes | Yes |

---

## Compute Per Node (11 nodes)

| Component | X Spec | C Spec |
|---|---|---|
| Substrate | SiC 600C rad-hard | GaN lower cost |
| CPU | RISC-V 4-8 cores | RISC-V 4 cores |
| L1/L2 | EPROM/SRAM | EPROM/SRAM |
| L3 | FeRAM non-volatile | FeRAM |
| Cold storage | MRAM rad-hard | Flash |
| Photonic array | LLM INT4 systolic | ASIC target |
| Quantum unit | 50-100 photonic qubits | Classical QUBO sim |
| Mechanical FSM | Camshaft drum | Simplified |

---

## Power System

| Source | Spec | Priority |
|---|---|---|
| Solar active | PTFE perovskite (X) or flex Si (C), 0.6m2 | 1 |
| Battery main | Si-C solid state 600-800 Wh/kg | 2 |
| Flywheel | Kinetic reserve + gyro | 3 |
| Thermoelectric | Seebeck in joints | 4 |
| Piezoelectric | Impact harvesters in feet | 5 |
| Regenerative | Descend_regen mode | 6 |

TRIMODAL-X: 5kg battery = 3000Wh = 7+ days at 18W avg  
TRIMODAL-C: 3kg battery = 1800Wh = 4+ days at 15W avg

---

## Weight Budget

### TRIMODAL-X (20kg)
```
Cargo payload:      5.0kg
Battery 800Wh/kg:   3.78kg
Cargo bay walls:    2.35kg
Exoskeleton TPMS:   3.37kg
Actuators:          3.50kg
Electronics:        0.80kg
Sensors:            0.40kg
TOTAL:             19.20kg  (0.80kg margin)
```

### TRIMODAL-C (15kg)
```
Cargo payload:      5.0kg
Battery 600Wh/kg:   3.75kg
Cargo bay walls:    0.80kg
Exoskeleton CF:     2.00kg
Actuators:          2.50kg
Electronics:        0.60kg
Sensors:            0.35kg
TOTAL:             15.00kg  (exact budget)
```

---

## Environmental Ratings

| Rating | X | C |
|---|---|---|
| Depth | 2000m | 10m splash |
| Temperature | 500C | -20C to +60C |
| Acid | Fluoroantimonic | None |
| EMP | Immune (fiber) | Hardened |
| Blast | 50m radius | N/A |
| IP rating | Beyond IP69K | IP67 |
| Duration | 168hr | 96hr |
