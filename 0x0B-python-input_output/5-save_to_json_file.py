#!/usr/bin/python3
"""Defines a function that writes an Object to text file."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation."""
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
