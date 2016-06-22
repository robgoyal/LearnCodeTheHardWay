#!/bin/python2
# Printing, Printing, Printing

# Here's some new strange stuff, remember type it exactly.

# Initialize days to store "Mon Tue Wed Thu Fri Sat Sun"
days = "Mon Tue Wed Thu Fri Sat Sun"
# Initialize months to store "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
# The \n character is the new line character
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# Prints the line "Here are the days: Mon Tue Wed Thu Fri Sat Sun"
print "Here are the days: ", days
# Prints the line "Here are the months: Jan Feb Mar Apr May Jun Jul Aug" with
# a newline character in between each
print "Here are the months: ", months

# This will print the following lines exactly as shown and several lines can be
# printed with just one print command
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
