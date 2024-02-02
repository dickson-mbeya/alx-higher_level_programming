#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if len(sys.argv) < 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
operators = ['+', '-', '*', '/']
if sys.argv[2] not in operators:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
a = sys.argv[1]
b = sys.argv[3]

a = int(a)
b = int(b)

if sys.argv[2] == '+':
    print(sys.argv[1], "+", sys.argv[3], '=', add(a, b))
elif sys.argv[2] == '-':
    print(sys.argv[1], "-", sys.argv[3], '=', sub(a, b))
elif sys.argv[2] == '*':
    print(sys.argv[1], "*", sys.argv[3], '=', mul(a, b))
elif sys.argv[2] == '/':
    print(sys.argv[1], "/", sys.argv[3], '=', div(a, b))

if __name__ == '__main__':
    sys
    add
    sub
    mul
    div
