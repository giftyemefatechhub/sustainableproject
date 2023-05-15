# Pig Dice Game

This repository contains the implementation of the Pig Dice Game in Python. The game allows players to roll dice and accumulate points while avoiding rolling a 1, which results in losing all points for the current round.

## Requirements

- Python 3.x

## How to Play

1. Clone the repository:

```shell[
git clone https://github.com/giftyemefatechhub/sustainableproject/tree/main

## Navigate to the project directory:
cd pig-dice-game

## Run the game:
python game.py

Follow the prompts to play the game. Each player takes turns rolling the dice and choosing whether to continue rolling or hold their current score.

The first player to reach a score of 100 or more wins the game.
Features
Interactive gameplay with computer-controlled opponents.
Three difficulty levels for computer opponents: Easy, Medium, and Hard.
Highscore tracking to keep record of players' scores.
Cheat code to double the dice roll value (for testing purposes).

# Files
game.py: Main script to start and run the game.
dice.py: Contains the Dice class for generating random dice rolls.
highscore.py: Contains the Highscore class for tracking and displaying high scores.
player.py: Contains the Player class representing a player in the game.
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please create a new issue or submit a pull request.


## How to test the Game

First, you need to install pytest. You can do this using pip, the Python package manager:
pip install pytest

Run the pytest command in the same directory:
pytest

You can also use various command-line options to customize the test run, such as -v to display verbose output or --cov to generate code coverage reports.



# License
This project is licensed under the MIT License. See the LICENSE file for details.
