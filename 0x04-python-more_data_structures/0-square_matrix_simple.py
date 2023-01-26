#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    for y in matrix:
        square_matrix = [list(map((lambda x: x ** 2), y))]
        return square_matrix
