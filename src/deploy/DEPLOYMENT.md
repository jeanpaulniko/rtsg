# NRTE Deployment Artifacts

Production-ready deployment configuration for the Network Relational Topological Embedding (NRTE) system with SmartHub frontend.

## Files Overview

### 1. `nrte_schema.sql` (131 lines)
Complete PostgreSQL schema for the NRTE database.

**Tables:**
- `entities` - Core semantic units (nouns, relations, things)
- `relations` - Directional edges between entities
- `dimension_vectors` - Embeddings in RTSG dimensions (relational, topological, geometric)
- `gram_cache` - Precomputed basis matrices and Gram products
- `embeddings` - Vector embeddings for similarity search (768-dim)
- `relation_embeddings` - Vector embeddings for relation vectors
- `schema_metadata` - Migration tracking

**Features:**
- pgvector extension for 768-dimensional embeddings with IVFFLAT indexing
- Comprehensive indexes on all foreign keys and query columns
- UUID support for distributed tracing
- JSONB metadata for extensibility
- Timestamps for audit trails

### 2. `seed_data.sql` (109 lines)
Initialization data for the 3 RTSG dimensions with basis matrices.

**Dimensions:**
1. **Relational** - Network structure properties
   - Coordinates: Symmetry, Connectivity, Centrality, Flow, Clustering
   - 5×5 basis matrix with inter-dimension correlations

2. **Topological** - Shape and topology properties
   - Coordinates: Genus, Betti-0, Betti-1, Euler-χ, Boundary
   - 5×5 basis matrix capturing topological relationships

3. **Geometric** - Spatial and curvature properties
   - Coordinates: Curvature, Volume, Area, Geodesic-L, Torsion
   - 5×5 basis matrix for geometric relationships

**Format:** All 25 Gram products per dimension stored as JSONB for efficient retrieval.

### 3. `Caddyfile` (105 lines)
Caddy reverse proxy configuration for domain management and routing.

**Routing:**
```
smarthub.my
├── /              → Static landing page (/opt/smarthub/landing)
├── /explore/*     → React SPA frontend (/opt/smarthub/frontend/dist)
├── /api/*         → Go API server (localhost:8080)
├── /wiki/*        → Wiki service (localhost:3000)
└── /metrics       → Metrics endpoint (localhost:8081)
```

