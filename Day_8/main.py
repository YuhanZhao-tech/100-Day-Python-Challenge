from ascii_art import logo
from Caesar_cipher import encode, decode

print(logo)
to_do = input("Enter 'encode' to encrypt a message, enter 'decode' to decrypt\n")
message = input("Enter the message\n")
shift = input("Enter shift number\n")

print("The message after {} is ".format(to_do) + eval(to_do + "('{}', {})".format(message, shift)))