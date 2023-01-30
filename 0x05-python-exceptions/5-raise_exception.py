#!/usr/bin/python3

def raise_exception():
    try:
        raise
    except TypeError:
        print("Exception has been raised")
