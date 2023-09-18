#!/usr/bin/python3
"""Place Module for HBNB project."""

from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

Base = declarative_base()

class Place(BaseModel, Base):
    """A place to stay."""

    __tablename__= 'places'
    city_id = Column(String(60), ForeignKey(cities.id) , nullable=False)
    user_id = Column(String(60), ForeignKey(users.id) , nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer(), default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
    # for DBStorage
    reviews = relationship('Review', cascade='all, delete, delete-orphan', backref='place')
    # for Filestorage
    #-----------------------------------------
