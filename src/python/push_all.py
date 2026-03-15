import requests, json, os, time

BASE = "https://smarthub.my/wiki/api/wiki"
KEY = "um6NrejNHEhAETpp-BSiOieNPyAZLikdKVMfXQ_iZ_g"
H = {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}

def read_file(path):
    with open(path, 'r') as f:
        return f.read()

def push_files(files, summary):
    payload = {
        "agent_id": "claude-opus-2026-03-15",
        "session_summary": summary,
        "rebuild": True,
        "files": files
    }
    r = requests.post(f"{BASE}/update", headers=H, json=payload)
    print(f"  Status: {r.status_code} | {r.text[:200]}")
    return r.status_code

# ============================================================
# BATCH 1: NRTE Brain-Graph Database
# ============================================================
print("=== BATCH 1: NRTE Brain-Graph Database ===")

nrte_schema = read_file("/sessions/clever-kind-hypatia/mnt/outputs/nrte_brain_graph_v2.sql")
nrte_theory = read_file("/sessions/clever-kind-hypatia/mnt/outputs/nrte_brain_graph_theory.md")

push_files([
    {"path": "nrte/brain_graph_schema_v2.md", "content": f"""---
title: "NRTE Brain-Graph Database Schema v2.0"
version: "2.0.0"
last_updated: "2026-03-15"
status: "COMPLETE — ready for deployment"
---

# NRTE Brain-Graph Database Schema v2.0

PostgreSQL schema implementing the five-layer brain-graph model:
Token/Engram → Prime → Composite → Pattern → Topology

With Physarum tube dynamics, hyperbolic + ultrametric embeddings,
GL action computation, and dimension-aware connection tracking.

## SQL Schema

```sql
{nrte_schema}
```
"""},
    {"path": "nrte/brain_graph_theory.md", "content": nrte_theory}
], "Added NRTE Brain-Graph v2.0: schema + mathematical specification. Implements token/engram layer, prime decomposition, Physarum tube dynamics, hyperbolic + ultrametric embeddings, GL action computation, tropical semiring assembly costs, 12-dimension connection tracking with temporal.")

time.sleep(1)

# ============================================================
# BATCH 2: Architecture v6 + Manuscript docs
# ============================================================
print("\n=== BATCH 2: Architecture & Manuscript ===")

arch_files = []
outputs = "/sessions/clever-kind-hypatia/mnt/outputs"

for fname, wiki_path in [
    ("architecture_v6_final.md", "papers/rtsg/architecture_v6_final.md"),
    ("manuscript_outline_complete.md", "papers/rtsg/manuscript_outline_complete.md"),
    ("section6_conclusion_final.md", "papers/rtsg/conclusion_adelic_gl_vacua.md"),
]:
    fpath = os.path.join(outputs, fname)
    if os.path.exists(fpath):
        arch_files.append({"path": wiki_path, "content": read_file(fpath)})
        print(f"  Added {fname}")

if arch_files:
    push_files(arch_files, "Updated RTSG architecture v6.0, manuscript outline, and conclusion section")
    time.sleep(1)

# ============================================================
# BATCH 3: KDP Metadata + Production Status
# ============================================================
print("\n=== BATCH 3: KDP Metadata & Status ===")

kdp_meta = read_file(os.path.join(outputs, "kdp_metadata.md"))

