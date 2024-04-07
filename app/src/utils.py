import uuid
from passlib.context import CryptContext
from fastapi import HTTPException, status
from jose import JWTError, jwt, ExpiredSignatureError
from datetime import timedelta, datetime
from .domain.user.models import User
from .config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, JWT_SECRET


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Create an access token.
    :param data: The data to encode in the token.
    :param expires_delta: The expiration time of the token.
    :return: The access token.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> dict:
    """
    Decode an access token.
    :param token: The access token to decode.
    :return: The decoded token.
    """
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        return payload
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    
def get_user_from_token(token: str) -> User | None :
    """
    Get the user from an access token.
    :param token: The access token.
    :return: The user.
    """
    payload = decode_access_token(token)
    if payload:
        username = payload.get("sub")
        from .domain.user.service import get_user_by_username
        from .dependencies_ import get_db
        
        db = next(get_db())
        user: User = get_user_by_username(db, username)
        if user:
            return user
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User does not exist")

def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt.
    :param password: The password to hash.
    :return: The hashed password.
    """
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password:str) -> bool:
    """
    Verify a password using bcrypt.
    :param password: The password to verify.
    :param hashed_password: The hashed password to compare against.
    :return: True if the password matches, False otherwise.
    """
    return pwd_context.verify(password, hashed_password)

def generate_unique_code(long_code: bool = False) -> str:
    """ 
    Generate a unique code.
    :param long_code: Whether to generate a long code.
    :return: The unique code.
    """
    unique_id = uuid.uuid4()
    unique_str = str(unique_id)
    if long_code:
        return unique_str
    code = unique_str.split("-")
    return code[0]