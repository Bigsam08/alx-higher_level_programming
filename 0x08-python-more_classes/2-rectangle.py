#!/usr/bin/python3
""" Creating a rectangle"""


class Rectangle:
    """ setting attributes """

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setting  width size
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getting Rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setting the height of Rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        perimeter of the rectangle
        """
        return (self.__width + self.__height) * 2
