import sys
from random import randint
from player import Player
from intelligence import Intelligent
from highscore import Highscore


class Game:
    def __init__(self):
        self.rules()
        self.number_of_players = (int(input("Enter number of players (1) or (2): ")))
        self.highscore = Highscore()

    def rules(self):
        print(" ")
        print("Welcome to One Dice Pig game!")
        print("..............................")
        print("Goal: Players take turn rolling a dice and player becomes winner when score reaches 100")
        print(" ")
        print("Gameplay Rules:")
        print("1. Each round, a player repeatedly rolls dice until either a 1 is rolled or the player decides to hold")
        print("2. If the player rolls a 1, they score no points and their turn ends.")
        print("3. If the player rolls any other number, it is added to their turn total & the player can choose to roll again or hold.")
        print("4. If a player holds, their turn total is added to their total score, and it becomes the opponent's turn.")
        print("5. Play continues until one player reaches 100 points or more.")
        print("6. When a player reaches 100 points or more, the opponent gets one more turn to try to catch up.")
        print("7. The player with the highest score at the end of the game wins.")
        print(" ")

    def play(self):
        if self.number_of_players == 1:
            self.computer = Intelligent("Computer")
            self.player = Player(input("Enter player name: "))
            self.player_vs_computer()
        elif self.number_of_players == 2:
            self.player1 = Player(input("Enter name of player 1: "))
            self.player2 = Player(input("Enter name of player 2: "))
            self.player_vs_player()

    def restart(self):
        restart = input("Do you want to restart game (y/n)? ")
        if restart == "y":
            print(f"{self.player} Restarted game. {self.computer} automatically won previous hand")
            print(".......................................................")
            self.player.player_score = 0
            self.computer.computer_score = 0
            self.rounds = 0
            print("New Game Started...")
            self.player_vs_computer()
        else:
            quit = input("Do you want to quit game (y/n)? ")
            print(".......................................................")
            if quit == "y":
                print(f"{self.player} Forfeited. Computer wins!")
                print("Thanks for playing")
                sys.exit()

    def end_game_message(self):
        print("Thanks for playing")
        print("Game Ended!")

    def player_quit(self):
            if self.player1.player_score < 50:
                quit = input(f"{self.player1} do you want to quit game (y/n)? ")
                if quit == "y":
                    print(".......................................................")
                    print(f"{self.player1} Forfeited. {self.player2} automatically won!")
                    self.highscore.won_game(self.player2)
                    self.highscore.update_score(self.player1, self.player1.player_score)
                    self.highscore.update_score(self.player2, self.player2.player_score)
                    print(" ")
                    self.highscore.show_highscore()
                    self.end_game_message()
                    sys.exit()
            if self.player2.player_score < 50:
                quit = input(f"{self.player2} do you want to quit game (y/n)? ")
                if quit == "y":
                    print(".......................................................")
                    print(f"{self.player2} Forfeited. {self.player1} automatically won!")
                    self.highscore.won_game(self.player1)
                    self.highscore.update_score(self.player1, self.player1.player_score)
                    self.highscore.update_score(self.player2, self.player2.player_score)
                    print(" ")
                    self.highscore.show_highscore()
                    self.end_game_message()
                    sys.exit()

    def player_vs_computer(self):
        first_to_play = randint(1, 10)
        self.rounds = 0
        if first_to_play <= 5:
            print(" ")
            print("···> Computer goes first")
            while self.computer.computer_score < 100 and self.player.player_score < 100:
                self.rounds += 1
                print(" ")
                print(f"ROUND {self.rounds}:")
                print(" ")
                if self.rounds >= 2:
                    print("···> Computer's turn")
                self.computer.round()
                if self.rounds >= 1:
                    print(" ")
                    print("···> Player's turn")
                self.player.round()
                self.highscore.update_score(self.player, self.player.player_score)
                print(".......................................................")
                if self.player.player_score < 50 and self.rounds == 10:
                    self.restart()
            if self.computer.computer_score >= 100 and self.computer.computer_score > self.player.player_score:
                print("Computer wins!")
            elif self.player.player_score >= 100 and self.player.player_score > self.computer.computer_score:
                print(f"{self.player} wins!")
            elif self.computer.computer_score == self.player.player_score:
                print("It's a tie!")
        else:
            print(" ")
            print(f"···> {self.player} goes first.")
            while self.computer.computer_score < 100 and self.player.player_score < 100:
                self.rounds += 1
                print(" ")
                print(f"ROUND {self.rounds}:")
                print(" ")
                if self.rounds >= 2:
                    print("···> Player's turn")
                self.player.round()
                self.highscore.update_score(self.player, self.player.player_score)
                if self.rounds >= 1:
                    print(" ")
                    print("···> Computer's turn")
                self.computer.round()
                print(".......................................................")
                if self.player.player_score < 50 and self.rounds == 10:
                    self.restart()
            if self.player.player_score >= 100 and self.player.player_score > self.computer.computer_score:
                print(f"{self.player} wins!")
            elif self.computer.computer_score >= 100 and self.computer.computer_score > self.player.player_score:
                print("Computer wins!")
            elif self.player.player_score == self.computer.computer_score:
                print("It's a tie!")
        self.highscore.show_highscore()
        print(" ")
        self.player.rename()
        self.end_game_message()

    def player_vs_player(self):
        first_to_play = randint(1, 10)
        self.rounds = 0
        if first_to_play <= 5:
            print(" ")
            print(f"···> {self.player1} goes first")
            while self.player1.player_score < 100 and self.player2.player_score < 100:
                self.rounds += 1
                print(" ")
                print(f"ROUND {self.rounds}:")
                print(" ")
                if self.rounds >= 2:
                    print(f"···> {self.player1}'s turn")
                self.player1.round()
                self.highscore.update_score(self.player1, self.player1.player_score)
                if self.rounds >= 1:
                    print(" ")
                    print(f"···> {self.player2}'s turn")
                self.player2.round()
                self.highscore.update_score(self.player2, self.player2.player_score)
                print(".......................................................")
                if self.rounds == 5 and (self.player1.player_score < 50 or self.player2.player_score < 50):
                    self.player_quit()
            if self.player1.player_score >= 100 and self.player1.player_score > self.player2.player_score:
                print(f"{self.player1} wins!")
                self.highscore.won_game(self.player1)
                print(" ")
            elif self.player2.player_score >= 100 and self.player2.player_score > self.player1.player_score:
                print(f"{self.player2} wins!")
                self.highscore.won_game(self.player2)
                print(" ")
            elif self.player1.player_score == self.player2.player_score:
                print("It's a tie!")
                print(" ")

        else:
            print(" ")
            print(f"···> {self.player2} goes first.")
            while self.player1.player_score < 100 and self.player2.player_score < 100:
                self.rounds += 1
                print(" ")
                print(f"ROUND {self.rounds}:")
                print(" ")
                if self.rounds >= 2:
                    print(f"···> {self.player2}'s turn")
                self.player2.round()
                self.highscore.update_score(self.player2, self.player2.player_score)
                if self.rounds >= 1:
                    print(" ")
                    print(f"···> {self.player1}'s turn")
                self.player1.round()
                self.highscore.update_score(self.player1, self.player1.player_score)
                print(".......................................................")
                if self.rounds == 5 and (self.player1.player_score < 50 or self.player2.player_score < 50):
                    self.player_quit()
            if self.player2.player_score >= 100 and self.player2.player_score > self.player1.player_score:
                print(f"{self.player2} wins!")
                self.highscore.won_game(self.player2)
                print(" ")
            elif self.player1.player_score >= 100 and self.player1.player_score > self.player2.player_score:
                print(f"{self.player1} wins!")
                self.highscore.won_game(self.player1)
                print(" ")
            elif self.player2.player_score == self.player1.player_score:
                print("It's a tie!")    
                print(" ")
        self.highscore.show_highscore()
        print(" ")
        self.player1.rename()
        print(" ")
        self.player2.rename()
        print(" ")
        self.end_game_message()


game = Game()
game.play()
