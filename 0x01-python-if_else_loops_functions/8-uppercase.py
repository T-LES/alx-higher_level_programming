#!/usr/bin/python3
def uppercase(str):
    for w in range(str):
        if ord(w) >= 97 and ord(w) <= 122:
            w = ord(w) - (ord('z') - ord('Z'))
        print("{:c}".format(w), end='')
    print("")
