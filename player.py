from random import randint
from dice import Dice


class Player:
    def __init__(self, name):
        self.name = name
        self.roundScore = 0
        self.playerScore = 0
    
    def __str__(self):
        return f"{self.name}"
    
    def round(self):
        choice = input("Type (r) to roll: ")
        while choice != "h":
            if choice == "h":
                break
            roll = Dice().value
            print(f"{self.name} rolled {roll}")
            if roll != 1:
                self.roundScore += roll
                choice = input("Would you like to roll again (r) or hold (h)? ")
            else:
                print(f"{self.name} rolled a 1 and pigged this round!")
                self.roundScore = 0
                break
        print(f"{self.name}'s scored {self.roundScore} for this round")
        self.playerScore += self.roundScore
        print(f"{self.name}'s total score: {self.playerScore}")
        self.roundScore = 0
        print("Computer's turn")