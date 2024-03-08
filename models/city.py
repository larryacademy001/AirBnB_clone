#!/usr/bin/python3
"""
City Module - Contains the City class
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    City class inherits from BaseModel and represents a city

    Public class attributes
        state_id (str): The ID of the state the city belongs to.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
