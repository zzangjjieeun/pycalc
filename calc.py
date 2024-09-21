#!/usr/bin/env python

# Copyright 2016 -- Levi Starrett & Jay Hankins
# for educational purposes only
#
# For use in CS 190: https://github.com/Purdue-CSUSB/CS-190-F2016/
#
# Calculator -- a four function calculator commandline tool

import sys
import math

# -------------------------------------------------------- #
# -- CALCULATOR FUNCTIONS -------------------------------- #
# -------------------------------------------------------- #

# Add function
# a -- addend
# b -- augend
def add(a, b):
    return a + b

# Subtract function
# a -- minuend
# b -- subtrahend
def sub(a, b):
    return a - b

# Multiply function
# a -- multiplicand
# b -- multiplier
def mult(a, b):
    return a * b

# Divide function
# a -- dividend
# b -- divisor
def div(a, b):
    return a / b

# Power function
# a -- base
# b -- exponent
def power(a, b):
    return a ** b

# Log function
# base -- log base
# x -- number to calculate log of
def log(base, x):
    return math.log(x, base)





# -------------------------------------------------------- #


# -------------------------------------------------------- #
# -- MAIN FUNCTIONAILTY -- DO NOT EDIT ------------------- #
# -------------------------------------------------------- #

a = None
b = None
op = None

while (True):
    # get input values
    a = input("Enter the first argument: ")
    op = input("Enter the operation: ")
    b = input("Enter the second argument: ")
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print ("Invalid number argument...")
        op = None

    # decide function
    if (op != None):
        if (op == "+"):
            print ("Sum: ", add(a, b))
        elif (op == "-"):
            print ("Difference: ", sub(a, b))
        elif (op == "*"):
            print ("Product: ", mult(a, b))
        elif (op == "/"):
            print ("Quotient: ", div(a, b))
        elif (op == "^"):
            print("Power: ", power(a, b))
        elif (op == "log"):
            print("Log: ", log(a, b))  # a는 밑, b는 숫자
        else:
            print ("Invalid operation...")

    q = input("Quit? [y/n] ")
    if (q == "y" or q == "Y"):
        break

# -------------------------------------------------------- #
