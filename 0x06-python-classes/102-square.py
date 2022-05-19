#!/usr/bin/python3
"""Class Square"""


class Square:
    """Defines a square class:
    - Private instance attribute: size
    - Instantatiation with optional size: def __init__(self, size=0)"""

    def __init__(self, size=0):
        """size is a private attribute"""
        self.size = size

    def area(self):
        """- Public instance method: def area(self): that returns
            the current square area"""
        return (self.__size * self.__size)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, new_size):
        if (type(new_size) is not int):
            raise (TypeError("size must be an integer"))
        elif (new_size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = new_size

    def __eq__(self, object2):
        """ == """
        return self.area() == object2.area()

    def __lt__(self, object2):
        """ < """
        return self.area() < object2.area()

    def __gt__(self, object2):
        """ > """
        return self.area() > object2.area()

    def __le__(self, object2):
        """ <= """
        return self.area() <= object2.area()

    def __ge__(self, object2):
        """ >= """
        return self.area() >= object2.area()

    def __ne__(self, object2):
        """ != """
        return self.area() != object2.area()
