from random import randint
from die import Die


class Player:
    def __init__(self, name):
        self.name = name
        self.roundScore = 0
        self.playerScore = 0
    
    def __str__(self):
        return f"{self.name}"
    
    def round(self):
        choice = "roll"
        while choice != "hold":
            choice = input("Do you want to roll or hold?")
            if choice == "hold":
                break
            roll = Die().value
            print("You rolled", roll)
            if roll != 1:
                self.roundScore += roll
                print("Your score for this round is ", self.roundScore)
            else:
                print("You pigged it!")
                self.roundScore = 0
                break
        self.playerScore += self.roundScore
        print("Your toatal score is ", self.playerScore)
        self.roundScore = 0