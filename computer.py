from random import random, randint
from die import Die


class Computer:
    def __init__(self, name):
        self.name = name
        self.roundScore = 0
        self.computerScore = 0
    
    def __str__(self):
        return f"{self.name}"
    
    def round(self):
        if self.roundScore < 20:
            roll = Die().value
            print("Computer rolls ", roll)
            if roll != 1:
                self.round_score += roll
                print("Round score is ", self.roundScore)
                self.round()
                self.roundScore = 0
            else:
                print("You pigged it!")
                self.roundScore = 0
                self.computerScore += self.roundScore
                print("Computer's total score is ", self.computerScore)
        else:
            print("Computer holds")
            self.computerScore += self.roundScore
            print("Computer's total score is", self.computerScore)
            self.roundScore = 0