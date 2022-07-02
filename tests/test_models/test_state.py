#!/usr/bin/python3

from datetime import datetime
import json
import unittest
import uuid
from models import state
from models.state import State
import os
import models


class TestReview(unittest.TestCase):
    """Test case class of unittest"""

    def setUp(self):
        """Method that sets all initial values"""
        self.state = State()
        self.state.name = "San Francisco"

    def test_state_instantiation(self):
        """Test to validation instantiation of State"""
        self.assertIsInstance(self.state, State)

    def test_state_atributes_id(self):
        """Test to validation datatype of id"""
        self.assertTrue(type(self.state.id) is str)

    def test_state_atributes_created_at(self):
        """Test to validation datatype of created_at"""
        self.assertTrue(type(self.state.created_at) is datetime)

    def test_state_atributes_update_at(self):
        """Test to validation datatype of updated_at"""
        self.assertTrue(type(self.state.updated_at) is datetime)

    def test_state_name(self):
        """Test to validation datatype of name"""
        self.assertTrue(type(self.state.name) is str)

    def test_state_save(self):
        """Test to validation if I successufully create
        the file.json"""
        PATH = './file.json'
        value = os.path.isfile(PATH)
        self.assertTrue(value)

    def test_state_to_dict(self):
        """Test to validation if method dict return data type dict"""
        self.assertTrue(type(self.state.to_dict()) is dict)

    def test_state__str__(self):
        """Test to validation if method str return correct format"""
        name = self.state.__class__.__name__
        state = f'[{name}] ({self.state.id}) {self.state.__dict__}'
        self.assertTrue(self.state.__str__() == state)

    def tearDown(self):
        """Method to close tests"""
        del self.state


if __name__ == '__main__':
    unittest.main()
