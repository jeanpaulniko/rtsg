# START HERE - NRTE Deployment Artifacts

Welcome! You have received a complete, production-ready deployment package for the **Network Relational Topological Embedding (NRTE)** system with SmartHub frontend.

**Generated:** March 15, 2026  
**Total Files:** 10  
**Total Lines:** 2,419  
**Total Size:** 88 KB  

## What You Have

### Core Deployment Files (Ready to Use)

1. **`nrte_schema.sql`** - PostgreSQL database schema
   - 7 tables: entities, relations, dimension_vectors, gram_cache, embeddings, relation_embeddings, schema_metadata
   - pgvector extension for similarity search
   - IVFFLAT indexes for fast queries

2. **`seed_data.sql`** - RTSG dimension initialization
   - 3 dimensions: Relational, Topological, Geometric
   - 5×5 basis matrices for each dimension
   - Gram products pre-computed

3. **`Caddyfile`** - Reverse proxy configuration
   - Auto TLS with Let's Encrypt
   - Routes: landing page, React SPA, API, Wiki, Metrics
   - Security headers and CORS

4. **`ecosystem.config.js`** - Process management
   - smarthub-api: 2 instances, cluster mode
   - smarthub-wiki: 1 instance
   - smarthub-migrations: on-demand
   - smarthub-metrics: metrics collector

5. **`deploy.sh`** - Deployment automation (executable)
   - 9 phases: validation → build → database → services → health checks
   - Options: --dry-run, --skip-tests, --db-only, --no-restart
   - Comprehensive error handling

### Documentation Files (Read These)

- **`README.md`** - Quick start guide (read this first!)
- **`DEPLOYMENT.md`** - Comprehensive deployment guide
- **`QUICK_REFERENCE.md`** - Command cheat sheet
- **`MANIFEST.txt`** - Detailed specifications
- **`INDEX.md`** - Navigation and file index

---

## 30-Second Quick Start

```bash
# 1. Prepare your system (one-time setup)
apt-get install caddy postgresql postgresql-contrib
npm install -g pm2
createuser -P nrte_api nrte_admin

# 2. Build your application
go build -o ./bin/api-server ./cmd/api
cd frontend && npm install && npm run build

# 3. Deploy (this script does everything!)
./deploy.sh

# 4. Verify
pm2 list
curl https://smarthub.my/explore/
```

That's it! The system is now running with:
- PostgreSQL database with NRTE schema
- React SPA frontend
- Go API server (2 instances)
- Wiki service
- Reverse proxy with TLS

---

## Architecture at a Glance

```
HTTPS (smarthub.my)
    ↓
Caddy (Reverse Proxy)
    ├─ / → Landing Page
    ├─ /explore/* → React SPA
    ├─ /api/* → Go API (Port 8080)
    ├─ /wiki/* → Wiki (Port 3000)
    └─ /metrics → Metrics (Port 8081)
         ↓
    PostgreSQL (Port 5432)
    - 7 tables
    - 768-dim vector embeddings
    - 3 RTSG dimensions
```

---

## Files by Purpose

### "I want to..."

| Goal | File | Section |
|------|------|---------|
| **Deploy the system** | `deploy.sh` | Run it! |
| **Understand what I'm deploying** | `README.md` | Quick Start |
| **Get detailed instructions** | `DEPLOYMENT.md` | All sections |
| **Look up a command** | `QUICK_REFERENCE.md` | Common Commands |
| **Understand the database** | `nrte_schema.sql` | Schema file |
| **See specifications** | `MANIFEST.txt` | All sections |
| **Find documentation** | `INDEX.md` | Navigation |
| **Configure services** | `ecosystem.config.js` | Edit this |
| **Configure routing** | `Caddyfile` | Edit this |
| **Troubleshoot** | `QUICK_REFERENCE.md` | Troubleshooting |

---

## The 3 RTSG Dimensions

Your database comes pre-loaded with:

### 1. Relational Dimension
Network structure properties: Symmetry, Connectivity, Centrality, Flow, Clustering

