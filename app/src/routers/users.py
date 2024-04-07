from typing import Annotated
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from ..dependencies_ import get_db, get_current_user, validate_token
from ..domain.user.schemas import UserCreate, User, UserProfile
from ..domain.user.service import create_user, get_user_by_username, get_user, check_email_and_username_exist,get_referred_users_from_user

router = APIRouter(
    tags=["user"],
    prefix="/user"
)


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user_(user: UserCreate, db: Session = Depends(get_db)):
    user_db = check_email_and_username_exist(db, user.email, user.username)
    if user_db:
        raise HTTPException(status_code=400, detail="User with this email or username is already registered")
    created_user = create_user(db, user)
    return created_user

@router.get("/me", response_model=UserProfile)
def user_(user: User = Depends(get_current_user)):
    return user

@router.get("/referred", response_model=Page[UserProfile])
def get_referred_users(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    referred_users = get_referred_users_from_user(db, current_user)
    return paginate(referred_users)

@router.get("/{username}", response_model=UserProfile)
def user_by_username_(username: str, db: Session = Depends(get_db), valid_token = Depends(validate_token)):
    user = get_user_by_username(db, username)
    if not user:
        return JSONResponse(status_code=404, content={"message": "User not found"})
    return user

