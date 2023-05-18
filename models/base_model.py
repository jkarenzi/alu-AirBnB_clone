#!/usr/bin/python3
"""BaseModel for all other classes"""

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        """constructor method for the class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:        
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """returns the string representation"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        The save() method updates the updated_at attribute with 
        the current datetime whenever called.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        The to_dict() method returns a dictionary containing all 
        the keys and values of the instance's __dict__
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict