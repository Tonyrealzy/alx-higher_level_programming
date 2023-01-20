#!/usr/bin/python3

def multiple_returns(sentence):
    x = len(sentence)
    y = sentence[0]

    if sentence:
        return (x, y)

    else:
        return (x, None)
