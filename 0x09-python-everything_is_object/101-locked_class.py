#!/usr/bin/python3

"""Defines a locked class"""


class LockedClass():
    """only attribute allowed for instansiation is first_name"""
    __slots__ = ['first_name']
