+++
title = "Developer Guide"
+++

# Developer Guide

## Backend

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

## Data Upload

Use `backend/data/sample_sites.csv` or `backend/data/sample_sites.json`:

```bash
curl -F "file=@backend/data/sample_sites.csv" http://localhost:5000/api/upload
```

## Frontend

The Hugo frontend uses section templates and JavaScript in `static/js`.
`Chart.js` is loaded from CDN in the shared base template.

## Coding standards

- Keep routes thin and move business logic into services
- Keep parsers focused on transformation and validation
- Prefer explicit JSON error responses with HTTP status codes
