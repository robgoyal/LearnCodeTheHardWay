#!/usr/bin/env/python

# Reading and Writing Files
# Code written by Robin Goyal
# Created on July 7, 2016
# Last updated on July 7, 2016

from sys import argv

script, filename = argv

# Output the contents of the file

txt = open(filename)
print txt.read()

