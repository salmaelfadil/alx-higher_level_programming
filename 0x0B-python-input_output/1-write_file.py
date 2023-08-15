#!/usr/bin/python3
"""Write_file function"""


def write_file(filename="", text=""):
    """writes a string in a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
