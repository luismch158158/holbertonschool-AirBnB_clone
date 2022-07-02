#!/usr/bin/python3
"""Module that describe the Amenity test class"""
from datetime import datetime
import json
import unittest
import uuid
from models.amenity import Amenity
import os
import models


class TestAmenity(unittest.TestCase):
    """
        Class for test the Amenity class method and atributes
    """

    def setUp(self):
        """All variables that we need
        to start for testing Amenity class"""
        self.amenity = Amenity()
        self.amenity.name = "Tv"
        self.amenity.save()

    def test_amenity_instantiation(self):
        """Test Amenity instantiation"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_amenity_atributes_id(self):
        """Test amenity atribue id"""
        self.assertTrue(type(self.amenity.id) is str)

    def test_amenity_atributes_created_at(self):
        """Test amenity atribute created at"""
        self.assertTrue(type(self.amenity.created_at) is datetime)

    def test_amenity_atributes_update_at(self):
        """Test amenity atributes update_at"""
        self.assertTrue(type(self.amenity.updated_at) is datetime)

    def test_amenity_atributes_id(self):
        """Test amenity atribue id"""
        self.assertTrue(type(self.amenity.name) is str)

    def test_amenity_save(self):
        """Test if the instance is stored correctly"""
        PATH = './file.json'
        value = os.path.isfile(PATH)
        self.assertTrue(value)

    def test_amenity_to_dict(self):
        """Test if the amenity dict has the correct format"""
        self.assertTrue(type(self.amenity.to_dict()) is dict)

    def test_amenity__str__(self):
        """Test if the amenity ___str__ method has the correct format
            described in the method"""
        name = self.amenity.__class__.__name__
        amenity = f'[{name}] ({self.amenity.id}) {self.amenity.__dict__}'
        self.assertTrue(self.amenity.__str__() == amenity)

    def tearDown(self):
        """Closing the test class and deleteing the instance
            created for testing"""
        del self.amenity


if __name__ == '__main__':
    unittest.main()
