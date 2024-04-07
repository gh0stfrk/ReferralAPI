from sqlalchemy.orm import Session
from typing import List
from .models import User
from .schemas import UserCreate
from ...utils import hash_password, generate_unique_code

def create_user(db: Session, user: UserCreate) -> User:
    """
    Create a new user in the database
    :param db: Database session
    :param user: User object to create
    :return: The created user object
    """
    db_user = User(username=user.username,name=user.name, hashed_password=hash_password(user.password),email=user.email, referral_code=generate_unique_code(), reffered_by=user.referred_by)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int) -> User:
    """
    Get a user by ID
    :param db: Database session
    :param user_id: ID of the user to get
    :return: The user object
    """
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> User:
    """
    Get a user by email
    :param db: Database session
    :param email: Email of the user to get
    :return: The user object 
    """
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str) -> User:
    """
    Get a user by username
    :param db: Database session
    :param username: Username of the user to get
    :return: The user object
    """
    return db.query(User).filter(User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
    """
    Get a list of users
    :param db: Database session
    :param skip: Number of users to skip
    :param limit: Number of users to return
    :return: List of user objects
    """
    return db.query(User).offset(skip).limit(limit).all()

def check_email_and_username_exist(db: Session, email: str, username: str) -> bool:
    """
    Check if an email or username already exists in the database
    :param db: Database session
    :param email: Email to check
    :param username: Username to check
    :return: True if the email or username already exists, False otherwise
    """
    user = get_user_by_email(db, email)
    if user:
        return True
    user = get_user_by_username(db, username)
    if user:
        return True
    return False