### 2. Topological Dimension
Shape properties: Genus, Betti-0, Betti-1, Euler-χ, Boundary

### 3. Geometric Dimension
Spatial properties: Curvature, Volume, Area, Geodesic-L, Torsion

Each has a 5×5 Gram matrix capturing inter-coordinate correlations.

---

## Database Schema Overview

**7 Tables:**
- `entities` - Semantic units (nouns, relations, things)
- `relations` - Directed edges (subject → predicate → object)
- `dimension_vectors` - RTSG embeddings per entity
- `gram_cache` - Precomputed basis matrices
- `embeddings` - 768-dimensional vector embeddings (pgvector)
- `relation_embeddings` - Vector embeddings for relations
- `schema_metadata` - Migration tracking

**Key Features:**
- UUID support for distributed tracing
- JSONB metadata for flexibility
- Comprehensive foreign key indexes
- IVFFLAT indexes for fast vector similarity search
- Cascade deletes for data integrity

---

## Deployment Phases

The `deploy.sh` script automatically:

1. **Validates prerequisites** (PostgreSQL, Go, Node.js, PM2, Caddy)
2. **Creates directories** (/opt/smarthub, /var/log/smarthub)
3. **Builds your application** (Go API, React frontend)
4. **Creates the database** (nrte_production with schema)
5. **Seeds data** (3 RTSG dimensions with Gram matrices)
6. **Configures the proxy** (Caddyfile → /etc/caddy/)
7. **Starts services** (smarthub-api, wiki, metrics via PM2)
8. **Verifies health** (health checks on all endpoints)

---

## Monitoring & Management

```bash
# View all services
pm2 list

# Watch in real-time
pm2 monit

# View logs
pm2 logs smarthub-api
pm2 logs smarthub-wiki

# Restart a service
pm2 restart smarthub-api

# View web server logs
tail -f /var/log/caddy/smarthub.log

# Test endpoints
curl https://smarthub.my/health
curl https://smarthub.my/api/v1/entities
```

---

## Common Tasks

### Deploy for the first time
```bash
./deploy.sh
```

### Preview changes without deploying
```bash
./deploy.sh --dry-run
```

### Deploy skipping tests (faster)
```bash
./deploy.sh --skip-tests
```

### Just run database migrations
```bash
./deploy.sh --db-only
```

### Restart services after editing config
```bash
pm2 reload ecosystem.config.js --env production
```

### Check service status
```bash
pm2 show smarthub-api
```

### View live logs
```bash
pm2 logs smarthub-api --lines 50
```

---

## What Gets Created

**Directories:**
```
/opt/smarthub/
  ├── bin/                (Binaries)
  ├── frontend/dist/      (React SPA)
  ├── landing/            (Static page)
  ├── data/
  │   ├── wiki/           (Wiki storage)
  │   └── cache/          (App cache)
  └── db/migrations/      (SQL files)

/var/log/
  ├── smarthub/           (Deployment logs)
  ├── pm2/                (Process manager logs)
  └── caddy/              (Web server logs)

/etc/caddy/
  └── Caddyfile           (Proxy config)
```

**Database:**
```
PostgreSQL: nrte_production
  ├── entities
  ├── relations
  ├── dimension_vectors
  ├── gram_cache
  ├── embeddings
  ├── relation_embeddings
  └── schema_metadata
```

---

## Access After Deployment

- **Frontend:** https://smarthub.my/explore/
- **API:** https://smarthub.my/api/v1/
- **Wiki:** https://smarthub.my/wiki/
- **Metrics:** https://smarthub.my/metrics
- **Health Check:** https://smarthub.my/health

---

## Customization

**Change service count:**
Edit `ecosystem.config.js` → Change `instances: 2` to your desired number

**Add environment variables:**
Edit `ecosystem.config.js` → Add to `env:` section

**Change routing:**
Edit `Caddyfile` → Modify route definitions

**Adjust database settings:**
Edit `nrte_schema.sql` → Modify before first deployment

---

## Troubleshooting

