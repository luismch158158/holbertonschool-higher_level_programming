#!/usr/bin/python3
"""Class Rectangle empty"""


class Rectangle:
    """Defines a Rectangle
    with Private instance attribute width
    and Private instance attribute height
    Also, computes area and perimeter"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter to width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter to width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter to width"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter to width"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Computes area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Computes perimeter of rectangle"""
        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            return (2 * self.__width + 2 * self.__height)

    def __str__(self):
        """Print square"""
        string = ""
        if (self.__width == 0) or (self.__height == 0):
            return string
        for i in range(self.__height):
            string += (str(self.print_symbol) * self.__width)
            if i is not (self.__height - 1):
                string += '\n'
        return string

    def __repr__(self):
        """Return string representation of rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Message when delete a rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
