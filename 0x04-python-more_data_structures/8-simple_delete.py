#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """ deletes a key in a dictionary.f a key doesn’t exist, the dictionary won’t change"""
    if key in a_dictionary:
        del a_dictionary[key]
        print(a_dictionary)
    else:
        print(a_dictionary)
