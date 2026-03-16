import json


def parse_sites_json(content: str):
    try:
        payload = json.loads(content)
    except json.JSONDecodeError as exc:
        raise ValueError("Invalid JSON payload") from exc

    if not isinstance(payload, list):
        raise ValueError("JSON upload must be an array of site objects")

    rows = []
    for item in payload:
        if not isinstance(item, dict):
            raise ValueError("Each JSON array item must be an object")
        rows.append(
            {
                "site_id": str(item.get("site_id", "")).strip(),
                "region": str(item.get("region", "")).strip(),
                "latitude": _to_optional_float(item.get("latitude")),
                "longitude": _to_optional_float(item.get("longitude")),
                "signal_strength": _to_float(item.get("signal_strength"), "signal_strength"),
                "status": str(item.get("status", "active")).strip() or "active",
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
