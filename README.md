# Number Guessing Game

This Python script implements a simple number guessing game. The computer generates a random number between 1 and 10, and the player has three attempts to guess the number.

## How to Run

1.  **Ensure Python is Installed:** Make sure you have Python 3 installed on your system.
2.  **Save the Script:** Save the provided code as a `.py` file (e.g., `guess_number.py`).
3.  **Run the Script:** Open your terminal or command prompt, navigate to the directory where you saved the file, and run the script using the command: `python guess_number.py`
4.  **Follow the Prompts:** The script will prompt you to enter a number between 1 and 10. Follow the on-screen instructions.

## Game Logic

* The script uses the `random` module to generate a random integer between 1 and 10 (inclusive).
* The player has three attempts to guess the generated number.
* After each guess, the script provides feedback:
    * If the guess is higher than the generated number, it prints "You guessed higher number try lower one".
    * If the guess is lower than the generated number, it prints "try higher value".
    * If the guess is correct, it prints "You won" and the game ends.
* If the player fails to guess the number within three attempts, the game ends without a win message.

## Code Explanation

```python
import random

# Generate a random number between 1 and 10
num = random.randint(1, 10)

# Loop for three guessing attempts
for i in range(3):
    # Get the player's guess
    guess = int(input("Enter number between 1&10 : "))

    # Check if the guess is correct, higher, or lower
    if guess > num:
        print("You guessed higher number try lower one")
    elif guess < num:
        print("try higher value")
    else:
        print("You won")
        break  # Exit the loop if the guess is correct
