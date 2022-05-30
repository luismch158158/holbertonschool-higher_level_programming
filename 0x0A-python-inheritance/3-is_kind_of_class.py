#!/usr/bin/python3
"""Class definition"""

def is_kind_of_class(obj, a_class):
    """
    Function that returns True, if the object of,
    or if the object is an instance of a class
    that inherited from, the specifies class,
    otherwise False
    """
    return (isinstance(obj, a_class))
