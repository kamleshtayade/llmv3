from fastapi.testclient import TestClient

from fastapi_feeder.main import app


def test_root():
    client = TestClient(app)
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Hello World"}


def test_users():
    client = TestClient(app)
    r = client.get("/users")
    assert r.status_code == 200
    assert r.json() == ["Rick", "Morty"]
