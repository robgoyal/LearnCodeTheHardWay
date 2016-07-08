#!/usr/bin/env/python

# Functions and Variables
# Code written by Robin Goyal
# Created on July 8, 2016
# Last updated on July 8, 2016

# Code to multiply two numbers with different ways

from sys import argv
script, arg1, arg2 = argv

def multiply(var1, var2):
    print var1*var2

num_one = 5
num_two = 10

placeholder1  = 2
placeholder2 = 5

value_1 = raw_input("What is the first number: ")
value_2 = raw_input("What is the second number: ")

multiply(5, 10) # Straight integers as arguments
multiply(num_one, num_two) # Variables as arguments
multiply(2+3, 5+5) # Basic math expression
multiply(int(arg1), int(arg2)) # Type conversion of argument inputs
multiply(int(value_1), int(value_2)) # Type conversion of string inputs
multiply(3 + placeholder1, 5 + placeholder2) # Variable and int
multiply((10+5)*2/6, (15+5)*2/4) # More complex math expression
multiply(5.0, 10.0) # Straight floats as arguments
