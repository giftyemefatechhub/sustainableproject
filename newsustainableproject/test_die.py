import unittest
from random import randint
from unittest.mock import patch
from die import Die


class TestDie(unittest.TestCase):
    @patch('die.randint', return_value=6)
    def test_die(self, mock_randint):
        die = Die()
        self.assertEqual(str(die),"6")



if __name__ == '__main__':
    unittest.main()