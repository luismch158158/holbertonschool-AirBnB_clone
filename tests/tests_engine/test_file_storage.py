#!/usr/bin/python3
"""Module that describe the FileStorage test class"""
import unittest
import json
import models
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os


class TestFileStorage(unittest.TestCase):
    """Class for test the BaseModel Class method and atributes"""

    def setUp(self):
        """All variables that we need"""
        self.filestorage = FileStorage()

    def test_filestorage_all(self):
        """Test the dictionary __objects"""
        self.assertTrue(type(self.filestorage.all() is dict))

    def test_filestorage_new(self):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = f'{self.filestorage.__class__.name}.{self.filestorage.id}'
        self.assertTrue(type(key) is str)

    def test_storage_save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        PATH = './file.json'
        value = os.path.isfile(PATH)
        self.assertTrue(value)

    def test_filestorage_reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        ; otherwise, do nothing. If the file doesn’t exist"""
        pass

    def tearDown(self):
        """Closing the test class and deleteing the instance
            created for testing"""
        pass


if __name__ == '__main__':
    unittest.main()
