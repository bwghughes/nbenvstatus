import re

import pytest
from apistar.test import TestClient

from app import app
from project.views import index


@pytest.fixture(scope='function')
def test_data():
    client = TestClient(app)
    response = client.post('/environments/?name=Test App 1')
    assert response.status_code == 200
    response = client.post('/environments/?name=Test App 2')
    assert response.status_code == 200


def test_index(test_data):
    """
    Testing index view, using the test client.
    """
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == 200
    assert b"Test App 1" in response.content
    assert b"Test App 1" in response.content


def test_update_on_id():
    client = TestClient(app)
    
    # Check all red
    response = client.get('/')
    assert b"card-danger" in response.content
    assert b"card-success" not in response.content
    
    # Make one green and check
    response = client.put('/environments/test-app-1', dict(data=dict(status=False)))
    assert response.status_code == 204
    response = client.get("/")
    assert b"card-success" in response.content
    count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("card-success"), str(response.content)))
    assert count == 1

    # And another
    response = client.put('/environments/test-app-2', dict(data=dict(status=False)))
    assert response.status_code == 204
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
    assert b"test-app" in response.content


def test_check_404_for_non_existant_env():
    client = TestClient(app)
    response = client.get('/environments/some-silly-slug')
    assert response.status_code == 404


def test_check_200_for_existing():
    client = TestClient(app)
    response = client.post('/environments/?name=Test App')
    assert response.status_code == 200
    response = client.get('/environments/test-app')
    assert response.status_code == 200


def test_create_gives_400_if_no_name_query_parameter():
    client = TestClient(app)
    response = client.post('/environments/')
    assert response.status_code == 400


def test_list_environments():
    client = TestClient(app)
    response = client.get('/environments/')
    assert response.status_code == 200
    assert len(response.json()) > 0
