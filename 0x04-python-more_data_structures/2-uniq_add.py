#!/usr/bin/python3

def uniq_add(my_list=[]):
    set_list = set(my_list)
    sum_list = 0

    for x in set_list:
        sum_list += x

    return sum_list
