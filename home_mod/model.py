"""
User model
"""

from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import mapper
from dbengine import BASE

class User(BASE):
    """
    User model class extending SQLAlchemy BASE
    """
    __tablename__ = 'users'

    _id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.name

# USERS = Table('users', META_DATA,
#               Column('id', Integer, primary_key=True),
#               Column('name', String(50)),
#               Column('email', String(100)))

# mapper(User, USERS)


class UserTest(BASE):
    """
    Another Test DB
    """

    __tablename__ = 'users_test'

    _id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return'<UserTest %r>' % self.name
