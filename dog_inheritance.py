# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:15:45 2020

@author: frumkina

Description: This is just for practice.
"""

# Parent class
class Dog:

    # Class attribute
    species = 'mammal'
    speed = '13 mph'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
    

# Child class (inherits from Dog class)
class Beagle(Dog):
    
    # Class attribute
    speed = '12 mph'
    
    # instance method
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
    
# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    
#    speed = '20 mph'
    
    # instance method
    def run(self):
        return "{} runs {}".format(self.name, self.speed)


# Child class (inherits from Dog class)
class Bulldog(Dog):
    
    # instance method
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
    
    
Daphne = Beagle("Daphne",14)
print(Daphne)
print(Daphne.species)
print(Daphne.name)
print(Daphne.age)
print(Daphne.description())
print(Daphne.speak("snore"))
print(Daphne.run("14 mph"))

Jack = RussellTerrier("Jack", 3)
print(Jack.run())