#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    prev = 0

    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if roman_string is None or type(roman_string) is not str:
        return 0

    for c in reversed(roman_string):
        value = dict.get(c, 0)
        if value >= prev:
            num += value
        else:
            num -= value

        prev = value
    return num
