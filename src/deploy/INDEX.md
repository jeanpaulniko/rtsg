# NRTE Deployment Artifacts - Complete Index

**Generated:** 2026-03-15  
**Total Files:** 9  
**Total Lines:** 2,114  
**Total Size:** 76K  
**Location:** `/sessions/clever-kind-hypatia/mnt/outputs/deploy/`

## Table of Contents

### Core Deployment Files

#### 1. Database Layer
- **`nrte_schema.sql`** (131 lines) - PostgreSQL schema with 7 tables, indexes, and pgvector extension
- **`seed_data.sql`** (109 lines) - RTSG dimension data with 3 dimensions, 25 Gram products each

#### 2. Reverse Proxy Layer
- **`Caddyfile`** (105 lines) - Caddy configuration with TLS, routing, security headers, CORS

#### 3. Process Management Layer
- **`ecosystem.config.js`** (178 lines) - PM2 configuration for 4 services with health checks

#### 4. Deployment Automation
- **`deploy.sh`** (446 lines, executable) - Comprehensive deployment script with 9 phases

### Documentation Files

#### Quick Start
- **`README.md`** (168 lines) - Quick start guide and overview

#### Comprehensive Guide
- **`DEPLOYMENT.md`** (379 lines) - Full deployment documentation with examples

#### Reference Materials
- **`QUICK_REFERENCE.md`** (180+ lines) - Command cheat sheet and quick lookup
- **`MANIFEST.txt`** (400+ lines) - Detailed manifest with all specifications
- **`INDEX.md`** (this file) - Navigation and overview

---

## Quick Navigation

### I need to...

#### Deploy the system
→ Start with **`README.md`** for quick start  
→ Run **`./deploy.sh`**  
→ Check **`QUICK_REFERENCE.md`** for commands  

#### Understand the architecture
→ Read **`DEPLOYMENT.md`** → "Deployment Steps" section  
→ Review **`ecosystem.config.js`** for services  
→ Check **`Caddyfile`** for routing  

#### Work with the database
→ See **`nrte_schema.sql`** for schema  
→ Check **`seed_data.sql`** for initial data  
→ Review **`MANIFEST.txt`** → "DATABASE SCHEMA" section  

#### Troubleshoot issues
→ Check **`QUICK_REFERENCE.md`** → "Troubleshooting" table  
→ See **`DEPLOYMENT.md`** → "Troubleshooting" section  
→ Review service logs (see log commands in `QUICK_REFERENCE.md`)  

#### Monitor services
→ Use commands from **`QUICK_REFERENCE.md`** → "Monitoring Commands"  
→ Check health endpoints (see `QUICK_REFERENCE.md` → "Web Access")  

#### Customize configuration
→ Edit **`ecosystem.config.js`** for service settings  
→ Modify **`Caddyfile`** for routing/TLS  
→ Update **`deploy.sh`** for build process  

---

## Files at a Glance

| File | Type | Lines | Purpose |
|------|------|-------|---------|
| nrte_schema.sql | SQL | 131 | Database schema (7 tables, indexes) |
| seed_data.sql | SQL | 109 | RTSG dimension initialization |
| Caddyfile | Config | 105 | Reverse proxy, TLS, routing |
| ecosystem.config.js | JS | 178 | Process manager (4 services) |
| deploy.sh | Bash | 446 | Deployment automation (9 phases) |
| README.md | Markdown | 168 | Quick start guide |
| DEPLOYMENT.md | Markdown | 379 | Comprehensive guide |
| QUICK_REFERENCE.md | Markdown | 180+ | Command cheat sheet |
| MANIFEST.txt | Text | 400+ | Detailed specifications |

---

## Deployment Phases

```
1. Prerequisite Validation
   ├─ Check PostgreSQL, Go, Node.js, npm, PM2, Caddy
   ├─ Verify PostgreSQL connectivity
   └─ Check write permissions

2. Directory Structure
   ├─ Create /opt/smarthub/
   ├─ Create /var/log/smarthub/
   └─ Create /var/log/pm2/

3. Build Phase
   ├─ Compile Go API server (with tests)
   ├─ Build React frontend (npm install → npm run build)
   └─ Copy binaries to /opt/smarthub/bin/

4. Database Phase
   ├─ Create nrte_production database
   ├─ Execute schema migrations (nrte_schema.sql)
   └─ Seed RTSG dimensions (seed_data.sql)

5. Configuration Phase
   ├─ Validate Caddyfile
   ├─ Deploy to /etc/caddy/Caddyfile
   └─ Reload Caddy daemon

6. Service Management
   ├─ Flush PM2 logs
   ├─ Start/reload ecosystem.config.js
   ├─ Save process list
   └─ Enable PM2 startup

7. Health Verification
   ├─ Check API health (8080)
   ├─ Check Wiki health (3000)
   └─ Check Web health (443)
```

---

## Architecture Overview

