#!/usr/bin/python3
"""Module that describe the Review test class"""
from datetime import datetime
import json
import unittest
import uuid
from models import review
from models.review import Review
import os
import models


class TestReview(unittest.TestCase):
    """Test case class of unittest"""

    def setUp(self):
        """Method that sets all initial values"""
        self.review = Review()
        self.review.place_id = "ascc6626ac2"
        self.review.user_id = "kllsnn3226scc"
        self.review.text = "Excelente locación, recomendado totalmente"

    def test_review_instantiation(self):
        """Test to validation instantiation of Review"""
        self.assertIsInstance(self.review, Review)

    def test_review_atributes_id(self):
        """Test to validation datatype of id"""
        self.assertTrue(type(self.review.id) is str)

    def test_review_atributes_created_at(self):
        """Test to validation datatype of created_at"""
        self.assertTrue(type(self.review.created_at) is datetime)

    def test_review_atributes_update_at(self):
        """Test to validation datatype of updated_at"""
        self.assertTrue(type(self.review.updated_at) is datetime)

    def test_review_place_id(self):
        """Test to validation datatype of city_id"""
        self.assertTrue(type(self.review.place_id) is str)

    def test_review_user_id(self):
        """Test to validation datatype of city_id"""
        self.assertTrue(type(self.review.user_id) is str)

    def test_review_text(self):
        """Test to validation datatype of city_id"""
        self.assertTrue(type(self.review.text) is str)

    def test_review_save(self):
        """Test to validation if I successufully create
        the file.json"""
        PATH = './file.json'
        value = os.path.isfile(PATH)
        self.assertTrue(value)

    def test_review_to_dict(self):
        """Test to validation if method dict return data type dict"""
        self.assertTrue(type(self.review.to_dict()) is dict)

    def test_review__str__(self):
        """Test to validation if method str return correct format"""
        name = self.review.__class__.__name__
        review = f'[{name}] ({self.review.id}) {self.review.__dict__}'
        self.assertTrue(self.review.__str__() == review)

    def tearDown(self):
        """Method to close tests"""
        del self.review


if __name__ == '__main__':
    unittest.main()
