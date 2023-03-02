from random import Random, randint
from computer import Computer
from player import Player



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

game = Game()
game.choose_player