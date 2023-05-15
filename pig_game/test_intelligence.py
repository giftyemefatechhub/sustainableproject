from dice import Dice
from intelligent import Intelligent


def test_round_difficulty_level_1():
    """Test the round method for difficulty level 1."""
    intelligent = Intelligent("Computer Player")
    intelligent.difficulty_level = 1
    intelligent.round_score = 0
    intelligent.computer_score = 0
    intelligent.round()
    # Add assertions here to check if the expected conditions are met


def test_round_difficulty_level_2():
    """Test the round method for difficulty level 2."""
    intelligent = Intelligent("Computer Player")
    intelligent.difficulty_level = 2
    intelligent.round_score = 0
    intelligent.computer_score = 0
    intelligent.round()



def test_round_difficulty_level_3():
    """Test the round method for difficulty level 3."""
    intelligent = Intelligent("Computer Player")
    intelligent.difficulty_level = 3
    intelligent.round_score = 0
    intelligent.computer_score = 0
    intelligent.round()


def test_str():
    """Test the str method."""
    intelligent = Intelligent("Computer Player")
    expected_output = "Computer Player"
    assert str(intelligent) == expected_output
