#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    for tuple_a and tuple_b:
        len(tuple_a) = w
        len(tuple_a) = x

    if w == 0:
        tuple_a = (0, 0)
    elif w == 1:
        tuple_a = (tuple_a[0], 0)

    if x == 0:
        tuple_b = (0, 0)
    elif x == 1:
        tuple_b = (tuple_b[0], 0)

    if w > 2:
        tuple_a = (tuple_a[0], tuple_a[1])
    elif x > 2:
        tuple_b = (tuple_b[0], tuple_b[1])

    sum = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    return sum
