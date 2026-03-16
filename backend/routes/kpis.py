from flask import Blueprint, jsonify, request

from models.kpi import KPI

kpi_bp = Blueprint("kpis", __name__)


@kpi_bp.get("/kpis")
def list_kpis():
    region = request.args.get("region")
    query = KPI.query
    if region:
        query = query.filter_by(region=region)
    rows = query.order_by(KPI.snapshot_date.asc()).all()
    return jsonify([row.to_dict() for row in rows]), 200
