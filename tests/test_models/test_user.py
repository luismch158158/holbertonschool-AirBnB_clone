#/usr/bin/python3

import unittest
from models.user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def test_user_instantiation(self):
        #duda
        self.assertIsInstance(self.user, User)

    def test_user_atributes(self):
        self.assertTrue(type(self.id) is int), 
        self.assertTrue(type(self.created_at) is datetime), 
        self.assertTrue(type(self.updated_at) is datetime), 
        self.assertTrue(type(self.email) is str), 
        self.assertTrue(type(self.password) is str), 
        self.assertTrue(type(self.first_name) is str), 
        self.assertTrue(type(self.last_name) is str), 

    def test_user_save(self):
        pass

    def test_user_to_dict(self):
        pass

    def test_user__str__(self):
        pass

    def tearDown(self):
        del self.user      

if __name__ == '__main__':
    unittest.main()
