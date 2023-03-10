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
    

class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of a rectangle"""
        return self.__width * self.__height
    
    def __str__(self):
        """informal rectangle description"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
    

class Square(Rectangle):
    """Class that inherits from Rectangle"""
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of square"""
        return self.__size ** 2
    
    def __str__(self):
        """informal description of square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
    