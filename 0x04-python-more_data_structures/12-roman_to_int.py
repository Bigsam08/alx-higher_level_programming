#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    rom_fig = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list = 0
    for i in range(len(roman_string)):
        if i > 0 and rom_fig[roman_string[i]] > rom_fig[roman_string[i - 1]]:
            list += rom_fig[roman_string[i]] - 2 * rom_fig[roman_string[i - 1]]
        else:
            list += rom_fig[roman_string[i]]
    return list
