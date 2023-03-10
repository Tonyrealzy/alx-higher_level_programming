#!/usr/bin/python3
"""Module that checks if object is an 
instance of the specified class"""


def inherits_from(obj, a_class):
    """checks if the object is an instance of a class"""
    if issubclass(isinstance(obj, a_class)):
        return True
    else:
        return False
