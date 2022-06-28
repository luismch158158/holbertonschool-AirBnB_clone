#!/usr/bin/python3
import models
import json
from models.base_model import BaseModel
from os.path import exists
"""

"""

class FileStorage():
    """
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        """
        return self.__objects
    
    def new(self, obj):
        """
        """
        #Ver validaciones de obj
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj
    
    def save(self):
        """
        """
        dictionary = {}
        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()

        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            file.write(json.dumps(dictionary))
    
    def reload(self):
        """
        """
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                self.__objects=json.loads(file.read())
            for key, value in self.__objects.items():
                self.__objects[key] = models.dictionaries[value['__class__']](**value)
        
        except FileNotFoundError:
            pass
