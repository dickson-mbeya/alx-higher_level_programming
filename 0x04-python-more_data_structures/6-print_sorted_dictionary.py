#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """ Prints a dictionary by ordered keys """
    sorted_dictionary = {k: a_dictionary[k] for k in sorted(a_dictionary)}
    return sorted_dictionary
