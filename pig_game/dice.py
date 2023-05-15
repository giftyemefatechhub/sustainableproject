from random import randint


class Dice:
    """A class representing a dice."""

    def __init__(self):
        """Initialize a Dice object with a random value between 1 and 6."""
        self.value = randint(1, 6)

    def __str__(self):
        """Return the string representation of the Dice object."""
        return str(self.value)
