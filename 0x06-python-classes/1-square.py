#!/usr/bin/python3
"""Class Square"""


class Square:
    """Defines a square
    with Private instance attribute: size
    and Instantiation with size (no type/value verification)"""

    def __init__(self, size):
        """ Private attribute size,
        this attribute is private because the
        size of square is crucial for a square"""
        self.__size = size
