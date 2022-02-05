#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Example on a class rolling dices.

Start by importing the modules needed.

Then define the class with its class name.

    class Dice():

The class may have properties, also called membed variables. These are a
property of each object that is instantiated from this class. This member is
just a variable declaration which also can have a default value.

        faces = 6

The constructor is a method which is called when someone instantiates an object
of this class.

        def __init__(self):

The parameter `self` is a reference to the actual instantiated object and can
be used within the method to set/read values and call methods of the object.

            self.rolls_made = 0

A python object is mutable, that means you can add properties to it in runtime.
The properties does not need to be defined before they are added to the object.
So the above construct is showing how to add a property to the newly created
object.

Any method in the class should always define the `self` as the first parameter.
This is implicitly sent to the method by the Python interpreteter. You can
compare the code from the main program and see how its actually done.

    # main.py
    myDie.roll()

    # dice.py
    roll(myDie)


"""

import random


class Dice():
    """Example of dice class."""

    faces = 6

    def __init__(self):
        """Roll a dice once and return the value."""
        random.seed()
        self.rolls_made = 0

    def roll(self):
        """Roll a dice once and return the value."""
        self.rolls_made += 1
        return random.randint(1, self.faces)

    def get_rolls_made(self):
        """Get number of rolls made."""
        return self.rolls_made
