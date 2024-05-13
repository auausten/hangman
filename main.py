import random
import time

words = []

file = open("words.txt", "r")
for line in file:
    clean_line = line.strip()
    words.append(clean_line)
file.close()

hangman_stages = [
    # Beginning Stage
    """
        +---+
        |   |
            |
            |
            |
            |
    ===========""",

    # Head Stage
    """
        +---+
        |   |
        O   |
            |
            |
            |
    ===========""",

    # Body Stage
    """
        +---+
        |   |
        O   |
        |   |
            |
            |
    ===========""",

    # Legs Stage
    """
        +---+
        |   |
        O   |
        |   |
        /\  |
            |
    ===========""",

    # Last Stage
    """
        +---+
        |   |
        O   |
       /|\  |
        /\  |
            |
    ==========="""
]

def display_stage(stage):
    print(hangman_stages[stage])

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def is_guess_correct(word, guess):
    return guess in word

def startup():
    word = random.choice(words).lower()
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 4

    while wrong_guesses < max_wrong_guesses:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed this")
            continue
        else:
            guessed_letters.append(guess)

        if is_guess_correct(word, guess):
            print(f"{guess} is in word")
            display_word(word, guessed_letters)
        else:
            wrong_guesses = wrong_guesses + 1
            print("Not in word.")
        
        display_stage(wrong_guesses)

        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You guessed the word:", word)
            break

        if wrong_guesses == max_wrong_guesses:
            print("You ran out of guesses. The word was:", word)

startup()