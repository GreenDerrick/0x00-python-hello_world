#!/usr/bin/python3
a = 98
b = 122
while b > 96:
    if b % 2 != 0:
        res = chr(b - 32)
    else:
        res = chr(b)
    print("{}".format(res), end=(''))
    b -= 1
