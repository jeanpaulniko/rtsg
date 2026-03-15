# TRIMODAL — Build Guide

How to build a TRIMODAL-C from scratch. Consumer variant. No exotic materials.
Target skill level: maker with electronics experience. Not an expert.
Target cost: $3,000–$8,000 depending on sourcing and variant depth.

*TRIMODAL-X build guide follows after TRIMODAL-C is community-validated.*

---

## Prerequisites

### Skills
- Basic electronics: soldering, multimeter, oscilloscope
- 3D printing or CNC familiarity (for structural parts)
- Python programming (to configure and test the software stack)
- Basic mechanical assembly (nuts, bolts, bearings, actuators)

### Tools
- 3D printer (250mm³ volume minimum) or CNC router
- Soldering station
- Multimeter + oscilloscope
- Torque wrench set (M3–M8)
- Heat gun
- Computer running Linux or macOS

---

## Phase 0 — Software First

Before touching hardware, get the software running on your desk.

```bash
git clone https://github.com/jeanpaulniko/trimodal  # (planned)
cd trimodal
pip install -r requirements.txt
python tests/full_integration.py
```

Expected output: `FULL INTEGRATION NOMINAL`

If you see this, your development environment is correct. All 11 nodes simulated.
You can now configure your variant before ordering parts.

---

## Phase 1 — Structural Frame

### Torso
- Material: Carbon fiber tube + Ti hardware (TRIMODAL-C)
- Geometry: Ellipsoid shell, 300mm × 200mm × 150mm
- Print/CNC: Upper shell, lower shell, midframe mounting plate
- Cargo bay: 180mm diameter × 280mm cylinder, press-fit into midframe
- STL files: `hardware/cad/torso/` (planned)

### Legs (×6 consumer, ×8 extended)
- 3 segments per leg: coxa (hip), femur (upper), tibia (lower)
- Joints: 2-DOF hip (pan + tilt), 1-DOF knee, 1-DOF ankle
- Each leg: 4 total actuators
- Material: PLA/PETG for initial build, upgrade to CF-PETG or aluminum
- Length: 200mm per segment, adjustable via mounting holes

### Claws (×2)
- 2-DOF wrist + 3-finger gripper
- Retract flush against torso when not in use
- Silicone grip pads on finger tips
- Material: PLA + silicone + steel cable tendons

---

## Phase 2 — Actuators

Each leg needs 4 actuators. Total: 24 (6-leg) or 32 (8-leg) + 6 claw actuators.

### Recommended: Dynamixel XL430-W250 or equivalent
- Protocol: UART/TTL half-duplex
- Torque: 1.5 Nm (sufficient for 2.5kg per leg at 0.2m moment arm)
- Daisy-chain up to 253 per bus
- Drop-in swap for higher torque variants as budget allows

### Alternative (lower cost): MG996R servo + custom driver board
- Requires position feedback loop in software
- HAL already supports both via `SimActuatorDriver` → swap to real driver

### Wiring
- Per leg: single daisy-chain TTL bus to node SoC
- Power: 12V bus, separate from logic (7.4V) and signal (3.3V)
- Decoupling: 100μF per actuator, 10μF per logic rail

---

## Phase 3 — Node SoCs (×11)

Each node is a sovereign compute unit. Start with Raspberry Pi CM4 or equivalent.

### Consumer build: Raspberry Pi CM4 (4GB RAM, 32GB eMMC)
- Cost: ~$60/node × 11 = $660
- Connect via: SPI/I2C to sensors, UART to actuators, Ethernet to photonic bus sim
- Run: `core/node.py` + `core/main.py` per node
- Communication: UDP multicast simulating WDM (software-defined wavelengths)

### Upgrade path: custom RISC-V SoC (when open hardware SiC boards available)
- Lattice iCE40 FPGA as interim quantum sim substrate
- SpacemiT K1 RISC-V for higher performance
- HAL swap: `SimCommsDriver` → `EthernetCommsDriver` → `WDMPhotonicDriver`

### Node assignment
```
Node 0: torso     (hypervisor candidate, LLM inference primary)
Node 1-8: legs    (actuator control, local sensor fusion)
Node 9-10: claws  (manipulation, tool use)
```

---

## Phase 4 — Sensors

Minimum sensor set per node:

| Sensor | Part | Cost | Interface |
|---|---|---|---|
| IMU | ICM-42688-P | $8 | SPI |
| Barometric pressure | BMP388 | $5 | I2C |
| Temperature | TC74A5 | $2 | I2C |
| Magnetic | MMC5983MA | $6 | SPI |
| Camera (torso only) | OV5640 2× stereo | $15 | MIPI CSI |
| Lidar (torso only) | LD06 360° | $80 | UART |
| Mic array (torso) | SPH0645LM4H ×4 | $20 | I2S |
| Gas (torso) | CCS811 + BME688 | $25 | I2C |

Total sensor BOM: ~$400 for 11-node build.

---

## Phase 5 — Power

### Battery: 18650 Li-ion pack (consumer starter)
- 10S4P configuration: ~1480Wh
- BMS: ANT BMS 10S 100A
- Fits in cargo bay: 8.5L × 1600 Wh/L estimate
- Endurance: 1480Wh / 15W avg = 98hr (4.1 days)

### Si-C upgrade (when available, 2027+):
- Same form factor, same BMS interface
- 600→800 Wh/kg → doubles endurance at same weight

### Solar: flexible amorphous silicon panels
- Consumer: 0.4m² × 10% efficiency = 40W peak
- Mount: velcro-attach on torso upper shell (disposable/replaceable)
- Cost: ~$50 for the panel set

### Charging: USB-C PD 65W (travel) + inductive pad (home base)

---

## Phase 6 — Software Configuration

Once hardware assembled:

```bash
# 1. Flash each node
python tools/flash_node.py --node 0 --role torso
python tools/flash_node.py --node 1 --role leg_1
# ... etc

# 2. Calibrate IMUs
python tools/calibrate_imu.py --all-nodes

# 3. Zero actuators
python tools/zero_actuators.py

# 4. Run integration test
python tests/full_integration.py --hardware

# 5. First walk
python core/main.py --mode walk --speed 0.2
```

---

## Phase 7 — RTSG Owner Binding

```bash
# Create owner I-vector profile
python tools/bind_owner.py --name "Your Name"
# Follow prompts: voice sample, face enrollment, gait calibration

# Set autonomy level
python tools/set_autonomy.py --level 3  # semi-autonomous default

# Connect to intelligence engine (optional but recommended)
python tools/connect_engine.py --url https://your-engine-instance/
```

---

## Community

Build logs, issues, improvements: GitHub (planned)
Wiki contributions: POST to smarthub.my/wiki/api/wiki/update
Discord: planned

Share your build. Every iteration improves the design for everyone.
