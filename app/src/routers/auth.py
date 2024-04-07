from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from ..dependencies_ import get_db
from ..domain.user.service import get_user_by_username
from ..domain.user.schemas import Token
from ..utils import verify_password, create_access_token

router = APIRouter(
    tags=["auth"],
    prefix="/auth"
)


@router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db:Session = Depends(get_db)):
    invalid_user_exception = HTTPException(status_code=400, detail="Incorrect username or password")
    user = get_user_by_username(db, form_data.username)
    if not user:
        raise invalid_user_exception
    
    authenticated = verify_password(form_data.password, user.hashed_password)
    token_data = {"id": user.id, "sub": user.username, "visited": 0}
    token = create_access_token(token_data)
    
    if authenticated:
        return Token(access_token=token, token_type="bearer")
    raise invalid_user_exception
    