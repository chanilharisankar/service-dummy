import os
from fastapi.testclient import TestClient
from app.main import app

def test_whoami_default(monkeypatch):
    monkeypatch.setenv("SERVICE_NAME", "foo")
    client = TestClient(app)
    response = client.get("/whoami")
    assert response.status_code == 200
    assert response.json() == {"identity": "Hi , I am service foo"}

def test_whoami_custom(monkeypatch):
    monkeypatch.setenv("SERVICE_NAME", "bar")
    client = TestClient(app)
    response = client.get("/whoami")
    assert response.status_code == 200
    assert response.json() == {"identity": "Hi , I am service bar"}
