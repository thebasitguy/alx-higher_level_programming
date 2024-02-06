#!/usr/bin/python3
"""Defines a class and function that checks inherited class"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited instance of a class.

    Args:
        obj (any): object to check.
        a_class (type): class to match the obj type to
    Returns:
        True if obj is an instance or inherited instance of a class
        or False if otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
