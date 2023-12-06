#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    wordA function that computes the square
    value of all integers of a matrix.
    """
    new_matrix = []
    for each_num in matrix:
        result = list(map(lambda x: x**2, each_num))
        new_matrix.append(result)
    return new_matrix

