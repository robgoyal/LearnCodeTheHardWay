#!/usr/bin/env/python

# Functions and Files
# Code written by Robin Goyal
# Created on July 8, 2016
# Last updated on July 8, 2016

# Imports the argv function from the sys module
from sys import argv
# Script and input file arguments are store in argv
script, input_file = argv

# Function used to print all the lines of the file
def print_all(f):
    print f.read()

# Redirects the pointer to the beginning of the file
def rewind(f):
    f.seek(0)

# Prints a single line at a time
def print_a_line(line_count, f):
    print line_count, f.readline()

# Opens the input file and stores into current_file
current_file = open(input_file)

# Invoking the print_all function
print "First let's print the whole file: \n"
print_all(current_file)

# Invoking the rewind function
print "Now let's rewind, kind of like a tape."
rewind(current_file)

# Print command
print "Let's print three lines: "

# Creates the current_line counter
current_line = 1
# Invoking the print_a_line function and prints the first line of current_file
print_a_line(current_line, current_file)

# Increments the counter by 1
current_line = current_line + 1
# Invoking the print_a_line function and prints the second line of current_file
print_a_line(current_line, current_file)

# Increments the counter by 1
current_line = current_line + 1
# Invoking the print_a_line function and prints the third line of current_file
print_a_line(current_line, current_file)

