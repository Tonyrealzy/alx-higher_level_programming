#!/usr/bin/python3
"""Module defining a rectangle"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for def width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """setter for def width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """getter for def height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """setter for def height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        
    def area(self):
        """returns the area of rectangle"""
        return (self.__height * self.__width)
    
    def perimeter(self):
        """returns the perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
             return 0
        return ((self.__height * 2) + (self.__width * 2))
    