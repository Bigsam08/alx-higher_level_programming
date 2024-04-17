#!/usr/bin/python3
""" working on creating square class with import """


class Square:
    """ Generating class square """
    def __init__(self, size=0):
        """ Initializing square class
        Args: size=0: size of the square
         """
        self.__size = size

    @property
    def size(self):
        """ size of  square """
        return self.__size

    @size.setter
    def size(self, value):
        """ designing square size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Finding the square area """
        return (self.__size ** 2)

    def __eq__(self, other):
        """ Comparing two squares """
        return self.area() == other.area()

    def __ne__(self, other):
        """ just one square """
        return self.area() != other.area()

    def __lt__(self, other):
        """ Comparing < two squares """
        return self.area() < other.area()

    def __le__(self, other):
        """ Comparing <= two squares """
        return self.area() <= other.area()

    def __gt__(self, other):
        """ Comparing > two squares """
        return self.area() > other.area()

    def __ge__(self, other):
        """ Comparing >= two squares """
        return self.area() >= other.area()
