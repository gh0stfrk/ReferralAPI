import pytest
from fastapi.testclient import TestClient
from fastapi.security import OAuth2PasswordRequestForm
from ...main import app
from ..database_test import configure_test_database, clear_database, drop_all
from ..base_insert import insert_into_users
from ..templates.user_template import user_json, insert_user_json
import json

USER_ROUTE = "/api/v1/user"
AUTH_ROUTE = "/api/v1/auth"

client = TestClient(app)

def setup_module(module):
    configure_test_database(app)

def setup_function(function):
    drop_all()
    configure_test_database(app)

# Auth tests

def test_login_success(user_json, insert_user_json):
    user = client.post(USER_ROUTE, json=user_json)
    form_data = OAuth2PasswordRequestForm(username=user_json["username"], password=user_json["password"])
    data = json.dumps(form_data.__dict__)
    print(data)
    headers = {"Content-Type": "application/json"}
    response = client.post(AUTH_ROUTE + "/login", data=data, headers=headers)
    assert response.status_code == 200
    
# User tests

def test_sanity():
    response = client.get("/")
    assert response.status_code == 200
    
def test_create_user(user_json):
    response = client.post(USER_ROUTE, json=user_json)
    assert response.status_code == 201

def test_recreate_user(user_json):
    user1 = client.post(USER_ROUTE, json=user_json)
    user2 = client.post(USER_ROUTE, json=user_json)
    assert user2.status_code == 400
