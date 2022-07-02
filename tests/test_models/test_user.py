#!/usr/bin/python3
from datetime import datetime
import json
import unittest
import uuid
from models.user import User
import os
import models
"""Class TestUser"""


class TestUser(unittest.TestCase):
    """
        Class for test the User Class method and atributes
    """

    def setUp(self):
        """All variables that we need
        to start testing User class"""
        self.user = User()
        self.user.first_name = "Leslie"
        self.user.last_name = "Paz"
        self.user.password = "***************"
        self.user.email = "prueba@gmail.com"
        self.user.save()

    def test_user_instantiation(self):
        """Test User instantiation"""
        self.assertIsInstance(self.user, User)

    def test_user_atributes_id(self):
        """Test User atribue id"""
        self.assertTrue(type(self.user.id) is str)

    def test_user_atributes_created_at(self):
        """Test User atribue created at"""
        self.assertTrue(type(self.user.created_at) is datetime)

    def test_user_atributes_update_at(self):
        """Test User atribue update_at"""
        self.assertTrue(type(self.user.updated_at) is datetime)

    def test_user_atributes_email(self):
        """Test User atribute email"""
        self.assertTrue(type(self.user.email) is str)

    def test_user_atributes_password(self):
        """Test User atribute password"""
        self.assertTrue(type(self.user.password) is str)

    def test_user_atributes_first_name(self):
        """Test User atribute firts_name"""
        self.assertTrue(type(self.user.first_name) is str)

    def test_user_atributes_last_name(self):
        """Test User atribute last_name"""
        self.assertTrue(type(self.user.last_name) is str)

    def test_user_save(self):
        """Test if the instance is stored correctly"""
        PATH = './file.json'
        value = os.path.isfile(PATH)
        self.assertTrue(value)

    def test_user_to_dict(self):
        """Test if the user dict has the correct format"""
        self.assertTrue(type(self.user.to_dict()) is dict)

    def test_user__str__(self):
        """Test if the usert ___str__ method has the correct format
            descrited in the method"""
        name = self.user.__class__.__name__
        user = f'[{name}] ({self.user.id}) {self.user.__dict__}'
        self.assertTrue(self.user.__str__() == user)

    def tearDown(self):
        """Closing the test class and deleteing the instance
        created for testing"""
        del self.user


if __name__ == '__main__':
    unittest.main()
