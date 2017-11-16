import re

from apistar.test import TestClient
from app import app
from project.views import index


def test_index():
    """
    Testing index view, using the test client.
    """
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == 200
    assert b"Monitoring" in response.content
    assert b"Nedbank" in response.content
    assert b"Nedbank ID" in response.content


def test_update_on_id():
    client = TestClient(app)
    
    # Check all red
    response = client.get('/')
    assert b"card-danger" in response.content
    assert b"card-success" not in response.content
    
    # Make one green and check
    response = client.put('/update/credit-decision-engine', dict(data=dict(status=False)))
    assert response.status_code == 204
    response = client.get("/")
    assert b"card-success" in response.content
    count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("card-success"), str(response.content)))
    assert count == 1

    # And another
    response = client.put('/update/mdm', dict(data=dict(status=False)))
    assert response.status_code == 204
    response = client.get("/")
    assert b"card-success" in response.content
    count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("card-success"), str(response.content)))
    assert count == 2


def test_create_works_and_id_displayed_on_page():
    client = TestClient(app)
    response = client.post('/create/?name=Test App')
    assert response.status_code == 200
    response = client.get('/test-app')
    assert response.status_code == 200
    response = client.get('/')
    assert b"test-app" in response.content
    

def test_check_404_for_non_existant_env():
    client = TestClient(app)
    response = client.get('/some-silly-slug')
    assert response.status_code == 404


def test_check_200_for_existing():
    client = TestClient(app)
    response = client.post('/create/?name=Test App')
    assert response.status_code == 200
    response = client.get('/test-app')
    assert response.status_code == 200


def test_create_gives_400_if_no_name_query_parameter():
    client = TestClient(app)
    response = client.post('/create/')
    assert response.status_code == 400