#!/usr/bin/env/python

# Else and If
# Code written by Robin Goyal
# Created on July 9, 2016
# Last updated on July 9, 2016

# Elif could be expanded as else if
# Elif is used when the first if statement in the block isnt true
# Else runs if all the other if/elif statements are not true

# Initializing the number of people, cars and truck
people = 30
cars = 40
trucks = 15

# If the number of cars is greater than the number of people, print the line
# "We should take the cars."
if cars > people:
    print "We should take the cars."

# Otherwise if the number of cars is less than the number of people,
# print "We should not take the cars."
elif cars < people:
    print "We should not take the cars."

# If the other ones are not true, then just print
# "We can't decide."
else:
    print "We can't decide."

# If the number of trucks is greater than the number of cars
# print the line "That's too many trucks."
if trucks > cars:
    print "That's too many trucks."

# Otherwise if the number of trucks is less than the number of cars
# print "Maybe we could take the trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."

# If the other ones are not true, then print
# We still can't decide
else:
    print "We still can't decide."

# If the number of people is less than the number of trucks
# print the line "Allright, let's just take the trucks."
if people > trucks:
    print "Allright, let's just take the trucks."

# Otherwise print the line "Fine, let's stay home then."
else:
    print "Fine, let's stay home then."
