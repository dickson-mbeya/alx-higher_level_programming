#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if len(sys.argv) < 4:
    sys.exit("Usage: ./100-my_calculator.py <a> <operator> <b>")

operators = ['+', '-', '*', '/']
if sys.argv[2] not in operators:
    sys.exit("Unknown operator. Available operators: +, -, * and /")

a = sys.argv[1]
b = sys.argv[3]

a = int(a)
b = int(b)

if sys.argv[2] == '+':
    print(sys.argv[1], "+", sys.argv[3], '=', a + b)
elif sys.argv[2] == '-':
    print(sys.argv[1], "-", sys.argv[3], '=', a - b)
elif sys.argv[2] == '*':
    print(sys.argv[1], "*", sys.argv[3], '=', a * b)
elif sys.argv[2] == '/':
    print(sys.argv[1], "/", sys.argv[3], '=', a / b)

if __name__ == '__main__':
    sys
    add
    sub
    mul
    div
