#!/usr/bin/python3
def fizzbuzz():
    for k in range(1, 101):
        if k % 3 == 0 and k % 5 != 0:
            print("Fizz ", end='')
        elif k % 5 == 0 and k % 3 != 0:
            print("Buzz ", end='')
        elif k % 5 == 0 and k % 3 == 0:
            print("FizzBuzz ", end='')
        else:
            print("{} ".format(k), end='')
