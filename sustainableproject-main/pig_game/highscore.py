class Highscore:
    """Class representing the highscore board."""

    def __init__(self):
        """Initialize the highscore board."""
        self.players = {}
        self.games_played = 0

    def update_score(self, player, score):
        """
        Update the player's score in the highscore board.

        Args:
            player (Player): The player.
            score (int): The player's score.
        """
        if player.name not in self.players:
            self.players[player.name] = {
                "games_played": 0,
                "games_won": 0,
                "high_score": 0,
                "win_percentage": 0
            }
        self.players[player.name]["games_played"] += 1
        self.games_played += 1
        if score > self.players[player.name]["high_score"]:
            self.players[player.name]["high_score"] = score

    def won_game(self, player):
        """
        Update the number of games won and win percentage for the player.

        Args:
            player (Player): The player who won the game.
        """
        self.players[player.name]["games_won"] += 1
        self.players[player.name]["win_percentage"] = (
           self.players[player.name]["games_won"] / self.players[player.name]["games_played"]) * 100

    def show_highscore(self):
        """Display the highscore board."""
        print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "Player", "Games Played", "Games Won", "High Score", 
            "Win Percentage"))
        for player, stats in self.players.items():
            print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(
                player, stats["games_played"], stats["games_won"], 
                stats["high_score"], str(stats["win_percentage"]) + "%"))
