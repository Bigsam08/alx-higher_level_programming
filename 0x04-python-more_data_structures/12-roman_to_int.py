#!/usr/bin/python3

"""
roman figures are alphabets attached to a specific number
this is a function that converts romnan numbers to numbers
"""


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    rom_fig = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    value1 = 0

    for i in reversed(roman_string):
        if i in rom_fig:
            value2 = rom_fig[i]
            if value2 >= value1:
                result += value2
            else:
                result -= value2
            value1 = value2
        else:
            return 0
    return result
