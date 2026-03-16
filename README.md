# TELECOM-DATA-PLATFORM-TEST

Fullstack telecom data platform simulation with:

- Hugo static frontend + Chart.js dashboards
- Flask REST backend + SQLAlchemy ORM
- PostgreSQL storage
- Docker Compose orchestration
- GitHub Actions CI pipeline
- Docs-as-code rendered into Hugo

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
docker-compose up --build
```

Open:

- Frontend: http://localhost:1313
- Backend API: http://localhost:5000/api/health

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
