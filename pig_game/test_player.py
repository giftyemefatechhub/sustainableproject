import pytest
from unittest.mock import patch
# from dice import Dice
# from highscore import Highscore
from player import Player


class TestPlayer:
    """Test case for the Player class."""

    def setup_method(self, method):
        """Set up the test case."""
        self.player = Player("Player")

    def teardown_method(self, method):
        """Tear down the test case."""
        self.player = None

    def test_str(self):
        """Test the __str__ method."""
        expected_output = "Player"
        assert str(self.player) == expected_output

    @patch("builtins.input", side_effect=["r", "h"])
    def test_round(self, mock_input):
        """Test the round method."""
      

    @patch("builtins.input", side_effect=["y", "New Name"])
    def test_rename(self, mock_input):
        """Test the rename method.""" 
