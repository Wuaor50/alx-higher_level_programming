#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = []
    new = list(set_1 - set_2) + list(set_2 - set_1)
    return list(set(new))
