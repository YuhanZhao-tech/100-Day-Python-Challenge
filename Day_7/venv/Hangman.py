import requests
import random

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)

word_list = response.content.splitlines()
word = random.choice(word_list).decode()

print("Welcome to Hangman!")