**Features:**
- Automatic TLS with Let's Encrypt
- Security headers (HSTS, X-Content-Type-Options, CSP)
- CORS support for /api/*
- Access logging (JSON, rotated)
- Forwarded headers for upstream services
- HTTP → HTTPS redirect

### 4. `ecosystem.config.js` (178 lines)
PM2 process manager configuration for all services.

**Services:**
1. **smarthub-api** - Go API server
   - 2 instances in cluster mode
   - Memory limit: 1GB
   - Health check: GET /health every 30s
   - Auto-restart on failure

2. **smarthub-wiki** - Existing wiki service
   - Single instance (fork mode)
   - Memory limit: 512MB
   - Health check: GET /health every 30s

3. **smarthub-migrations** - Database migration service
   - On-demand execution
   - Does not auto-start

4. **smarthub-metrics** - Metrics collector
   - Single instance
   - Memory limit: 256MB
   - Health check endpoint on :8081

**Features:**
- Graceful shutdown (30s timeout)
- Structured JSON logging
- Per-service log rotation
- Environment variable management
- Deployment hooks for PM2+

### 5. `deploy.sh` (446 lines)
Comprehensive deployment automation script.

**Phases:**
1. **Prerequisite Checks** - Validates required tools and connectivity
2. **Directory Creation** - Sets up /opt/smarthub structure
3. **Binary Copying** - Deploys compiled binaries
4. **API Build** - Compiles Go server with test suite
5. **Frontend Build** - npm install → npm run build
6. **Database Migrations** - Creates schema and seeds data
7. **Caddy Update** - Validates and reloads proxy config
8. **Service Restart** - Uses PM2 to reload all processes
9. **Health Checks** - Verifies all endpoints are accessible

**Options:**
```bash
./deploy.sh --help              # Show usage
./deploy.sh --dry-run           # Simulate without changes
./deploy.sh --skip-tests        # Skip test suites
./deploy.sh --db-only           # Migrations only
./deploy.sh --no-restart        # Build but don't restart services
```

**Environment Variables:**
- `DB_HOST` - Database hostname (default: localhost)
- `DB_PORT` - Database port (default: 5432)
- `DB_NAME` - Database name (default: nrte_production)
- `DB_USER` - Database user (default: postgres)
- `DEPLOY_ROOT` - Installation directory (default: /opt/smarthub)

**Features:**
- Comprehensive error handling with rollback hooks
- Colored console output with timestamps
- Detailed logging to `/var/log/smarthub/deploy-*.log`
- Caddy configuration validation
- PM2 health checks post-deployment
- PostgreSQL connectivity verification

## Deployment Steps

### Prerequisites
```bash
# System packages
apt-get install caddy postgresql postgresql-contrib

# Go binaries (from ./bin/)
go build -o ./bin/api-server ./cmd/api
go build -o ./bin/db-migrate ./cmd/migrations

# Node environment
cd frontend && npm install && npm run build

# PM2 process manager
npm install -g pm2

# Database user setup
createuser -P nrte_api    # User for API (read-only to most tables)
createuser -P nrte_admin  # User for migrations (full access)
```

### Deploy
```bash
# Standard deployment
./deploy.sh

# Dry run to preview changes
./deploy.sh --dry-run

# Skip tests for faster iteration
./deploy.sh --skip-tests

# Database migrations only
./deploy.sh --db-only
```

### Post-Deployment
```bash
# Verify services
pm2 list
pm2 logs smarthub-api

# Check endpoints
curl https://smarthub.my/health
curl https://smarthub.my/explore/
curl https://smarthub.my/api/v1/entities

# Monitor processes
pm2 monit

# View logs
tail -f /var/log/caddy/smarthub.log
tail -f /var/log/pm2/smarthub-api-out.log
```

## Database Schema Details

### Entities Table
```sql
CREATE TABLE entities (
    id BIGSERIAL PRIMARY KEY,
    uuid UUID UNIQUE,
    name VARCHAR(255),
    type VARCHAR(50),           -- noun, relation, thing, entity
    lojban_form VARCHAR(255),   -- Optional Lojban representation
    english VARCHAR(1024),      -- English description
    metadata JSONB,
    created_at, updated_at TIMESTAMP WITH TIME ZONE
);
```

### Relations Table
```sql
CREATE TABLE relations (
    id BIGSERIAL PRIMARY KEY,
    subject_id BIGINT FK,
    predicate VARCHAR(255),
    object_id BIGINT FK,
    weight FLOAT,               -- Relationship strength
    metadata JSONB,
    created_at, updated_at TIMESTAMP WITH TIME ZONE
);
```

### Dimension Vectors Table
```sql
CREATE TABLE dimension_vectors (
    id BIGSERIAL PRIMARY KEY,
    entity_id BIGINT FK,
    dimension VARCHAR(50),      -- relational, topological, geometric
    basis_index INT,
    components FLOAT[],
    number_system VARCHAR(50),  -- real, complex, quaternion
    confidence FLOAT,
    created_at, updated_at TIMESTAMP WITH TIME ZONE
);
```

### Gram Cache Table
```sql
CREATE TABLE gram_cache (
    id BIGSERIAL PRIMARY KEY,
    dimension VARCHAR(50),
    dim1 INT,
    dim2 INT,
    number_system VARCHAR(50),
    matrix_data JSONB,          -- Basis matrix as JSON
    gram_product FLOAT,
    computed_at TIMESTAMP
);
```

### Embeddings Table
```sql
CREATE TABLE embeddings (
    id BIGSERIAL PRIMARY KEY,
    entity_id BIGINT FK,
    model VARCHAR(100),
    vector vector(768),         -- pgvector type
    model_version VARCHAR(50),
    created_at, updated_at TIMESTAMP WITH TIME ZONE
);
```

## Performance Considerations

### Indexing Strategy
- Foreign keys indexed for join performance
- Dimension lookups: `(entity_id, dimension)` composite index
- Vector search: IVFFLAT index with 100 lists (configurable)
- Time-based queries: indexes on `created_at` and `updated_at`

### Connection Pooling
- API server: `MAX_POOL_SIZE=20` (ecosystem.config.js)
- Wiki: `MAX_POOL_SIZE=10` (default)
- Adjust based on workload via environment variables

### Cache Strategy
- `CACHE_TTL=3600` (1 hour) for entity lookups
- Gram matrices cached in `gram_cache` table
- Vector embeddings cached in `embeddings` table with model versioning

### Monitoring
- Metrics collector runs on port 8081
- PM2 health checks every 30s per service
- Database query logging available via PostgreSQL
- Access logs available in /var/log/caddy/smarthub.log

## Directory Structure

```
/opt/smarthub/
├── bin/
│   ├── api-server
│   ├── wiki-server
│   ├── db-migrate
│   └── metrics-collector
├── frontend/
│   └── dist/                   # Built React app
├── landing/
│   └── index.html              # Static landing page
├── data/
│   ├── wiki/                   # Wiki data store
│   └── cache/                  # Application cache
└── db/
    └── migrations/             # SQL migration files
```

## Security Notes

1. **Database Users**
   - `nrte_api`: Read-only to most tables, write to embeddings/caches
   - `nrte_admin`: Full access for migrations only
   - Enforce SSL connections: `sslmode=require`

2. **TLS Certificates**
   - Caddy auto-renews Let's Encrypt certificates
   - Store in `/etc/caddy/data/` with proper permissions
   - Monitor expiration: `caddy list-certstore`

3. **API Authentication**
   - Implement JWT/OAuth2 in API server
   - Caddy passes Authorization headers via `X-Forwarded-*`
   - Rate limiting recommended on /api/* endpoints

4. **Data Isolation**
   - Use entity UUIDs for distributed tracing
   - Relation metadata supports access control tagging
   - Implement row-level security in PostgreSQL if needed

## Rollback Procedure

If deployment fails:

1. Check logs: `/var/log/smarthub/deploy-*.log`
2. Revert Caddyfile: `git checkout Caddyfile && caddy reload`
3. Revert binaries: `git checkout bin/`
4. Reset services: `pm2 reload ecosystem.config.js --env production`
5. Database: Keep schema/data (backward compatible), manual revert if needed

For critical failures:
```bash
# Stop all services
pm2 stop all

# Restore from backup
pg_restore -d nrte_production /path/to/backup.sql

# Restart
pm2 start ecosystem.config.js --env production
```

## Troubleshooting

**API won't start**
```bash
pm2 logs smarthub-api
# Check: DB connectivity, port 8080 available, binary permissions
```

**Frontend shows 404**
```bash
# Verify build output
ls -la /opt/smarthub/frontend/dist/index.html
# Check Caddy config: caddy validate -c /etc/caddy/Caddyfile
```

**Database errors**
```bash
# Check connectivity
psql -h localhost -U nrte_admin -d nrte_production -c "SELECT 1"
# View logs
tail -f /var/log/postgresql/postgresql.log
```

**TLS certificate issues**
```bash
# Check certificate status
caddy list-certstore
# View Caddy logs
tail -f /var/log/caddy/smarthub.log
```

## License
Same as NRTE project
