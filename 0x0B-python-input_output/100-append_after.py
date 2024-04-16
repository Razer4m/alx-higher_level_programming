#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """Append a line of text to a file after each string."""

    text = ""
    with open(filename) as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w") as w:
        w.write(text)
