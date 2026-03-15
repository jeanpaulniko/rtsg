#!/bin/bash
##############################################################################
# SmartHub NRTE Deployment Script
# Comprehensive deployment automation for the NRTE system
#
# Usage: ./deploy.sh [--help] [--dry-run] [--skip-tests]
#
# This script:
#   1. Creates directory structure
#   2. Validates prerequisites
#   3. Builds the API server
#   4. Builds the frontend
#   5. Runs database migrations
#   6. Updates reverse proxy configuration
#   7. Restarts all services via PM2
#
##############################################################################

set -euo pipefail

# Configuration
readonly DEPLOY_ROOT="/opt/smarthub"
readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly LOG_FILE="/var/log/smarthub/deploy-$(date +%Y%m%d-%H%M%S).log"
readonly DRY_RUN="${DRY_RUN:-false}"
readonly SKIP_TESTS="${SKIP_TESTS:-false}"

# Color output
readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly BLUE='\033[0;34m'
readonly NC='\033[0m' # No Color

# Logging functions
log() {
  echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $*" | tee -a "$LOG_FILE"
}

log_success() {
  echo -e "${GREEN}[✓]${NC} $*" | tee -a "$LOG_FILE"
}

log_error() {
  echo -e "${RED}[✗] ERROR:${NC} $*" | tee -a "$LOG_FILE"
}

log_warning() {
  echo -e "${YELLOW}[!] WARNING:${NC} $*" | tee -a "$LOG_FILE"
}

# Help text
show_help() {
  cat << EOF
SmartHub NRTE Deployment Script

Usage: ./deploy.sh [OPTIONS]

OPTIONS:
  --help              Show this help message
  --dry-run           Simulate deployment without making changes
  --skip-tests        Skip running test suites
  --no-restart        Skip service restart (testing mode)
  --db-only           Only run database migrations and exit

ENVIRONMENT VARIABLES:
  DRY_RUN             Set to 'true' to simulate deployment
  SKIP_TESTS          Set to 'true' to skip tests
  DEPLOY_ROOT         Deployment root directory (default: /opt/smarthub)
  DB_HOST             Database host (default: localhost)
  DB_PORT             Database port (default: 5432)
  DB_NAME             Database name (default: nrte_production)

EOF
}

# Trap errors
trap 'on_error' ERR

on_error() {
  log_error "Deployment failed at line $LINENO"
  log_error "Check logs at: $LOG_FILE"
  exit 1
}

