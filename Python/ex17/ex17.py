#!/usr/bin/env/python

# More Files
# Code written by Robin Goyal
# Created on July 7, 2016
# Last updated on July 7, 2016

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# We could do these two on one line, how?

in_file = open(from_file)
indata = in_file.read()

# The oneliner for the above two is
# indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Allright, all done."

out_file.close()
in_file.close()
