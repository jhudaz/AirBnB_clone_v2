#!/usr/bin/python3
"""This is the state class"""
import sqlalchemy
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    storage = os.environ.get("HBNB_TYPE_STORAGE")
    if storage == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="delete", backref="state")
    else:
        @property
        def cities(self):
            city_list = []
            data = models.storage.all(City)
            for city in data:
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
