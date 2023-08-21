#!/usr/bin/python3
"""Base class"""


class Base:
    """defines a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @static.method
    def to_json_string(list_dictionaries):
        """returns json string representation of dicts"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)
