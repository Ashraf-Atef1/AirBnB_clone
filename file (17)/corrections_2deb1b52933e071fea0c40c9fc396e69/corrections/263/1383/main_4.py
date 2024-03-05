#!/usr/bin/python3
from models.city import City
from models.base_model import BaseModel

c = City()
print(isinstance(c, BaseModel))
