#!/usr/bin/python3
def remove_char_at(str, n):
    temp = ""
    for c in range(len(str)):
        if c == n:
            continue
        temp = temp + str[c]
    str = temp[:]
    return str
