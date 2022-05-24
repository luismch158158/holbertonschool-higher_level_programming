#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list_pass=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list_pass) == 0:
        return None

    if not isinstance(list_pass, list):
        raise TypeError("Data types to enter must be a list of integers")

    for member in list_pass:
        if not isinstance(member, int):
            raise TypeError("Members in a list must be a integers")

    result = list_pass[0]
    i = 1
    while i < len(list_pass):
        if list_pass[i] > result:
            result = list_pass[i]
        i += 1
    return result