push_files([
    {"path": "publishing/kdp_metadata_all_books.md", "content": kdp_meta},
    {"path": "publishing/production_status.md", "content": f"""---
title: "RTSG Book Production Status"
last_updated: "2026-03-15"
producer: "claude-opus-4.6 (Cowork)"
---

# RTSG Book Production Status — Updated 2026-03-15

## ALL BOOKS: KDP-Ready PDFs Generated

### Academic Books (from wiki source material)

| # | Title | Pages | Words | Status |
|---|-------|-------|-------|--------|
| 1 | RTSG Monograph: A Unified Framework | 252 | ~67K | KDP PDF DONE |
| 2 | RTSG Companion Papers: Applications Across Disciplines | 294 | ~69K | KDP PDF DONE |

### Bestseller Series (12 titles)

| # | Title | Audience | Size | Status |
|---|-------|----------|------|--------|
| 1 | The Three Spaces | General public | ~25K | KDP PDF DONE |
| 2 | Zero Is Not Nothing | Therapists/counselors | ~23K | KDP PDF DONE |
| 3 | The Compatibility Matrix | General/military/HR | ~19K | KDP PDF DONE |
| 4 | Five Filters | Philosophy/cogsci | ~17K | KDP PDF DONE |
| 5 | Gravity Thinks First | Science-curious public | ~15K | KDP PDF DONE |
| 6 | The Language Bus | Linguistics/education | ~13K | KDP PDF DONE |
| 7 | Strategy Is Geometry | Military/defense | ~15K | KDP PDF DONE |
| 8 | Museum of Everything | Curators/educators | ~12K | KDP PDF DONE |
| 9 | Growing in Three Spaces | Children 8-12 | ~12K | KDP PDF DONE |
| 10 | Baby's First Geometry | Ages 0-3 | ~11K | KDP PDF DONE |
| 11 | Instantiation | Graduate textbook | ~12K | KDP PDF DONE |
| 12 | Social Worker's Compass | Social workers | ~13K | KDP PDF DONE |

### Memoir

| # | Title | Audience | Size | Status |
|---|-------|----------|------|--------|
| 1 | Barefoot on 125th Street | General public | ~26K | KDP PDF DONE |

### Existing KDP Drafts (on Amazon, need manuscript upload)

| Title | KDP Status | Last Modified |
|-------|-----------|---------------|
| The Age of Intelligence | Draft | Mar 14 |
| The Tank Protocol | Draft | Mar 14 |
| ZAP: The Zero-Point Trauma Recovery Protocol | Draft | Mar 13 |
| Barefoot on 125th | Draft | Mar 13 |
| How to Buy Intelligence | Draft | Mar 13 |
| The 850 Signs | Draft | Mar 13 |
| RTSG Mathematics | Draft ($3.00, has cover) | Mar 13 |

## Total: 15 KDP-ready PDFs generated + 8 existing KDP drafts

## Next Steps
- Upload manuscript PDFs to existing KDP drafts
- Create new KDP titles for remaining books
- Generate/upload covers
- Set pricing and categories
- Publish
"""}
], "Updated KDP metadata for all 15 books and production status")

time.sleep(1)

# ============================================================
# BATCH 4: Product Pipeline v7 (comprehensive update)
# ============================================================
print("\n=== BATCH 4: Product Pipeline v7 ===")

push_files([
    {"path": "publishing/product_pipeline_v7.md", "content": """---
title: "Product Pipeline v7"
last_updated: "2026-03-15"
---

# Product Pipeline v7 — Updated 2026-03-15

## Books (15 KDP-Ready PDFs)

| # | Title | Format | Status |
|---|-------|--------|--------|
| 1 | RTSG Monograph: A Unified Framework | .pdf (252pp) | KDP-ready |
| 2 | RTSG Companion Papers | .pdf (294pp) | KDP-ready |
| 3 | The Three Spaces | .pdf | KDP-ready |
| 4 | Zero Is Not Nothing | .pdf | KDP-ready |
| 5 | The Compatibility Matrix | .pdf | KDP-ready |
| 6 | Five Filters | .pdf | KDP-ready |
| 7 | Gravity Thinks First | .pdf | KDP-ready |
| 8 | The Language Bus | .pdf | KDP-ready |
| 9 | Strategy Is Geometry | .pdf | KDP-ready |
| 10 | Museum of Everything | .pdf | KDP-ready |
| 11 | Growing in Three Spaces | .pdf | KDP-ready |
| 12 | Baby's First Geometry | .pdf | KDP-ready |
| 13 | Instantiation | .pdf | KDP-ready |
| 14 | Social Worker's Compass | .pdf | KDP-ready |
| 15 | Barefoot on 125th Street | .pdf | KDP-ready |

## Software

| Product | Status | Notes |
|---------|--------|-------|
| NRTE Brain-Graph v2.0 | Schema complete | PostgreSQL + Physarum dynamics + hyperbolic embeddings |
| RTSG Explorer | Prototype complete | React + Recharts |
| RTSG Chess Engine | Concept stage | Learns from human play |
| Intelligence Inspector | Complete (v5) | $3 |
| Trauma Healer | Complete (v5) | $3 |
| SmartHub Compute Engine | Rust cdylib complete | p-adic, adelic, Gram matrix, Jacobi eigenvalues |

## Infrastructure

| Component | Status | Notes |
|-----------|--------|-------|
| VPS (72.62.83.202) | Active | smarthub.my |
| Wiki API | Active | 348 pages, 428K words |
| Caddy reverse proxy | Config ready | Not yet deployed |
| PM2 process manager | Config ready | Not yet deployed |
| PostgreSQL NRTE | Schema v2.0 ready | Not yet deployed |
| Go API server | Planned | Endpoints designed |

## Audio Products

| Product | Status | Price |
|---------|--------|-------|
| 4-voice brain training | Complete (MP3+WAV) | $3 |
| 6-voice brain training | Complete (MP3+WAV) | $5 |
| 8-voice brain training | Complete (MP3+WAV) | $7 |
| Complete bundle | Ready | $9 |

Last updated: 2026-03-15
"""}
], "Product Pipeline v7: 15 KDP-ready PDFs, NRTE Brain-Graph v2.0, infrastructure status")

