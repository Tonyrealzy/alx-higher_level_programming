#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new_list = sorted(a_dictionary.keys())

    for k in new_list:
        print("{}: {}".format(k, a_dictionary[k]))
