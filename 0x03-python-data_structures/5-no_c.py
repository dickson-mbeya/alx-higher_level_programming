#!/usr/bin/python3
def no_c(my_string):
    c = ['C', 'c']
    return ''.join(char for char in my_string if char not in c)