**Service won't start:**
```bash
pm2 logs smarthub-api
# Check permissions, ports, database connectivity
```

**Database connection fails:**
```bash
psql -h localhost -U nrte_admin -d nrte_production
# Verify PostgreSQL is running and credentials are correct
```

**TLS certificate error:**
```bash
tail -f /var/log/caddy/smarthub.log
# Caddy automatically manages certificates
```

**Frontend shows 404:**
```bash
ls -la /opt/smarthub/frontend/dist/index.html
# Verify build completed successfully
```

See `QUICK_REFERENCE.md` for more troubleshooting steps.

---

## Documentation Guide

| If you want to... | Read this |
|------------------|-----------|
| Get started quickly | `README.md` |
| Understand everything | `DEPLOYMENT.md` |
| Look up a command | `QUICK_REFERENCE.md` |
| Navigate all files | `INDEX.md` |
| See all details | `MANIFEST.txt` |

---

## Prerequisites Checklist

Before running `deploy.sh`, ensure you have:

- [ ] PostgreSQL installed and running
- [ ] Go 1.19+ installed
- [ ] Node.js 16+ and npm installed
- [ ] PM2 installed: `npm install -g pm2`
- [ ] Caddy installed
- [ ] Write access to `/opt` directory
- [ ] Database users created: `nrte_api`, `nrte_admin`

---

## Next Steps

### Immediate (Now)
1. Read `README.md` for overview
2. Check `QUICK_REFERENCE.md` for deployment commands
3. Verify prerequisites are installed

### Short-term (Next 5 minutes)
1. Customize `ecosystem.config.js` if needed
2. Review `Caddyfile` for your domain
3. Run: `./deploy.sh --dry-run` to preview

### Deployment (Next 10 minutes)
1. Run: `./deploy.sh`
2. Wait for completion
3. Check: `pm2 list` to verify services started
4. Access: https://smarthub.my/explore/

### Post-deployment (Next hour)
1. Monitor logs: `pm2 logs`
2. Test API endpoints
3. Verify database: `psql -d nrte_production -c "SELECT COUNT(*) FROM entities;"`
4. Review security settings in `DEPLOYMENT.md`

---

## Support

- **Quick answers:** See `QUICK_REFERENCE.md` → Troubleshooting
- **Detailed guides:** See `DEPLOYMENT.md` → Troubleshooting
- **Command help:** See `QUICK_REFERENCE.md` → Common Commands
- **Configuration:** See individual config files with inline comments
- **Specifications:** See `MANIFEST.txt` for complete details

---

## Key Files

| File | Purpose | Edit When |
|------|---------|-----------|
| `deploy.sh` | Deployment automation | Build/deploy changes |
| `nrte_schema.sql` | Database schema | Database structure changes |
| `seed_data.sql` | Initial data | RTSG dimension changes |
| `Caddyfile` | Reverse proxy | Routing/TLS/header changes |
| `ecosystem.config.js` | Service management | Service ports/instances/env |

---

## You're All Set!

All files are production-ready and well-documented. Everything you need is in this directory:

```
/sessions/clever-kind-hypatia/mnt/outputs/deploy/
```

**Ready to deploy?**
```bash
./deploy.sh
```

**Need help?**
Check the appropriate documentation file above.

**Questions about a command?**
See `QUICK_REFERENCE.md`.

---

## Summary

✅ 10 comprehensive files  
✅ 2,419 lines of code/docs  
✅ PostgreSQL schema with pgvector  
✅ 3 RTSG dimensions with 5×5 Gram matrices  
✅ Caddy reverse proxy with auto TLS  
✅ PM2 process management  
✅ Fully automated deployment script  
✅ Complete documentation  
✅ Production-ready configuration  
✅ Troubleshooting guides  

**Everything is ready to go. Deploy with confidence!**

---

**Questions?** Start with `README.md` then `DEPLOYMENT.md`.
**In a hurry?** Jump to `QUICK_REFERENCE.md` for commands.
**Need details?** See `MANIFEST.txt` for complete specifications.
