from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

from .utils import get_user_from_token, decode_access_token
from .database import SessionLocal


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def get_current_user(token = Depends(oauth2_scheme)):
    """ Get current user """
    # from .domain.user.schemas import User
    from .domain.user.service import get_user_by_username
    user = get_user_from_token(token)
    return user

def validate_token(token: str = Depends(oauth2_scheme)) -> bool:
    """ Validate token """
    token_status = decode_access_token(token)
    return True if token_status else False

def get_db():
    """ Create a database session """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
