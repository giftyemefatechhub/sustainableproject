from random import randint


class Dice:
    """
    A class representing a standard six-sided dice.
    """

    def __init__(self):
        """
        Initialize a Dice object with a random integer value between 1 and 6.
        """
        self.value = randint(1, 6)

    def __str__(self):
        """
        Return a string representation of the Dice object.
        """
        return f"{self.value}"
