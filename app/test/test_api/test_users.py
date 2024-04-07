import pytest
from fastapi.testclient import TestClient
from ...main import app
from ..database_test import configure_test_database, clear_database
from ..base_insert import insert_into_users
from ..templates.user_template import user_json

USER_ROUTE = "/api/v1/user"

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_module(module):
    configure_test_database(app)

@pytest.fixture(scope="function")
def setup_function(function):
    print("Bingo")
    clear_database()
    
def test_create_user(user_json):
    clear_database()
    response = client.post(USER_ROUTE, json=user_json)
    assert response.status_code == 201

def test_do_nothing():
    assert True