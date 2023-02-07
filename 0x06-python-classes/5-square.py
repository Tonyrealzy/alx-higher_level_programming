#!/usr/bin/python3
"""Module defines the class Square"""


class Square:
    """A non-empty class named Square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size
    """Initialising the private method size"""
    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) == int:
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return (self.__size ** 2)
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print("")
                