+++
title = "API Reference"
+++

# API Reference

Base URL: `http://localhost:5000/api`

## Endpoints

- `GET /health` - service health check
- `GET /sites?region=<name>` - list sites (optional region filter)
- `GET /sites/{id}` - get one site by internal DB id
- `POST /site` - create site
- `PUT /site/{id}` - update site
- `DELETE /site/{id}` - delete site
- `GET /kpis?region=<name>` - list KPI snapshots
- `POST /upload` - upload CSV/JSON telecom site file

## Upload format

CSV required columns:

- `site_id`
- `region`
- `signal_strength`

JSON upload must be an array of objects with the same fields.
