#!/usr/bin/env/python

# While Loops
# Code written by Robin Goyal
# Created on July 9, 2016
# Last updated on July 9, 2016

elements = int(raw_input("How many elements would you like in your list?: "))
increment = int(raw_input("What do you want to increment the number by?: "))

def list_creator(inp, increase):
    i = 0
    numbers = []

    for j in range(elements):
        print "At the top i is %d" % i
        numbers.append(i)
        i += increase
        print "Numbers now: ", numbers
        print "At the bottom is is %d" % i

    print "The numbers are: "

    for num in numbers:
        print num

list_creator(elements, increment)
