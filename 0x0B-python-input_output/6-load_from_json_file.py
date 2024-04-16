#!/usr/bin/python3
"""Defines a function that creates a Object from JSON. """
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    with open(filename, mode="r") as file:
        return json.load(file)
