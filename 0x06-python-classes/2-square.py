#!/usr/bin/python3
""" drawing a square class """


class Square:
    """ class square defining"""
    def __init__(self, size=0):
        """ Initializing a square class
        Args: size=0: square size
         """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
