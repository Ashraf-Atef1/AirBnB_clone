#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """The class BaseModel that defines all common \
        attributes/methods for other classes"""

    def __init__(self):
        """Insilization"""

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Retrun: [<class name>] (<self.id>) <self.__dict__>"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute \
            updated_at with the current datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all \
            keys/values of __dict__ of the instance"""

        object_dict = self.__dict__
        object_dict["created_at"] = self.created_at.isoformat()
        object_dict["updated_at"] = self.updated_at.isoformat()
        object_dict["__class__"] = self.__class__.__name__
        return object_dict
