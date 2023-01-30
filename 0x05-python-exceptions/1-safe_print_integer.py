#!/usr/bin/python3

def safe_print_integer(value):
    result = isinstance(value, int)
    try:
        if result == True:
            print("{:d}".format(value))
            return True
    except:
        if result == False:
            return False
