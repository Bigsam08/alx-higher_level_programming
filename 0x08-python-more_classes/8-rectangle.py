#!/usr/bin/python3
""" Defining a class Rectangle """


class Rectangle:
    """ Rectangle attributes"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ the Rectangle"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ Getting Rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting size of Rectangle width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getting height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the  height size of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            area of Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """
            print out rectangle with '#' symbol
            using print function
        """
        for i in range(self.area()):
            if i % self.__width == 0:
                if i != 0:
                    print()
            print(self.print_symbol, end="")
        return ""

    def __repr__(self):
        """ str representation of Rectangle"""
        return F"Rectangle({self.__width}, {self.__height})"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Comperes two rectangles
            Returns: The biggest
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        return rect_2

    def __del__(self):
        """ Delete  Rectangle """
        type(self).number_of_instances -= 1
        print(F"Bye rectangle...")
