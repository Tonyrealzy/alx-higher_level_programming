#!/usr/bin/python3
"""Module defines the class Square"""


class Square:
    """A non-empty class named Square"""

    def __init__(self, size=0):
        self.__size = size

        try:
            type(size) == int
            size >= 0
        
        except (TypeError, ValueError) as error:
            print ("size must be an integer")
            print ("size must be >= 0")