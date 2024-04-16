#!/usr/bin/python3
""" drawing a square class """


class Square:
    """ class square definition"""
    def __init__(self, size=0):
        """ Initializing a square class
        Args: size=0: square size
         """
        self.__size = size

    @property
    def size(self):
        """ retriving square size """
        return self.__size

    @size.setter
    def size(self, value):
        """ re_setting the square size """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ getting the area of the square """

        return (self.__size ** 2)

    def my_print(self):
        """ new square shape output"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
