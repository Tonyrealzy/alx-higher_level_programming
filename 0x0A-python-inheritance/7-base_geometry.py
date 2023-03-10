#!/usr/bin/python3
"""Module of an empty class"""


class BaseGeometry:
    """Not an empty class"""
def area(self):
    """Exception message"""
    raise Exception("area() is not implemented")

def integer_validator(self, name, value):
    """Validates value
    Args:
        name(str): name
        value(int): value
        """
    self.name = name
    self.value = value
    if type(value) is not int:
        raise TypeError("{} must be an integer".format(name))
    if int(value) <= 0:
        raise ValueError("{} must be greater than 0".format(name))