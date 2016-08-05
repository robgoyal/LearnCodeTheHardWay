#!/usr/bin/env/python

# ex38.py
# Code written by Robin Goyal
# Created on 28-07-2016
# Last updated on 28-07-2016

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ') # same as split(ten_things, ' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# more_stuff.pop() says call pop on more_stuff
# whereas pop(more_stuff) calls pop with the argument more_stuff
# Similar to the other function calls
while len(stuff) != 10:
    next_one = more_stuff.pop() # pop(more_stuff)
    print "Adding: ", next_one
    stuff.append(next_one) # append(stuff, next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop() # pop(stuff)
print ' '.join(stuff)
print '#'.join(stuff[3:5])

