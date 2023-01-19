from Blackjack import round

run = {'y': True, 'n':False}[input("Would you like to play a round of Black jack? 'y' to play, 'n' to quit: ")]

while run:
    round()
    run = {'y': True, 'n':False}[input("Would you like to start a new round? 'y' or 'n': ")]