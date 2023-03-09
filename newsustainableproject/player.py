from random import randint
from die import Die


class Player:
    def __init__(self, name):
        self.name = name
        self.round_score = 0
        self.player_score = 0
    
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
                self.round_score += roll
                print("Your score for this round is ", self.round_score)
            else:
                print("You pigged it!")
                self.round_score = 0
                break
        self.player_score += self.round_score
        print("Your toatal score is ", self.player_score)
        self.round_score = 0