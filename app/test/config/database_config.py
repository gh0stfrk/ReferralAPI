from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

from ...src.database import Base
from ...src.dependencies_ import get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.sqlite"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()
        
def configure_test_database(app):
    Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = override_get_db

def drop_all_tables():
    Base.metadata.drop_all(bind=engine)
    
def truncate_tables(tables):
    ''' Truncate rows of all input tables '''
    with engine.connect() as con:
        
        IGNORE_CONSTRAINTS = """PRAGMA ignore_check_constraints = 0"""
        DISABLE_IGNORE_CONSTRAINTS = """PRAGMA ignore_check_constraints = 1"""

        # statement = f"DELETE FROM {var}"

        con.execute(text(IGNORE_CONSTRAINTS))
        
        for line in tables:
            # con.execute(statement.bindparams(table=line))
            con.execute(text(f"DELETE FROM {line}"))
            print(f"DELETE FROM {line}")
        con.execute(text(DISABLE_IGNORE_CONSTRAINTS))
    # Base.metadata.drop_all(bind=engine)