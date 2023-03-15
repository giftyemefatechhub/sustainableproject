import unittest
from game import Game


class TestGame(unittest.TestCase):
    """A class for testing the Game class."""

    def test_game_init(self):
        """Test the initialization of Game object with various numbers
        of players."""
        game = Game(1)
        self.assertIsInstance(game.computer, Intelligent)
        self.assertIsInstance(game.player, Player)

        # Test for two player game initialization
        game = Game(2)
        self.assertIsInstance(game.player1, Player)
        self.assertIsInstance(game.player2, Player)

        # Test for invalid number of players
        with self.assertRaises(ValueError):
            game = Game(3)

    def test_choose_player(self):
        """Test the choose_player method for both single and two 
        player games."""
        game = Game(1)
        # Manually set computer and player scores to test win condition
        game.computer.computer_score = 100
        game.player.player_score = 50
        self.assertEqual(game.choose_player(), "Computer")

        # Test for two player game
        game = Game(2)
        # Manually set player1 and player2 scores to test win condition
        game.player1.player_score = 100
        game.player2.player_score = 80
        self.assertEqual(game.choose_player(), "Player 1")


if __name__ == '__main__':
    unittest.main()
