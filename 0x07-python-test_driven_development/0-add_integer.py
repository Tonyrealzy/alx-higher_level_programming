#!/usr/bin/python3

"""A function that adds two integers"""

def add_integer(a, b=98):
    """
    Args:
        a: first number
        b: second number
    Returns:
        sum of a and b
    """
    
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    
    a = int(a)
    b = int(b)
    return a + b