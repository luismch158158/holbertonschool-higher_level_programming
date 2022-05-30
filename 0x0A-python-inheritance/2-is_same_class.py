#!/usr/bin/python3
"""Class definition"""


def is_same_class(obj, a_class):
    """Return True if the object is exactly an instance
    of the specified class, otherwise False"""
    return(type(obj) is a_class)
