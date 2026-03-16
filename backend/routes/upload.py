from flask import Blueprint, jsonify, request

from services.upload_service import process_upload

upload_bp = Blueprint("upload", __name__)


@upload_bp.post("/upload")
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part in request"}), 400

    file = request.files["file"]
    if file.filename is None or file.filename.strip() == "":
        return jsonify({"error": "File name is required"}), 400

    try:
        upload = process_upload(file.filename, file.read())
    except UnicodeDecodeError:
        return jsonify({"error": "Only UTF-8 files are supported"}), 400
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
    except Exception as exc:  # pragma: no cover
        return jsonify({"error": "Upload failed", "details": str(exc)}), 500

    return jsonify(upload.to_dict()), 201
