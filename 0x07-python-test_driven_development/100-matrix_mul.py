#!/usr/bin/python3
"""Multiplies 2 matrices"""

def matrix_mul(m_a, m_b):
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if not all(isinstance(ele, (int,float)) for ele in row):
            raise TypeError("m_a should contain only integers or floats")
        if not all(len(row) == len(m_a[0])):
            raise TypeError("each row of m_a must should be of the same size")
    
    for row in m_b:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("m_b should contain only integers or floats")
        if not all(len(row) == len(m_b[0])):
            raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b[0]):
        raise ValueError("m_a and m_b can't be multiplied")
    
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            elem_sum = 0
            for k in range(len(m_b)):
                elem_sum += m_a[i][k] * m_b[k][j]
            row.append(elem_sum)
        result.append(row)

    return result
