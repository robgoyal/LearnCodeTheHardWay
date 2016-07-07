#!/usr/bin/env/python

# Reading Files
# Code written by Robin Goyal
# Created on July 7, 2016
# Last updated on July 7, 2016

from sys import argv

script, filename = argv
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

