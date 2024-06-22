#!/usr/bin/python3
<<<<<<< HEAD
"""Lists states"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
=======
"""
Module Docs
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer, MetaData
from sqlalchemy.orm import relationship
>>>>>>> 643653f5f799640582e021b490799985cf16eddb
Base = declarative_base()
class State(Base):
<<<<<<< HEAD
    """Class representing the states table"""
    __tablename__ = 'states'
@@ -21,3 +32,12 @@ class State(Base):
        cascade="all, delete-orphan",
        backref=backref("state", cascade="all"),
        single_parent=True)
=======
    """
    Class Docs
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')
>>>>>>> 643653f5f799640582e021b490799985cf16eddb
