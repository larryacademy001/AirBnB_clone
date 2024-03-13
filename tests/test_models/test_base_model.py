#!/usr/bin/env python3
"""Unittest base_model module.

Test cases for base_model class and methods documentation and instances.
"""
import unittest
from models import base_model
import time
from datetime import datetime
from unittest import mock
BaseModel = base_model.BaseModel


class TestBaseModel(unittest.TestCase):
    """Class for testing BaseModel class"""

    def test_instantiation(self):
        """... checks if BaseModel is properly instantiated"""
        bm = BaseModel()
        self.assertIs(type(bm), BaseModel)
        bm.name = "Holberton"
        bm.number = 89
        attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "number": int
        }
        for attr, typ in attrs_types.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, bm.__dict__)
                self.assertIs(type(bm.__dict__[attr]), typ)
        self.assertEqual(bm.name, "Holberton")
        self.assertEqual(bm.number, 89)

    def test_datetime_attributes(self):
        """... checks if two BaseModel instances have different datetime"""
        tic = datetime.now()
        bm = BaseModel()
        toc = datetime.now()
        self.assertTrue(tic <= bm.created_at <= toc)
        time.sleep(1e-4)
        tic = datetime.now()
        bm2 = BaseModel()
        toc = datetime.now()
        self.assertTrue(tic <= bm2.created_at <= toc)
        self.assertEqual(bm.created_at, bm.updated_at)
        self.assertEqual(bm2.created_at, bm2.updated_at)
        self.assertNotEqual(bm.created_at, bm2.created_at)
        self.assertNotEqual(bm.updated_at, bm2.updated_at)

    def test_uuid(self):
        """... uuid should be valid"""
        bm = BaseModel()
        bm2 = BaseModel()
        for inst in [bm, bm2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(bm.id, bm2.id)

    def test_to_dict(self):
        """... checks if BaseModel is properly casted to dictionary"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        d = my_model.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "Holberton")
        self.assertEqual(d['my_number'], 89)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        tf = "%Y-%m-%dT%H:%M:%S.%f"
        bm = BaseModel()
        new_d = bm.to_dict()
        self.assertEqual(new_d["__class__"], "BaseModel")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], bm.created_at.strftime(tf))
        self.assertEqual(new_d["updated_at"], bm.updated_at.strftime(tf))

    def test_str(self):
        """test str method for correct output"""
        bm = BaseModel()
        string = "[BaseModel] ({}) {}".format(bm.id, bm.__dict__)
        self.assertEqual(string, str(bm))

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        bm = BaseModel()
        old_created_at = bm.created_at
        old_updated_at = bm.updated_at
        bm.save()
        new_created_at = bm.created_at
        new_updated_at = bm.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)


if __name__ == "__main__":
    unittest.main()
