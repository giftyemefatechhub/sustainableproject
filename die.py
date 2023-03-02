from random import randint

class Die:
    def __init__(self):
        self.value = randint(1,6)

    def __str__(self):
        return f"{self.value}"
