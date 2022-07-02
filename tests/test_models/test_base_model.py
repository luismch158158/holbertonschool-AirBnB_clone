#!/usr/bin/python3
from datetime import datetime
import json
import unittest
import uuid
from models.base_model import BaseModel
import os
import models
"""Class BaseModel"""


class TestBaseModel(unittest.TestCase):
    """
        Class for test the BaseModel Class method and atributes
    """

    def setUp(self):
        """All variables that we need
        to start testing BaseModel class"""
        self.basemodel = BaseModel()
        self.basemodel.save()

    def test_basemodel_instantiation(self):
        """Test User instantiation"""
        self.assertIsInstance(self.basemodel, BaseModel)

    def test_basemodel_atributes_id(self):
        """Test User atribue id"""
        self.assertTrue(type(self.basemodel.id) is str)

    def test_basemodel_atributes_created_at(self):
        """Test BaseModel atribue created at"""
        self.assertTrue(type(self.basemodel.created_at) is datetime)

    def test_basemodel_atributes_update_at(self):
        """Test Basemodel atribue update_at"""
        self.assertTrue(type(self.basemodel.updated_at) is datetime)

    def test_basemodel_save(self):
        """Test if the instance is stored correctly"""
        PATH = './file.json'
        value = os.path.isfile(PATH)
        self.assertTrue(value)

    def test_basemodel_to_dict(self):
        """Test if the basemodel dict has the correct format"""
        self.assertTrue(type(self.basemodel.to_dict()) is dict)

    def test_basemodel__str__(self):
        """Test if the basemodel ___str__ method has the correct format
            descrited in the method"""
        name = self.basemodel.__class__.__name__
        basemodel = f'[{name}] ({self.basemodel.id}) {self.basemodel.__dict__}'
        self.assertTrue(self.basemodel.__str__() == basemodel)

    def tearDown(self):
        """Closing the test class and deleteing the instance
        created for testing"""
        del self.basemodel


if __name__ == '__main__':
    unittest.main()
