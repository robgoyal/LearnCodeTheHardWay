#!/usr/bin/env/python

# Designing and Debugging
# Code written by Robin Goyal
# Created on July 14, 2016
# Last updated on July 14, 2016

# An escape room style game

# Import escaperoom module functions

from escaperoom import Light, Chest, Key, Book, combo_gen
from time import sleep

# Initialize items, moves and combo values
items = ["Light", "Chest", "Key", "Book"]
moves = 0
lockCombo, binCombo = combo_gen()

print """
Welcome HUMAN! After a night of frivolous partying and unwise decisions, you
found yourself in my clutches. This is not a game but a matter of life or death. It
was bad luck for you to have fallen in my grasp but now its time to play. You are in
my famous escape room. If you'd like to leave, you must succesfully escape the room
within 5 moves.
GOODLUCK!
"""
print "You look around and see some items lying around."

def new_decision():
    global moves
    moves += 1

    if moves == 5:
        print "You have run out of moves. YOU LOSE.\nAND DIE!"
        exit(0)

    print "What item do you choose to look at? \n"

    for i in items: print i
    print

    initial_decision = raw_input("> ")
    sleep(2)

# Decision structure
# Recursive function call to ask what the next move is after finishing another move
    if initial_decision == items[0]:
        Light(binCombo)
        new_decision()
    elif initial_decision == items[1]:
        Chest(lockCombo)
        new_decision()
    elif initial_decision == items[2]:
        Key()
        new_decision()
    elif initial_decision == items[3]:
        Book()
        new_decision()
    else:
        print "That was not one of the options. As a result of not following my options.\nYOU HAVE DIED."
        sleep(2)
        exit(0)

new_decision()
