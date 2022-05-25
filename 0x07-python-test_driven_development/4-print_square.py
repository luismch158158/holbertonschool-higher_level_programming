#!/usr/bin/python3
""" This program print squares of #"""


def print_square(size):
    """Print square with the character # in stdout"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size != 0:
        j = 0
        while j < size:
            print("#" * size)
            j += 1
