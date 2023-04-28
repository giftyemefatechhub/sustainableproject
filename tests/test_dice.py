from random import seed
"""

Importing seef from random

"""
import pytest
from dice import Dice

# Set a seed for deterministic results in the test
seed(42)


def test_dice_value():
    """
    Test the value attribute of a Dice object.

    The value attribute of a Dice object should be within the valid range of 1 to 6.
    """
    # Create a Dice object
    dice = Dice()

    # Ensure the value is within the valid range
    assert dice.value >= 1 and dice.value <= 6


def test_dice_string_representation():
    """
    Test the string representation of a Dice object.

    The string representation of a Dice object should match the expected value.
    """
    # Create a Dice object with a specific value
    dice = Dice()
    dice.value = 4

    # Check the string representation of the Dice object
    assert str(dice) == "4"
