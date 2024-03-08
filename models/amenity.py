#!/usr/bin/python3
"""
Amenity Module - Contains the Amenity class
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class inherits from BaseModel and represents an amenity

    Public class attributes:
        name (str): The name of the amenity.
    """

    name = ""
