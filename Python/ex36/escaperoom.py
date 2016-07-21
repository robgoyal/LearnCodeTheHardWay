#!/usr/bin/env/python

# Designing and Debugging
# Code written by Robin Goyal
# Created on July 14, 2016
# Last updated on July 14, 2016

# Module to include the functions for the decisions and generating the combination

from time import sleep
from random import randint

# Used docstring to print messages to the console


def Light(binaryCombo):
    print """
    You pick up the flashlight and look at it to realize that it is a UV light. In the process
    of looking at it you accidentally flash it at the wall and you see a weird order of 0's and 1's.
    The numbers read
    """

    print binaryCombo + "\n" + "You look at it for a big longer but realize that's all you can do with the flashlight."
    sleep(1)

# Return statement to exit the function and continue on with the code in the main file
    return

def Chest(lockCombo):
    print """
    You study the chest and see that it has a number combination lock.
    Would you like to try a possible combination?
    """
# winner message saved for code readability within while loop
    winner = "THE CHEST OPENED! You take the key and test to see if it opens the door. The door swings open and you escape the room fleeing for your life. CONGRATULATIONS. YOU WIN."

# loop infinitely to ask to enter a number to test the lock

    while(True):
        combination = int(raw_input("Enter a number to test the lock: \n> "))
        if combination == int(lockCombo):
            sleep(1)
            print "Calculating"
            sleep(1)
            print winner
            exit(0)

        else:
            print "That wasn't the correct number. Would you like to \n1. Guess another number? \n2. Try a different object?"
            nextMove = int(raw_input("> "))
            if nextMove == 1:
                continue
            elif nextMove == 2:
                sleep(2)
                return
            else:
                print "That wasn't an option.\nYOU DIE!."
                exit(0)

def Key():
    print """
    You pick up the key and quickly try to unlock the door at the end of the room.
    Unfortunately it does not open.
    """
    sleep(1)
    return


def Book():
    print """
    You pick up the book and blow off the dust. The title reads
    'Binary Numbers for DUMMIES'
    You spend a lot of time reading the book and are now able to understand binary numbers.
    """
    sleep(1)
    return

def combo_gen():
    combo = ""
    binCombo = ""

# Generate a random number and convert to binary
    for i in range(5):
        combo += str(randint(1, 10))

    for j in combo:
        binCombo += "{0:b}".format(int(j)) + "\n"

    return combo, binCombo
