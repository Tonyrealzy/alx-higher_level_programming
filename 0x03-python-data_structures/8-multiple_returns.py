#!/usr/bin/python3

def multiple_returns(sentence):
    x = len(sentence)
    y = sentence[0]

    if not sentence:
        return (x, None)

    else:
        return (x, y)
