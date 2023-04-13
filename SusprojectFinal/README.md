
# Pig Game

A brief description of what this project does and who it's for

This is a Pig Game and it is a school projet. The Game has the following rules:

Pig is a simple dice game first described in print by John Scarne in 1945.[1] Players take turns to roll a single dice as many times as they wish, adding all roll results to a running total, but losing their gained score for the turn if they roll a 1.

As with many games of folk origin, Pig is played with many rule variations, including the use of two dice instead of one. Commercial variants of two-dice Pig include Pass the Pigs, Pig Dice,[2] and Skunk.[3] Pig is commonly used by mathematics teachers to teach probability concepts.

Pig is one of a family of dice games described by Reiner Knizia as "jeopardy dice games", where the dominant type of decision is whether or not to jeopardize previous gains by rolling for potential greater gains.[4]

Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold":

If the player rolls a 1, they score nothing and it becomes the next player's turn.
If the player rolls any other number, it is added to their turn total and the player's turn continues.
If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.
The first player to score 100 or more points wins.

For example, the first player, Donald, begins a turn with a roll of 5. Donald could hold and score 5 points, but chooses to roll again. Donald rolls a 2, and could hold with a turn total of 7 points, but chooses to roll again. Donald rolls a 1, and must end his turn without scoring. The next player, Alexis, rolls the sequence 4-5-3-5-6, after which she chooses to hold, and adds her turn total of 23 points to her score.

Info from: https://en.wikipedia.org/wiki/Pig_(dice_game)

## Authors

- [@giftyemefatechhub](https://github.com/giftyemefatechhub)

- [@slundy123456](https://github.com/slundy123456)

- [@sonejoel560](https://github.com/sonejoel560)



## Documentation

[Documentation](https://linktodocumentation)


## Environment Variables

To run this project, you will need to add the following environment variables to your .venv file

# Variables
PROJECT_NAME = SusprojectFinal
PYTHON_FILES = *.py
OUTPUT_FORMAT = png


## License

[MIT](https://github.com/giftyemefatechhub/sustainableproject/blob/main/LICENSE.md)


## Tech Stack

**Client:** Python




## Running Tests

To run tests, run the following command


  python -m pip install pytest -cov
  python -pytest test_filename.py


## Creating HTML for coverage

python -m pytest --cov- report html --cov .


## Requirements

# Code analysis

#cohesion
flake8
flake8-docstrings

#metrics.pylint
pylint


# Code style
black

# Documentation
pdoc3


# Unit test and coverage
pytest -cov

    