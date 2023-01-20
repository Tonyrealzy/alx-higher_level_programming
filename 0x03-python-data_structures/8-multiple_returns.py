#!/usr/bin/python3

def multiple_returns(sentence):
    x = len(sentence)
    y = sentence[0]

    if sentence:
        return (x, None)

    else:
        return (x, y)
