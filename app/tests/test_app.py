import pytest
from src import create_app
from src.database import db

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        db.create_all()

    return app.test_client()

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"

def test_create_user(client):
    response = client.post("/users")
    assert response.status_code == 201
    assert "id" in response.json

def test_get_users(client):
    client.post("/users")
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json, list)
