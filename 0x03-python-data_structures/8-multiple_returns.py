#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        first = 'None'
        return (len(sentence), first)
    else:
        return (len(sentence), sentence[0])
