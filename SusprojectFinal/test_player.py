import unittest
from unittest.mock import patch
from dice import Dice
from player import Player


class TestPlayer(unittest.TestCase):
    """
    Unit tests for the Player class.
    """

    def setUp(self):
        """
        Set up a Player object for testing.
        """
        self.player = Player("John")

    def test_player_init(self):
        """
        Test that a Player object is initialized correctly.
        """
        self.assertEqual(self.player.name, "John")
        self.assertEqual(self.player.round_score, 0)
        self.assertEqual(self.player.player_score, 0)

    @patch('builtins.input', side_effect=["r", "h"])
    def test_player_round(self, mock_input):
        """
        Test the round method of the Player class.
        """
        Dice.value = 3
        self.player.round()
        self.assertEqual(self.player.round_score, 3)
        self.assertEqual(self.player.player_score, 3)
        # Roll a 1
        Dice.value = 1
        self.player.round()
        self.assertEqual(self.player.round_score, 0)
        self.assertEqual(self.player.player_score, 3)


if __name__ == '__main__':
    unittest.main()
