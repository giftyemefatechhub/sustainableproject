from dice import Dice


class Intelligent:
    def __init__(self, name):
        self.name = name
        self.roundScore = 0
        self.computerScore = 0
        self.difficulty_level = int(input("Choose Game Mode (1 for Easy, 2 for Medium, 3 for Hard): "))
    
    def __str__(self):
        return f"{self.name}"
    
    def round(self):
        if self.difficulty_level == 1:
            if self.roundScore < 10:
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
            elif self.roundScore >= 10:
                print("Computer holds")
                remainder = 10 - self.roundScore
                self.roundScore = self.roundScore + remainder 
                print(f"Computer scored {self.roundScore} for this round")
                self.computerScore += self.roundScore
                print(f"Computer's total: {self.computerScore}")
                self.roundScore = 0
        elif self.difficulty_level == 2:
                if self.roundScore < 15:
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
                elif self.roundScore >= 15:
                    print("Computer holds")
                    remainder = 15 - self.roundScore
                    self.roundScore = self.roundScore + remainder 
                    print(f"Computer scored {self.roundScore} for this round")
                    self.computerScore += self.roundScore
                    print(f"Computer's total: {self.computerScore}")
                    self.roundScore = 0
        elif self.difficulty_level == 3:
                if self.roundScore < 25:
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
                elif self.roundScore >= 25:
                    print("Computer holds")
                    remainder = 25 - self.roundScore
                    self.roundScore = self.roundScore + remainder 
                    print(f"Computer scored {self.roundScore} for this round")
                    self.computerScore += self.roundScore
                    print(f"Computer's total: {self.computerScore}")
                    self.roundScore = 0
