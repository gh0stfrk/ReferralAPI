import pytest

@pytest.fixture
def user_json():
    return {
  "name": "rust",
  "username": "rust",
  "email": "rust@example.com",
  "password": "rust"
}
