#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == {}:
        return None
    else:
        for k in a_dictionary:
            return max(a_dictionary, a_dictionary.get)
