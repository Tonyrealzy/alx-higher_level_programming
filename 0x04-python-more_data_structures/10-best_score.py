#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == {}:
        return None
    else:
        for k in a_dictionary:
            if max(a_dictionary[k]):
                return k
