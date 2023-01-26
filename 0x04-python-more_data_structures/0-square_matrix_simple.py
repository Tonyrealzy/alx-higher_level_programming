#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix:
        square_matrix = [[x**2 for x in y] for y in matrix]
        return square_matrix
