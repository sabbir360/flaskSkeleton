"""
Used for DB migrate
"""
from dbengine import DBENGINE, BASE
# from home_mod.model import *

def status_of_init(table_name):
    """
    Print table name while exec.
    """
    print("Executing table:")
    print(table_name.__tablename__)

def init_db():
    """
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    # import yourapplication.models
    """
    # status_of_init(User)
    # META_DATA.create_all(bind=DBENGINE)
    BASE.metadata.create_all(bind=DBENGINE)
    print("Done....")

init_db()
