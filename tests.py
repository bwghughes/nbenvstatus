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
    response = client.put('/update/1', dict(data=dict(status=False)))
    assert response.status_code == 204
    response = client.get("/")
    assert b"card-success" in response.content
    count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("card-success"), str(response.content)))
    assert count == 1

    # And another
    response = client.put('/update/2', dict(data=dict(status=False)))
    assert response.status_code == 204
    response = client.get("/")
    assert b"card-success" in response.content
    count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("card-success"), str(response.content)))
    assert count == 2
