import unittest
from random import randint 
from unittest.mock import patch
from dice import Dice

class TestDie(unittest.TestCase):
    @patch('die.randint', return_value=6)
    def test_die(self, mock_randint):
        die = Dice()
        self.assertEqual(str(die),"6")

#from random import randint

#class Die:
#    def __init__(self):
#        self.value = randint(1,6)

#    def __str__(self):
#        return f"{self.value}"

if __name__ == '__main__':
    unittest.main()