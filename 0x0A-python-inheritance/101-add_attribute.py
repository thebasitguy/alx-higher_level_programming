#!/usr/bin/python3
"""Defines a function that adds an attribute to an object"""


def add_attribute(obj, att, value):
    """Adds a new attribute to an object if possible

    Args:
        obj (any): object to add an attribute to
        att (str): name of the attribute to add to obj
        value (any): value of att
    Raises:
        TypeError: if the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
