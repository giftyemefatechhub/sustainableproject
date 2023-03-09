from random import randint


class Die:
    """
    A class representing a six-sided die.

    Attributes:
    - value (int): the current value of the die, between 1 and 6.
    """

    def __init__(self):
        """Create a new Die instance with a random value between 1 and 6."""
        self.value = randint(1, 6)

    def __str__(self):
        """Return the string representation of the current value of the die."""
        return f"{self.value}"
