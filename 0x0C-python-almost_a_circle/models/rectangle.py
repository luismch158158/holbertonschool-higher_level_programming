#!/usr/bin/python3
"""
Program that defines Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle with width, height,
    x and y parameters"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor of Rectangle: width (int), height (int)
        x(int) and y(int)"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Display # in the stdout
        taking care of x and y"""

        for jump_line in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """This magic method print informal"""
        return("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Update the class Rectangle that
        assigns an argument to each attribute like: id, width
        height, x and y, for *args and **kwargs"""
        parameters = ["id", "width", "height", "x", "y"]
        len_param = len(parameters)
        len_args = len(args)
        if args and args[0] is not None:
            final_len = len_param if (len_args > len_param) else len_args
            for i in range(final_len):
                setattr(self, parameters[i], args[i])
        elif kwargs is not None:
            for key, value in kwargs.items():
                if (hasattr(self, key)):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Update the class Rectangle that returns
        the dictionary representation of a Rectangle"""
        return ({
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y,
            })

    @property
    def width(self):
        """Getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of width"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter of x"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter of y"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
