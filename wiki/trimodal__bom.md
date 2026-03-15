# TRIMODAL — Bill of Materials

Complete BOM for both variants. Prices USD, Q1 2026 estimates.
Links to suppliers planned — community will maintain these.

---

## TRIMODAL-C (Consumer) — Target $3,000–$8,000

### Structural
| Item | Qty | Unit $ | Total | Notes |
|---|---|---|---|---|
| CF tube 30mm OD × 2mm wall × 500mm | 12 | 15 | 180 | Legs |
| Ti M4 hardware set | 1 | 45 | 45 | 200pc |
| 3D printed torso shells | 1 set | 60 | 60 | CF-PETG |
| 3D printed leg segments | 1 set | 80 | 80 | CF-PETG |
| Claw assembly kit | 2 | 40 | 80 | Steel + silicone |
| Cargo bay cylinder CF | 1 | 35 | 35 | 180mm bore |
| Bearings (various) | 1 set | 30 | 30 | 608, 6804 sizes |
| **Structural subtotal** | | | **510** | |

### Actuators
| Item | Qty | Unit $ | Total | Notes |
|---|---|---|---|---|
| Dynamixel XL430-W250 | 30 | 50 | 1500 | 24 legs + 6 claws |
| Dynamixel U2D2 adapter | 2 | 35 | 70 | USB-TTL interface |
| TTL bus cable set | 1 | 25 | 25 | |
| Motor driver boards | 4 | 20 | 80 | Power stage |
| **Actuator subtotal** | | | **1675** | Largest cost item |

### Compute (11 nodes)
| Item | Qty | Unit $ | Total | Notes |
|---|---|---|---|---|
| Raspberry Pi CM4 4GB/32GB | 11 | 65 | 715 | One per node |
| CM4 IO board (custom) or Waveshare | 11 | 25 | 275 | |
| 32GB microSD (backup) | 11 | 8 | 88 | |
| **Compute subtotal** | | | **1078** | |

### Sensors
| Item | Qty | Unit $ | Total | Notes |
|---|---|---|---|---|
| ICM-42688-P IMU | 11 | 8 | 88 | Per node |
| BMP388 pressure | 11 | 5 | 55 | Per node |
| OV5640 stereo camera pair | 1 | 30 | 30 | Torso |
| LD06 lidar | 1 | 80 | 80 | Torso |
| SPH0645 mic array ×4 | 1 set | 20 | 20 | Torso |
| CCS811 + BME688 gas | 1 | 25 | 25 | Torso |
| MMC5983MA magnetometer | 11 | 6 | 66 | Per node |
| **Sensor subtotal** | | | **364** | |

### Power
| Item | Qty | Unit $ | Total | Notes |
|---|---|---|---|---|
| Samsung 50E 21700 cells | 40 | 8 | 320 | 10S4P, 1480Wh |
| ANT BMS 10S 100A | 1 | 45 | 45 | |
| 12V→5V DC-DC (per node) | 11 | 5 | 55 | |
| Flexible solar panel 100W | 1 | 50 | 50 | 0.4m² |
| Inductive charge pad + coil | 1 | 40 | 40 | Home dock |
| Wiring harness | 1 | 35 | 35 | Pre-crimped |
| **Power subtotal** | | | **545** | |

### Communications
| Item | Qty | Unit $ | Total | Notes |
|---|---|---|---|---|
| Gigabit Ethernet switch (11-port) | 1 | 30 | 30 | Internal node bus |
| Cat6 flat cable + connectors | 1 | 20 | 20 | |
| ESP32-S3 WiFi/BT module | 1 | 8 | 8 | Owner app link |
| SIM7600G LTE module | 1 | 35 | 35 | Remote ops |
| **Comms subtotal** | | | **93** | |

### Miscellaneous
| Item | Total | Notes |
|---|---|---|
| Fasteners, wire, connectors | 80 | |
| Heatshrink, cable management | 30 | |
| Thermal paste, compound | 15 | |
| Silicone sealant | 20 | IP67 sealing |
| **Misc subtotal** | **145** | |

### TRIMODAL-C TOTAL
| Category | Cost |
|---|---|
| Structural | $510 |
| Actuators | $1,675 |
| Compute | $1,078 |
| Sensors | $364 |
| Power | $545 |
| Comms | $93 |
| Misc | $145 |
| **TOTAL** | **$4,410** |

*Self-build with sourcing effort. Target range $3,000–$8,000 depending on actuator choice.*

---

## TRIMODAL-X (Extreme) — Target $50,000–$200,000+

Extreme variant pricing reflects specialized materials. Not consumer.

### Additional materials vs TRIMODAL-C
| Item | Cost | Notes |
|---|---|---|
| SiC substrate SoC upgrade (×11) | $15,000 | GaN→SiC, 600°C rated |
| PTFE + iridium PVD coating (all surfaces) | $8,000 | Specialist process |
| SiC ceramic pressure vessel machining | $3,000 | Custom bore |
| Aerogel blanket (custom cut) | $500 | Uniform coverage |
| DU/WC/Ti cermet torso panels (×2) | $4,000 | Export controlled, mfr direct |
| TiC + CVD diamond coating | $2,500 | Specialist deposition |
| Borosilicate glass liner (cargo bay) | $400 | Custom blown |
| PTFE perovskite solar suit | $1,200 | Custom encapsulation |
| Si-C battery upgrade (5kg, 800Wh/kg) | $6,000 | Next-gen cells |
| FeRAM + MRAM per node (×11) | $2,200 | Rad-hard memory |
| Iridium sintered filter elements | $800 | 0.1μm, custom |
| Photonic quantum unit (×11) | $45,000 | Primary cost driver |
| **X upgrade total** | **~$88,600** | Over TRIMODAL-C base |

**TRIMODAL-X TOTAL: ~$93,000–$150,000** (volume pricing, prototype)

*For context: a remotely operated vehicle (ROV) for similar depth: $200,000–$500,000.*
*TRIMODAL-X is cheaper, more capable, and autonomous.*

---

## Upgrade Paths

Consumer → Extreme is modular. Every subsystem upgrades independently:

1. **Battery**: Li-ion → Si-C (same form factor, swap cells)
2. **Compute**: RPi CM4 → RISC-V SoC → SiC RISC-V (same SBC footprint)
3. **Armor**: PLA/CF → CF/TiC → full ceramic stack (redesign torso shells)
4. **Solar**: Amorphous Si → GaAs flex → PTFE perovskite (velcro swap)
5. **Comms**: Ethernet → fiber sim → real WDM (swap HAL driver)
6. **Quantum**: Classical QUBO sim → FPGA → photonic QPU (API unchanged)

The software stack is identical across all upgrade levels.
HAL drivers are the only thing that changes.
