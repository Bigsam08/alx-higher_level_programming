#!/usr/bin/python3
"""Creating a Rectangle class."""


class Rectangle:

    def __init__(self, width=0, height=0):
        """Designing Rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ setting the rectangle width"""
        return self.__width

    @width.setter
    """ handling error msg with width size """
    def width(self, value):
        if not type(int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getting rectangle height."""
        return self.__height

    @height.setter
    """ setting the height and handling err figures """
    def height(self, value):
        if not type(int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        #if self.width == 0 or self.height == 0:
         #   return 0
        return (self.__width + self.__height) * 2
