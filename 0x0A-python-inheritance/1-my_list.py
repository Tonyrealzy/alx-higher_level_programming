#!/usr/bin/python3
"""Module of a class MyList"""


class MyList(list):
    def __init__(self):
        """initialising the object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted self"""
        print(sorted(self))