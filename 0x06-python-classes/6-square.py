#!/usr/bin/python3
""" drawing  a square class """


class Square:
    """ Defining a class square """

    def __init__(self, size=0, position=(0, 0)):
        """getting diagram."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the size of square to value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ sets position of square."""
        return self.__position

    @position.setter
    def position(self, value):
        """ assigns value to position of square"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ square area."""
        return self.__size ** 2

    def my_print(self):
        """prints out the square of character # to the console output
        with the position  assigned by the position setter.
        """
        if self.__size == 0:
            print()
            return
        for i in range(0, self.__position[1]):
            print()
        for a in range(0, self.__size):
            for b in range(0, self.__position[0]):
                print(" ", end="")
            for c in range(0, self.__size):
                print("#", end="")
            print()
