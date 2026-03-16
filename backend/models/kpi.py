from datetime import date, datetime, timezone

from app.extensions import db


class KPI(db.Model):
    __tablename__ = "kpis"

    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(64), nullable=False, index=True)
    snapshot_date = db.Column(db.Date, nullable=False, default=date.today)
    network_uptime = db.Column(db.Float, nullable=False)
    latency = db.Column(db.Float, nullable=False)
    packet_loss = db.Column(db.Float, nullable=False)
    traffic_volume = db.Column(db.Float, nullable=False)
    signal_strength = db.Column(db.Float, nullable=False)
    created_at = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False
    )

    def to_dict(self):
        return {
            "id": self.id,
            "region": self.region,
            "snapshot_date": self.snapshot_date.isoformat(),
            "network_uptime": self.network_uptime,
            "latency": self.latency,
            "packet_loss": self.packet_loss,
            "traffic_volume": self.traffic_volume,
            "signal_strength": self.signal_strength,
            "created_at": self.created_at.isoformat(),
        }
