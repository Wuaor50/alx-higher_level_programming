#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for i in range(x):
        my_list[i]
        try:
            print("{:d}".format(my_list[i]), end="")
            n = n + 1
        except Exception:
            pass
    print()
    return n
