#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    rom_fig = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    value2 = 0

    for i in reversed(roman_string):
        if i in rom_fig:
            value1 = rom_fig[i]
            if value1 >= value2:
                result += value1
            else:
                result -= value1
                value2 = value1
            else:
                return 0
            return result
