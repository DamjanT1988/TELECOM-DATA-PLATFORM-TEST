from flask import Blueprint, jsonify, request

from app.extensions import db
from models.site import Site
from services.site_service import validate_site_payload

site_bp = Blueprint("sites", __name__)


@site_bp.get("/sites")
def list_sites():
    region = request.args.get("region")
    query = Site.query
    if region:
        query = query.filter_by(region=region)
    rows = query.order_by(Site.site_id.asc()).all()
    return jsonify([row.to_dict() for row in rows]), 200


@site_bp.get("/sites/<int:record_id>")
def get_site(record_id: int):
    row = db.session.get(Site, record_id)
    if row is None:
        return jsonify({"error": "Site not found"}), 404
    return jsonify(row.to_dict()), 200


@site_bp.post("/site")
def create_site():
    payload = request.get_json(silent=True) or {}
    try:
        clean = validate_site_payload(payload)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    existing = Site.query.filter_by(site_id=clean["site_id"]).first()
    if existing:
        return jsonify({"error": "site_id already exists"}), 409

    row = Site(**clean)
    db.session.add(row)
    db.session.commit()
    return jsonify(row.to_dict()), 201


@site_bp.put("/site/<int:record_id>")
def update_site(record_id: int):
    payload = request.get_json(silent=True) or {}
    row = db.session.get(Site, record_id)
    if row is None:
        return jsonify({"error": "Site not found"}), 404

    try:
        clean = validate_site_payload(payload)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    conflicting = Site.query.filter_by(site_id=clean["site_id"]).first()
    if conflicting and conflicting.id != record_id:
        return jsonify({"error": "site_id already exists"}), 409

    row.site_id = clean["site_id"]
    row.region = clean["region"]
    row.latitude = clean["latitude"]
    row.longitude = clean["longitude"]
    row.signal_strength = clean["signal_strength"]
    row.status = clean["status"]
    db.session.commit()
    return jsonify(row.to_dict()), 200


@site_bp.delete("/site/<int:record_id>")
def delete_site(record_id: int):
    row = db.session.get(Site, record_id)
    if row is None:
        return jsonify({"error": "Site not found"}), 404

    db.session.delete(row)
    db.session.commit()
    return jsonify({"deleted": record_id}), 200
