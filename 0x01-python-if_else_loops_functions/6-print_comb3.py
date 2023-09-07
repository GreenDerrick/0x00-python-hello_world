#!/usr/bin/python3
for i in range(0, 9):
    for j in range (0, 9):
        if (i, j) != (j, i):
            print("{:01d}{:01d}".format(i, j), end=(', '))
