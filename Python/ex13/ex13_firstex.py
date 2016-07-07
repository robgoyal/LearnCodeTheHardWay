#!/bin/python2

# Parameters, Unpacking, Variables
# A program to take two numbers as arguments and multiply them

# Not writing enough arguments provides an error which says
# It requires more variables to unpack

from sys import argv

script, var1, var2,  principal, rate, compound_period, time = argv

# the int function performs type conversion
print int(var1) * int(var2)


# Calculating accrued amount of compound interest

accrued_amt = float(principal)*(1 + float(rate)/100/float(compound_period))**(float(time)*float(compound_period))
print accrued_amt
