#!/usr/bin/python3
def uppercase(str):
    for w in range(len(str)):
        if ord(str[w]) >= 97 and ord(str[w]) <= 122:
            w = ord(str[w]) - (ord('z') - ord('Z'))
        else:
            w = ord(str[w])
        print("{:c}".format(w), end='')
    print("")
