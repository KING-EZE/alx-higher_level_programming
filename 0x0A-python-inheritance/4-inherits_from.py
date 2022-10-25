#!/usr/bin/python3
"""checks an object is an instance of a class that inherited from a specific
class or not"""


def inherits_from(obj, a_class):
    """return true if object is an instance of a class that inherited from a
    specific class(directly or indirectly); otherwise return false"""

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
