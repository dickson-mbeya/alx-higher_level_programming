#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

number = str(number)

l_dgt = number[-1]
l_dgt = int(l_dgt)

print(number)
number = int(number)
if number < 0:
    l_dgt = -1 * l_dgt
else:
    l_dgt = l_dgt

if l_dgt > 5:
    print("Last digit of", number, "is", l_dgt, "and is greater than 5")
elif l_dgt == 0:
    print("Last digit of", number, "is", l_dgt, "and is 0")
elif l_dgt < 6 and l_dgt != 0:
    print("Last digit of", number, "is", l_dgt, "and is less than 6 and not 0")
pass
