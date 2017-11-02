from apistar.test import TestClient
from project.views import index
from app import app


# def test_index():
#     """
#     Testing a view directly.
#     """
#     data = index(session=Session)
#     assert "Nedbank Montioring" in data


def test_index():
    """
    Testing index view, using the test client.
    """
    client = TestClient(app)
    response = client.get('http://localhost/')
    assert response.status_code == 200
    assert b"Monitoring" in response.content
    assert b"Nedbank" in response.content
    assert b"Nedbank ID" in response.content


def test_update():
    client = TestClient(app)
    response = client.put('http://localhost/1', status=False)
    pass


