#!/usr/bin/python3
"""this module defines a Json file reading function"""
import json


def load_from_json_file(filename):
    """Create a python object from a given JSON file"""
    with open(filename) as f:
        return json.load(f)
