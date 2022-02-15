from sqlalchemy import Column, Integer, String
from main.configurations.database.db import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column('username', String(100))
    names = Column('names', String(100))
    lastNames = Column('last_names', String(100))
    email = Column('email', String(100))
    password = Column('password', String(200))

    def __init__(self, username=None, names=None, lastNames=None, email=None ,password=None):
        self.username = username
        self.names = names
        self.lastNames = lastNames
        self.email = email
        self.password = password

    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'names': self.names,
            'lastNames': self.lastNames,
            'email': self.email,
            'password': self.password,
        }


    def __repr__(self):
        return "<User '{}'>".format(self.username)