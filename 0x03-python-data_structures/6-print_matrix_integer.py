#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            print("{}".format(column), end=" " if column != row[-1] else "$")
        print()
