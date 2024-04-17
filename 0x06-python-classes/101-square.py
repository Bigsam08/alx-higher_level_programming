#!/usr/bin/python3
"""A  Square class."""


class Square:
    """working on a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Designing the properties of the square
        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of square  """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Area of square """
        return self.size ** 2

    def my_print(self):
        """Print character #."""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)

    def __str__(self):
        """Return a character representing square."""
        char = ""
        if self.size == 0:
            return char
        char += "\n" * self.position[1]
        char += "\n".join((" " * self.position[0] + "#" * self.size)for p in range(self.size))
        return char
