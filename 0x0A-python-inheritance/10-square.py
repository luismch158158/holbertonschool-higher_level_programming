#!/usr/bin/python3
"""Class definition"""


class BaseGeometry:
    """Class BaseGeometry implemented"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')


class Rectangle(BaseGeometry):
    """Class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Returns area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Magic method str for print() will print, and str()
        should return personalized description"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


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
