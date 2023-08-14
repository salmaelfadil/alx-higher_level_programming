#!/usr/bin/python3
"""Class MyList"""


class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """sorts a list"""
        print(sorted(self))
