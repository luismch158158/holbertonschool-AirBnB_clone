#!/usr/bin/python3
"""Module that describe the BaseModel class"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """class BaseModel that defines all common attributes/methods
        for other classes """

    def __init__(self, *args, **kwargs):
        """Constructor of BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None and len(kwargs) != 0:
            for key in kwargs.keys():
                if key != '__class__':
                    setattr(self, key, kwargs[key])
                    if key == "created_at":
                        self.__dict__[key] = datetime.fromisoformat(
                                                            kwargs[key])
                    if key == "updated_at":
                        self.__dict__[key] = datetime.fromisoformat(
                                                            kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """This method return string representation"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """This method update attributte with time now"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """This method return dictionary of all key/value of instance"""
        dict_new = self.__dict__.copy()

        if "updated_at" in dict_new:
            formated_updated = dict_new['updated_at'].isoformat()
            dict_new['updated_at'] = formated_updated
        if "created_at" in dict_new:
            formated_created = dict_new['created_at'].isoformat()
            dict_new['created_at'] = formated_created
        dict_new['__class__'] = self.__class__.__name__
        return (dict_new)
