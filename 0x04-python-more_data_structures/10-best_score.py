#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    
    for key, value in a_dictionary.items():
        max_value = max(a_dictionary.values())
        if value == max_value:
            return(key)
