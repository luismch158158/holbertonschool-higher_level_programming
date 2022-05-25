#!/usr/bin/python3
"""
This program multiply two matrices with the library numpy
"""
import numpy as np


def lazy_matrix_mul(matrix_a, matrix_b):
    """
    Multiply two matrices
    matrix_a : lists of lists (int or float)
    matrix_b : lists of list (int or float)
    """

    return np.matmul(matrix_a, matrix_b)
