#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a given class

    Args:
        obj (any): object to check.
        a_class (type): class to match the type of obj to.
    Returns:
        True if obj is exactly an instance of a_class
        or False if otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
