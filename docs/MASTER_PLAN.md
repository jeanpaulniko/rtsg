# RTSG Intelligence Engine — Master Deployment Plan

**Author:** Jean-Paul Niko / Claude
**Date:** 2026-03-15
**Target:** https://smarthub.my/
**VPS:** root@musclemap.me (72.62.83.202), 6 CPU, 32GB RAM, Linux
**Status:** PLANNING → EXECUTION

---

## 0. Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    smarthub.my (Caddy)                       │
├──────────┬──────────┬───────────┬───────────┬───────────────┤
│  /       │  /api    │  /wiki    │  /explore │  /docs        │
│  Landing │  REST    │  Existing │  RTSG 3D  │  Math Papers  │
│  (React) │  (Go)    │  Wiki     │  Explorer │  (Markdown)   │
├──────────┴──────────┴───────────┴───────────┴───────────────┤
│                    Reverse Proxy (Caddy)                     │
├──────────┬──────────┬───────────────────────────────────────┤
│  Go API  │  Rust    │  PostgreSQL + SQLite                  │
│  Server  │  Compute │  NRTE Database                        │
│  (PM2)   │  Engine  │  Vector Store                         │
└──────────┴──────────┴───────────────────────────────────────┘
```

---

## 1. WORKSTREAM A: Frontend (TypeScript/React + Three.js)

### Goal
Interactive 3D RTSG Dimension Explorer as the centerpiece of smarthub.my.

### Features
- Pick any two RTSG dimensions (Relational, Topological, Geometric)
- Pick number system (ℝ, ℂ, ℚ_p for any p, full adeles 𝔸)
- Pick mathematical perspective (algebra, geometry, topology, number theory, category theory, analysis, differential geometry, trigonometry, calculus)
- 3D visualization of inner product shapes using Three.js / React Three Fiber
- Gram matrix heatmaps, eigenvalue spectra, radar plots
- Cross-dimensional coupling visualization
- Entity browser: load entities from NRTE database, see their shape signatures
- Document analysis: upload text, decompose into entity shapes
- Comparison mode: overlay shapes from different dimensions/number systems

### Technology
- **Framework:** React 18 + TypeScript (strict mode)
- **3D:** React Three Fiber (Three.js r128 wrapper) + drei helpers
- **Charts:** Recharts for 2D, custom Three.js meshes for 3D
- **Styling:** Tailwind CSS
- **Build:** Bun (fast bundler, runs on VPS)
- **State:** React context + useReducer (no external state library)

### Sub-tasks
1. Scaffold TypeScript React project with Bun
2. Implement NRTE data model types
3. Build dimension selector UI (dropdowns + visual cards)
4. Build number system selector with live preview
5. Build perspective switcher
6. Implement inner product computation engine (all number systems)
7. Build Gram matrix visualization component
8. Build eigenvalue spectrum chart
9. Build 3D shape renderer (Three.js mesh from Gram matrix eigenvectors)
10. Build cross-dimensional heatmap
11. Build entity browser (fetches from API)
12. Build document upload + shape decomposition
13. Build comparison overlay mode
14. Build landing page with hero section
15. Responsive layout + mobile support
16. Bundle and deploy to /explore on Caddy

---

## 2. WORKSTREAM B: Backend API (Go → C)

### Goal
RESTful API serving NRTE data, computing inner products, managing entities.

### Endpoints
```
GET    /api/v1/dimensions          — List RTSG dimensions
GET    /api/v1/dimensions/:id      — Get dimension basis vectors
GET    /api/v1/entities            — List entities from NRTE DB
GET    /api/v1/entities/:id        — Get entity with shape data
POST   /api/v1/inner-product       — Compute ⟨v₁, v₂⟩ in chosen number system
POST   /api/v1/gram-matrix         — Compute full Gram matrix for a basis set
POST   /api/v1/cross-product       — Cross-dimensional inner product
POST   /api/v1/analyze-document    — Decompose text into entity shapes
GET    /api/v1/number-systems      — Available number systems + metadata
GET    /api/v1/perspectives        — Available math perspectives
POST   /api/v1/transform           — Apply matrix transformation to shape
GET    /api/v1/health              — Health check
```

### Technology
- **Language:** Go 1.22 (primary), Rust (compute-intensive inner product kernels)
- **Final target:** Compile Go to C via cgo, Rust to C via FFI, link as modular daemons
- **HTTP:** net/http (stdlib) or Chi router
- **Database:** PostgreSQL (primary NRTE store) + SQLite (session cache)
- **Process manager:** PM2 (already on VPS)
- **Serialization:** JSON (API), MessagePack (internal)

### Sub-tasks
1. Define Go project structure (cmd/api, pkg/nrte, pkg/math, pkg/compute)
2. Define NRTE database schema in PostgreSQL
3. Implement entity CRUD handlers
4. Implement inner product computation in Go (real, complex)
5. Implement p-adic inner product in Rust (performance-critical)
6. Implement adelic product computation in Rust
7. Build Gram matrix endpoint
8. Build cross-dimensional product endpoint
9. Build document analysis pipeline (tokenize → entity lookup → shape assembly)
10. Build health/metrics endpoints
11. Write Go↔Rust FFI bridge (cgo + Rust cdylib)
12. Compile to standalone C-linked binaries
13. Configure PM2 process management
14. Deploy behind Caddy reverse proxy

---

## 3. WORKSTREAM C: Database (NRTE)

### Goal
Connect to and extend the existing noun-relation-thing-entity database.

### Schema (PostgreSQL)
```sql
-- Core NRTE tables
CREATE TABLE entities (
    id          SERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
    type        TEXT NOT NULL,           -- noun, relation, thing, entity
    lojban_form TEXT,                    -- Lojban syntactic form
    english     TEXT,                    -- English representation
    created_at  TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE relations (
    id          SERIAL PRIMARY KEY,
    subject_id  INT REFERENCES entities(id),
    predicate   TEXT NOT NULL,           -- relation type
    object_id   INT REFERENCES entities(id),
    weight      FLOAT DEFAULT 1.0,
    metadata    JSONB
);

-- RTSG shape layers
CREATE TABLE dimension_vectors (
    id          SERIAL PRIMARY KEY,
    entity_id   INT REFERENCES entities(id),
    dimension   TEXT NOT NULL,           -- relational, topological, geometric
    basis_index INT NOT NULL,
    components  FLOAT[] NOT NULL,        -- vector components
    number_system TEXT DEFAULT 'real'
);

CREATE TABLE gram_cache (
    id          SERIAL PRIMARY KEY,
    dim1        TEXT NOT NULL,
    dim2        TEXT NOT NULL,
    number_sys  TEXT NOT NULL,
    matrix_data JSONB NOT NULL,
    computed_at TIMESTAMPTZ DEFAULT NOW()
);

-- Vector embeddings for similarity search
CREATE TABLE embeddings (
    id          SERIAL PRIMARY KEY,
    entity_id   INT REFERENCES entities(id),
    model       TEXT NOT NULL,
    vector      FLOAT[] NOT NULL
);
```

### Sub-tasks
1. Audit existing NRTE database structure on VPS
2. Design migration scripts for shape layers
3. Implement entity import from existing Lojban/English data
4. Build dimension_vectors population pipeline
5. Build Gram cache for frequently computed matrices
6. Set up pgvector extension for similarity search
7. Create indexes for fast entity lookup
8. Write seed data from current RTSG basis vectors

---

## 4. WORKSTREAM D: Wiki Architecture Update

### Goal
Update all smarthub.my/wiki documents with latest math (Architecture v6.0, Kill Log, Stampacchia proof, No-Go theorem).

### Documents to update/create
1. **RTSG Main Page** — Update with v6.0 framework status
2. **Kill Log** — Full 10-entry kill log with dates and sources
3. **Theorem A** — Existence, uniqueness, coercivity (Section 2)
4. **Theorem B / Lemma M** — Stampacchia truncation proof (Section 3)
5. **Weil Connection** — Structural isomorphism + No-Go theorem (Section 4)
6. **Conclusion** — Final verdict and open problems (Section 5)
7. **Computational Appendix** — All simulation results and code
8. **RTSG Explorer Docs** — API documentation for the new explorer
9. **NRTE Database Docs** — Schema, entity types, relation types
10. **Deployment Architecture** — This master plan, kept live

### Sub-tasks
1. Push Architecture v6.0 final to wiki
2. Push Section 2 (Theorem A) to wiki
3. Push Section 3 (Theorem B / Stampacchia) to wiki
4. Push Section 4 (Weil Connection / No-Go) to wiki
5. Push Section 5 (Conclusion) to wiki
6. Push Kill Log as standalone page
7. Create API documentation page
8. Create NRTE schema documentation page
9. Update main landing page with links to all new content
10. Verify all cross-references and links

---

## 5. WORKSTREAM E: Deployment & DevOps

### Goal
Everything running as modular daemons on the VPS, served by Caddy.

### Caddy Configuration
```
smarthub.my {
    # Static frontend
    handle /explore/* {
        root * /opt/smarthub/frontend/dist
        file_server
        try_files {path} /explore/index.html
    }

    # Go API
    handle /api/* {
        reverse_proxy localhost:8080
    }

    # Existing wiki
    handle /wiki/* {
        reverse_proxy localhost:3000
    }

    # Landing page
    handle {
        root * /opt/smarthub/landing
        file_server
    }
}
```

### PM2 Process Configuration
```yaml
apps:
  - name: smarthub-api
    script: /opt/smarthub/bin/api-server
    instances: 2
    exec_mode: cluster

  - name: smarthub-compute
    script: /opt/smarthub/bin/compute-engine
    instances: 1

  - name: smarthub-wiki
    script: /opt/smarthub/wiki/server.js
    instances: 1
```

### Sub-tasks
1. SSH into VPS and audit current Caddy config
2. Audit current PM2 processes
3. Create /opt/smarthub directory structure
4. Deploy Go API binary
5. Deploy Rust compute engine
6. Deploy React frontend build
7. Update Caddy config
8. Configure PM2 for all services
9. Set up log rotation
10. Health check monitoring

---

## 6. EXECUTION ORDER

### Phase 1: Foundation (can start now, no VPS access needed)
- [x] Create master plan (this document)
- [ ] Write all Go API code locally
- [ ] Write all Rust compute code locally
- [ ] Build React frontend locally
- [ ] Push math documents to wiki via API

### Phase 2: Database (needs VPS access)
- [ ] Audit existing NRTE database
- [ ] Run migration scripts
- [ ] Seed dimension vectors

### Phase 3: Deploy (needs VPS SSH)
- [ ] Deploy binaries to VPS
- [ ] Update Caddy config
- [ ] Configure PM2
- [ ] Verify all endpoints

### Phase 4: Integration
- [ ] Connect frontend to live API
- [ ] Connect API to live database
- [ ] End-to-end testing
- [ ] Update wiki with API docs

---

## 7. WHAT I CAN DO RIGHT NOW (This Session)

Without SSH access to the VPS, I can:

1. ✅ Write the complete Go API server code
2. ✅ Write the Rust compute engine code
3. ✅ Build the full React/TypeScript frontend
4. ✅ Push updated math documents to the wiki via the existing API
5. ✅ Generate all SQL migration scripts
6. ✅ Generate Caddy and PM2 configuration files
7. ✅ Package everything for deployment

What requires your action (VPS SSH):
- Installing Go/Rust/Bun on the VPS
- Running database migrations
- Deploying binaries
- Updating Caddy config

---

## 8. TECHNOLOGY STACK SUMMARY

| Layer | Technology | Rationale |
|:------|:-----------|:----------|
| Frontend | React 18 + TypeScript + Three.js | 3D math viz, type safety |
| Build | Bun | Fast bundler, runs Go-like on server |
| API | Go 1.22 (Chi router) | Fast, simple, compiles to single binary |
| Compute | Rust (FFI to Go) | p-adic/adelic math needs performance |
| Final binary | C (via cgo + Rust cdylib) | Modular daemons in RAM |
| Primary DB | PostgreSQL + pgvector | NRTE store + vector search |
| Cache DB | SQLite | Session cache, Gram matrix cache |
| Process mgmt | PM2 | Already on VPS |
| Reverse proxy | Caddy | Already on VPS, auto-TLS |
| Wiki | Existing system | Already running at /wiki |
