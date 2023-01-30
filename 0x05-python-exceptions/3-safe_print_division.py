#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        if a and b != 0:
            c = a / b
    except ZeroDivisionError:
        c = None
    finally:
        print("Inside result:", "{}".format(c))
    return (c)
