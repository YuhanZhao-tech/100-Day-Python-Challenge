# Number guessing game
from random import randint

difficulty = {'easy': 10, 'hard': 5}

def compare(user_input, target) -> bool:
    """Compare user input against target value, return True if the user guessed the value correctly,
    False otherwise"""

    if user_input < target:
        print("Too low.\nGuess again.")
        return False
    elif user_input > target:
        print("Too high.\nGuess again.")
        return False
    else:
        print("Correct!")
        return True

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
attempts = difficulty[input("Choose a difficulty. Type 'easy' or 'hard': ")]

# global variable
target = randint(0, 100)
goal = False

while attempts and not goal:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    goal = compare(guess, target)
    attempts -= 1

if not attempts and not goal:
    print("You have ran out of attempts, game over!")