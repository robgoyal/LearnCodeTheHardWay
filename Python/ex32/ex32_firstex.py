#!/usr/bin/env/python

# Loops and Lists
# Code written by Robin Goyal
# Created on July 9, 2016
# Last updated on July 9, 2016

# Answers to the STUDY DRILLS

# The range function can go through a list of integers with a step in between
# elements = range(0,6) would perform the same function than interating through a for loop
# Many operations besides append are available for lists
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop that goes through a list

for number in the_count:
    print "This is count %d" % number

# same as above

for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it

for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one

elements = []

# then use the range function to do 0 to 5 counts

for i in range(0, 6):
    print "Adding %d to the list." % i

    # append is a function that lists understand

    elements.append(i)

# now we can print them out too

for i in elements:
    print "Element was: %d" % i
