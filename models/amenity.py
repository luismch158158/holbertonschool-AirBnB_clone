#!/usr/bin/python3
from models.base_model import BaseModel
import models

class Amenity(BaseModel):
    """
    Class Amenity that inherits from BaseModel
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes Amenity"""
        super().__init__(*args, **kwargs)