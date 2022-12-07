#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = list(set_1) + list(set_2)
    return list(set(new))
