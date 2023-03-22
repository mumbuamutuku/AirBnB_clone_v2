#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime
from os import getenv
from sqlalchemy.ext.declarative import declarative_base


class BaseModel:
    """This class will defines all common attributes/methods
    for other classes
    """
    id = Column("id", String(60), nullable=False, primary_key=True)
    created_at = Column("created_at", DateTime, nullable=False,
                        default=datetime.utcnow())
    updated_at = Column("updated_at", DateTime, nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
        flag = 1
        if kwargs:
            if "created_at" not in kwargs:
                setattr(self, "created_at", datetime.now())
            if "updated_at" not in kwargs:
                setattr(self, "updated_at", datetime.now())
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
                if key == "id":
                    flag = 0
             if flag == 1:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now() 

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = str(type(self).__name__)
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary.keys():
            del dictionary["_sa_instance_state"]
        return dictionary

     def delete(self):
        """
        Deletes the current instance from the storage models.storage
        """
        models.storage.delete(self)
