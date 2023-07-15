#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    tuple_a1 = tuple_a + (0, 0)
    tuple_b2 = tuple_b + (0, 0)
    a = tuple_a1[0] + tuple_b2[0]
    b = tuple_a1[1] + tuple_b2[1]
    new_tuple = a, b
    return new_tuple
