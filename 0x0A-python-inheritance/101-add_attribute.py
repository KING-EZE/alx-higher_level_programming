#!/usr/bin/python3
"""This module defines a function that adds attributes to an objects"""


def add_attribute(obj, att, value):
    """add a new attribute to an object if possbile"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
