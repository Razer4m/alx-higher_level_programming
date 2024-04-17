#!/usr/bin/python3

def inherits_from(obj, a_class):
    """Check if obj is an instance of a class inherited from a_class."""
    return issubclass(type(obj), a_class) and type(obj) != a_class
