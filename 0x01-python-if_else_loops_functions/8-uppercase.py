#!/usr/bin/python3
def uppercase(str):
    i = 0
    length = len(str) - 1
    
    while i != length:
        final = ord(str[i]) - 32
        if final < 65:
            print("{}".format(str[i]), end=(''))
        else:
            print("{}".format(chr(final)), end=(''))
        i+=1
    final = ord(str[i]) - 32
    if final < 65:
        print("{}".format(str[i]), end=('\n'))
    else:
        print("{}".format(chr(final)), end=('\n'))
