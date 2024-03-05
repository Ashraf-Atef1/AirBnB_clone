#!/usr/bin/python3
from models.review import Review
from models.base_model import BaseModel

r = Review()
print(isinstance(r, BaseModel))
