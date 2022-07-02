#!/usr/bin/python3
"""Module that describe the City class"""

from models.base_model import BaseModel
import models


class City(BaseModel):
    """
    Class City that inherits from BaseModel
    """

    state_id = ""
    name = ""
