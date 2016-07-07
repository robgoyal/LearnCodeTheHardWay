#!/usr/bin/env/python

# Reading Files
# Code written by Robin Goyal
# Created on July 7, 2016
# Last updated on July 7, 2016

# Imports argv from sys
from sys import argv

# Stores the arguments into the variables script and filename
script, filename = argv
# Opens the file in the variable txt
txt = open(filename)

# Prints the filename
print "Here's your file %r:" % filename
# Outputs the text of the file
print txt.read()

# Asks to print the file name again
print "Type the filename again:"
file_again = raw_input("> ")

# Opens the file in the variable txt_again
txt_again = open(file_again)

# Outputs the text of the file again
print txt_again.read()

