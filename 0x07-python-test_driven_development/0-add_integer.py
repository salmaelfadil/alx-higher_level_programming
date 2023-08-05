#!/usr/bin/python3
"""0-add_integer module"""


def add_integer(a, b=98):
    """
    Adds two integers
    Args:
    @a: first int
    @b: second int, default = 98
    Return: added int
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int or type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
