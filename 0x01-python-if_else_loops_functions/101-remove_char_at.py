#!/usr/bin/python3
def remove_char_at(str, n):
    new = ''
    k = 0
    for char in str:
        if k != n:
            new += str[k]
            k += 1
            return (new)
