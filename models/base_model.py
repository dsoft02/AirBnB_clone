#!/usr/bin/python3
"""This module defines a base class that defines
all common attributes/methods for other classes in
our AirBnB clone
"""

from models import storage
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all common attributes/methods
    of our AirBnB clone project"""

    def __init__(self, *args, **kwargs):
        """New BaseModel initialization

        Args:
            *args (any) : Unused.
            **kwargs (dict): Key and value pairs of attributes
        """
        dtformat = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            cdatefld = kwargs['created_at']
            cupfld = kwargs['updated_at']
            kwargs['updated_at'] = datetime.strptime(cupfld, dtformat)
            kwargs['created_at'] = datetime.strptime(cdatefld, dtformat)
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns the string representation of the BaseModel instance"""
        cls_name = self.__class__.__name__
        return '[{}] ({}) {}'.format(cls_name, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns the dictionary containing all
        keys/values of __dict__ of the instance"""
        dct = {}
        dct.update(self.__dict__)
        dct.update({'__class__': self.__class__.__name__})
        dct['created_at'] = self.created_at.isoformat()
        dct['updated_at'] = self.updated_at.isoformat()
        return dct
