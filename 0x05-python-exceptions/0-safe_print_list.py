#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            num = num + 1
        print()
        return num
    except Exception:
        print()
        return num
