#!/usr/bin/python3
""" operator invert"""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, value):
        """ invert != opeartor """
        return self.real != value

    def __ne__(self, value):
        """invert == operator """
        return self.real == value
