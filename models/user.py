#!/usr/bin/python3
from models.base_model import BaseModel
import models

class User(BaseModel):
    """
    Class User that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes User"""
        super().__init__(*args, **kwargs)
