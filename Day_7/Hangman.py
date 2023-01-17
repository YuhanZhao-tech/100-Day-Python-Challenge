import requests
import random
from ascii_art import TITLE, HANGMANPICS

# Get a random word from an online word list
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
word_list = response.content.splitlines()
word = random.choice(word_list).decode()



# Keeping track of game status
progress = []
for char in word:
    progress.append("_")
life = 6

#game starts
print("Welcome to Hangman\n{}\nGuess the word ".format(TITLE))
# Game loop
while True:

    # print the current string  
    print("  ".join(progress))

    # Get user input
    user_input = input("Guess a letter: ").lower()

    if user_input in progress:
        print("You have already guessed it!")

    # if the guess is correct
    elif word.find(user_input) != -1:
        print(user_input + " is in the word!")
        for i in range(len(word)):
            if word[i] == user_input:
                progress[i] = user_input
        
        if progress.count("_") == 0:
            print("You win")
            break
    
    # if the guess is incorrect
    else:
        life -= 1
        print(HANGMANPICS[6 - life])
        if life == 0:
            print("You loose!")
            break
        print("{} is not in the word. You have {} guesses left".format(user_input, life))
        