time.sleep(1)

# ============================================================
# BATCH 5: Deploy configs (schema, Caddy, PM2)
# ============================================================
print("\n=== BATCH 5: Deploy Configs ===")

deploy_files = []
deploy_dir = os.path.join(outputs, "deploy")
if os.path.isdir(deploy_dir):
    for fname in os.listdir(deploy_dir):
        fpath = os.path.join(deploy_dir, fname)
        if os.path.isfile(fpath) and not fname.endswith('.pdf'):
            wiki_path = f"deploy/{fname.replace('.sql', '.md').replace('.sh', '.md').replace('.js', '.md')}"
            content = read_file(fpath)
            ext = os.path.splitext(fname)[1]
            if ext in ['.sql', '.sh', '.js']:
                lang = {'sql': 'sql', '.sh': 'bash', '.js': 'javascript'}.get(ext, '')
                content = f"# {fname}\n\n```{lang}\n{content}\n```"
            deploy_files.append({"path": wiki_path, "content": content})
            print(f"  Added {fname}")

if deploy_files:
    push_files(deploy_files, "Deploy configs: NRTE schema, Caddy, PM2, seed data, deploy script")
    time.sleep(1)

# ============================================================
# BATCH 6: Rust compute engine source
# ============================================================
print("\n=== BATCH 6: Rust Compute Engine ===")

rust_dir = os.path.join(outputs, "smarthub-compute")
rust_files = []
if os.path.isdir(rust_dir):
    for root, dirs, files in os.walk(rust_dir):
        for fname in files:
            fpath = os.path.join(root, fname)
            rel = os.path.relpath(fpath, rust_dir)
            wiki_path = f"compute/{rel.replace(os.sep, '_').replace('.rs', '.md').replace('.toml', '.md').replace('.h', '.md')}"
            content = read_file(fpath)
            ext = os.path.splitext(fname)[1]
            lang_map = {'.rs': 'rust', '.toml': 'toml', '.h': 'c', '.go': 'go'}
            lang = lang_map.get(ext, '')
            if lang:
                content = f"# {rel}\n\n```{lang}\n{content}\n```"
            rust_files.append({"path": wiki_path, "content": content})
            print(f"  Added {rel}")

if rust_files:
    push_files(rust_files, "SmartHub Compute Engine: Rust cdylib for p-adic, adelic, Gram matrix, Jacobi eigenvalues, C FFI")
    time.sleep(1)

# ============================================================
# BATCH 7: Master Plan
# ============================================================
print("\n=== BATCH 7: Master Plan ===")

master_plan_path = os.path.join(outputs, "MASTER_PLAN.md")
if os.path.exists(master_plan_path):
    push_files([
        {"path": "meta/master_plan_v2.md", "content": read_file(master_plan_path)}
    ], "Master deployment plan v2 for smarthub.my")

print("\n=== ALL BATCHES COMPLETE ===")
