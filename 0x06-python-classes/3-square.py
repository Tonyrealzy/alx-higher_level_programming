#!/usr/bin/python3
"""Module defines the class Square"""


class Square:
    """A non-empty class named Square"""

    def __init__(self, size=0):
        self.__size = size
        """Initialising the private method size"""

        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return (self.__size ** 2)
