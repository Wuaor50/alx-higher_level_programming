#!/usr/bin/python3
def common_elements(set_1, set_2):
    new = []
    new = list(set_1 - set_2) + list(set_2 - set_1)
    return list(set_1 - set(new))
