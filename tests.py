import re

import pytest
from apistar.test import TestClient

from app import app
from project.views import index


@pytest.fixture(scope='function')
def test_data():
    """Fixture to create environments for testing."""
    client = TestClient(app)
    response = client.post('/environments/?name=Test App 1')
    assert response.status_code == 200
    response = client.post('/environments/?name=Test App 2')
    assert response.status_code == 200


def test_index(test_data):
    """Testing index view, using the test client."""
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == 200
    assert b"TEST APP 1" in response.content
    assert b"TEST APP 2" in response.content


def test_update_on_id():
    """Check updates on scrren function as we think they do"""
    client = TestClient(app)
    
    # Check all red
    response = client.get('/')
    assert b"card-danger" in response.content
    assert b"card-success" not in response.content
    
    # Make one green and check
    test_result = True
    response = client.put(f"/environments/test-app-1?test_result={test_result}")
    assert response.status_code == 200
    assert response.json()
    response = client.get("/")
    assert b"card-success" in response.content
    count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("card-success"), str(response.content)))
    assert count == 1

    # And another
    response = client.put(f"/environments/test-app-2?test_result={test_result}")
    assert response.status_code == 200
    assert response.json()
    response = client.get("/")
    assert b"card-success" in response.content
    count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("card-success"), str(response.content)))
    assert count == 2


def test_create_works_and_id_displayed_on_page():
    client = TestClient(app)
    response = client.post('/environments/?name=Test App')
    assert response.status_code == 200
    response = client.get('/environments/test-app')
    assert response.status_code == 200
    response = client.get('/')
    assert b"TEST APP" in response.content

def test_404_for_non_existant_environment():
    """Check non existant slug is indeed non existant"""
    client = TestClient(app)
    response = client.get('/environments/some-silly-slug')
    assert response.status_code == 404


def test_200_for_existing():
    """Check existing records a retrievable by the slug"""
    client = TestClient(app)
    response = client.post('/environments/?name=Test App')
    assert response.status_code == 200
    response = client.get('/environments/test-app')
    assert response.status_code == 200


def test_create_gives_bad_request_if_no_name_query_parameter():
    """Check we have  afailure with a malformed request"""
    client = TestClient(app)
    response = client.post('/environments/')
    assert response.status_code == 400


def test_list_environments():
    """Check all environments are returned"""
    client = TestClient(app)
    response = client.get('/environments/')
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_health_endpoint():
    """Health endpoint for monitoring"""
    client = TestClient(app)
    response = client.get('/health/')
    assert response.status_code == 200


def test_delete_endpoint():
    """Endpoint is deleted when called"""
    client = TestClient(app)
    response = client.post('/environments/?name="Test App Delete"')
    assert response.status_code == 200
    response = client.delete('/environments/test-app-delete')
    assert response.status_code == 204
    response = client.get('/environments/test-app-delete/')
    assert response.status_code == 404

    
