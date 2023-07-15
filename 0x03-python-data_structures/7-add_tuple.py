#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    a = tuple_a([0]) + tuple_b([0]) + (0, 0)
    b = tuple_a([1]) + tuple_b([1]) + (0, 0)
    new_tuple = a, b
    return new_tuple
