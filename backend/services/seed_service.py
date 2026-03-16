from datetime import date
from pathlib import Path

from app.extensions import db
from models.kpi import KPI
from models.site import Site
from parsers.csv_parser import parse_sites_csv
from services.site_service import upsert_sites


def seed_if_empty():
    if Site.query.count() == 0:
        _seed_sites_from_realistic_csv()

    if KPI.query.count() == 0:
        db.session.add_all(
            [
                KPI(
                    region="Stockholm",
                    snapshot_date=date(2026, 3, 10),
                    network_uptime=99.91,
                    latency=23.2,
                    packet_loss=0.2,
                    traffic_volume=1200.5,
                    signal_strength=-71.0,
                ),
                KPI(
                    region="Gothenburg",
                    snapshot_date=date(2026, 3, 10),
                    network_uptime=99.70,
                    latency=28.5,
                    packet_loss=0.4,
                    traffic_volume=950.4,
                    signal_strength=-66.0,
                ),
                KPI(
                    region="Malmo",
                    snapshot_date=date(2026, 3, 10),
                    network_uptime=99.55,
                    latency=31.1,
                    packet_loss=0.7,
                    traffic_volume=820.2,
                    signal_strength=-70.0,
                ),
                KPI(
                    region="Stockholm",
                    snapshot_date=date(2026, 3, 11),
                    network_uptime=99.93,
                    latency=22.6,
                    packet_loss=0.2,
                    traffic_volume=1275.8,
                    signal_strength=-70.0,
                ),
                KPI(
                    region="Gothenburg",
                    snapshot_date=date(2026, 3, 11),
                    network_uptime=99.75,
                    latency=27.4,
                    packet_loss=0.3,
                    traffic_volume=980.1,
                    signal_strength=-65.0,
                ),
                KPI(
                    region="Malmo",
                    snapshot_date=date(2026, 3, 11),
                    network_uptime=99.60,
                    latency=30.5,
                    packet_loss=0.6,
                    traffic_volume=860.3,
                    signal_strength=-69.0,
                ),
            ]
        )

    db.session.commit()


def _seed_sites_from_realistic_csv():
    csv_path = Path(__file__).resolve().parents[1] / "data" / "realistic_sites.csv"
    if csv_path.exists():
        rows = parse_sites_csv(csv_path.read_text(encoding="utf-8"))
        upsert_sites(rows)
        return

    # Safe fallback if data file is missing.
    db.session.add_all(
        [
            Site(
                site_id="101",
                region="Stockholm",
                latitude=59.3293,
                longitude=18.0686,
                signal_strength=-72.0,
                status="active",
            ),
            Site(
                site_id="102",
                region="Gothenburg",
                latitude=57.7089,
                longitude=11.9746,
                signal_strength=-65.0,
                status="active",
            ),
            Site(
                site_id="103",
                region="Malmo",
                latitude=55.6050,
                longitude=13.0038,
                signal_strength=-69.0,
                status="maintenance",
            ),
        ]
    )
