#!/usr/bin/python3
def uniq_add(my_list=[]):
    set1 = set(my_list)
    my_list = (list(set1))
    list_sum = 0
    for i in my_list:
        list_sum += i
    return list_sum
