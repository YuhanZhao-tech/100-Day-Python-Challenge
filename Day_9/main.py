from Bidder import Bidder
from Secret_auction import SecretAuction
from art import logo

print("Welcom to the secret auction program\n{}".format(logo))
secret_auction = SecretAuction()
run = True
while(run):
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))
    secret_auction.add_bidder(name, bid)

    run = {"yes":True, "no":False}[input("Are there any other bidders? ")]

winner = secret_auction.highest_bidder()
print("the winner is {} with a bid of ${}".format(winner.get_name(), winner.get_bid()))