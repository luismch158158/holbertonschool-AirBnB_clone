#!/usr/bin/python3
"""Module that describe the FileStorage class"""
import models
import json
from models.base_model import BaseModel
from os.path import exists
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review


class FileStorage():
    """This class FileStorage serializes instances to a JSON
    and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dictionary = {}
        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()

        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            file.write(json.dumps(dictionary))

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        ; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                self.__objects = json.loads(file.read())
            for key, value in self.__objects.items():
                self.__objects[
                    key] = (models.dictionaries[value['__class__']](**value))

        except FileNotFoundError:
            pass
