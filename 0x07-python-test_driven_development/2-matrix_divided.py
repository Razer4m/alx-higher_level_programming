#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The input matrix containing integers or floats.
        div (int or float): The number to divide all elements of the matrix by.
    Returns:
        A new matrix representing the result of the division
    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
                   or if each row of the matrix does not have the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    mtrx = [[round(element / div, 2) for element in row] for row in matrix]
    return mtrx
