#!/usr/bin/python3
"""inherits_from function"""


def inherits_from(obj, a_class):
    """checks if an object directly or indirectly inherited from
    specified class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
