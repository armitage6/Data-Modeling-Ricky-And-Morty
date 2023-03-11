import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    las_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    gmail = Column(String(250), nullable=False)
    favorite = relationship('favorite')

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user = Column(String(250))
    personaje = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    character = relationship('character')

    def to_dict(self):
        return {}

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    status = Column(String(250))
    species = Column(String(250))
    gender = Column(String(250))
    origin = Column(String(250))
    location = Column(String(250))
    episode = Column(String(250))
    favorite_id = Column(Integer, ForeignKey('favorite.id'))
   

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
