#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    f, g = 0, 0
    while f < x:
        try:
            print("{:d}".format(my_list[f]), end='')
            g += 1
        except (ValueError, TypeError):
            pass
        f += 1
    print()
    return g
