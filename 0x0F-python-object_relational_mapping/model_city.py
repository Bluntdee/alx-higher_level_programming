#!/usr/bin/python3
<<<<<<< HEAD
"""Lists states"""

from sqlalchemy import Column, Integer, String, ForeignKey
@@ -15,3 +16,21 @@ class City(Base):
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
=======
"""
Model Docs
"""
from model_state import Base, State
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
class City(Base):
    """
    Class Docs
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
>>>>>>> 643653f5f799640582e021b490799985cf16eddb
