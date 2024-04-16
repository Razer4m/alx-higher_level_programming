#!/usr/bin/python3
"""
Defines a function that write_file
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns # of characters."""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
