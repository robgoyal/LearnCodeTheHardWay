#!/usr/bin/env/python

# More Practice
# Code written by Robin Goyal
# Created on July 9, 2016
# Last updated on July 9, 2016

# Print "Let's practice everything."
print "Let's practice everything."
# Print statement which uses the escape charcter, newline character and tab
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs'

# Multi line string using """
# Tabs, newline characters also used
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
# Print dashed lines
print "------------"
# Prints the poem variable
print poem
# Print dashed lines
print "------------"

# Assigning the mathematical expression on the right to five
five = 10 - 2 + 3 - 6
# Prints the string and variable five using the string formatting character %s
print "This should be five: %s" % five

# Crates a function which takes one input argument
def secret_formula(started):
# Assigns the input argument multiplied by 500 into jelly beans
    jelly_beans = started * 500
# Assigns the number of jelly_beans divided by 1000 into jars
    jars = jelly_beans / 1000
# Assigns the number of jars divided by 100 into crates
    crates = jars / 100
# Returns the number of jelly beans, jars and crates
    return jelly_beans, jars, crates

# Initializes the variable 10000 into start_point
start_point = 10000
# Passed the argument start_point into secret_formula and stores the returned
# variables into beans, jars, and crates
beans, jars, crates = secret_formula(start_point)

# Prints the line using decimal string formatter %d
print "With a starting point of: %d" % start_point
# Prints the number of beans, jars, and crates using the decimal string formatter
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# Divides the start_point by 10
start_point = start_point / 10
# Prints the line "We can also do that this way:"
print "We can also do that this way:"
# Another way to return the values from the secret_formula function
# A better way since we don't have to waste memory space with more variables
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

