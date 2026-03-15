# RTSG — Relational Three-Space Geometry

**A unified mathematical framework for intelligence, consciousness, and physics.**

By Jean-Paul Niko · [smarthub.my](https://smarthub.my)

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## What is RTSG?

Relational Three-Space Geometry decomposes reality into three fundamental spaces:

- **Quantum Space (QS)**: The space of possibility — non-well-founded, contains everything that could exist
- **Consciousness Space (CS)**: The bridge — language, cognition, filters that extract observables from possibility
- **Physical Space (PS)**: The actual — measurable, observable reality

The framework formalizes intelligence as a 12-dimensional vector (the I-vector), models consciousness as a Ginzburg-Landau field theory, and connects to deep number theory through adelic analysis.

## Repository Structure

```
rtsg/
├── wiki/              # 348+ pages of research (monograph, papers, companions)
├── src/
│   ├── rust/          # SmartHub Compute Engine (p-adic, adelic, Gram matrices)
│   ├── sql/           # NRTE Brain-Graph database schema (PostgreSQL)
│   ├── frontend/      # RTSG Explorer (React + Recharts)
│   ├── python/        # Verification scripts, wiki tools
│   └── deploy/        # Caddy, PM2, deployment configs
├── docs/              # Architecture, master plan, manuscript outlines
└── PROPRIETARY_BOUNDARY.md
```

## Key Components

### NRTE Brain-Graph Database

A PostgreSQL database implementing a five-layer cognitive architecture:

- **Tokens/Engrams**: reusable morphemes (free monoid)
- **Primes**: irreducible semantic units across 12 intelligence dimensions
- **Composites**: concepts factored into prime spectra
- **Patterns/Topologies**: higher-order structures
- **Physarum dynamics**: network optimization via tube thickness evolution

### Compute Engine (Rust)

High-performance cdylib for p-adic inner products, adelic restricted products, Gram matrix computation, Jacobi eigenvalue algorithms, and C FFI for integration with Go/Python.

### Mathematics

- Adelic Ginzburg-Landau field theory on idele class groups
- Stampacchia truncation proof of L-infinity regularity
- Spectral gap analysis
- Weil explicit formula connection (No-Go theorem for local differential Hessians)
- Kill Log: 10 documented obstacles and their resolutions

### Books (15 titles)

- **Academic**: RTSG Monograph (13 chapters), Companion Papers (16 disciplines)
- **Bestsellers**: The Three Spaces, Zero Is Not Nothing, The Compatibility Matrix, and 9 more
- **Memoir**: Barefoot on 125th Street

## Quick Start

```bash
# Database
psql -U postgres -c "CREATE DATABASE nrte;"
psql -U postgres -d nrte -f src/sql/nrte_brain_graph_v2.sql

# Compute Engine
cd src/rust && cargo build --release

# Frontend — drop into any React project
cp src/frontend/rtsg_explorer.jsx your-project/src/
```

## License

GPL-3.0. See [LICENSE](LICENSE) and [PROPRIETARY_BOUNDARY.md](PROPRIETARY_BOUNDARY.md).

The framework is open. The trained models are not.

## Citation

```bibtex
@misc{niko2026rtsg,
  author = {Niko, Jean-Paul},
  title = {Relational Three-Space Geometry: A Unified Framework},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/jeanpaulniko/rtsg}
}
```
