#!/usr/bin/python3
"""checks if object is an instance of a class or an inherited class"""


def is_kind_of_class(obj, a_class):
    """return true if the object is an instance of class or an instance of the
    inherited class"""

    return (isinstance(obj, a_class))
