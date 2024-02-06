#!/usr/bin/python3
"""Defines class MyList that inherits from list"""


class MyList(list):
    """Implements sorted printing for the built-in list class"""

    def print_sorted(self):
        """Prints a list sorted in ascending order"""
        print(sorted(self))
