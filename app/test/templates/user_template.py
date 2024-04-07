import pytest
from datetime import datetime


@pytest.fixture
def user_json():
    return {
  "name": "rust",
  "username": "rust",
  "email": "rust@example.com",
  "password": "rust"
}

@pytest.fixture
def insert_user_json():
  return {
  "hashed_password": "$2b$12$vnrmXHbLcOxmRyHuk9oWh.K3yHrA6EzuXYhIquST.lC5/NPHEOoCW",
  "referral_code": "3703f493",
  "created_at": "2024-04-07T14:09:04",
  "username": "rust",
  "email": "rust@example.com", 
  "id": 6,
  "name": "rust",
  "is_deleted": False,
  "reffered_by": "system",
  "updated_at": "2024-04-07T14:09:04"
}
