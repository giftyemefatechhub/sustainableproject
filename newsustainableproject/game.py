from random import Random, randint
from computer import Computer
from player import Player


class Game:
    """
    A class representing a game of dice between a player and a computer.

    Attributes:
    - computer (Computer): the computer player.
    - player (Player): the human player.
    """

    def __init__(self):
        """Create a new Game instance with a computer and a player."""
        self.computer = Computer("Computer")
        self.player = Player("Player")

    def choose_player(self):
        """
        Choose a player to go first randomly.

        Simulate the game by running rounds between the computer and player
        until one of them reaches
        a score of 100 or more. Print the winner.
        """
        rng = randint(1, 10)
        if rng < 6:
            print("Computer goes first")
            while (self.computer.comp_score < 100 and self.player.player_score < 100):
                self.computer.round()
                self.player.round()
            if self.computer.comp_score >= 100:
                print("Computer wins!")
            else:
                print("You win!")
        else:
            print("Player goes first.")
            while self.computer.comp_score < 100 and self.player.player_score < 100:
                self.player.round()
                self.computer.round()
            if self.computer.comp_score >= 100:
                print("Computer wins!")
            else:
                print("You win!")


game = Game()
game.choose_player()
