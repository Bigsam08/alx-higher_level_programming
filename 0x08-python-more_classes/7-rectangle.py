#!/usr/bin/python3
"""
    Drawing Rectangle
"""


class Rectangle:
    """Designing Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            Rectangle attributes
        """
        self.width = width
        self.height = height
        rectangle.number_of_instances += 1

    @property
    def width(self):
        """Default Rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting width size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Default height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
            setting Rectangle Size
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """
            print rectangle using # symbol
        """
        for i in range(self.area()):
            if i % self.__width == 0:
                if i != 0:
                    print()
            print(self.print_symbol, end='')
        return ""

    def __repr__(self):
        """representation of the Rectangle as string"""
        return F"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ Deleting Rectamgle """
        rectangle.number_of_instances -= 1
        print(F"Bye rectangle...")
