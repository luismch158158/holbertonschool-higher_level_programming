#!/usr/bin/python3
"""
This program divides all elements of a by divisor
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix
    matrix of list of lists of integers or floats
    Return a new matrix
    """

    new_matrix = []
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(error)

    if len(matrix) == 0:
        return new_matrix

    rows = len(matrix)
    elements = len(matrix[0])

    if (type(div) not in (float, int)):
        raise TypeError("div must be a number")

    if (div == 0):
        raise ZeroDivisionError("division by zero")

    for row in matrix:

        if not isinstance(row, list):
            raise TypeError(error)

        if len(row) != elements:
            raise TypeError("Each row of the matrix must have the same size")

        for num in row:
            if (type(num) not in [float, int]):
                raise TypeError(error)
        new_matrix.append(list(map(lambda x: round(x / div, 2), row)))

    return new_matrix
