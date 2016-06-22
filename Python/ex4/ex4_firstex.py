#!/bin/python2

# Variables and Names

# initializing cars to 100
cars = 100
# initializing space_in_a_car to 4.0
# The variable does not need to be 4.0. The following
# expressions do not require this variable to a floating point number
space_in_a_car = 4.0
# initializing drivers to 30
drivers = 30
# initializing passengers to 90
passengers = 90
# calculating the number of cars not driven and storing in a variable
cars_not_driven = cars - drivers
# initializing the number of cars driven to the number of drivers
cars_driven = drivers
# calculate the carpool capacity and storing in a variable
carpool_capacity = cars_driven * space_in_a_car
# calculating the average number of passengers per car and storing in a variable
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car"
