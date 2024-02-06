#!/usr/bin/python3
"""Defines a function that checks inherited class"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class

    Args:
        obj (any): object to check.
        a_class (type): class to match the type of obj to
    Returns:
        True if obj is an inherited instance of a_class
        or False if otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
