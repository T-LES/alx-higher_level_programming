#!/usr/bin/python3
for w in range(123, 96, -1):
    if w % 2 != 0:
        print("{:c}".format(w - 32), end="")
    else:
        print("{:c}".format(w), end="")
