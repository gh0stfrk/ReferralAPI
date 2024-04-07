import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")

JWT_SECRET = os.getenv("JWT_SECRET", "super_secret_token*")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120

API_PREFIX = "/api"
ROUTE_PREFIX_V1 = "/v1"