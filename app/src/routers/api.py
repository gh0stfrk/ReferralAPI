from fastapi import APIRouter
from . import users, auth
from ..config import ROUTE_PREFIX_V1

router = APIRouter()

def include_all_routes():
    """
    Merge all routes 
    """
    router.include_router(users.router, prefix=ROUTE_PREFIX_V1)
    router.include_router(auth.router, prefix=ROUTE_PREFIX_V1)
    
include_all_routes()