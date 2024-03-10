#!/usr/bin/env python3
"""This is Base Model Class that defines all
common attributes/methods for other classes
"""
import models
import uuid
from datetime import datetime

time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Template for all subclasses.

    Public instance attributes:
        id: string - assign with an uuid when an instance is created:
        created_at: datetime - assign with the current datetime
        when an instance is created
        updated_at: datetime - assign with the current datetime
        when an instance is created and it will be updated every
        time you change your object
    """

    def __init__(self, *args, **kwargs):
        """Constructor Method

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        self.__dict__[key] = datetime.strptime(
                            value, time_format)
                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """official string representation"""

        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at with the current datetime and save modelobject"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a modified dictionary with all attributes of an object"""

        new_obj_dict = self.__dict__.copy()
        new_obj_dict["__class__"] = type(self).__name__
        new_obj_dict["created_at"] = self.created_at.strftime(time_format)
        new_obj_dict["updated_at"] = self.updated_at.strftime(time_format)
        return new_obj_dict
