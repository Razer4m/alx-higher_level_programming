#!/usr/bin/python3
"""
Defines a function that appends at the end
"""


def append_write(filename="", text=""):
    """Appends a string at end of a (UTF8) and returns # of characters"""
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
