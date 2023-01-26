#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix:
        square_matrix = list(map(lambda x: x ** 2, y)) for y in matrix
        return square_matrix
