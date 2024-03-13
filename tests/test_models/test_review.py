#!/usr/bin/env python3
"""Unittest review module.

Test cases for review class and methods documentation and instances.
"""
import unittest
from datetime import datetime
from models import review
from models.base_model import BaseModel
Review = review.Review

class TestReview(unittest.TestCase):
    """Test the Review class"""
    def test_is_subclass(self):
        """Test Review for subclass of BaseModel"""
        r = Review()
        self.assertIsInstance(r, BaseModel)
        self.assertTrue(hasattr(r, "id"))
        self.assertTrue(hasattr(r, "created_at"))
        self.assertTrue(hasattr(r, "updated_at"))

    def test_place_id_attr(self):
        """Test Amenity for attribute
        place_id and if it's empty
        """
        r = Review()
        self.assertTrue(hasattr(r, "place_id"))
        self.assertEqual(r.place_id, "")

    def test_user_id_attr(self):
        """Test Amenity for attribute
        user_id and if it's empty
        """
        r = Review()
        self.assertTrue(hasattr(r, "user_id"))
        self.assertEqual(r.user_id, "")

    def test_text_attr(self):
        """Test Amenity for attribute
        text and if it's empty
        """
        r = Review()
        self.assertTrue(hasattr(r, "text"))
        self.assertEqual(r.text, "")

    def test_to_dict_creates_dict(self):
        """test to_dict making sure they
        are created with proper attributes
        """
        r = Review()
        new_d = r.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in r.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned
        from to_dict are correct
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        r = Review()
        new_d = r.to_dict()
        self.assertEqual(new_d["__class__"], "Review")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], r.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], r.updated_at.strftime(t_format))

    def test_str(self):
        """test str method for correct output"""
        r = Review()
        string = "[Review] ({}) {}".format(r.id, r.__dict__)
        self.assertEqual(string, str(r))
