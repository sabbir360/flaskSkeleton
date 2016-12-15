"""
ORM, basically DB connection will start here. And spreard out to whole system.
"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import SQLALCHEMY_DB_PATH


DBENGINE = create_engine(SQLALCHEMY_DB_PATH, convert_unicode=True, echo=True)
META_DATA = MetaData()
DB_SESSION = scoped_session(sessionmaker(autocommit=False, bind=DBENGINE))

BASE = declarative_base()
BASE.query = DB_SESSION.query_property()


# class Model(BASE):
#     """
#     Core model
#     """
#     created_at = Column(DateTime(), nullable=False)
#     updated_at = Column(DateTime(), nullable=False)
#     __tablename__ = None

#     def __init__(self, table_name):
#         self.created_at = strftime("%Y-%m-%d %H:%M:%S", gmtime())
#         self.update_at = created_at
#         self.__tablename__ = table_name

