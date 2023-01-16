import random

print("Welcome to Rock Paper Scissors")
choice_dict = {
    0:"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", 
    1:"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    2:"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}
result_dict = {
    0:(2, 1),
    1:(0, 2),
    2:(1, 0)
}

while (True):
    try:
        choice = int(input("What do you choose? 0 for rock, 1 for paper or 2 for scissors.\n"))
        print("You chose\n" + choice_dict[choice])
    except KeyError:
        print("Please enter a valid number")
        break

    
    com_choice = random.randint(0, 2)
    print("Computer chose\n" + choice_dict[com_choice])

    if (choice == com_choice): print("Draw")
    elif (com_choice == result_dict[choice][0]): print("You Win!")
    else: print("You loose")

    game_on = int(input("Enter 0 to quit, 1 to continue "))
    if game_on == 0:
        break
