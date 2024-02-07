#!/usr/bin/python3
"""Function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file

    Args:
        filename (str): name of the file to append to
        text (str): string to append to the file
    Returns:
        Number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text) 
