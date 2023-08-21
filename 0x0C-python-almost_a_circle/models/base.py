#!/usr/bin/python3
"""Base class"""
import json
import csv
import os.path

class Base:
    """defines a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string representation of dicts"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save object in a file"""
        filename = "{}.json".format(cls.__name__)
        obj_list = []

        if list_objs is not None:
            obj_list = [obj.to_dictionary() for obj in list_objs]

        json_str = cls.to_json_string(obj_list)

        with open(filename, 'w') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if not json_string:
            return []
        return json.loads(json_string)
