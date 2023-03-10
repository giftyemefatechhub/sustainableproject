from random import randint
from die import Die


class Player:
    """
    A class representing the player of the game.

     Attributes:
    - name: a string representing the player's name.
    - round_score: an integer representing the player's score for the current round.
    - player_score: an integer representing the player's total score.
    """

    def __init__(self, name):
        """
        Initialize a player object with a name and scores.

        Args:
        - name: a string representing the player's name.
        """
        self.name = name
        self.round_score = 0
        self.player_score = 0

    def __str__(self):
        """Return a player object as a string."""
        return f"{self.name}"

    def round(self):
        """Goes through a round, player rolls or hold the dice. Score updates."""
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
