from app.extensions import db
from models.site import Site


def validate_site_payload(payload):
    required = ["site_id", "region", "signal_strength"]
    missing = [field for field in required if payload.get(field) in (None, "")]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")

    return {
        "site_id": str(payload["site_id"]).strip(),
        "region": str(payload["region"]).strip(),
        "latitude": _to_optional_float(payload.get("latitude")),
        "longitude": _to_optional_float(payload.get("longitude")),
        "signal_strength": float(payload["signal_strength"]),
        "status": str(payload.get("status", "active")).strip() or "active",
    }


def upsert_sites(rows):
    processed = 0
    for row in rows:
        clean = validate_site_payload(row)
        site = Site.query.filter_by(site_id=clean["site_id"]).first()
        if site is None:
            site = Site(**clean)
            db.session.add(site)
        else:
            site.region = clean["region"]
            site.latitude = clean["latitude"]
            site.longitude = clean["longitude"]
            site.signal_strength = clean["signal_strength"]
            site.status = clean["status"]
        processed += 1
    db.session.commit()
    return processed


def _to_optional_float(value):
    if value in (None, ""):
        return None
    return float(value)
