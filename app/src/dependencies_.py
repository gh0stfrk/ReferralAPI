from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

from .utils import get_user_from_token
from .database import SessionLocal


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def get_current_user(token = Depends(oauth2_scheme)):
    """ Get current user """
    from .domain.user.schemas import User
    user = get_user_from_token(token)
    user_schema = User.from_orm(user)
    return user_schema

def get_db():
    """ Create a database session """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
