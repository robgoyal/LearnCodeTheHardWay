#!/usr/bin/env/python

# What If
# Code written by Robin Goyal
# Created on July 9, 2016
# Last updated on July 9, 2016

# ANSWERS TO STUDY DRILL QUESTIONS

# The if statement evaluates the condition and if its true, it'll run the code within the if block
# The code is indented so the interpreter knows the code that is in the if-block
# If it isn't indented, that code will not run under the if-block

people = 25
cats = 15
dogs = 10

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."

if not(True and False):
    print "This is False"

if True or False:
    print "This is True"

if not(False):
    print "This is also True"


