#!/usr/bin/python3
import uuid
import datetime

class BaseModel:
    __doc__ = """
    This is a base model class that all objects inherit from
    It includes several methods to store objects and acts as a layer
    of abstraction for file storage or DB storage
    Methods:
    - save -> updates the update time of object
    - to_dict -> returns a dictionary of all attibutes of the class/ object
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()


    def __str__(self) -> str:
        return f"[{self.__class__.__name__} ({self.id}) <{self.__dict__}>]"

    def save(self):
        """This method updates the update time"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self) -> dict:
        """This method returns a dictionary of all attributes in the class/ object"""
        self.__dict__['__class__']  = self.__class__.__name__
        self.__dict__['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        self.__dict__['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return self.__dict__
 