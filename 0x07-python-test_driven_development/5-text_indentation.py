#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    lines = []
    line = ""

    for char in text:
        line += char
        if char in punctuations:
            lines.append(line.strip())
            lines.append("")
            line = ""

    if line.strip():
        lines.append(line.strip())

    for line in lines:
        print(line)
