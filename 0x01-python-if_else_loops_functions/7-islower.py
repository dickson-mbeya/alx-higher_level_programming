#!/usr/bin/python3
def islower(c):
    if ord(c) in range(97, 123):
        return True
    elif ord(c) in range(48, 57) or ord(c) in range(65, 90):
        return False
    pass
