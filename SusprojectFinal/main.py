from random import randint


class Game:
    """
    Represents a game of Pig
    """

    def __init__(self):
        """
        Initializes a new game of Pig
        """
        self.computer = Computer("Computer")
        self.player = Player("Player")

    def choose_player(self):
        """
        Chooses which player goes first based on a random number
        """
        rng = randint(1, 10)
        if rng < 6:
            print("Computer goes first")
            while (self.computer.computer_score < 100 and
                   self.player.player_score < 100):
                self.computer.round()
                self.player.round()
            if self.computer.computer_score >= 100:
                print("Computer wins!")
                return
            else:
                print("You win!")
                return
        else:
            print("Player goes first.")
            while (self.computer.computer_score < 100 and
                   self.player.player_score < 100):
                self.player.round()
                self.computer.round()
            if self.computer.computer_score >= 100:
                print("Computer wins!")
                return
            else:
                print("You win!")
                return


class Die:
    """
    Represents a single die that can be rolled
    """

    def __init__(self):
        """
        Initializes a new die with a random value between 1 and 6
        """
        self.value = randint(1, 6)

    def __str__(self):
        """
        Returns a string representation of the die's value
        """
        return f"{self.value}"


class Computer:
    """
    Represents the computer player in a game of Pig
    """

    def __init__(self, name):
        """
        Initializes a new computer player with the given name
        """
        self.name = name
        self.round_score = 0
        self.computer_score = 0

    def __str__(self):
        """
        Returns a string representation of the computer player's name
        """
        return f"{self.name}"

    def round(self):
        """
        Plays a round of the game for the computer player
        """
        if self.round_score < 20:
            roll = Die().value
            print("Computer rolls ", roll)
            if roll != 1:
                self.round_score += roll
                print("Round score is ", self.round_score)
                self.round()
                self.round_score = 0
            else:
                print("You pigged it!")
                self.round_score = 0
                self.computer_score += self.round_score
                print("Computer's total score is ", self.computer_score)
        else:
            print("Computer holds")
            self.computer_score += self.round_score
            print("Computer's total score is", self.computer_score)
            self.round_score = 0


class Player:
    """
    Represents the human player in a game of Pig
    """

    def __init__(self, name):
        """
        Initializes a new human player with the given name
        """
        self.name = name
        self.round_score = 0
        self.player_score = 0

    def __str__(self):
        """
        Returns a string representation of the human player's name
        """
        return f"{self.name}"

    def round(self):
        """
        Plays a round of the game for the human player
        """
        choice = "roll"
        while choice != "hold":
            choice = input("Do you want to roll or hold?")
            if choice == "hold":
                break
            roll = Die().value
            print("You rolled", roll)
            if roll != 1:
                self.round_score += roll
                print("Your score for this round is ", self.round_score)
            else:
                print("You pigged it!")
                self.round_score = 0
                break
        self.player_score += self.round_score
        print("Your toatal score is ", self.player_score)
        self.round_score = 0


game = Game()
game.choose_player