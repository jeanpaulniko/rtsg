# NRTE Deployment Artifacts

Production-ready deployment configuration for the Network Relational Topological Embedding (NRTE) system.

## Quick Start

1. **Review files:**
   - `nrte_schema.sql` - Database schema
   - `seed_data.sql` - Dimension data
   - `Caddyfile` - Reverse proxy config
   - `ecosystem.config.js` - Process management
   - `deploy.sh` - Deployment automation

2. **Deploy:**
   ```bash
   ./deploy.sh
   ```

3. **Access:**
   - Frontend: https://smarthub.my/explore/
   - API: https://smarthub.my/api/
   - Wiki: https://smarthub.my/wiki/

## Files

| File | Lines | Purpose |
|------|-------|---------|
| `nrte_schema.sql` | 131 | PostgreSQL schema with entities, relations, dimensions, embeddings |
| `seed_data.sql` | 109 | Seed data for 3 RTSG dimensions with 5×5 basis matrices |
| `Caddyfile` | 105 | Caddy reverse proxy with TLS, routing, security headers |
| `ecosystem.config.js` | 178 | PM2 process config for API (2 instances), Wiki, Metrics |
| `deploy.sh` | 446 | Full deployment automation with validation and health checks |

## Database Schema

**Core Tables:**
- `entities` - Semantic units with Lojban forms
- `relations` - Directional edges (subject → predicate → object)
- `dimension_vectors` - RTSG embeddings (relational, topological, geometric)
- `gram_cache` - Precomputed 5×5 basis matrices
- `embeddings` - 768-dim vector embeddings with pgvector
- `relation_embeddings` - Vector embeddings for relations

**Features:**
- pgvector extension for similarity search
- IVFFLAT indexes for fast vector queries
- UUID support for distributed tracing
- JSONB metadata for flexibility
- Comprehensive foreign key and query indexes

## RTSG Dimensions

Three orthogonal dimensions with 5-coordinate bases:

1. **Relational** - Network structure
   - Symmetry, Connectivity, Centrality, Flow, Clustering

2. **Topological** - Shape properties
   - Genus, Betti-0, Betti-1, Euler-χ, Boundary

3. **Geometric** - Spatial properties
   - Curvature, Volume, Area, Geodesic-L, Torsion

Each dimension includes a 5×5 Gram matrix capturing inter-coordinate correlations.

## Architecture

```
smarthub.my (Caddy)
├── /               → Landing page
├── /explore/*      → React SPA
├── /api/*          → Go API (2 instances, cluster mode)
├── /wiki/*         → Wiki service
└── /metrics        → Prometheus metrics

PostgreSQL (nrte_production)
├── entities
├── relations
├── dimension_vectors
├── gram_cache
├── embeddings
└── relation_embeddings
```

## Deployment

### Prerequisites
```bash
# Install dependencies
apt-get install caddy postgresql postgresql-contrib
npm install -g pm2

# Build services
go build -o ./bin/api-server ./cmd/api
cd frontend && npm install && npm run build

# Setup database users
createuser -P nrte_api
createuser -P nrte_admin
```

### Deploy
```bash
# Full deployment
./deploy.sh

# Dry run
./deploy.sh --dry-run

# Skip tests
./deploy.sh --skip-tests

# Database only
./deploy.sh --db-only
```

### Verify
```bash
pm2 list
curl https://smarthub.my/health
curl https://smarthub.my/api/v1/entities
```

## Configuration

**Environment Variables:**
- `DB_HOST` - Database host (localhost)
- `DB_PORT` - Database port (5432)
- `DB_NAME` - Database name (nrte_production)
- `DB_USER` - Database user (postgres)

**Service Ports:**
- API: 8080
- Wiki: 3000
- Metrics: 8081
- Caddy (HTTPS): 443

## Monitoring

```bash
# View logs
pm2 logs smarthub-api
tail -f /var/log/caddy/smarthub.log

# Monitor processes
pm2 monit

# Health checks
curl -s http://localhost:8080/health | jq .
```

## Documentation

See `DEPLOYMENT.md` for:
- Detailed schema documentation
- Performance tuning guide
- Security considerations
- Troubleshooting procedures
- Database user management
- Rollback procedures

## Support

For issues:
1. Check logs in `/var/log/smarthub/`
2. Review `DEPLOYMENT.md` troubleshooting section
3. Verify PM2 services: `pm2 status`
4. Test database: `psql -h localhost -U nrte_admin -d nrte_production`
