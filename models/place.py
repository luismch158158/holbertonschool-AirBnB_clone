#!/usr/bin/python3
"""Module that describe the Place class"""
from models import amenity
from models.base_model import BaseModel
import models


class Place(BaseModel):
    """
    Class Place that inherits from BaseModel
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
