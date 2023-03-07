import unittest
from io import StringIO
from unittest.mock import patch
from player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Mary")
        self.inputs = []
        self.patcher = patch("builtins.input", side_effect=self.get_input)
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def get_input(self, prompt):
        return self.inputs.pop(0)

    def set_input(self, inputs):
        self.inputs = inputs

    def test_init(self):
        self.assertEqual(self.player.name, "Mary")
        self.assertEqual(self.player.playerScore, 0)
        self.assertEqual(self.player.roundScore, 0)

    def test_hold(self):
        self.set_input(["roll", "hold"])
        self.player.round()
        self.assertEqual(self.player.roundScore, 0)
        self.assertGreater(self.player.playerScore, 0)

    def test_roll(self):
        self.set_input(["roll", "2", "roll", "1", "hold"])
        self.player.round()
        self.assertGreaterEqual(self.player.roundScore, 0)
        self.assertGreaterEqual(self.player.playerScore, 0)

    def test_round(self):
        self.set_input(["roll", "roll", "1"])
        self.player.round()
        self.assertEqual(self.player.playerScore, 0)
        self.assertEqual(self.player.roundScore, 0)
        
#from random import randint
#from die import Die


#class Player:
#    def __init__(self, name):
#        self.name = name
#        self.roundScore = 0
#        self.playerScore = 0
    
#    def __str__(self):
#        return f"{self.name}"
    
#    def round(self):
#        choice = "roll"
#        while choice != "hold":
#            choice = input("Do you want to roll or hold?")
#            if choice == "hold":
#                break
#            roll = Die().value
#            print("You rolled", roll)
#            if roll != 1:
#                self.roundScore += roll
#                print("Your score for this round is ", self.roundScore)
#            else:
#                print("You pigged it!")
#                self.roundScore = 0
#                break
#        self.playerScore += self.roundScore
#        print("Your toatal score is ", self.playerScore)
#        self.roundScore = 0

if __name__ == '__main__':
    unittest.main()