# Check prerequisites
check_prerequisites() {
  log "Checking prerequisites..."

  local missing=()

  # Check required commands
  for cmd in docker docker-compose postgresql psql caddy pm2 git node npm go; do
    if ! command -v "$cmd" &> /dev/null; then
      missing+=("$cmd")
    fi
  done

  if [ ${#missing[@]} -gt 0 ]; then
    log_error "Missing required commands: ${missing[*]}"
    return 1
  fi

  # Check file permissions
  if [ ! -w /opt ]; then
    log_error "No write permission for /opt directory"
    return 1
  fi

  # Check PostgreSQL connectivity
  if ! pg_isready -h "${DB_HOST:-localhost}" -p "${DB_PORT:-5432}" &> /dev/null; then
    log_error "Cannot connect to PostgreSQL at ${DB_HOST:-localhost}:${DB_PORT:-5432}"
    return 1
  fi

  # Check PM2
  if ! pm2 ping &> /dev/null; then
    log_warning "PM2 daemon not running, starting it..."
    if [ "$DRY_RUN" != "true" ]; then
      pm2 start /dev/null --name dummy && pm2 delete dummy
    fi
  fi

  log_success "All prerequisites met"
}

# Create directory structure
create_directories() {
  log "Creating directory structure..."

  local dirs=(
    "$DEPLOY_ROOT/bin"
    "$DEPLOY_ROOT/frontend/dist"
    "$DEPLOY_ROOT/landing"
    "$DEPLOY_ROOT/data/wiki"
    "$DEPLOY_ROOT/data/cache"
    "$DEPLOY_ROOT/db/migrations"
    "/var/log/smarthub"
    "/var/log/pm2"
  )

  for dir in "${dirs[@]}"; do
    if [ "$DRY_RUN" = "true" ]; then
      log "  [DRY-RUN] mkdir -p $dir"
    else
      mkdir -p "$dir"
      chmod 755 "$dir"
    fi
  done

  log_success "Directory structure created"
}

# Copy binaries
copy_binaries() {
  log "Copying binaries..."

  local binaries=(
    "api-server"
    "wiki-server"
    "db-migrate"
    "metrics-collector"
  )

  for binary in "${binaries[@]}"; do
    local src="./bin/$binary"
    local dst="$DEPLOY_ROOT/bin/$binary"

    if [ ! -f "$src" ]; then
      log_warning "Binary not found: $src"
      continue
    fi

    if [ "$DRY_RUN" = "true" ]; then
      log "  [DRY-RUN] cp $src $dst"
    else
      cp "$src" "$dst"
      chmod 755 "$dst"
    fi
  done

  log_success "Binaries copied"
}

# Build API server
build_api() {
  log "Building API server..."

  if [ "$DRY_RUN" = "true" ]; then
    log "  [DRY-RUN] go build -o ./bin/api-server ./cmd/api"
    return 0
  fi

  if [ ! -d "./cmd/api" ]; then
    log_warning "API source not found, skipping build"
    return 0
  fi

  if [ "$SKIP_TESTS" != "true" ]; then
    log "  Running API tests..."
    if ! go test -v ./cmd/api/... -timeout 30s; then
      log_error "API tests failed"
      return 1
    fi
  fi

  go build -o ./bin/api-server ./cmd/api
  log_success "API server built"
}

# Build frontend
build_frontend() {
  log "Building frontend..."

  if [ "$DRY_RUN" = "true" ]; then
    log "  [DRY-RUN] npm install && npm run build"
    return 0
  fi

  if [ ! -f "./frontend/package.json" ]; then
    log_warning "Frontend source not found, skipping build"
    return 0
  fi

  cd ./frontend || return 1

  npm install --production
  if [ "$SKIP_TESTS" != "true" ]; then
    log "  Running frontend tests..."
    npm run test:ci || log_warning "Frontend tests failed (non-blocking)"
  fi

  npm run build
  cp -r dist/* "$DEPLOY_ROOT/frontend/dist/"

  cd - > /dev/null
  log_success "Frontend built and deployed"
}

# Run database migrations
run_migrations() {
  log "Running database migrations..."

  if [ "$DRY_RUN" = "true" ]; then
    log "  [DRY-RUN] Running migrations from ./db/migrations"
    return 0
  fi

  if [ ! -d "./db/migrations" ]; then
    log_warning "Migrations directory not found, skipping"
    return 0
  fi

  # Create nrte_production database if it doesn't exist
  PGHOST="${DB_HOST:-localhost}" PGPORT="${DB_PORT:-5432}" psql -U postgres -tc \
    "SELECT 1 FROM pg_database WHERE datname = 'nrte_production'" | grep -q 1 || \
    PGHOST="${DB_HOST:-localhost}" PGPORT="${DB_PORT:-5432}" psql -U postgres -c \
    "CREATE DATABASE nrte_production;"

  # Run schema migrations
  PGHOST="${DB_HOST:-localhost}" PGPORT="${DB_PORT:-5432}" PGDATABASE="nrte_production" \
    psql -U "${DB_USER:-postgres}" -f ./db/migrations/schema.sql

  # Seed initial data
  PGHOST="${DB_HOST:-localhost}" PGPORT="${DB_PORT:-5432}" PGDATABASE="nrte_production" \
    psql -U "${DB_USER:-postgres}" -f ./db/migrations/seed.sql

  log_success "Database migrations completed"
}

# Update Caddy configuration
update_caddy() {
  log "Updating Caddy configuration..."

  if [ "$DRY_RUN" = "true" ]; then
    log "  [DRY-RUN] cp ./Caddyfile /etc/caddy/Caddyfile"
    log "  [DRY-RUN] caddy reload -c /etc/caddy/Caddyfile"
    return 0
  fi

  if [ ! -f "./Caddyfile" ]; then
    log_error "Caddyfile not found in current directory"
    return 1
  fi

  # Validate Caddyfile
  if ! caddy validate --config ./Caddyfile &> /dev/null; then
    log_error "Caddyfile validation failed"
    return 1
  fi

  cp ./Caddyfile /etc/caddy/Caddyfile
  caddy reload -c /etc/caddy/Caddyfile

  log_success "Caddy configuration updated and reloaded"
}

# Update PM2 configuration and restart services
restart_services() {
  log "Restarting PM2 services..."

  if [ "$DRY_RUN" = "true" ]; then
    log "  [DRY-RUN] pm2 flush"
    log "  [DRY-RUN] pm2 start ./ecosystem.config.js --env production"
    return 0
  fi

  # Clear logs
  pm2 flush

  # Start or reload services
  if pm2 list | grep -q "smarthub-api"; then
    log "  Reloading existing processes..."
    pm2 reload ecosystem.config.js --env production --update-env
  else
    log "  Starting new processes..."
    pm2 start ecosystem.config.js --env production
  fi

  # Save PM2 configuration
  pm2 save
  pm2 startup

  # Wait for services to start
  sleep 3

  # Check service health
  log "  Checking service health..."
  if ! curl -sf http://localhost:8080/health > /dev/null 2>&1; then
    log_warning "API health check failed (may still be starting)"
  fi

  log_success "PM2 services restarted"
}

# Health checks
run_health_checks() {
  log "Running health checks..."

  local checks=(
    "API:http://localhost:8080/health"
    "Wiki:http://localhost:3000/health"
    "Caddy:https://smarthub.my/health"
  )

  local failed=0

  for check in "${checks[@]}"; do
    local name="${check%%:*}"
    local url="${check##*:}"

    if curl -sf "$url" > /dev/null 2>&1; then
      log_success "$name is healthy"
    else
      log_warning "$name health check failed or is starting"
      ((failed++))
    fi
  done

  if [ "$failed" -gt 0 ]; then
    log_warning "Some health checks failed, monitor logs for details"
  fi
}

# Rollback function
rollback() {
  log_error "Initiating rollback..."
  log "Rollback implementation required: restore from backup or use git revert"
  exit 1
}

# Main deployment flow
main() {
  local no_restart=false
  local db_only=false

  # Parse arguments
  while [[ $# -gt 0 ]]; do
    case $1 in
      --help)
        show_help
        exit 0
        ;;
      --dry-run)
        DRY_RUN=true
        shift
        ;;
      --skip-tests)
        SKIP_TESTS=true
        shift
        ;;
      --no-restart)
        no_restart=true
        shift
        ;;
      --db-only)
        db_only=true
        shift
        ;;
      *)
        log_error "Unknown option: $1"
        show_help
        exit 1
        ;;
    esac
  done

  # Print deployment info
  log "============================================"
  log "SmartHub NRTE Deployment"
  log "============================================"
  log "Deploy Root: $DEPLOY_ROOT"
  log "DRY RUN: $DRY_RUN"
  log "Skip Tests: $SKIP_TESTS"
  log "Log File: $LOG_FILE"
  log "============================================"

  # Run deployment steps
  check_prerequisites || rollback
  create_directories

  if [ "$db_only" = true ]; then
    run_migrations
    log_success "Database migrations completed"
    exit 0
  fi

  copy_binaries
  build_api
  build_frontend
  run_migrations

  if [ "$no_restart" != true ]; then
    update_caddy
    restart_services
    run_health_checks
  fi

  log_success "============================================"
  log_success "Deployment completed successfully!"
  log_success "Access SmartHub at: https://smarthub.my"
  log_success "============================================"
}

# Run main function
main "$@"