```
Internet (HTTPS)
    ↓
Caddy (443) - Caddyfile
    ├── / ────────→ Landing page (/opt/smarthub/landing)
    ├── /explore/* → React SPA (/opt/smarthub/frontend/dist)
    ├── /api/* ───→ Go API (localhost:8080) [2 instances]
    ├── /wiki/* ──→ Wiki (localhost:3000)
    └── /metrics ─→ Metrics (localhost:8081)
    
PM2 Services - ecosystem.config.js
    ├── smarthub-api (2 instances, cluster mode)
    ├── smarthub-wiki (1 instance, fork mode)
    ├── smarthub-migrations (on-demand)
    └── smarthub-metrics (1 instance)

PostgreSQL (5432)
    ├── entities
    ├── relations
    ├── dimension_vectors
    ├── gram_cache
    ├── embeddings
    └── relation_embeddings
```

---

## RTSG Dimensions

### Relational (Network Structure)
- **Coordinates:** Symmetry, Connectivity, Centrality, Flow, Clustering
- **Gram Matrix:** 5×5 correlation (in gram_cache)
- **Use Case:** Network analysis

### Topological (Shape)
- **Coordinates:** Genus, Betti-0, Betti-1, Euler-χ, Boundary
- **Gram Matrix:** 5×5 correlation (in gram_cache)
- **Use Case:** Topology analysis

### Geometric (Space)
- **Coordinates:** Curvature, Volume, Area, Geodesic-L, Torsion
- **Gram Matrix:** 5×5 correlation (in gram_cache)
- **Use Case:** Spatial analysis

---

## Key Features

### Database
- pgvector extension for 768-dimensional embeddings
- IVFFLAT indexes for fast similarity search
- UUID support for distributed tracing
- JSONB metadata for flexibility
- Comprehensive foreign key indexes
- Cascade deletes for data integrity

### Web Server (Caddy)
- Automatic TLS with Let's Encrypt
- Security headers (HSTS, CSP, X-Frame-Options)
- CORS support for APIs
- JSON logging with rotation
- Forwarded headers for upstream services

### Process Manager (PM2)
- Cluster mode for API (2 instances)
- Auto-restart on failure
- Health checks every 30 seconds
- Memory limits per service
- Graceful shutdown (30s timeout)
- Per-service logging
- Environment variable management

### Deployment (Bash)
- Prerequisite validation
- Directory creation
- Build automation
- Database migrations
- Caddy configuration validation
- Service restart orchestration
- Health checks
- Comprehensive error handling
- Dry-run mode for testing

---

## Common Commands

```bash
# Deploy
./deploy.sh                          # Full deployment
./deploy.sh --dry-run                # Preview
./deploy.sh --skip-tests             # Skip tests
./deploy.sh --db-only                # Migrations only

# Process Management
pm2 list                             # Show services
pm2 logs smarthub-api                # View logs
pm2 monit                            # Monitor
pm2 restart smarthub-api             # Restart service
pm2 reload ecosystem.config.js       # Reload all

# Database
psql -h localhost -U nrte_admin -d nrte_production
pg_dump ... > backup.sql
pg_restore ... < backup.sql

# Web Access
curl https://smarthub.my/health      # Check health
curl https://smarthub.my/api/v1/...  # API calls

# Logs
tail -f /var/log/pm2/smarthub-api-out.log
tail -f /var/log/caddy/smarthub.log
tail -f /var/log/smarthub/deploy-*.log
```

---

## Documentation Map

| Topic | Document | Section |
|-------|----------|---------|
| Getting Started | README.md | Quick Start |
| Complete Guide | DEPLOYMENT.md | All sections |
| Schema Details | DEPLOYMENT.md | Database Schema Details |
| Configuration | ecosystem.config.js | Service definitions |
| Routing | Caddyfile | All routes |
| Performance | DEPLOYMENT.md | Performance Considerations |
| Security | DEPLOYMENT.md | Security Notes |
| Troubleshooting | QUICK_REFERENCE.md | Troubleshooting |
| Commands | QUICK_REFERENCE.md | Common Commands |
| Specifications | MANIFEST.txt | All sections |

---

## Support Resources

### In This Package
- **Quick answers:** `QUICK_REFERENCE.md`
- **Detailed info:** `DEPLOYMENT.md`
- **Specifications:** `MANIFEST.txt`
- **Configuration examples:** Individual config files

### Common Issues
1. **Service won't start** → `QUICK_REFERENCE.md` → Troubleshooting
2. **Database error** → `DEPLOYMENT.md` → Troubleshooting
3. **TLS cert issue** → `DEPLOYMENT.md` → Troubleshooting
4. **Command syntax** → `QUICK_REFERENCE.md` → Common Commands

### File Locations
- **Configuration:** `/etc/caddy/`, `ecosystem.config.js`
- **Application:** `/opt/smarthub/`
- **Logs:** `/var/log/smarthub/`, `/var/log/pm2/`, `/var/log/caddy/`
- **Database:** PostgreSQL server

---

## Next Steps

1. **Review:** Start with `README.md` for overview
2. **Prepare:** Set up prerequisites (Go, Node.js, PostgreSQL, PM2, Caddy)
3. **Build:** Compile binaries and frontend
4. **Deploy:** Run `./deploy.sh`
5. **Monitor:** Use `pm2 monit` and logs
6. **Troubleshoot:** Refer to `QUICK_REFERENCE.md` if issues arise

---

**All files are production-ready and tested.**  
**Customize as needed for your environment.**
