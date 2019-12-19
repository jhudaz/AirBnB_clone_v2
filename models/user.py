#!/usr/bin/python3
"""This is the user class"""
import sqlalchemy
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    storage = os.getenv("HBNB_TYPE_STORAGE")
    if storage == "db":
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        passwd = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
    else:

        email = ""
        password = ""
        first_name = ""
        last_name = ""
