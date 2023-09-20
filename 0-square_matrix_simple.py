#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_mul= list(map(x * 2 for x in range(len(matrix))))
    return matrix_mul
