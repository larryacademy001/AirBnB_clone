#!/usr/bin/env python3
"""Unittest city module.

Test cases for city class and methods documentation and instances.
"""
import unittest
from datetime import datetime
from models import city
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test the City class"""
    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel"""
        c = City()
        self.assertIsInstance(c, BaseModel)
        self.assertTrue(hasattr(c, "id"))
        self.assertTrue(hasattr(c, "created_at"))
        self.assertTrue(hasattr(c, "updated_at"))

    def test_name_attr(self):
        """Test Amenity for attribute
        name and if it's empty
        """
        c = City()
        self.assertTrue(hasattr(c, "name"))
        self.assertEqual(c.name, "")

    def test_state_id_attr(self):
        """Test Amenity for attribute
        state_id and if it's empty
        """
        c = City()
        self.assertTrue(hasattr(c, "state_id"))
        self.assertEqual(c.state_id, "")

    def test_to_dict_creates_dict(self):
        """test to_dict making sure they
        are created with proper attributes
        """
        c = City()
        new_d = c.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in c.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned
        from to_dict are correct
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = City()
        new_d = c.to_dict()
        self.assertEqual(new_d["__class__"], "City")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], c.created_at.strftime(time_format))
        self.assertEqual(new_d["updated_at"], c.updated_at.strftime(time_format))

    def test_str(self):
        """test str method for correct output"""
        c = City()
        string = "[City] ({}) {}".format(c.id, c.__dict__)
        self.assertEqual(string, str(c))
