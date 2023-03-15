from dice import Dice


class Player:
    """
    Class representing a player in a dice game.

    Attributes:
        name (str): The name of the player.
        round_score (int): The player's score for the current round.
        player_score (int): The player's total score across all rounds.
    """

    def __init__(self, name):
        """
        Initializes a new player object.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.round_score = 0
        self.player_score = 0

    def __str__(self):
        """
        Returns a string representation of the player.

        Returns:
            str: The player's name.
        """
        return f"{self.name}"

    def round(self):
        """
        Simulates a round of dice rolling for the player.

        The player is prompted to roll the dice until they either choose to
        hold or roll a 1. The player's round
        score is updated based on the sum of their rolls, and their total
        score is updated at the end of the
        round based on their round score.

        Returns:
            None
        """
        choice = input("Type (r) to roll: ")
        while choice != "h":
            roll = Dice().value
            print(f"{self.name} rolled {roll}")
            if roll != 1:
                self.round_score += roll
                choice = input(
                    "Would you like to roll again (r) or hold (h)? ")
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
