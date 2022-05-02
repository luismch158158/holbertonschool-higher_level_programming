#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != "":
        a = sentence[0]
        lengthen = len(sentence)
    else:
        a = None
        lengthen = 0

    return (lengthen, a)
