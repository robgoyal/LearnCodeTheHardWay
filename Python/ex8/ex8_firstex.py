#!/bin/python2
# Printing, Printing

# Initialize the formatter variable to format 4 values into strings
formatter = "%r %r %r %r"

# Prints "1 2 3 4" with the formatter variable
print formatter % (1, 2, 3, 4)
# Prints "one two three four" with the formatter variable
print formatter % ("one", "two", "three", "four")
# Prints "True False False True" with the formatter variable
print formatter % (True, False, False, True)
# Prints the formatter variable 4 times
print formatter % (formatter, formatter, formatter, formatter)
# Prints the following lines with the formatter variable
print formatter % (
        "I had this thing.",
        "That you could type up right.",
        "But it didn't sing.",
        "So I said goodnight."
        )
