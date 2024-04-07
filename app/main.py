from fastapi import FastAPI
from .src.database import Base, engine
from .src.routers.api import router
from .src.config import API_PREFIX

def create_application() -> FastAPI:
    """ Create/Configure FastAPI application """
    application = FastAPI(title="User Referral System")
    Base.metadata.create_all(bind=engine)
    
    application.include_router(router, prefix=API_PREFIX)
    
    return application

app = create_application()

@app.get("/")
async def root():
    return {"msg": "Welcome to the root!"}