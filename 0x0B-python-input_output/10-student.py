#!/usr/bin/python3
"""class student"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initalizes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrives a dictrionary representation of student"""
        if attrs is None:
            return self.__dict__
        json_dict = {}

        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)
        return json_dict
