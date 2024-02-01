#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print('0 arguments.')
elif len(sys.argv) == 2:
    print('1 argument:')
    print(f'{(len(sys.argv)-1)}: {sys.argv[1]}')
else:
    for arg in sys.argv[1:]:
        if sys.argv.index(arg) == 1:
            print((len(sys.argv)-1), "arguments:")
        print(f'{sys.argv.index(arg)}: {arg}')
