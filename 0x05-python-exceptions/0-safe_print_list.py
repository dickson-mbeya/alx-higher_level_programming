#!/usr/bin/python3
try:
    def safe_print_list(my_list=[], x=0):
        new_list = my_list[:x]
        result = int(''.join(map(str, new_list)))
        print(result)
        return x
except IndexError:
    pass
except ValueError:
    pass
except NameError:
    pass
