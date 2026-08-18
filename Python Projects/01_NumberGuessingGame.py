"""
Number Guessing Game

A simple command-line number guessing game.

The program:
1. Asks the user to define a number range.
2. Randomly selects a number within that range.
3. Gives the player a fixed number of attempts to guess it.
4. Provides hints after every incorrect guess.
5. Displays the result when the player wins or runs out of attempts.

"""

import random


# Number of attempts the player gets to guess the number.
MAX_ATTEMPTS = 7


def get_number(prompt):
    """
    Ask the user for an integer and keep asking until valid input is given.
    Args:
        prompt (str): The message displayed to the user.
    Returns:
        int: The integer entered by the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_range():
    """
    Get a valid lower and upper bound from the user.
    The lower bound must be smaller than or equal to the upper bound.
    Returns:
        tuple[int, int]: A tuple containing the lower and upper bounds.
    """
    while True:
        lower_bound = get_number("Enter the lower bound: ")
        upper_bound = get_number("Enter the upper bound: ")

        if lower_bound >= upper_bound:
            print( "Invalid range. The lower bound must be ""smaller than the upper bound.")
            continue

        return lower_bound, upper_bound


def start_guess_game():
    """
    Start and manage a complete number guessing game.
    The user chooses a range, and the program randomly selects
    a number within that range. The player then gets a fixed
    number of attempts to guess the number.
    """
    print("\n" + "=" * 50)
    print("Welcome to the Number Guessing Game!")
    print("=" * 50)

    # Get the range selected by the player.
    lower_bound, upper_bound = get_range()

    # Generate a random number within the selected range.
    target_number = random.randint(lower_bound, upper_bound)

    print(f"\nI have selected a number between "f"{lower_bound} and {upper_bound}.")
    print(f"You have {MAX_ATTEMPTS} attempts to guess it.")
    print("Good luck!\n")

    # Keep track of how many guesses the player has made.
    for attempt in range(1, MAX_ATTEMPTS + 1):
        remaining_attempts = MAX_ATTEMPTS - attempt
        guess = get_number(f"Attempt {attempt}/{MAX_ATTEMPTS} - Enter your guess: ")
        # Check whether the player guessed the correct number.
        if guess == target_number:
            print(f"\nCorrect! The number was {target_number}."f"\nYou guessed it in {attempt} attempt(s).")
            return

        # Provide a hint based on the player's guess.
        if guess > target_number:
            print("Too high! Try a lower number.")
        else:
            print("Too low! Try a higher number.")

        # Tell the player how many attempts remain.
        if remaining_attempts > 0:
            print(f"Attempts remaining: {remaining_attempts}\n")

    # This section runs when the player uses all attempts.
    print(f"\nSorry! You have used all {MAX_ATTEMPTS} attempts."f"\nThe correct number was {target_number}.""\nBetter luck next time!")


def main():
    """
    Run the main program.
    The user can choose whether to start the game.
    """
    print("Hi! Welcome to the Number Guessing Game.")
    print(f"You will have {MAX_ATTEMPTS} chances to guess the number.")

    while True:
        choice = input("\nDo you want to play the game? (Y/N): ").strip().lower()
        if choice == "y":
            start_guess_game()
            break
        if choice == "n":
            print("Thank you for playing! See you next time.")
            break
        print("Invalid choice. Please enter Y or N.")


# Run the program only when this file is executed directly.
if __name__ == "__main__":
    main()
