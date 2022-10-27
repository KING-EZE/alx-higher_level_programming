#!/usr/bin/python3
"""This module defines a file appending function"""


def append_write(filename="", text=""):
    """Append a new file at the end of the UTF8 text file"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
