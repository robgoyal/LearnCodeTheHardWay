#!/usr/bin/env/python

# ex42.py
# Code written by Robin Goyal
# Created on 08-08-2016
# Last updated on 08-08-2016

# Class Animal is an object
class Animal(object):
    pass

# Class Dog is an Animal
class Dog(Animal):

# Class Dog has an init that takes self and name as parameters
    def __init__(self, name):
        self.name = name

# Class Cat is an Animal
class Cat(Animal):

# Class Cat has an init that takes self and name as parameters
    def __init__(self, name):
        self.name = name

# Class Person is an object
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
    pass

# Class Salmon is a Fish
class Salmon(Fish):
    pass

# CLass Halibut is a Fish
class Halibut(Fish):
    pass

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
flipper = Fish()

# Set crouse to an instance of Salmon
crouse = Salmon()

# Set harry to an instance of Halibut
harry = Halibut()
