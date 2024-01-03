#!/usr/bin/python3
for k in range(ord('z'), ord('a') - 1, - 2):
    print("{}{}".format(chr(k), chr(k - 33)), end='')
