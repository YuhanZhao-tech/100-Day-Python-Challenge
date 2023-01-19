# Number guessing game
import random

difficulty = {'easy': 10, 'hard': 5}

def compare(user_input, target):
    if user_input < target:
        print("Too low.\nGuess again.")
    elif user_input > target:
        print("Too high.\nGuess again.")
    else:
        global goal
        goal = True
        print("Correct!")

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
attempts = difficulty[input("Choose a difficulty. Type 'easy' or 'hard': ")]

# global variable
target = random.randint(0, 100)
goal = False

while attempts and not goal:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    compare(guess, target)
    attempts -= 1

if not attempts and not goal:
    print("You have ran out of attempts, game over!")