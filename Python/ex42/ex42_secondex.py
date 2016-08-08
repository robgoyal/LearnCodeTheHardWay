#!/usr/bin/env/python

# ex42.py
# Code written by Robin Goyal
# Created on 08-08-2016
# Last updated on 08-08-2016

# Class Animal is an object
class Animal(object):
    def __init__(self):
        self.name = 'Animal'


# Class Dog is an Animal
class Dog(Animal):

# Class Dog has an init that takes self and name as parameters
    def __init__(self, name):
        self.name = name

    def action(self):
        print "The dog barks"

# Class Cat is an Animal
class Cat(Animal):

# Class Cat has an init that takes self and name as parameters
    def __init__(self, name):
        self.name = name

    def action(self):
        print "The cat meows"
# Class Person is anobject
class Person(object):

# Class Person has an init that takes self and name as parameters
    def __init__(self, name):
        self.name = name

        self.pet = None

# CLass Employee is a Person
class Employee(Person):

# Class Employee has an init that takes self, name and salary as parameters
    def __init__(self, name, salary):

# Init function
        super(Employee, self).__init__(name)

# Set the salary attribute to salary
        self.salary = salary

# Class Fish is an object
class Fish(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

# Class Salmon is a Fish
class Salmon(Fish):
    def __init__(self, name, species, color):
        super(Salmon, self).__init__(name, species)
        self.name = name

    def color(self):
        return self.color

# CLass Halibut is a Fish
class Halibut(Fish):
    def __init__(self, name, species, color):
        super(Halibut, self).__init__(name, species)
        self.color = color

    def color(self):
        return self.color

# Set rover to an instance of Dog
rover = Dog("Rover")

# Set satan to an instance of Cat
satan = Cat("Satan")

# Set mary to an instance of Person
mary = Person("Mary")

# Set frank to an instance of Employee
frank = Employee("Frank", 120000)

# From frank, get the pet attribute and set it to rover
frank.pet = rover

# Set flipper to an instance of Fish
flipper = Fish("flipper", "Fish")

# Set crouse to an instance of Salmon
crouse = Salmon("flipper", "Fish", "pink")

# Set harry to an instance of Halibut
harry = Halibut("flipper", "Fish", "black")
