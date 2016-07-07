#!/usr/bin/env/python

# Names, Variables, Code, Functions
# Code written by Robin Goyal
# Created on July 7, 2016
# Last updated on July 7, 2016

# this one is like your scripts with argv

def print_two (*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument

def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments

def print_none():
    print "I got nothing'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

