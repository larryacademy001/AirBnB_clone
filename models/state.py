#!/usr/bin/python3
"""
State Module - Contains the State class
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    State class inherits from BaseModel and represents state

    Public class attribute
        name (str): The name of the state.
    """

    name = ""
