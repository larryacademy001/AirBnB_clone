#!/usr/bin/env python3
"""Unittest state module.

Test cases for state class and methods documentation and instances.
"""
import unittest
from datetime import datetime
from models import state
from models.base_model import BaseModel
State = state.State


class TestState(unittest.TestCase):
    """Test the State class"""
    def test_is_subclass(self):
         """Test State for subclass of BaseModel"""
        s = State()
        self.assertIsInstance(s, BaseModel)
        self.assertTrue(hasattr(s, "id"))
        self.assertTrue(hasattr(s, "created_at"))
        self.assertTrue(hasattr(s, "updated_at"))

    def test_name_attr(self):
        """Test Amenity for attribute
        name and if it's empty
        """
        s = State()
        self.assertTrue(hasattr(s, "name"))
        self.assertEqual(s.name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict making sure they
        are created with proper attributes
        """
        s = State()
        new_d = s.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in s.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned
        from to_dict are correct
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        s = State()
        new_d = s.to_dict()
        self.assertEqual(new_d["__class__"], "State")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], s.created_at.strftime(time_format))
        self.assertEqual(new_d["updated_at"], s.updated_at.strftime(time_format))

    def test_str(self):
        """test str method for correct output"""
        s = State()
        string = "[State] ({}) {}".format(s.id, s.__dict__)
        self.assertEqual(string, str(s))
