# Hangman

This is a simple command-line implementation of the classic Hangman game in Python. The player needs to guess letters to reveal a hidden word before they run out of lives.
Features

    Selects a random word from a list of fruits.
    The player has a limited number of attempts (lives) to guess the word.
    Tracks the player's guesses and provides feedback if the letter is correct or not.
    The game ends when the player correctly guesses all letters or runs out of lives.

How to Play

    The program randomly selects a word from a predefined list of fruits.
    The player must guess one letter at a time.
    Correct guesses will reveal the letter in the word, while incorrect guesses will decrease the player's lives.
    The game ends when:
        The player correctly guesses all the letters in the word (you win!).
        The player runs out of lives (you lose!).

Instructions

    Clone or download the project.
    Run the Python file in your terminal/command line:

    python hangman.py

    Follow the on-screen prompts to input your guesses.

Code Overview

    Hangman Class: Contains all the game logic, including:
        Selecting a random word.
        Checking guesses.
        Updating the word progress.
        Handling lives.
    Game Flow: The play_game function initializes a game and starts the loop for user input, checking if the player has won or lost after each guess.

Example Gameplay

Input a single letter: a
Great job, a is in the word!
Current progress: _a__e
Remaining unique letters to guess: 3

Input a single letter: p
Great job, p is in the word!
Current progress: pa__e
Remaining unique letters to guess: 2

...

You won! The word was "peach".

Dependencies

    Python 3.x

License

This project is open-source and available under the MIT License.