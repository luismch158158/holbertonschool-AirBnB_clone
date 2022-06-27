#!/usr/bin/python3

import uuid
from datetime import datetime

"""Base Model """
class BaseModel():
    """class BaseModel that defines all common attributes/methods
        for other classes """
    def __init__(self):
        self.id=str(uuid.uuid4())
        self.created_at=datetime.now()
        self.updated_at=datetime.now()

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        update_at=datetime.now()

    def to_dict(self):
        return ({
            'my_number': self.my_number,
            'name': self.name,
            '__class__': self.__class__.__name__,
            'updated_at': self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f") ,
            'id': self.id,
            'created_at': self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            })
