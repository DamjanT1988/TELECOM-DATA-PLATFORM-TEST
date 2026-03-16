import csv
from io import StringIO


REQUIRED_SITE_FIELDS = {"site_id", "region", "signal_strength"}


def parse_sites_csv(content: str):
    reader = csv.DictReader(StringIO(content))
    fieldnames = set(reader.fieldnames or [])
    missing = REQUIRED_SITE_FIELDS - fieldnames
    if missing:
        raise ValueError(f"Missing required CSV fields: {', '.join(sorted(missing))}")

    rows = []
    for row in reader:
        rows.append(
            {
                "site_id": str(row.get("site_id", "")).strip(),
                "region": str(row.get("region", "")).strip(),
                "latitude": _to_optional_float(row.get("latitude")),
                "longitude": _to_optional_float(row.get("longitude")),
                "signal_strength": _to_float(row.get("signal_strength"), "signal_strength"),
                "status": str(row.get("status", "active")).strip() or "active",
            }
        )
    return rows


def _to_float(value, field_name: str) -> float:
    try:
        return float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"Invalid numeric value for {field_name}") from exc


def _to_optional_float(value):
    if value is None or value == "":
        return None
    return _to_float(value, "latitude/longitude")
