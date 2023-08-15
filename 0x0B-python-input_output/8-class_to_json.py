#!/usr/bin/python3
"""class_to_json function"""
import json

def class_to_json(obj):
    """returns dictionary description with simple data structure"""
    return obj.__dict__
