#!/usr/bin/python3
"""
A string to JSON fucntion
"""

import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string."""
    return json.loads(my_str)
