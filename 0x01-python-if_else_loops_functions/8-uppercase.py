#!/usr/bin/python3
def uppercase(str):
    d = ''
    for i in str:
        if ord(i) in range(97, 123):
            i = chr(ord(i) - 32)
        d = d + i
    print("{}".format(d))
