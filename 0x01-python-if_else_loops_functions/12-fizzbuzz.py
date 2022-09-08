#!/usr/bin/python3
def fizzbuzz():
    for i in range(100):
        s = i + 1
        if s % 3 == 0 and s % 5 == 0:
            print("FizzBuzz", end=" ")
        elif s % 5 == 0:
            print("Buzz", end=" ")
        elif s % 3 == 0):
            print("Fizz", end=" ")
        else:
            print("{:d}".format(s), end=" ")
