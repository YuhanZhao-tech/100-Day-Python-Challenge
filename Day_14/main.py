from Higher_lower import random_select, print_versus, check_answer
from ascii_art import logo

def game() -> None:
    print("Welcome to Higher and Lower!\n{}".format(logo))
    game_on = True
    while game_on:
        contenders = random_select()
        guess = {'A': 0, 'B': 1}[print_versus(contenders)]
        if check_answer(contenders, guess):
            print(f"Correct! {contenders[guess]['name']} has more followers!")
        else:
            print("Ah oh, Wrong answer")
            return


game()