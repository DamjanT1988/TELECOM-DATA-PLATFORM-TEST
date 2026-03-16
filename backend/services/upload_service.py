from app.extensions import db
from models.upload import Upload
from parsers.csv_parser import parse_sites_csv
from parsers.json_parser import parse_sites_json
from services.site_service import upsert_sites


def process_upload(filename: str, raw_bytes: bytes):
    file_type = _infer_type(filename)
    text = raw_bytes.decode("utf-8")

    if file_type == "csv":
        rows = parse_sites_csv(text)
    elif file_type == "json":
        rows = parse_sites_json(text)
    else:
        raise ValueError("Unsupported file type. Use .csv or .json")

    processed = upsert_sites(rows)
    upload = Upload(
        filename=filename,
        file_type=file_type,
        records_processed=processed,
        status="processed",
        message=f"Processed {processed} rows",
    )
    db.session.add(upload)
    db.session.commit()
    return upload


def _infer_type(filename: str):
    name = filename.lower()
    if name.endswith(".csv"):
        return "csv"
    if name.endswith(".json"):
        return "json"
    return None
