#!/usr/bin/python3
"""Module that defines the city model representing a city for a MySQL database"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the base class for the declarative model
Base = declarative_base()

class City(Base):
    """Represents a city for a MySQL database.

    Attributes:
        id (str): The city's id
        name (sqlalchemy.Integer): The city's name
        state_id (sqlalchemy. String): The city's state id
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
