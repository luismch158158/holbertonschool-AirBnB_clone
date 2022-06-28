#!/usr/bin/python3

from models.base_model import BaseModel
import json
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
        for key in self.__objects:
            dictionary[key] = self.__objects[key].to_dict()
            # print("-----------")
            # print(dictionary)
            # print("-----------")


        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(dictionary, file)
    
    def reload(self):
        """
        """
        if exists(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                file_json = json.load(file)
            for key, value in file_json.items():
                self.__objects[key] = value
