#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """ Prints a dictionary by ordered keys """
    sorted_dictionary = {key: a_dictionary[key] for key in sorted(a_dictionary)}
    return sorted_dictionary
