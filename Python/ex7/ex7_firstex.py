#!/bin/python2
# More Printing

# Prints "Mary had a little lamb."
print "Mary had a little lamb."
# Prints "It's fleece was white as snow" with string formatter
print "Its fleece was white as %s." % 'snow'
# Prints "And everywhere that Mary went"
print "And everywhere that Mary went."
# Prints "." 10 times
print "." * 10 # what'd that do?

# Initializes the string "Cheeseburger" to 12 different variables by each character
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# what that comma at the end. try removing it to see what happens

# Prints cheeseburger using the 12 variables
# Removing the comma at the end wont place the variables on the same line
# Removing the comma will output:
# Cheese
# Burger

# Whereas not removing the comma will output
# Cheese Burger
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12


