#!/usr/bin/python3
"""Read_file function"""


def read_file(filename=""):
    """Reads a file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
