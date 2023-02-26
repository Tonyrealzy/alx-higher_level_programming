#!/usr/bin/python3

"""Prints a text with 2 new lines after each
of these characters: ., ? and :"""

def text_indentation(text):
    """
    Args:
        text: string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1

        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")