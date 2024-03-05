#!/usr/bin/python3
from models.base_model import BaseModel

class Review(BaseModel):
    """The class BaseModel that defines all common \
        attributes/methods for other classes"""
    place_id = ""
    user_id = ""
    text = ""
