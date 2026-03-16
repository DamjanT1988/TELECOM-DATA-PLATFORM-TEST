# TELECOM-DATA-PLATFORM-TEST

Fullstack telecom data platform simulation with:

- Hugo static frontend + Chart.js dashboards
- Flask REST backend + SQLAlchemy ORM
- PostgreSQL storage
- Docker Compose orchestration
- GitHub Actions CI pipeline
- Docs-as-code rendered into Hugo

Default startup behavior seeds sites from `backend/data/realistic_sites.csv`.

## Project Structure

```text
backend/        Flask API, models, services, parsers, tests
frontend/       Hugo site and static assets
docs/           architecture, API, deployment, developer docs
database/       SQL schema
devops/         references for docker and CI layout
.github/        CI workflow
docker-compose.yml
```

## Quick Start

```bash
docker compose up --build
```

Open:

- Frontend: http://localhost:1313
- Backend API health: http://localhost:5000/api/health
- PostgreSQL (host): localhost:5433

Note: `http://localhost:5000/` intentionally returns `404`. API routes are under `/api/*`.

## Default Data Behavior

- On first startup (empty DB), site data is seeded from `backend/data/realistic_sites.csv`.
- KPI seed data is inserted for demo dashboards.
- If you already have old data, reset once to re-seed defaults:

```bash
docker compose down -v
docker compose up --build
```

## Test Dataset Files

- Small sample:
  - `backend/data/sample_sites.csv`
  - `backend/data/sample_sites.json`
- Realistic medium:
  - `backend/data/realistic_sites.csv`
  - `backend/data/realistic_sites.json`
- Large load/perf:
  - `backend/data/large_sites_5000.csv`
  - `backend/data/large_sites_2000.json`

## Key API Endpoints

- `GET /api/sites`
- `GET /api/sites/{id}`
- `GET /api/kpis`
- `POST /api/upload`
- `POST /api/site`
- `PUT /api/site/{id}`
- `DELETE /api/site/{id}`

## Local Backend Development

```bash
cd backend
python -m venv .venv
. .venv/Scripts/Activate.ps1
pip install -r requirements.txt
python run.py
```

Run tests:

```bash
pytest
```
