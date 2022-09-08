#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        modulo = number % 10
    else:
        modulo = -(number % -10)
    print("{:d}".format(modulo))
    return(modulo)
