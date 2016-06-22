#!/bin/python2
# Strings And Text

# Initialize x to "There are 10 types of people" with string formatter
x = "There are %d types of people." % 10
# Initializing binary to "binary"
binary = "binary"
# Initializing do_not to "don't"
do_not = "don't"
# Initializing y to "Those who know binary and those who don't" with string formatters
y = "Those who know %s and those who %s." % (binary, do_not)

# Print "There are 10 types of people"
print x
# Print "Those who know binary and those who don't"
print y

# Print "I said: There are 10 types of people" with %r string formatter
print "I said: %r." % x
# Print "I also said: "Those who know binary and those who don't""
print "I also said: '%s'." % y

# Initialize hilarious to False
hilarious = False
# Initialize joke_evaluation to "Isn't that joke so funny?! False" with string formatter
joke_evaluation = "Isn't that joke so funny?! %r"

# Print joke_evaluation with the string formatter
print joke_evaluation % hilarious

# Initialize w with "This is the left side of ..."
w = "This is the left side of ... "
# Initialize e with "a string with a right side."
e = "a string with a right side."

# Prints the concactenation of the two strings
print w + e
