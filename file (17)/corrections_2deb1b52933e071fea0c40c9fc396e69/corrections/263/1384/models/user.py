#!/usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
    """The class BaseModel that defines all common \
        attributes/methods for other classes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
