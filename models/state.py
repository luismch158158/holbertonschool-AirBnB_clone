#!/usr/bin/python3
from models.base_model import BaseModel
import models

class State(BaseModel):
    """
    Class State that inherits from BaseModel
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes state"""
        super().__init__(*args, **kwargs)