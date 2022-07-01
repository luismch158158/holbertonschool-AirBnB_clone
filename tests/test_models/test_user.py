#/usr/bin/python3
from datetime import datetime
import json
import unittest
import uuid
from models.user import User
import os
import models

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()
        self.user.first_name = "Leslie"
        self.user.last_name = "Paz"
        self.user.password = "***************"
        self.user.email = "prueba@gmail.com"
        self.user.save()

    def test_user_instantiation(self):
        self.assertIsInstance(self.user, User)

    def test_user_atributes_id(self):
        self.assertTrue(type(self.user.id) is str)

    def test_user_atributes_created_at(self):
        self.assertTrue(type(self.user.created_at) is datetime)

    def test_user_atributes_update_at(self):
        self.assertTrue(type(self.user.updated_at) is datetime)

    def test_user_atributes_email(self):
        self.assertTrue(type(self.user.email) is str)

    def test_user_atributes_password(self):
        self.assertTrue(type(self.user.password) is str)

    def test_user_atributes_first_name(self):
        self.assertTrue(type(self.user.first_name) is str)

    def test_user_atributes_last_name(self):
        self.assertTrue(type(self.user.last_name) is str) 

    def test_user_save(self):
        PATH = './file.json'
        value = os.path.isfile(PATH)
        self.assertTrue(value)

    def test_user_to_dict(self):
        self.assertTrue(type(self.user.to_dict()) is dict)

    def test_user__str__(self):
        name = self.user.__class__.__name__
        user = f'[{name}] ({self.user.id}) {self.user.__dict__}'
        self.assertTrue(self.user.__str__() == user)

    def tearDown(self):
        del self.user      

if __name__ == '__main__':
    unittest.main()
