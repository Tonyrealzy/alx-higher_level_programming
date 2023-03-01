#!/usr/bin/python3
"""Module defining a rectangle"""


class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """is called when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
    
    def __str__(self):
        """returns the string representation of a rectangle"""
        rectangle = ""
        if self.__height == 0 or self.__width == 0:
            return rectangle
        for i in range(self.__height - 1):
            rectangle += str(self.print_symbol) * self.__width + "\n"
        rectangle += str(self.print_symbol) * self.__width

        return rectangle
    
    def __repr__(self):
        """returns the representation of a rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)