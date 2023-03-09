from random import random, randint
from die import Die



class Computer:
    """Represents a computer player in a game of Pig.

    Attributes:
        name (str): The name of the computer player.
        round_score (int): The score accumulated by the computer player during the current round.
        computer_score (int): The total score accumulated by the computer player across all rounds.
    """

    def __init__(self, name):
        """Initializes a new instance of the Computer class.

        Args:
            name (str): The name of the computer player.
        """
        self.name = name
        self.round_score = 0
        self.comp_score = 0

    def __str__(self):
        """Returns a string representation of the computer player."""
        return f"{self.name}"

    def round(self):
        """Executes a round of play for the computer player.
        The computer player will roll the die and accumulate points until either a 1 is rolled or the round score reaches 20. If a 1 is rolled, the round score is reset to 0 and the turn ends. Otherwise, the round score is accumulated and the computer player rolls again. If the round score reaches 20, the computer player will hold and the accumulated points will be added to
        the total score for the player. Does not return anything.
        """
        if self.round_score < 20:
            roll = Die().value
            print("Computer rolls ", roll)
            if roll != 1:
                self.round_score += roll
                print("Round score is ", self.round_score)
                self.round()
                self.round_score = 0
            else:
                print("You pigged it!")
                self.round_score = 0
                self.comp_score += self.round_score
                print("Computer's total score is ", self.comp_score)
        else:
            print("Computer holds")
            self.comp_score += self.round_score
            print("Computer's total score is", self.comp_score)
            self.round_score = 0
