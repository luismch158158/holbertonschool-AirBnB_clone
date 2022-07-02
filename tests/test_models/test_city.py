#!/usr/bin/python3

from datetime import datetime
import json
import unittest
import uuid
from models import city
from models.city import City
import os
import models


class TestReview(unittest.TestCase):
    """Test case class of unittest"""

    def setUp(self):
        """Method that sets all initial values"""
        self.city = City()
        self.city.state_id = "ascca65161asc"
        self.city.name = "Londres"

    def test_city_instantiation(self):
        """Test to validation instantiation of city"""
        self.assertIsInstance(self.city, City)

    def test_city_atributes_id(self):
        """Test to validation datatype of id"""
        self.assertTrue(type(self.city.id) is str)

    def test_city_atributes_created_at(self):
        """Test to validation datatype of created_at"""
        self.assertTrue(type(self.city.created_at) is datetime)

    def test_city_atributes_update_at(self):
        """Test to validation datatype of updated_at"""
        self.assertTrue(type(self.city.updated_at) is datetime)

    def test_city_state_id(self):
        """Test to validation datatype of state_id"""
        self.assertTrue(type(self.city.state_id) is str)

    def test_city_name(self):
        """Test to validation datatype of name"""
        self.assertTrue(type(self.city.name) is str)

    def test_city_save(self):
        """Test to validation if I successufully create
        the file.json"""
        PATH = './file.json'
        value = os.path.isfile(PATH)
        self.assertTrue(value)

    def test_city_to_dict(self):
        """Test to validation if method dict return data type dict"""
        self.assertTrue(type(self.city.to_dict()) is dict)

    def test_city__str__(self):
        """Test to validation if method str return correct format"""
        name = self.city.__class__.__name__
        city = f'[{name}] ({self.city.id}) {self.city.__dict__}'
        self.assertTrue(self.city.__str__() == city)

    def tearDown(self):
        """Method to close tests"""
        del self.city


if __name__ == '__main__':
    unittest.main()
