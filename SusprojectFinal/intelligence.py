from dice import Dice


class Intelligent:
    """
    This class represents an intelligent computer player that can play a game
    of Pig Dice.
    """

    def __init__(self, name):
        """
        Initializes an instance of the Intelligent class.

        Args:
            name (str): The name of the computer player.
        """
        self.name = name
        self.round_score = 0
        self.computer_score = 0
        self.difficulty_level = int(
            input("Choose Game Mode (1 for Easy, 2 for Medium, 3 for Hard): "))

    def __str__(self):
        """
        Returns the name of the computer player as a string.

        Returns:
            str: The name of the computer player.
        """
        return f"{self.name}"

    def round(self):
        """
        Simulates a round of Pig Dice for the computer player based on their
        chosen difficulty level.
        """
        if self.difficulty_level == 1:
            if self.round_score < 10:
                roll = Dice().value
                print(f"Computer rolls {roll}")
                if roll != 1:
                    self.round_score += roll
                    self.round()
                    self.round_score = 0
                else:
                    print("Computer rolled 1 and pigged this round!")
                    self.round_score = 0
                    print(f"Computer scored {self.round_score} for this round")
                    self.computer_score += self.round_score
                    print(f"Computer's total score: {self.computer_score}")
            elif self.round_score >= 10:
                print("Computer holds")
                remainder = 10 - self.round_score
                self.round_score = self.round_score + remainder
                print(f"Computer scored {self.round_score} for this round")
                self.computer_score += self.round_score
                print(f"Computer's total: {self.computer_score}")
                self.round_score = 0
        elif self.difficulty_level == 2:
            if self.round_score < 15:
                roll = Dice().value
                print(f"Computer rolls {roll}")
                if roll != 1:
                    self.round_score += roll
                    self.round()
                    self.round_score = 0
                else:
                    print("Computer rolled 1 and pigged this round!")
                    self.round_score = 0
                    print(f"Computer scored {self.round_score} for this round")
                    self.computer_score += self.round_score
                    print(f"Computer's total score: {self.computer_score}")
            elif self.round_score >= 15:
                print("Computer holds")
                remainder = 15 - self.round_score
                self.round_score = self.round_score + remainder
                print(f"Computer scored {self.round_score} for this round")
                self.computer_score += self.round_score
                print(f"Computer's total: {self.computer_score}")
                self.round_score = 0
        elif self.difficulty_level == 3:
            if self.round_score < 25:
                roll = Dice().value
                print(f"Computer rolls {roll}")
                if roll != 1:
                    self.round_score += roll
                    self.round()
                    self.round_score = 0
                else:
                    print("Computer rolled 1 and pigged this round!")
                    self.round_score = 0
                    print(f"Computer scored {self.round_score} for this round")
                    self.computer_score += self.round_score
                    print(f"Computer's total score: {self.computer_score}")
            elif self.round_score >= 25:
                print("Computer holds")
                remainder = 25 - self.round_score
                self.round_score = self.round_score + remainder
                print(f"Computer scored {self.round_score} for this round")
                self.computer_score += self.round_score
                print(f"Computer's total: {self.computer_score}")
                self.round_score = 0
