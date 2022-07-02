#!/usr/bin/python3
"""Module that initializing"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.review import Review
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State

dictionaries = {"BaseModel": BaseModel, "User": User,
                "Place": Place, "State": State, "City": City,
                "Amenity": Amenity, "Review": Review}

storage = FileStorage()
storage.reload()
