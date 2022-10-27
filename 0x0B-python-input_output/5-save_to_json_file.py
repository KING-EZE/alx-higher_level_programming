#!/usr/bin/python3
"""This module defines the JSON file writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a json text file format"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
