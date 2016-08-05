#!/usr/bin/env/python

# ex37.py
# Code written by Robin Goyal
# Created on 28-07-2016
# Last updated on 28-07-2016

# The purpose of this exercise was to use all the keywords in short programs but
# I'll only be using the keywords that I'm unsure of

## With as
with open("foo.txt") as f:
    data = f.read()

## Assert
assert type(5.0) is int, "5.0 is not an integer"

## Break
x = True
while x:
    break

## Finally
try:
    print 5/0
finally:
    print "ERROR"

## in
if 4 in range(0, 4):
    print "TRUE"

## lambda (square)
square = lambda x: x**2
print square(8)



