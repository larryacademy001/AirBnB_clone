#!/usr/bin/python3
"""
Review Module - Contains the Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class inherits from BaseModel and represents a review.

    Public class attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
