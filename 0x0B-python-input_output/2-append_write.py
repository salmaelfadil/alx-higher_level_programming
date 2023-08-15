#!/usr/bin/python3
"""append_write"""


def append_write(filename="", text=""):
    """appends text into file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
