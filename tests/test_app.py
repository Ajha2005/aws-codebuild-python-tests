
import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_route(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["message"] == "Welcome to AWS CodeBuild!"
    assert response.json["status"] == "Application is running"


def test_health_route(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_invalid_route(client):
    response = client.get("/invalid")

    assert response.status_code == 404
