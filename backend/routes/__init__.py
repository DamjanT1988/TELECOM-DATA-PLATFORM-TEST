from routes.health import health_bp
from routes.kpis import kpi_bp
from routes.sites import site_bp
from routes.upload import upload_bp


def register_blueprints(app):
    app.register_blueprint(health_bp, url_prefix="/api")
    app.register_blueprint(site_bp, url_prefix="/api")
    app.register_blueprint(kpi_bp, url_prefix="/api")
    app.register_blueprint(upload_bp, url_prefix="/api")
