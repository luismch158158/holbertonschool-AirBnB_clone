#!/usr/bin/python3
from models.base_model import BaseModel
import models

class City(BaseModel):
    """
    Class City that inherits from BaseModel
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes City"""
        super().__init__(*args, **kwargs)