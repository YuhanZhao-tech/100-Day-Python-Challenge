from ascii_art import logo
from Caesar_cipher import cipher

print(logo)
to_do = input("Enter 'encode' to encrypt a message, enter 'decode' to decrypt\n")
message = input("Enter the message\n")
shift = int(input("Enter shift number\n"))

print("The message after {} is ".format(to_do) + cipher(message, shift, to_do))