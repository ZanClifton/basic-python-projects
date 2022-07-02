import os
from art import logo


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


all_bids = {}
bidders = "y"

print(logo)
print("Welcome to the secret auction!")

while bidders == "y":
    name = input("\nWhat is your name? ")
    bid = int(input("What is your bid? £"))

    def add_new_bid(name, bid):
        all_bids[name] = bid

    add_new_bid(name, bid)

    bidders = input("\nAre there any other bidders? y/n ")

    clearConsole()
    print(logo)

highest_bidder = max(all_bids, key=all_bids.get)
print(
    f"{highest_bidder} won with a bid of £{all_bids[highest_bidder]}!\nCongratulations, {highest_bidder}!")
