#!/usr/bin/python3
def weight_average(my_list=[]):
    '''Returns weighted average of integer tuple'''
    sum_products = 0
    sum_weights = 0

    for value, weight in my_list:
        sum_products += value * weight
        sum_weights += weight
    if len(my_list) == 0:
        return 0
    else:
        weighted_average = sum_products / sum_weights
        return weighted_average
