#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = len(my_list)
    if idx < 0:
        return my_list
    elif idx > n:
        return my_list
    new = my_list[:]
    new[idx] = element
    return new
