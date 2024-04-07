import os
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET", "super_secret_token*")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120

API_PREFIX = "/api"
ROUTE_PREFIX_V1 = "/v1"