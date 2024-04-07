from pydantic import BaseModel, EmailStr, field_serializer
from datetime import datetime, timezone
from typing import Optional


class User(BaseModel):
    id: int
    name: str
    email: str
    username: str
    referral_code: str
    reffered_by: str 
    created_at: datetime
    
    @field_serializer('created_at')
    def serialize_dt(dt: datetime) -> str:
        return dt.isoformat()
    
    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str
    referred_by: str | None = None
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    
class UserProfile(BaseModel):
    name: str
    username: str
    email: EmailStr
    created_at: datetime
    
    @field_serializer('created_at')
    def serialize_dt(dt: datetime) -> str:
        return dt.strftime("%Y-%m-%d")
    
    class Config:
        from_attributes = True