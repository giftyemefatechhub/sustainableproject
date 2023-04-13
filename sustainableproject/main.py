from random import Random, randint

class Game:
    def __init__(self):
        self.computer = Computer("Computer")
        self.player = Player("Player")
    
    def choose_player(self):
        rng = randint(1, 10)
        if rng < 6:
            print("Computer goes first")
            while self.computer.computerScore < 100 and self.player.playerScore < 100:
                self.computer.round()
                self.player.round()
            if self.computer.computerScore >= 100:
                print("Computer wins!")
                return
            else:
                print("You win!")
                return
        else:
            print("Player goes first.")
            while self.computer.computerScore < 100 and self.player.playerScore < 100:
                self.player.round()
                self.computer.round()
            if self.computer.computerScore >= 100:
                print("Computer wins!")
                return
            else:
                print("You win!")
                return

class Die:
    def __init__(self):
        self.value = randint(1,6)

    def __str__(self):
        return f"{self.value}"

class Computer:
    def __init__(self, name):
        self.name = name
        self.roundScore = 0
        self.computerScore = 0
    
    def __str__(self):
        return f"{self.name}"
    
    def round(self):
        if self.roundScore < 20:
            roll = Die().value
            print("Computer rolls ", roll)
            if roll != 1:
                self.round_score += roll
                print("Round score is ", self.roundScore)
                self.round()
                self.roundScore = 0
            else:
                print("You pigged it!")
                self.roundScore = 0
                self.computerScore += self.roundScore
                print("Computer's total score is ", self.computerScore)
        else:
            print("Computer holds")
            self.computerScore += self.roundScore
            print("Computer's total score is", self.computerScore)
            self.roundScore = 0

class Player:
    def __init__(self, name):
        self.name = name
        self.roundScore = 0
        self.playerScore = 0
    
    def __str__(self):
        return f"{self.name}"
    
    def round(self):
        choice = "roll"
        while choice != "hold":
            choice = input("Do you want to roll or hold?")
            if choice == "hold":
                break
            roll = Die().value
            print("You rolled", roll)
            if roll != 1:
                self.roundScore += roll
                print("Your score for this round is ", self.roundScore)
            else:
                print("You pigged it!")
                self.roundScore = 0
                break
        self.playerScore += self.roundScore
        print("Your toatal score is ", self.playerScore)
        self.roundScore = 0


game = Game()
game.choose_player