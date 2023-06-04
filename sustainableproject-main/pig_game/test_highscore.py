from highscore import Highscore
from player import Player


def test_update_score():
    """Test the update_score method."""
    highscore = Highscore()
    player = Player("Alice")
    highscore.update_score(player, 100)

    assert highscore.players[player.name]["games_played"] == 1
    assert highscore.games_played == 1
    assert highscore.players[player.name]["high_score"] == 100


def test_won_game():
    """Test the won_game method."""
    highscore = Highscore()
    player = Player("Bob")
    highscore.update_score(player, 0)
    highscore.won_game(player)

    assert highscore.players[player.name]["games_won"] == 1
    assert highscore.players[player.name]["win_percentage"] == 100.0


def test_show_highscore():
    """Test the show_highscore method."""
    highscore = Highscore()

    # Ensure the show_highscore method doesn't raise any exceptions
    highscore.show_highscore()
