#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        no = -(number) % 10
    else:
        no = number % 10
    print('{}'.format(no), end='')
    return no
