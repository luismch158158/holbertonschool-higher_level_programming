#!/usr/bin/python3
"""New class of Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Definition Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor of Square Class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The overloading"""
        return("[Square] ({:d}) {:d}/{:d} - {:d}"
               .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Getter of the size with width"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter of size using value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the class Square that
        assigns an argument to each attribute like: id, size
        x and y, for *args and **kwargs"""
        parameters = ["id", "size", "x", "y"]
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
        """Update the class Square that returns
        the dictionary representation of a Rectangle"""
        return ({
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y,
            })
