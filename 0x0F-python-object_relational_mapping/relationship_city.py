#!/usr/bin/python3
<<<<<<< HEAD
"""Lists states"""

from sqlalchemy import Column, Integer, String, ForeignKey
@@ -12,3 +13,21 @@ class City(Base):
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
=======
"""
Module Docs
"""
from relationship_state import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, ForeignKey
class City(Base):
    """
    Class Docs
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
>>>>>>> 643653f5f799640582e021b490799985cf16eddb`
