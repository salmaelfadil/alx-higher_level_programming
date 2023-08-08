#!/usr/bin/python3
"""function print_square prints a square with size provided"""


def print_square(size):
    """
    prints a square using '#' depending on size provided
    Args:
        @size: size of square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for i in range(size):
        print("#" * size)
