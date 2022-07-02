#!/usr/bin/python3
"""Module that describe the Place test class"""

from datetime import datetime
import json
import unittest
import uuid
from models import place
from models.place import Place
import os
import models


class TestPlace(unittest.TestCase):
    """Test case class of unittest """

    def setUp(self):
        """Method that sets all initial values"""
        self.place = Place()
        self.place.city_id = "nlalnc662asc2"
        self.place.user_id = "jhsin6619"
        self.place.name = "Posada de Don Tito"
        self.place.description = "Bonito y acogedor"
        self.place.number_rooms = 6
        self.place.number_bathrooms = 3
        self.place.max_guest = 8
        self.place.price_by_night = 45
        self.place.latitude = 40.416775
        self.place.longitude = -3.703790
        self.place.amenity_ids = ["tv", "ducha", "cocina"]
        self.place.save()

    def test_place_instantiation(self):
        """Test to validation instantiation of place"""
        self.assertIsInstance(self.place, Place)

    def test_place_atributes_id(self):
        """Test to validation datatype of id"""
        self.assertTrue(type(self.place.id) is str)

    def test_place_atributes_created_at(self):
        """Test to validation datatype of created_at"""
        self.assertTrue(type(self.place.created_at) is datetime)

    def test_place_atributes_update_at(self):
        """Test to validation datatype of updated_at"""
        self.assertTrue(type(self.place.updated_at) is datetime)

    def test_place_city_id(self):
        """Test to validation datatype of city_id"""
        self.assertTrue(type(self.place.city_id) is str)

    def test_place_user_id(self):
        """Test to validation datatype of user_id"""
        self.assertTrue(type(self.place.user_id) is str)

    def test_place_name(self):
        """Test to validation datatype of name"""
        self.assertTrue(type(self.place.name) is str)

    def test_place_description(self):
        """Test to validation datatype of name"""
        self.assertTrue(type(self.place.description) is str)

    def test_place_number_rooms(self):
        """Test to validation datatype of number of rooms"""
        self.assertTrue(type(self.place.number_rooms) is int)

    def test_place_number_bathrooms(self):
        """Test to validation datatype of number of bathrooms"""
        self.assertTrue(type(self.place.number_bathrooms) is int)

    def test_place_max_guest(self):
        """Test to validation datatype of max_guest"""
        self.assertTrue(type(self.place.max_guest) is int)

    def test_place_price_by_night(self):
        """Test to validation datatype of price_by_night"""
        self.assertTrue(type(self.place.price_by_night) is int)

    def test_place_latitude(self):
        """Test to validation datatype of latitude"""
        self.assertTrue(type(self.place.latitude) is float)

    def test_place_longitude(self):
        """Test to validation datatype of longitude"""
        self.assertTrue(type(self.place.longitude) is float)

    def test_place_amenity_ids(self):
        """Test to validation datatype of amenity_ids"""
        self.assertTrue(type(self.place.amenity_ids) is list)

    def test_place_save(self):
        """Test to validation if I successufully create
        the file.json"""
        PATH = './file.json'
        value = os.path.isfile(PATH)
        self.assertTrue(value)

    def test_place_to_dict(self):
        """Test to validation if method dict return data type dict"""
        self.assertTrue(type(self.place.to_dict()) is dict)

    def test_place__str__(self):
        """Test to validation if method str return correct format"""
        name = self.place.__class__.__name__
        place = f'[{name}] ({self.place.id}) {self.place.__dict__}'
        self.assertTrue(self.place.__str__() == place)

    def tearDown(self):
        """Method to close tests"""
        del self.place


if __name__ == '__main__':
    unittest.main()
