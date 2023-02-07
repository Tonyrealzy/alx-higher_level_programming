#!/usr/bin/python3
"""Module defines the class Square"""


class Square:
    """A non-empty class named Square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position
        """Initialising the private method position"""
    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            i, j = 0, 0
            par = self.__position[0]
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print("{}{}".format(" " * par, "#" * self.__size))
