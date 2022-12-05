#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for i, j in enumerate(my_string):
        if j == 'c' or j == 'C':
            continue
        new_str = new_str + j
    return new_str
