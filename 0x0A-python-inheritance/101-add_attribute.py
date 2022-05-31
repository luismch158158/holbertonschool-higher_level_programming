#!/usr/bin/python3
"""
Program will try to add attributes to class if it possible
"""


def add_attribute(obj, key, value):
    """
    This function add attributes to class if it possible
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    return (setattr(obj, key, value))
