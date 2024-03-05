#!/usr/bin/python3
import json

class FileStorage():
    """The class BaseModel that defines all common \
        attributes/methods for other classes"""

    __file_path = "file.json"
    __objects = {}
    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.all()[key] = obj
    def save(self):
        json_dict = {}
        for key, value in self.all().items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as fp:
            json.dump(json_dict, fp)
    def reload(self):
        from models.base_model import BaseModel

        classes_dict = {'BaseModel': BaseModel}
        try:
            with open(self.__file_path, "r") as fp:
                json_dict = json.load(fp)
        except Exception:
            return
        for key, value in json_dict.items():
            self.all()[key] = classes_dict[key.split(".")[0]](**value)
