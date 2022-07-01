#/usr/bin/python3

from datetime import datetime
import json
import unittest
import uuid
from models.place import Place

class TestPlace(unittest.TestCase):
    """
    """
    def setUp(self):
        self.place = Place()

    def test_place_atributes_id(self):
        self.assertTrue(type(self.place.id) is str)

    def test_place_created_at(self):
        self.assertTrue(type(self.place.created_at) is datetime)
        self.assertTrue(type(self.place.updated_at) is datetime)
        self.assertTrue(type(self.place.city_id) is str)
        self.assertTrue(type(self.place.user_id) is str)


    def test_place_instantiation(self):
        pass

    def test_place_save(self):
        pass

    def test_place_to_dict(self):
        pass

    def test_place__str__(self):
        pass

    def tearDown(self):
        del self.place      

if __name__ == '__main__':
    unittest.main()
