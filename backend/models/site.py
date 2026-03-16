from datetime import datetime, timezone

from app.extensions import db


class Site(db.Model):
    __tablename__ = "sites"

    id = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.String(32), unique=True, nullable=False)
    region = db.Column(db.String(64), nullable=False, index=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    signal_strength = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(32), nullable=False, default="active")
    created_at = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    def to_dict(self):
        return {
            "id": self.id,
            "site_id": self.site_id,
            "region": self.region,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "signal_strength": self.signal_strength,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
