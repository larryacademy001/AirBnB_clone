#!/usr/bin/env python3
"""
Unittest for amenity module.
"""
import unittest
from datetime import datetime
from models import amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""
    def test_is_subclass(self):
        """Test Amenity for subclass of BaseModel"""
        am = Amenity()
        self.assertIsInstance(am, BaseModel)
        self.assertTrue(hasattr(am, "id"))
        self.assertTrue(hasattr(am, "created_at"))
        self.assertTrue(hasattr(am, "updated_at"))

    def test_name_attr(self):
        """Test Amenity for attribute
        name and if it's empty
        """
        am = Amenity()
        self.assertTrue(hasattr(am, "name"))
        self.assertEqual(am.name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict making sure they
        are created with proper attributes
        """
        am = Amenity()
        print(am.__dict__)
        new_d = am.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in am.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned
        from to_dict are correct
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = Amenity()
        new_d = am.to_dict()
        self.assertEqual(new_d["__class__"], "Amenity")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], am.created_at.strftime(time_format))
        self.assertEqual(new_d["updated_at"], am.updated_at.strftime(time_format))

    def test_str(self):
        """test str method for correct output"""
        am = Amenity()
        string = "[Amenity] ({}) {}".format(am.id, am.__dict__)
        self.assertEqual(string, str(am))
