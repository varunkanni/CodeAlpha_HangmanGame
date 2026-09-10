"""
Hangman Game
------------
A simple text-based Hangman game.

Concepts used: random, while loop, if-else, strings, lists.
"""

import random

# A small predefined list of words to choose from
WORD_LIST = ["python", "hangman", "computer", "elephant", "guitar"]

MAX_INCORRECT_GUESSES = 6

HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """,
]


def choose_word(word_list):
    """Randomly select a word from the list."""
    return random.choice(word_list).lower()


def display_word(word, guessed_letters):
    """
    Return a string showing guessed letters in their correct positions
    and underscores for letters not yet guessed.
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word(WORD_LIST)
    guessed_letters = []      # letters the player has guessed (correct or not)
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters. Try to guess it one letter at a time.")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print(HANGMAN_STAGES[incorrect_guesses])
        print("Word: " + display_word(word, guessed_letters))
        print(f"Incorrect guesses remaining: {MAX_INCORRECT_GUESSES - incorrect_guesses}")
        if guessed_letters:
            print("Guessed letters: " + ", ".join(sorted(guessed_letters)))

        guess = input("Guess a letter: ").lower().strip()

        # --- Input validation ---
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.\n")
            continue

        guessed_letters.append(guess)

        # --- Check the guess ---
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
            # Check if the player has now guessed the entire word
            if all(letter in guessed_letters for letter in word):
                print(HANGMAN_STAGES[incorrect_guesses])
                print(f"Congratulations! You guessed the word: {word}")
                print("You win!")
                return
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")

    # If the loop exits, the player has run out of guesses
    print(HANGMAN_STAGES[incorrect_guesses])
    print(f"Game over! You've run out of guesses. The word was: {word}")


def main():
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
        print()
    print("Thanks for playing Hangman!")


if __name__ == "__main__":
    main()
