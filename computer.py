from dice import Dice


class Computer:
    def __init__(self, name):
        self.name = name
        self.roundScore = 0
        self.computerScore = 0
    
    def __str__(self):
        return f"{self.name}"
    
    def round(self):
        if self.roundScore < 20:
            roll = Dice().value
            print(f"Computer rolls {roll}")
            if roll != 1:
                self.roundScore += roll
                self.round()
                self.roundScore = 0
            else:
                print("Computer rolled 1 and pigged this round!")
                self.roundScore = 0
                print(f"Computer scored {self.roundScore} for this round")
                self.computerScore += self.roundScore
                print(f"Computer's total score: {self.computerScore}")
        else:
            print("Computer holds")
            print(f"Computer scored {self.roundScore} for this round")
            self.computerScore += self.roundScore
            print(f"Computer's total: {self.computerScore}")
            self.roundScore = 0
