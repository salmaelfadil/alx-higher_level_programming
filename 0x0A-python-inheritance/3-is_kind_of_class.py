#!/usr/bin/python3
"""is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """checks if object is instance of specified class
    or a class that intherits from it"""
    return (isinstance(obj, a_class))
