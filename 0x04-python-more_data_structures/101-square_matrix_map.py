#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    sq_mtx = list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
    return sq_mtx
