from dice import Dice
from highscore import Highscore


class Player:
    def __init__(self, name):
        self.name = name
        self.round_score = 0
        self.player_score = 0
        self.highscore = Highscore()


    def __str__(self):
        return f"{self.name}"

    def round(self):
        choice = input("Type (r) to roll: ")
        while choice != "h":
            '''
            Cheat code
            '''
            if choice == "roll":
                roll = Dice().value * 2
            else:
                roll = Dice().value
            print(f"{self.name} rolled {roll}")
            if roll != 1:
                self.round_score += roll
                choice = input("Would you like to roll again (r) or hold (h)? ")
            else:
                print(f"{self.name} rolled a 1 and pigged this round!")
                self.round_score = 0
                break
            if choice == "h":
                break
        print(f"{self.name}'s scored {self.round_score} for this round")
        self.player_score += self.round_score
        print(f"{self.name}'s total score: {self.player_score}")
        self.round_score = 0

    def rename(self):
        new_name = input(f"{self.name} would you like to change your name? (y/n) ")
        if new_name.lower() == "y":
            old_name = self.name
            self.name = input("Enter new name: ")
            print(f"{old_name} changed name to {self.name}")
        else:
            print("Name remain unchanged")
