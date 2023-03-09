import unittest
from unittest.mock import patch
from io import StringIO
from computer import Computer
from die import Die




class TestComputer(unittest.TestCase):
    """
    A test suite for the Computer class.
    """

    def setUp(self):
        """
        Method to setup a computer object for testing.
        """
        self.computer = Computer("Computer")

    def test_round(self):
        """
        A test method to check if the computer object correctly behaves in
        different scenarios.

        Scenario 1: When the computer rolls a 1 on the first roll.
        Scenario 2: When the computer rolls a number other than 1 and stops at
        20.
        Scenario 3: When the computer rolls a number other than 1 and keeps
        rolling.

        The method uses the patch function to mock the Die class and the
        StringIO class to capture the console output.
        It then uses assert statements to check if the output and the object's
        state match the expected values.
        """

        # Test case where the computer rolls 1 on the first roll
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.computer.round_score = 10
            Die.value = 1
            self.computer.round()
            self.assertEqual(self.computer.round_score, 0)
            self.assertEqual(self.computer.comp_score, 0)
            self.assertIn("You pigged it!", fake_output.getvalue())

        # Test case where the computer rolls a number other than 1 and stops at 20
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.computer.round_score = 10
            Die.value = 3
            self.computer.round()
            self.assertEqual(self.computer.round_score, 0)
            self.assertGreater(self.computer.comp_score, 0)
            self.assertIn("Computer holds", fake_output.getvalue())

        # Test case where the computer rolls a number other than 1 and keeps rolling
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.computer.round_score = 10
            Die.value = 3
            self.computer.round()
            self.assertEqual(self.computer.round_score, 0)
            self.assertGreater(self.computer.comp_score, 0)
            self.assertIn("Computer rolls", fake_output.getvalue())


if __name__ == '__main__':
    unittest.main()
