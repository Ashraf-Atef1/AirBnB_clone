#!/usr/bin/python3
from models.place import Place
from models.base_model import BaseModel

p = Place()
print(isinstance(p, BaseModel))
