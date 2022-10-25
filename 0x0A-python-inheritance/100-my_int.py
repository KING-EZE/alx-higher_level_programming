#!/usr/bin/python3
"""this module defines a class Myint that inherits from int"""


class MyInt(int):
    """Invert int operator == and !="""

    def __eq__(self, value):
        """override == operator with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """override != operator with == behavior"""
        return self.real == value
