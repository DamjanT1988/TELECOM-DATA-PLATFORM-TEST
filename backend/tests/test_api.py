import io


def test_health(client):
    res = client.get("/api/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"


def test_create_list_delete_site(client):
    payload = {
        "site_id": "200",
        "region": "Stockholm",
        "latitude": 59.3,
        "longitude": 18.0,
        "signal_strength": -67,
        "status": "active",
    }
    created = client.post("/api/site", json=payload)
    assert created.status_code == 201
    site = created.get_json()

    listed = client.get("/api/sites?region=Stockholm")
    assert listed.status_code == 200
    assert any(item["site_id"] == "200" for item in listed.get_json())

    deleted = client.delete(f"/api/site/{site['id']}")
    assert deleted.status_code == 200


def test_upload_csv(client):
    data = {
        "file": (
            io.BytesIO(
                b"site_id,region,latitude,longitude,signal_strength,status\n"
                b"500,Stockholm,59.3,18.0,-70,active\n"
            ),
            "sites.csv",
        )
    }
    res = client.post("/api/upload", data=data, content_type="multipart/form-data")
    assert res.status_code == 201
    assert res.get_json()["records_processed"] == 1
