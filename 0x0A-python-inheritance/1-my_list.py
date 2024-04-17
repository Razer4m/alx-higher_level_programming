#!/usr/bin/python3
"""Defines a custom list class."""

class MyList(list):
    """Custom list class inheriting from list."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
