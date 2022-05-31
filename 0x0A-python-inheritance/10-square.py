#!/usr/bin/python3
"""Class definition"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class square"""
    def __init__(self, size):
        """Instantiation with size"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Implement area of rectangle"""
        return (self.__size * self.__size)
