#!/usr/bin/python3
"""load_from_json_file"""


def load_from_json_file(filename):
    """function that creates an object from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
