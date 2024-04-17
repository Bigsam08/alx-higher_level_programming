#!/usr/bin/python3
""" magic class """
import math

class MagicClass:
    """ starting the MagicClass."""
    def __init__(self, radius=0):
        """Initializing data."""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """area calculation"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """ circumference calculation"""
        return 2 * math.pi * self._MagicClass__radius
