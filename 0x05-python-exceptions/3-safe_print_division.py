#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        if a and b != 0:
            return (a / b)
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result:", "{}".format(a / b))
