#!/usr/bin/env/python

# Making Decisions
# Code written by Robin Goyal
# Created on July 9, 2016
# Last updated on July 9, 2016

# The Adventures of Harry Potter

print "\nWelcome to the WIZARDING WORLD!"
print """
As a curious wizard, you explore near Hogwarts and stumble upon a dark cave
which you hear has magical powers. You are afraid of entering a dark cave, so what do you do?
1. Explore the cave.
2. Go back to your comfy bed at Hogwarts.
"""

# Prompt to question if the user enters the cave or not

cave = raw_input("> ")

if cave == "1":
    print"You explore the cave further and hiding in the bushes was Lord Voldemort. He decides to fight you. What do you do?\n"

    print "1. You choose not to be a coward and fight him."
    print "2. You attempt to flee from Lord Voldemort.\n"

    # Decision point where the user questions whether he fights Lord Voldemort or not
    fight = raw_input("> ")

    if fight == "1":

        print "You and Voldemort both draw your wands in an attempt to fight him to fulfill the prophecy. \
        As a uber newb, you have the choice between two spells. Which spell do you choose?\n"
        print "1. Expelliarmus"
        print "2. Avada Kedavra\n"

        # Final decision point to choose what spell to use
        spell = raw_input("> ")

        if spell  == "1":
            print "Voldemort countered the childish spell and killed you. He then took over the world and became the ultimate ruler.\n"

        elif spell == "2":
            print "Voldemort stood dumbfounded from you using the MURDER spell and ultimately, THE PROPHECY HAS BEEN FULFILLED BY THE GREAT HARRY POTTER. \n"

    elif fight == "2":

        print "You dodge the multiple spells that Voldemort throws at you and succesfully escape from his clutches. Good job!"
        print "Now it's time to over to the Three Broomsticks for some Butterbeer.\n"

elif cave == "2":
    print "You made a wise choice, time to have some nice Butterbeer at the Three Broomsticks\n"

