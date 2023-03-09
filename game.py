from random import randint
from computer import Computer
from player import Player


class Game:
    def __init__(self, number_of_players):
        if number_of_players == 1:
            self.computer = Computer("Computer")
            self.player = Player(input("Enter player name:"))
        elif number_of_players == 2:
            self.player1 = Player(input(f"Enter name of player 1: "))
            self.player2 = Player(input(f"Enter name of player 1: "))
            first_to_play = randint(1, 10)
            if first_to_play <= 5:
                print(f"({self.player1} goes first)")
                while self.player1.playerScore < 100 and self.player2.playerScore < 100:
                    self.player1.round()
                    self.player2.round()
                
                if self.player1.playerScore >= 100:
                    print(f"{self.player1} wins!")
                    return
                else:
                    print(f"{self.player2} win!")
                    return
            else:
                print(f"{self.player2} goes first.")
                while self.player1.playerScore < 100 and self.player2.playerScore < 100:
                    self.player2.round()
                    self.player1.round()
                if self.player2.playerScore >= 100:
                    print(f"{self.player2} wins!")
                    return
                else:
                    print(f"{self.player1} win!")
                    return
        else:
            raise ValueError("Invalid number of players. Game can be played by 1 or 2 players. Try again!")

    
    def choose_player(self):
        first_to_play = randint(1, 10)
        rounds = 1
        if first_to_play <= 5:
            print("Computer goes first")
            while self.computer.computerScore < 100 and self.player.playerScore < 100:
                print(f"ROUND {rounds}")
                print("---------------")
                if rounds >= 2:
                    print("Computer's turn")
                self.computer.round()
                if rounds >= 1:
                    print("Player's turn")
                self.player.round()
                rounds += 1
            if self.computer.computerScore >= 100:
                print("Computer wins!")
                return
            else:
                print(f"{self.player} win!")
                return
        else:
            rounds = 1
            print(f"{self.player} goes first.")
            while self.computer.computerScore < 100 and self.player.playerScore < 100:
                print(f"ROUND {rounds}")
                print("---------------")
                if rounds >= 2:
                    print(f"Player's turn")
                self.player.round()
                if rounds >= 1:
                    print(f"Computer's turn")
                self.computer.round()
                rounds += 1
            if self.computer.computerScore >= 100:
                print("Computer wins!")
                return
            else:
                print(f"{self.player} win!")
                return

game = Game(int(input("Enter number of players (1) or (2): ")))
game.choose_player()