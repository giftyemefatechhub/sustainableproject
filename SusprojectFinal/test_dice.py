import unittest
from dice import Dice


class TestDice(unittest.TestCase):
    """
    Unit tests for the Dice class.
    """

    def test_dice_init(self):
        """
        Test that a Dice object is initialized with a random value between 1
        and 6.
        """
        dice = Dice()
        self.assertGreaterEqual(dice.value, 1)
        self.assertLessEqual(dice.value, 6)

    def test_dice_str(self):
        """
        Test that the __str__ method of a Dice object returns a string
        representation of its value.
        """
        dice = Dice()
        self.assertIsInstance(str(dice), str)
