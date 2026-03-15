# NRTE Deployment Quick Reference

## One-Command Deploy
```bash
./deploy.sh
```

## Common Commands

### Deployment
```bash
./deploy.sh                  # Full deployment
./deploy.sh --dry-run        # Preview changes
./deploy.sh --skip-tests     # Skip test suites
./deploy.sh --db-only        # Database migrations only
./deploy.sh --no-restart     # Build without restarting services
```

### Process Management
```bash
pm2 list                     # Show all services
pm2 logs smarthub-api        # View API logs
pm2 logs                     # View all logs
pm2 monit                    # Monitor services
pm2 restart smarthub-api     # Restart API
pm2 reload ecosystem.config.js --env production  # Reload all
pm2 stop all                 # Stop all services
pm2 start ecosystem.config.js --env production   # Start all
```

### Database
```bash
# Connect to database
psql -h localhost -U nrte_admin -d nrte_production

# Run migrations
psql -h localhost -U nrte_admin -d nrte_production -f nrte_schema.sql
psql -h localhost -U nrte_admin -d nrte_production -f seed_data.sql

# Backup
pg_dump -h localhost -U nrte_admin nrte_production > backup.sql

# Restore
pg_restore -h localhost -U nrte_admin -d nrte_production backup.sql
```

### Web Access
```bash
curl https://smarthub.my/health                    # API health
curl https://smarthub.my/explore/                  # Frontend
curl https://smarthub.my/api/v1/entities           # API endpoint
curl https://smarthub.my/wiki/                     # Wiki
```

### Logs
```bash
# Application logs
tail -f /var/log/pm2/smarthub-api-out.log
tail -f /var/log/pm2/smarthub-wiki-out.log
tail -f /var/log/pm2/smarthub-metrics-out.log

# Web server logs
tail -f /var/log/caddy/smarthub.log

# Deployment logs
tail -f /var/log/smarthub/deploy-*.log
```

### Configuration
```bash
# Caddy
caddy validate -c /etc/caddy/Caddyfile
caddy reload -c /etc/caddy/Caddyfile

# PM2
pm2 save                    # Save process list to startup
pm2 startup                 # Enable PM2 auto-startup

# Environment variables
export DB_HOST=mydb.example.com
export DB_PORT=5432
./deploy.sh
```

## Architecture Summary

```
Internet → Caddy (443/TLS) →
  / → Landing page
  /explore/* → React SPA (:dist)
  /api/* → Go API (:8080, 2 instances)
  /wiki/* → Wiki (:3000)
  /metrics → Metrics (:8081)
       ↓
  PostgreSQL (:5432)
    - entities
    - relations
    - dimension_vectors
    - gram_cache
    - embeddings
```

## Database Schema Quick Ref

### Core Tables
- `entities` - Semantic units (id, uuid, name, type, english, metadata)
- `relations` - Edges (id, subject_id, predicate, object_id, weight)
- `dimension_vectors` - Embeddings (entity_id, dimension, basis_index, components)
- `gram_cache` - Basis matrices (dimension, dim1, dim2, matrix_data, gram_product)
- `embeddings` - Vector embeddings (entity_id, model, vector[768])

### RTSG Dimensions (3x)
**Relational**: Symmetry, Connectivity, Centrality, Flow, Clustering
**Topological**: Genus, Betti-0, Betti-1, Euler-χ, Boundary
**Geometric**: Curvature, Volume, Area, Geodesic-L, Torsion

## Troubleshooting

| Problem | Solution |
|---------|----------|
| API won't start | Check: `pm2 logs smarthub-api` |
| DB connection fails | Verify: `psql -h localhost -U nrte_admin -d nrte_production` |
| TLS cert error | Check: `/var/log/caddy/smarthub.log` |
| Port already in use | `lsof -i :8080` or `netstat -tulpn \| grep 8080` |
| PM2 daemon crashed | `pm2 kill && pm2 start ecosystem.config.js --env production` |
| Frontend 404 | Verify: `ls /opt/smarthub/frontend/dist/index.html` |

## Directory Structure

```
/opt/smarthub/
├── bin/                 (Binaries)
├── frontend/dist/       (React SPA)
├── landing/             (Static landing page)
├── data/
│   ├── wiki/            (Wiki data)
│   └── cache/           (App cache)
└── db/migrations/       (SQL files)

/var/log/
├── smarthub/            (Deployment logs)
├── pm2/                 (Process manager logs)
└── caddy/               (Web server logs)

/etc/caddy/
└── Caddyfile            (Reverse proxy config)
```

## Key Files

| File | Purpose | Edit When |
|------|---------|-----------|
| `nrte_schema.sql` | DB schema | Database structure changes |
| `seed_data.sql` | Initial data | RTSG dimension changes |
| `Caddyfile` | Proxy config | Routing/TLS/header changes |
| `ecosystem.config.js` | Process config | Service ports/instances/env |
| `deploy.sh` | Automation | Build/deploy process changes |

## Performance Tuning

```bash
# Increase PM2 instances
# Edit ecosystem.config.js → instances: 4

# Adjust cache TTL
export CACHE_TTL=7200  # 2 hours

# Database connection pool
export MAX_POOL_SIZE=30

# Vector index lists (more = slower but more accurate)
# Edit nrte_schema.sql → lists = 100
```

## Security Checklist

- [ ] Database password-protected
- [ ] API TLS/HTTPS enabled
- [ ] Firewalls block direct DB access
- [ ] API authentication implemented (JWT/OAuth2)
- [ ] Rate limiting on /api/* endpoints
- [ ] Log rotation configured
- [ ] Backups automated and tested
- [ ] PM2 startup protection: `pm2 startup`

## Monitoring Commands

```bash
# Real-time process monitor
pm2 monit

# Detailed service status
pm2 show smarthub-api

# Web-based dashboard
pm2 web                    # Access at localhost:9615

# System resource usage
top
htop
iostat

# Database connections
psql -c "SELECT datname, usename, application_name, state FROM pg_stat_activity;"

# API metrics
curl http://localhost:8081/metrics
```

## Deployment Checklist

Pre-deployment:
- [ ] Build binaries: `go build -o ./bin/api-server ./cmd/api`
- [ ] Build frontend: `cd frontend && npm run build`
- [ ] Test migrations locally
- [ ] Validate Caddyfile: `caddy validate -c ./Caddyfile`
- [ ] Check disk space: `df -h /opt /var`

Deployment:
- [ ] Run: `./deploy.sh`
- [ ] Verify: `pm2 list`
- [ ] Check health: `curl https://smarthub.my/health`

Post-deployment:
- [ ] Monitor logs: `pm2 logs smarthub-api`
- [ ] Test API: `curl https://smarthub.my/api/v1/entities`
- [ ] Verify frontend: Visit https://smarthub.my/explore/
- [ ] Save process list: `pm2 save`
