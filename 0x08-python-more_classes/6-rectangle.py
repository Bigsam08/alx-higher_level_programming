#!/usr/bin/python3
""" Defining a Rectangle """


class Rectangle:
    """Designing a Rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Rectangle attributes"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
            Get Rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            Default height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setting  height of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Area of the Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            perimeter of the Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """ printing rectangle with symbol # """
        for i in range(self.area()):
            if i % self.__width == 0:
                if i != 0:
                    print()
            print("#", end="")
        return ""

    def __repr__(self):
        """ Returns representation of Rectangle as string"""

        return F"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ deleting msg with rectangle instance """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
