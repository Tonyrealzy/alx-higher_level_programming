#!/usr/bin/python3
"""Module that checks if object is an
instance of the specified class"""


def is_same_class(obj, a_class):
    """ returns True if the object is exactly an
    instance of the specified class ; otherwise False"""
    if type(obj) is a_class:
        return True
    else:
        return False
    