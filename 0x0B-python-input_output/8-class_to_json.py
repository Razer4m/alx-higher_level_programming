#!/usr/bin/python3
"""Defines function that returns dictionery"""


def class_to_json(obj):
    """Returns the dict descrip for JSON seria of an object."""
    return obj.__dict__
