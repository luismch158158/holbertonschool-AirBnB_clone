#!/usr/bin/python3
from models.base_model import BaseModel
import models

class Review(BaseModel):
    """
    Class Review that inherits from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes review"""
        super().__init__(*args, **kwargs)