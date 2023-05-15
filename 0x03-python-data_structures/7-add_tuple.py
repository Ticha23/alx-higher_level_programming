#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    tuple_p = tuple_a + (0, 0)
    tuple_j = tuple_b + (0, 0)
    new_tuple = tuple_p[0] + tuple_j[0], tuple_p[1] + tuple_j[1]
    return new_tuple
