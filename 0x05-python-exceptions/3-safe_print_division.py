#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        if a >= 0 and b > 0:
            return (a / b)
    except Exception:
        return None
    finally:
        print("Inside result:", "{}".format(a / b))
