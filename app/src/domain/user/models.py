from ...database import Base
from sqlalchemy.sql import func
from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, unique=True, primary_key=True, index=True)
    name = Column(String)
    username = Column(String(length=15), unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_deleted = Column(Boolean, default=False)
    referral_code = Column(String) 
    reffered_by = Column(String, default="system")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True),  onupdate=func.now(), server_default=func.now())