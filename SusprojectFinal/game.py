from random import randint
from intelligence import Intelligent
from player import Player


class Game:
    """
    A class that represents a game of Pig.

    Attributes:
        computer (Intelligent): The computer player in a single player game.
        player (Player): The human player in a single player game.
        player1 (Player): The first player in a two player game.
        player2 (Player): The second player in a two player game.
    """

    def __init__(self, number_of_players):
        """
        Initializes a Game object with the specified number of players.

        Args:
            number_of_players (int): The number of players in the game.

        Raises:
            ValueError: If the number of players is not 1 or 2.
        """
        if number_of_players == 1:
            self.computer = Intelligent("Computer")
            self.player = Player(input("Enter player name: "))
        elif number_of_players == 2:
            self.player1 = Player(input(f"Enter name of player 1: "))
            self.player2 = Player(input(f"Enter name of player 2: "))
            first_to_play = randint(1, 10)
            rounds = 1
            if first_to_play <= 5:
                print(f"{self.player1} goes first")
                print("\n")
                while (self.player1.player_score < 100 and
                       self.player2.player_score < 100):
                    print(f"ROUND {rounds}:")
                    print("-------")
                    if rounds >= 2:
                        print(f"{self.player1}'s turn")
                    self.player1.round()
                    if rounds >= 1:
                        print(f"{self.player2}'s turn")
                    self.player2.round()
                    print(".......................................................")
                    rounds += 1

                if self.player1.player_score >= 100:
                    print(f"{self.player1} wins!")
                    return
                else:
                    print(f"{self.player2} win!")
                    return
            else:
                print(f"{self.player2} goes first.")
                print("\n")
                while (self.player1.player_score < 100 and
                       self.player2.player_score < 100):
                    print(f"ROUND {rounds}:")
                    print("-------")
                    if rounds >= 2:
                        print(f"{self.player2}'s turn")
                    self.player2.round()
                    if rounds >= 1:
                        print(f"{self.player1}'s turn")
                    self.player1.round()
                    print(".................................................."
                          ".....")
                    rounds += 1
                if self.player2.player_score >= 100:
                    print(f"{self.player2} wins!")
                    return
                else:
                    print(f"{self.player1} win!")
                    return
        else:
            raise ValueError(
                """Invalid number of players. Game can be played by 1 or
                2 players. Try again!""")

    def choose_player(self):
        """
        Determines which player goes first and starts the game.

        Returns:
            None
        """
        first_to_play = randint(1, 10)
        rounds = 1
        if first_to_play <= 5:
            print("Computer goes first")
            print("\n")
            while (self.computer.computer_score < 100 and 
                   self.player.player_score < 100):
                print(f"ROUND {rounds}:")
                print("-------")
                if rounds >= 2:
                    print("Computer's turn")
                self.computer.round()
                if rounds >= 1:
                    print("Player's turn")
                self.player.round()
                print(".................................................."
                      ".....")
                rounds += 1
            if self.computer.computer_score >= 100:
                print("Computer wins!")
                return
            else:
                print(f"{self.player} win!")
                return


game = Game(int(input("Enter number of players (1) or (2): ")))
game.choose_player()
