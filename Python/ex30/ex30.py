#!/usr/bin/env/python

# Else and If
# Code written by Robin Goyal
# Created on July 9, 2016
# Last updated on July 9, 2016

people = 30
cars = 40
trucks = 15

if cars > people:
    print "We should take the cars."

elif cars < people:
    print "We should not take the cars."

else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."

elif trucks < cars:
    print "Maybe we could take the trucks."

else:
    print "We still can't decide."

if people > trucks:
    print "Allright, let's just take the trucks."

else:
    print "Fine, let's stay home then."
