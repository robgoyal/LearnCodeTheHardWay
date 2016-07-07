#!/usr/bin/env/python

# Reading Files
# Code written by Robin Goyal
# Created on July 7, 2016
# Last updated on July 7, 2016

# Using raw_input instead of using argv

filename = raw_input("Type the filename: \n> ")
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

