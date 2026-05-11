import pytest
from src.app import create_app

@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_dogs_endpoint(client):
    response = client.get('/dogs')
    assert response.status == "200 OK"

def test_dog_endpoint_success(client):
    response = client.get('/dogs/1')
    dog = response.json
    assert dog['name'] == 'Charlie'

def test_dog_endpoint_failure(client):
    response = client.get('/dogs/99')
    assert response.status == "204 NO CONTENT"