#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda g: list(map(lambda f: f**2, g)), matrix))
