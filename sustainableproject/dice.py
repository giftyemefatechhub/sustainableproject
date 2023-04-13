from random import randint


class Dice:
    def __init__(self):
        self.value = randint(1, 6)

    def __str__(self):
        return f"{self.value}"
