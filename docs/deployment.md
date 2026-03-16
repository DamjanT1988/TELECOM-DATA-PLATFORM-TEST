+++
title = "Deployment"
+++

# Deployment Guide

## Local Docker Compose

```bash
docker-compose up --build
```

Services:

- Frontend (Hugo): `http://localhost:1313`
- Backend (Flask): `http://localhost:5000`
- PostgreSQL: `localhost:5433`

## Runtime behavior

- `database/schema.sql` initializes tables in PostgreSQL.
- Flask app auto-creates missing tables and inserts seed records when empty.
- Frontend fetches API data from `http://localhost:5000/api`.

## CI/CD

The GitHub Actions pipeline:
1. Installs backend dependencies
2. Runs tests
3. Builds Docker images
4. Boots compose stack and performs a health check
