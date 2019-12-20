#!/usr/bin/python3
"""This is the amenity class"""
import sqlalchemy
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = 'amenities'
    storage = os.getenv("HBNB_TYPE_STORAGE")
    if storage == "db":
        name = Column(String(128), nullable=False)

    else:
        name = ""
