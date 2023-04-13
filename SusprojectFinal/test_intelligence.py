import unittest
from dice import Dice
from intelligence import Intelligent


class TestIntelligent(unittest.TestCase):
    """Tests for the Intelligent class"""

    def setUp(self):
        """Set up a new instance of Intelligent before each test method"""
        self.intelligent = Intelligent("Computer")

    def test_init(self):
        """Test that the Intelligent instance is initialized correctly"""
        self.assertEqual(self.intelligent.name, "Computer")
        self.assertEqual(self.intelligent.round_score, 0)
        self.assertEqual(self.intelligent.computer_score, 0)
        self.assertIn(self.intelligent.difficulty_level, [1, 2, 3])

    def test_str(self):
        """Test the string representation of the Intelligent instance"""
        self.assertEqual(str(self.intelligent), "Computer")

    def test_round_easy(self):
        """Test the round method for easy difficulty level"""
        self.intelligent.difficulty_level = 1
        self.intelligent.round_score = 9
        Dice.value = 2
        self.intelligent.round()
        self.assertEqual(self.intelligent.round_score, 2)
        self.assertEqual(self.intelligent.computer_score, 0)

    def test_round_easy_pig(self):
        """Test the round method for easy difficulty level when a pig is rolled"""
        self.intelligent.difficulty_level = 1
        self.intelligent.round_score = 9
        Dice.value = 1
        self.intelligent.round()
        self.assertEqual(self.intelligent.round_score, 0)
        self.assertGreater(self.intelligent.computer_score, 0)

    def test_round_medium(self):
        """Test the round method for medium difficulty level"""
        self.intelligent.difficulty_level = 2
        self.intelligent.round_score = 14
        Dice.value = 3
        self.intelligent.round()
        self.assertEqual(self.intelligent.round_score, 3)
        self.assertEqual(self.intelligent.computer_score, 0)

    def test_round_medium_pig(self):
        """Test the round method for medium difficulty level when a pig is rolled"""
        self.intelligent.difficulty_level = 2
        self.intelligent.round_score = 14
        Dice.value = 1
        self.intelligent.round()
        self.assertEqual(self.intelligent.round_score, 0)
        self.assertGreater(self.intelligent.computer_score, 0)

    def test_round_hard(self):
        """Test the round method for hard difficulty level"""
        self.intelligent.difficulty_level = 3
        self.intelligent.round_score = 24
        Dice.value = 4
        self.intelligent.round()
        self.assertEqual(self.intelligent.round_score, 4)
        self.assertEqual(self.intelligent.computer_score, 0)

    def test_round_hard_pig(self):
        """Test the round method for hard difficulty level when a pig is rolled"""
        self.intelligent.difficulty_level = 3
        self.intelligent.round_score = 24
        Dice.value = 1
        self.intelligent.round()
        self.assertEqual(self.intelligent.round_score, 0)
        self.assertGreater(self.intelligent.computer_score, 0)


if __name__ == '__main__':
    unittest.main()
