#!/usr/bin/env/python

# Functions and Variables
# Code written by Robin Goyal
# Created on July 7, 2016
# Last updated on July 7, 2016

# function cheese and crackers accepts arguments cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Series of print lines
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
# Calling the function with numbers
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
# Initializing amount_of_cheese to 10
amount_of_cheese = 10
# Initializing amount_of_crackers to 50
amount_of_crackers = 50
# Calling the function with variable names
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
# Calling the function with math expressions in the arguments
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
# Calling the function with math expressions in the arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


