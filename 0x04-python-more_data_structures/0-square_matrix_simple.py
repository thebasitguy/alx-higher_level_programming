#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = []
    for line in matrix:
        sq_matrix.append([c**2 for c in line])
    return sq_matrix
