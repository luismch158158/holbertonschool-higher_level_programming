#!/usr/bin/python3
"""Class Square"""


class Square:
    """Defines a square class:
    - Private instance attribute: size
    - Instantatiation with optional size: def __init__(self, size=0)"""

    def __init__(self, size=0, position=(0, 0)):
        """Size and position are private attribute"""
        self.size = size
        self.position = position


    @property
    def size(self):
        """Property of size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """size is a private attribute:
            - size must be an integer, otherwise raise a TypeError
            exception with the message size must be an integer
            - if size is less than 0, raise a ValueError exception
            with the message size must be >= 0"""
        if (type(value) is not int):
            raise (TypeError("size must be an integer"))
        elif (value < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position to a value."""
        if (type(value) is not tuple) or (len(value) != 2)\
                or (type(value[0]) is not int)\
                or (type(value[1]) is not int)\
                or (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value


    def area(self):
        """- Public instance method: def area(self): that returns
            the current square area"""
        return (self.__size * self.__size)



    def my_print(self):
        """Print square with the character # in stdout"""
        if self.__size == 0:
            print()
        else:
            for jump_line in range(self.position[1]):
                print()
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
