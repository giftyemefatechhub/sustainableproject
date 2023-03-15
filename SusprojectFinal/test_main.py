import unittest
from random import randint


from game import Game
from main import Computer
from main import Die
from player import Player


class TestPigGame(unittest.TestCase):
    """
    Unit tests for Pig game
    """

    def test_game(self):
        """
        Test Game class
        """
        game = Game()
        self.assertIsInstance(game.computer, Computer)
        self.assertIsInstance(game.player, Player)

    def test_die(self):
        """
        Test Die class
        """
        die = Die()
        self.assertGreaterEqual(die.value, 1)
        self.assertLessEqual(die.value, 6)

    def test_computer(self):
        """
        Test Computer class
        """
        computer = Computer("Computer")
        self.assertEqual(computer.name, "Computer")
        self.assertEqual(computer.round_score, 0)
        self.assertEqual(computer.computer_score, 0)

    def test_player(self):
        """
        Test Player class
        """
        player = Player("Player")
        self.assertEqual(player.name, "Player")
        self.assertEqual(player.round_score, 0)
        self.assertEqual(player.player_score, 0)

    def test_choose_player(self):
        """
        Test choose_player method of Game class
        """
        game = Game()
        self.assertIsNone(game.choose_player())

    def test_computer_round(self):
        """
        Test round method of Computer class
        """
        computer = Computer("Computer")
        computer.round_score = 0
        computer.computer_score = 0
        for i in range(100):
            computer.round()
            if computer.computer_score >= 100:
                break
        self.assertGreaterEqual(computer.computer_score, 0)

    def test_player_round(self):
        """
        Test round method of Player class
        """
        player = Player("Player")
        player.round_score = 0
        player.player_score = 0
        for i in range(100):
            player.round()
            if player.player_score >= 100:
                break
        self.assertGreaterEqual(player.player_score, 0)


if __name__ == '__main__':
    unittest.main()
