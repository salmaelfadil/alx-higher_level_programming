#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry:
    """base geometry class"""
    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks that value is an int greater than 0"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <=0:
            raise ValueError("<name> must be greater than 0")
