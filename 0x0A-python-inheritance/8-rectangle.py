#!/usr/bin/python3
"""Class definition"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height
