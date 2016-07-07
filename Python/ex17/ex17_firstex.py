#!/usr/bin/env/python

# More Files
# Code written by Robin Goyal
# Created on July 7, 2016
# Last updated on July 7, 2016

# Attempt to make the script as short and concise as possible
from sys import argv

script, from_file, to_file = argv

print "We are going to transfer content from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)
print "Allright, all done."
out_file.close()
in_file.close()
