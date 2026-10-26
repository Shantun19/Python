
import random


WORDS = [
    "rainbow",
    "computer",
    "science",
    "programming",
    "python",
    "mathematics",
    "player",
    "condition",
    "reverse",
    "water",
    "board",
    "geeks",
]

MAX_ATTEMPTS = 12


def choose_word():
    """Return a random word from the word list."""
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    """Return the word with unguessed letters hidden."""
    result = []

    for letter in word:
        if letter in guessed_letters:
            result.append(letter)
        else:
            result.append("_")

    return " ".join(result)


def get_valid_guess(guessed_letters):
    """Ask for a valid letter that has not been guessed."""
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        return guess


def play_game():
    """Run one complete round of the game."""
    secret_word = choose_word()
    guessed_letters = set()
    attempts_left = MAX_ATTEMPTS

    print("\nLet's play the Word Guessing Game!")

    while attempts_left > 0:
        print("\nWord:", display_word(secret_word, guessed_letters))
        print("Attempts left:", attempts_left)

        # Check whether every letter has been guessed.
        if all(letter in guessed_letters for letter in secret_word):
            print("\nYou win! 🎉")
            print("The word was:", secret_word)
            return

        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct! Good guess.")
        else:
            attempts_left -= 1
            print("Wrong guess!")

    print("\nGame over!")
    print("The word was:", secret_word)


def main():
    """Start the application."""
    name = input("What is your name? ").strip()

    if not name:
        name = "Player"

    print(f"\nGood luck, {name}!")

    play_game()


if __name__ == "__main__":
    main()
