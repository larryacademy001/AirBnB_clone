#!/usr/bin/env python3
"""
Unittest for user module.
"""
import unittest
from datetime import datetime
from models import user
from models.base_model import BaseModel
User = user.User


class TestUser(unittest.TestCase):
    """Test the User class"""
    def test_is_subclass(self):
        """Test User for subclass of BaseModel"""
        u = User()
        self.assertIsInstance(u, BaseModel)
        self.assertTrue(hasattr(u, "id"))
        self.assertTrue(hasattr(u, "created_at"))
        self.assertTrue(hasattr(u, "updated_at"))

    def test_email_attr(self):
        """Test Amenity for attribute
        email and if it's empty
        """
        u = User()
        self.assertTrue(hasattr(u, "email"))
        self.assertEqual(u.email, "")

    def test_password_attr(self):
        """Test Amenity for attribute
        password and if it's empty
        """
        u = User()
        self.assertTrue(hasattr(u, "password"))
        self.assertEqual(u.password, "")

    def test_first_name_attr(self):
        """Test Amenity for attribute
        first_name and if it's empty
        """
        u = User()
        self.assertTrue(hasattr(u, "first_name"))
        self.assertEqual(u.first_name, "")

    def test_last_name_attr(self):
        """Test Amenity for attribute
        last_name and if it's empty
        """
        u = User()
        self.assertTrue(hasattr(u, "last_name"))
        self.assertEqual(u.last_name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict making sure they
        are created with proper attributes
        """
        u = User()
        new_d = u.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in u.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned
        from to_dict are correct
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = User()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "User")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(time_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(time_format))

    def test_str(self):
        """test str method for correct output"""
        u = User()
        string = "[User] ({}) {}".format(u.id, u.__dict__)
        self.assertEqual(string, str(u))
