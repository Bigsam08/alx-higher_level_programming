#!/usr/bin/python3
""" empty class """


class BaseGeometry:
    """ a class BaseGeaometry """

    def area(self):
        """ Returns the area """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validating content value """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
