#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        if a and b:
            return (a / b)
    except Exception:
        return None
    finally:
        print("Inside result:", "{}".format(a / b))
