#!/usr/bin/env python3
"""Unittest place module.

Test cases for place class and methods documentation and instances.
"""
import unittest
from datetime import datetime
from models import place
from models.base_model import BaseModel
Place = place.Place


class TestPlace(unittest.TestCase):
    """Test the Place class"""
    def test_is_subclass(self):
        """Test Place for subclass of BaseModel"""
        p = Place()
        self.assertIsInstance(p, BaseModel)
        self.assertTrue(hasattr(p, "id"))
        self.assertTrue(hasattr(p, "created_at"))
        self.assertTrue(hasattr(p, "updated_at"))

    def test_city_id_attr(self):
        """Test Amenity for attribute
        city_id and if it's empty
        """
        p = Place()
        self.assertTrue(hasattr(p, "city_id"))
        self.assertEqual(p.city_id, "")

    def test_user_id_attr(self):
        """Test Amenity for attribute
        user_id and if it's empty
        """
        p = Place()
        self.assertTrue(hasattr(p, "user_id"))
        self.assertEqual(p.user_id, "")

    def test_name_attr(self):
        """Test Amenity for attribute
        name and if it's empty
        """
        p = Place()
        self.assertTrue(hasattr(p, "name"))
        self.assertEqual(p.name, "")

    def test_description_attr(self):
        """Test Amenity for attribute
        description and if it's empty
        """
        p = Place()
        self.assertTrue(hasattr(p, "description"))
        self.assertEqual(p.description, "")

    def test_number_rooms_attr(self):
        """Test Amenity for attribute
        number_rooms and if it's empty
        """
        p = Place()
        self.assertTrue(hasattr(p, "number_rooms"))
        self.assertEqual(type(p.number_rooms), int)
        self.assertEqual(p.number_rooms, 0)

    def test_number_bathrooms_attr(self):
        """Test Amenity for attribute
        number_bathrooms and if it's empty
        """
        p = Place()
        self.assertTrue(hasattr(p, "number_bathrooms"))
        self.assertEqual(type(p.number_bathrooms), int)
        self.assertEqual(p.number_bathrooms, 0)

    def test_max_guest_attr(self):
        """Test Amenity for attribute
        max_guest and if it's empty
        """
        p = Place()
        self.assertTrue(hasattr(p, "max_guest"))
        self.assertEqual(type(p.max_guest), int)
        self.assertEqual(p.max_guest, 0)

    def test_price_by_night_attr(self):
        """Test Amenity for attribute
        price_by_night and if it's empty
        """
        p = Place()
        self.assertTrue(hasattr(p, "price_by_night"))
        self.assertEqual(type(p.price_by_night), int)
        self.assertEqual(p.price_by_night, 0)

    def test_latitude_attr(self):
        """Test Amenity for attribute
        latitude and if it's empty
        """
        p = Place()
        self.assertTrue(hasattr(p, "latitude"))
        self.assertEqual(type(p.latitude), float)
        self.assertEqual(p.latitude, 0.0)

    def test_longitude_attr(self):
        """Test Amenity for attribute
        longitude and if it's empty
        """
        p = Place()
        self.assertTrue(hasattr(p, "longitude"))
        self.assertEqual(type(p.longitude), float)
        self.assertEqual(p.longitude, 0.0)

    def test_amenity_ids_attr(self):
        """Test Amenity for attribute
        amenity_ids and if it's empty
        """
        p = Place()
        self.assertTrue(hasattr(p, "amenity_ids"))
        self.assertEqual(type(p.amenity_ids), list)
        self.assertEqual(len(p.amenity_ids), 0)

    def test_to_dict_creates_dict(self):
        """test to_dict making sure they
        are created with proper attributes
        """
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in p.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned
        from to_dict are correct
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(new_d["__class__"], "Place")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], p.created_at.strftime(time_format))
        self.assertEqual(new_d["updated_at"], p.updated_at.strftime(time_format))

    def test_str(self):
        """test str method for correct output"""
        p = Place()
        string = "[Place] ({}) {}".format(p.id, p.__dict__)
        self.assertEqual(string, str(p))
