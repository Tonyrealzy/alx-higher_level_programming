#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key:
        a_dictionary.remove(key)

    return a_dictionary
