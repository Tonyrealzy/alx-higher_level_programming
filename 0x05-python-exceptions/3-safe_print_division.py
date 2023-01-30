#!/usr/bin/python3

def safe_print_division(a, b):
    c = None
    try:
        if a and b != 0:
            c = a / b
            print("Inside result: {}".format(c))
    except ZeroDivisionError:
        print("Inside result: {}".format(c))
    finally:
        return (c)
