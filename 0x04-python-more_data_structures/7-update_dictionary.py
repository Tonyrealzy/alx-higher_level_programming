#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    newlist = sorted(a_dictionary.keys())

    for k in newlist:
        if k:
            a_dictionary[k] = value
        else:
            a_dictionary[k] = value
