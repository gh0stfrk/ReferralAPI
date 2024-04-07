from .database_tables import tables
from .config import database_config

def configure_test_database(app):
    """ Configures test database """
    database_config.configure_test_database(app)
    
def clear_database():
    """ Clears database """
    database_config.truncate_tables(tables)

def drop_all():
    database_config.drop_all_tables()