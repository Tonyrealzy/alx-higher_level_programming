#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        if a and b != 0:
            c = a / b
            return (c)
    except ZeroDivisionError:
        c = None
        return (c)
    finally:
        print("Inside result:", "{}".format(c))
