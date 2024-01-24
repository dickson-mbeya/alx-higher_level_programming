#!/usr/bin/python3
#islower = __import__('7-islower').islower
def main():
    print("a is {}".format("lower" if islower("a") else "upper"))
    print("H is {}".format("lower" if islower("H") else "upper"))
    print("A is {}".format("lower" if islower("A") else "upper"))
    print("3 is {}".format("lower" if islower("3") else "upper"))
    print("g is {}".format("lower" if islower("g") else "upper"))


def islower(c):
    if ord(c) in range(97, 123):
        return True
    elif ord(c) in range(48, 57) or ord(c) in range(65, 90):
        return False
    pass


main()
#def islower(c):
#    for c in range(48, 123):
#        if 48 <= ord(c) <= 57 or 65 <= ord(c) <= 90:
#            print(c, "is Upper")
#        elif 97 <= ord(c) <= 122:
#            print(c, "is lower")
#        pass

#islower('H')

#>>> c = 'a'
#>>> ord(c) in range(97, 123)
#True