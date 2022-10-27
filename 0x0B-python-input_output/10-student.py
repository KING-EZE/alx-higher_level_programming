#!/usr/bin/python3
"""This module defines a class student"""


class Student:
    """Represents a new student"""

    def __init__(self, first_name, last_name, age):
        """init a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation of the student if attrs is a list
        of strings, represent only the attributes occured in the list"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
