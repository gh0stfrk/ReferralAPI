from sqlalchemy.sql import text

from .config import database_config

engine = database_config.engine

def insert_into_users(input):
    """ Insert into table users """
    with engine.connect() as conn:
        data = (input, )
        statement = text(
            """INSERT INTO users(id, name, username, email, hashed_password, is_deleted, referral_code, reffered_by, created_at, updated_at ) VALUES(:id, :name, :username, :email, :hashed_password, :is_deleted, :referral_code, :reffered_by, :created_at, :updated_at)"""
        )
    
    for line in data:
        conn.execute(statement, **line)