#!/usr/bin/python3
""" A class BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class  """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area att"""
        return self.__width * self.__height

    def __str__(self):
        """ __str__  att"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
