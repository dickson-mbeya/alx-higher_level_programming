#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 200, "M": 1000}
    first_key, first_value = next(iter(roman.items()))
    result = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = roman[char]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result
