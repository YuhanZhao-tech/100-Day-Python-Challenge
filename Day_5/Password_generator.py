# Password generator
import string
import random
letters = list(string.ascii_letters)
numbers = list(range(10))
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']

print("Welcome to the password generator")
#print(len(letters))
num_char = int(input("How many symbols would you like in your password?\n"))
num_symbol = int(input("How many symbols would you like?\n"))
num_digit = int(input("How many digits would you like?\n"))

password = []
for i in range(num_char):
    password.append(random.choice(letters))
for i in range(num_symbol):
    password.append(random.choice(symbols))
for i in range(num_digit):
    password.append(str(random.choice(numbers)))

random.shuffle(password)
password = "".join(password)
print(password)



