#!/usr/bin/python3
"""
Defines an individual user class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    A class that defines an individual User

    Public class attributes (all attributes are strings)
    email : user email
    password : user password
    first_name: first name
    last_name: last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
