import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_health(client):
    rv = client.get('/health')
    assert rv.status_code == 200
    assert rv.data == b'healthy'


# def test_quote(client):
#     rv = client.get('/quote')
#     assert rv.status_code == 200


def test_root(client):
    rv = client.get('/')
    assert rv.status_code == 200