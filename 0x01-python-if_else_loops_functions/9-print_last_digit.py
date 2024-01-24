#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        ldgt = (number % 10)
        print(ldgt, end="")
    else:
        number = abs(number)
        ldgt = (number % 10)
        print(ldgt, end="")
    return ldgt
