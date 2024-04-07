from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from ..dependencies_ import get_db, get_current_user
from ..domain.user.schemas import UserCreate, User
from ..domain.user.models import User as UserModel
from ..domain.user.service import create_user, get_user_by_email, get_user, check_email_and_username_exist

router = APIRouter(
    tags=["user"],
    prefix="/user"
)


@router.post("/", response_model=User)
def create_user_(user: UserCreate, db: Session = Depends(get_db)):
    user_db = check_email_and_username_exist(db, user.email, user.username)
    if user_db:
        raise HTTPException(status_code=400, detail="User with this email or username is already registered")
    return create_user(db, user)


@router.get("/me", response_model=User)
def get_user_(user: User = Depends(get_current_user)):
    return user