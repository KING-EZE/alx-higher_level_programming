#!/usr/bin/python3
"""This module define the JSON to object function"""
import json


def from_json_string(my_str):
    """Returns the python object representation of the json object"""
    return json.loads(my_str)
