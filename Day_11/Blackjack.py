# Black Jack
import random
from ascii_art import logo

DECK = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_total(deck_list) -> int:
    num_of_ace = 0
    total = 0
    for card in deck_list:
        if card == 1:
            num_of_ace += 1
        else:
            total += card

    for ace in range(num_of_ace):
        if total + 11 <= 21:
            total += 11
        else:
            total += 1

    return total



#print(calculate_total([10, 1]))
def round() -> None:
    player = [random.choice(DECK), random.choice(DECK)]
    dealer = [random.choice(DECK), random.choice(DECK)]
    print("Welcome to Blackjack!\n{}".format(logo))
    run = True
    while run:
        player_score = calculate_total(player)
        dealer_score = calculate_total(dealer)
        if player_score >= 21 or dealer_score >= 21:
            break

        print(f"Your cards: {player}, current score: {player_score}\nDealer's first card: {dealer[0]}")
        run = {'y': True, 'n': False}[input("Type 'y' to get another card, type 'n' to pass: ")]
        if run:
            player.append(random.choice(DECK))
            if calculate_total(dealer) <= 17:
                dealer.append(random.choice(DECK))

    player_final = calculate_total(player)
    dealer_final = calculate_total(dealer)
    print(f"your final hand: {str(player)}, final score: {str(player_final)}")
    print(f"dealer's final hand: {str(dealer)}, final score: {str(dealer_final)}")
    if player_final == dealer_final or (player_final > 21 and dealer_final > 21):
        print("Draw!")

    # only one player is busted
    elif player_final <= 21 and dealer_final > 21:
        print("Dealer's busted, you win!")
    
    elif player_final > 21 and dealer_final <= 21:
        print("You are busted, you loose!")

    else:
        result = {'player': player_final, 'dealer': dealer_final}
        print(f"{max(result, key=result.get)} wins!")

    
