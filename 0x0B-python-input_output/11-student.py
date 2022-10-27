#!/usr/bin/python3
"""This module defines a class student"""


class Student:
    """Represnts a student"""

    def __init__(self, first_name, last_name, age):
        """init a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """gets  a dictionary representation of the student, if attrs is a list
        of strings, represnts only attrs in the list"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattrs(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the student"""
        for k, v in json.items():
            setattr(self, k, v)
