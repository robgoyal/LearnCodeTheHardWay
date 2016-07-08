#!/usr/bin/env/python

# Functions Can Return Something
# Code written by Robin Goyal
# Created on July 8, 2016
# Last updated on July 8, 2016

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's just do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# Using the functions to display the expression
# 37 * (15 + 7 - 6*2)/5

# Excepted answer is 74
calculation = multiply(37, divide(add(15, subtract(7, multiply(6, 2))), 5))

print calculation
