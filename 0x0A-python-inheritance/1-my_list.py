#!/usr/bin/python3
"""Class MyList"""


class MyList(list):
    """inherits from list"""
    def __init__(self):
        """initalizes the object"""
        super().__init__()

    def print_sorted(self):
        """sorts a list"""
        print(sorted(self))
