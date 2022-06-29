#!/usr/bin/python3
"""Base Model """

import uuid
from datetime import datetime
import models


new_date = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel():
    """class BaseModel that defines all common attributes/methods
        for other classes """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if  kwargs is not None and len(kwargs) != 0:
            for key in kwargs.keys():
                if key != '__class__':
                    setattr(self, key, kwargs[key])
                    if key == "created_at":
                        self.__dict__[key] = datetime.strptime(kwargs[key], new_date)
                    if key == "updated_at":
                        self.__dict__[key] = datetime.strptime(kwargs[key], new_date)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)


    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        return ({
            'my_number': self.my_number,
            'name': self.name,
            '__class__': self.__class__.__name__,
            'updated_at': self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            'id': self.id,
            'created_at': self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            })
