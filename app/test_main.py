from fastapi.testclient import TestClient

from main import app

from os import environ

client = TestClient(app)

environ['API_KEY'] = "API_KEY"


def test_check():
    response = client.post("/check", json={"pattern": [1, 2, 3]}, headers={"api-key": "API_KEY"})
    assert response.status_code == 400
    client.post("/load", json={"chunk": [1, 2, 3]}, headers={"api-key": "API_KEY"})
    response = client.post("/check", json={"pattern": [1, 2, 3]}, headers={"api-key": "API_KEY"})
    assert response.status_code == 200
    assert response.json() == {"exists": True}
    client.post("/load", json={"chunk": [1, 2, 3]}, headers={"api-key": "API_KEY"})
    response = client.post("/check", json={"pattern": [3, 2, 1]}, headers={"api-key": "API_KEY"})
    assert response.status_code == 200
    assert response.json() == {"exists": False}
    client.post("/load", json={"chunk": [1, 2, 3]}, headers={"api-key": "API_KEY"})
    response = client.post("/check", json={"pattern": [1, None, 3]}, headers={"api-key": "API_KEY"})
    assert response.status_code == 200
    assert response.json() == {"exists": True}
    client.post("/load", json={"chunk": [1, 2, 3]}, headers={"api-key": "API_KEY"})
    response = client.post("/check", json={"pattern": [1, "NaN", 3]}, headers={"api-key": "API_KEY"})
    assert response.status_code == 422


def test_load():
    response = client.post("/load", json={"chunk": [1, 2, 3]}, headers={"api-key": "API_KEY"})
    assert response.status_code == 200
    response = client.post("/load", json={"chunk": [1, None, 3]}, headers={"api-key": "API_KEY"})
    assert response.status_code == 200
    response = client.post("/load", json={"chunk": [1, "NaN", 3]}, headers={"api-key": "API_KEY"})
    assert response.status_code == 422
