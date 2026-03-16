+++
title = "Architecture"
+++

# System Architecture

The platform uses a layered architecture:

1. Hugo static frontend for dashboards and reports
2. JavaScript API client for REST communication
3. Flask API service for business logic and ingestion
4. PostgreSQL database for telecom entities and KPI time series

## Data Flow

Frontend -> Flask API -> SQLAlchemy -> PostgreSQL

Admin uploads (CSV/JSON) are validated, parsed, and upserted into `sites`.
KPI records are persisted in `kpis` and visualized in Chart.js dashboards.

## Components

- `backend/app`: app factory, config, extensions
- `backend/models`: SQLAlchemy entity models
- `backend/routes`: API blueprints
- `backend/services`: ingestion and seed logic
- `backend/parsers`: CSV/JSON parsing
- `frontend/hugo-site`: Hugo pages and static assets
