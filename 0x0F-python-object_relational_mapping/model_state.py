#!/usr/bin/python3
<<<<<<< HEAD
"""Lists states"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model_city import City
=======
"""
Module Docs
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
>>>>>>> 643653f5f799640582e021b490799985cf16eddb
Base = declarative_base()
class State(Base):
<<<<<<< HEAD
    """Class representing the states table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
=======
    """
    Class Docs
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
>>>>>>> 643653f5f799640582e021b490799985cf16eddb
