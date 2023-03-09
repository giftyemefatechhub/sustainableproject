import unittest
from unittest.mock import patch
from game import Game


class TestGame(unittest.TestCase):
    """A class for testing the Game class."""

    def setUp(self):
        """Set up a Game instance for testing."""
        self.game = Game()

    @patch('builtins.print')
    def test_choose_player(self, mock_print):
        """Test that the game ends when a player reaches a score of 100 or more
        and that
        either the computer or the player goes first."""
        self.game.player.player_score = 100
        self.game.choose_player()
        mock_print.assert_called_with('You win!')

        self.game.computer.computer_score = 100
        self.game.choose_player()
        mock_print.assert_called_with('Computer wins!')

        self.assertIn(mock_print.call_args_list[0][0][0], [
                      'Computer goes first', 'Player goes first'])
