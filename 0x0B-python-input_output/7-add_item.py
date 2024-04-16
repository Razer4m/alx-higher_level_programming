#!/usr/bin/python3
"""Defines a function that creates a Object from JSON. """
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    # Load existing items from the file if it exists
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    # Add new items from command line arguments
    items.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(items, "add_item.json")


if __name__ == "__main__":
    main()
