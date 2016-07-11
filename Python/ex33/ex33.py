#!/usr/bin/env/python

# While Loops
# Code written by Robin Goyal
# Created on July 9, 2016
# Last updated on July 9, 2016

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d \n" % i

print "The numbers: "

for num in numbers:
    print num
