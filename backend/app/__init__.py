import logging
import time

from flask import Flask, jsonify
from sqlalchemy.exc import OperationalError

from app.config import Config
from app.extensions import db
from routes import register_blueprints
from services.seed_service import seed_if_empty


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    if test_config:
        app.config.update(test_config)
    _configure_logging(app)

    db.init_app(app)

    with app.app_context():
        _initialize_database_with_retry(app)
        seed_if_empty()

    register_blueprints(app)
    _register_cors(app)
    _register_error_handlers(app)
    return app


def _configure_logging(app):
    level = getattr(logging, app.config.get("LOG_LEVEL", "INFO").upper(), logging.INFO)
    logging.basicConfig(
        level=level, format="%(asctime)s %(levelname)s [%(name)s] %(message)s"
    )
    app.logger.setLevel(level)


def _register_error_handlers(app):
    @app.errorhandler(413)
    def payload_too_large(_):
        return jsonify({"error": "File too large"}), 413


def _register_cors(app):
    @app.after_request
    def add_headers(response):
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
        response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
        return response


def _initialize_database_with_retry(app):
    # Compose startup can race DNS/DB readiness; retry avoids crash-looping.
    retries = 15
    delay_seconds = 2
    for attempt in range(1, retries + 1):
        try:
            # Lightweight auto-create for local/demo use.
            db.create_all()
            return
        except OperationalError as exc:
            if attempt == retries:
                app.logger.exception("Database initialization failed after retries")
                raise
            app.logger.warning(
                "Database not ready (attempt %s/%s): %s", attempt, retries, exc
            )
            time.sleep(delay_seconds)
