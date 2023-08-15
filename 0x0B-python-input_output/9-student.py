#!/usr/bin/python3
"""class student"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initalizes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrives a dictrionary representation of student"""
        return self.__dict__
