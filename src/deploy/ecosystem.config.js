// PM2 Ecosystem Configuration for SmartHub NRTE
// Manages all service processes: API, Wiki, and ancillary services
// Uses cluster mode for the API to leverage multiple cores

module.exports = {
  apps: [
    {
      // SmartHub NRTE API Server
      name: 'smarthub-api',
      script: '/opt/smarthub/bin/api-server',
      instances: 2,
      exec_mode: 'cluster',

      // Environment variables
      env: {
        NODE_ENV: 'production',
        PORT: '8080',
        DB_HOST: 'localhost',
        DB_PORT: '5432',
        DB_NAME: 'nrte_production',
        DB_USER: 'nrte_api',
        LOG_LEVEL: 'info',
        CACHE_TTL: '3600',
        MAX_POOL_SIZE: '20',
      },

      // Process management
      watch: false,
      ignore_watch: [
        'node_modules',
        'logs',
        'tmp',
        '.git',
      ],
      max_memory_restart: '1G',

      // Error handling and restart
      autorestart: true,
      max_restarts: 10,
      min_uptime: '10s',

      // Graceful shutdown
      kill_timeout: 30000,
      listen_timeout: 30000,

      // Logging
      output: '/var/log/pm2/smarthub-api-out.log',
      error: '/var/log/pm2/smarthub-api-err.log',
      log: '/var/log/pm2/smarthub-api.log',
      time: true,

      // Health checks and metrics
      health_check: {
        endpoint: 'http://localhost:8080/health',
        timeout: 5000,
        interval: 30000,
      },

      // Instance configuration
      merge_logs: false,
      cwd: '/opt/smarthub',
    },

    {
      // SmartHub Wiki (existing service)
      name: 'smarthub-wiki',
      script: '/opt/smarthub/bin/wiki-server',
      instances: 1,
      exec_mode: 'fork',

      // Environment variables
      env: {
        NODE_ENV: 'production',
        PORT: '3000',
        WIKI_DATA_PATH: '/opt/smarthub/data/wiki',
        LOG_LEVEL: 'info',
      },

      // Process management
      watch: false,
      max_memory_restart: '512M',
      autorestart: true,
      max_restarts: 10,
      min_uptime: '10s',

      // Graceful shutdown
      kill_timeout: 20000,

      // Logging
      output: '/var/log/pm2/smarthub-wiki-out.log',
      error: '/var/log/pm2/smarthub-wiki-err.log',
      log: '/var/log/pm2/smarthub-wiki.log',
      time: true,

      // Health checks
      health_check: {
        endpoint: 'http://localhost:3000/health',
        timeout: 5000,
        interval: 30000,
      },

      cwd: '/opt/smarthub',
    },

    {
      // Database migration and maintenance service (runs on demand)
      name: 'smarthub-migrations',
      script: '/opt/smarthub/bin/db-migrate',
      instances: 1,
      exec_mode: 'fork',
      autorestart: false,

      env: {
        NODE_ENV: 'production',
        DB_HOST: 'localhost',
        DB_PORT: '5432',
        DB_NAME: 'nrte_production',
        DB_USER: 'nrte_admin',
        MIGRATIONS_PATH: '/opt/smarthub/db/migrations',
      },

      output: '/var/log/pm2/smarthub-migrations-out.log',
      error: '/var/log/pm2/smarthub-migrations-err.log',
      log: '/var/log/pm2/smarthub-migrations.log',
      time: true,

      cwd: '/opt/smarthub',
    },

    {
      // Metrics and monitoring collector
      name: 'smarthub-metrics',
      script: '/opt/smarthub/bin/metrics-collector',
      instances: 1,
      exec_mode: 'fork',

      env: {
        NODE_ENV: 'production',
        PORT: '8081',
        DB_HOST: 'localhost',
        DB_PORT: '5432',
        DB_NAME: 'nrte_production',
        METRICS_INTERVAL: '60000',
      },

      max_memory_restart: '256M',
      autorestart: true,
      max_restarts: 10,
      min_uptime: '10s',

      output: '/var/log/pm2/smarthub-metrics-out.log',
      error: '/var/log/pm2/smarthub-metrics-err.log',
      log: '/var/log/pm2/smarthub-metrics.log',
      time: true,

      health_check: {
        endpoint: 'http://localhost:8081/health',
        timeout: 5000,
        interval: 30000,
      },

      cwd: '/opt/smarthub',
    },
  ],

  // Deployment configuration for PM2+
  deploy: {
    production: {
      user: 'smarthub',
      host: 'smarthub.my',
      ref: 'origin/main',
      repo: 'git@github.com:your-org/smarthub.git',
      path: '/opt/smarthub',
      'post-deploy': 'npm install && npm run build && pm2 reload ecosystem.config.js --env production',
      'pre-deploy-local': 'echo "Deploying to production"',
    },
  },
};
