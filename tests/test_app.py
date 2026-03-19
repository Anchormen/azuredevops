import re

import pytest
from app.main import app
from fastapi import status
from fastapi.testclient import TestClient


@pytest.fixture()
def client():
    yield TestClient(app)


def test_square(client):
    response = client.get("/square_number?number=2")
    assert response.status_code == status.HTTP_200_OK
    assert "Square of 2.0 is 4.0" == response.json()


def test_hello_world(client):
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert re.match(".* on host .*", response.json())
