#!/usr/bin/python3

"""Defines a MagicClass matching exactly a bytecode provided by Holberton"""

import math


class MagicClass:
    """Circle representation"""

    def __init__(self, radius=0):

        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns area of the MagicClass"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returns circumference of the MagicClass"""
        return (2 * math.pi * self.__radius)
