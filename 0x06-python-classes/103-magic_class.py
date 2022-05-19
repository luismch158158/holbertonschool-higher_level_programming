#!/usr/bin/python3
"""Class MagicClass"""
import math


class MagicClass:
    """Magic class"""
    def __init__(self, radius=0):
        """Initializator"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Area method"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Circ method"""
        return 2 * math.pi * self.__radius
