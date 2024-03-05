#!/usr/bin/python3
from models.amenity import Amenity
from models.base_model import BaseModel

a = Amenity()
print(isinstance(a, BaseModel))
