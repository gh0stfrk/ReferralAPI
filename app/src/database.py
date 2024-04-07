import os
from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_SERVER


SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite"

# SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:5432/referral"

engine = create_engine(
    os.getenv("DB_URL", SQLALCHEMY_DATABASE_URL),
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()