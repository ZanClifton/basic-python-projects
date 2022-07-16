import os
import random
from art import logo

def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')

def calculate_score(hand):
    length = len(hand)
    score = sum(hand)
    ace = False
    if 11 in hand:
        ace = True
    if length == 2 and score == 21:
        score = 0
    elif score > 21 and ace:
        index = hand.index(11)
        print(index)
        hand[index] = 1
        score -= 10
    return score

def compare_scores(player, dealer):
    if player == dealer:
        return "Draw!"
    elif dealer == 0:
        return "Blackjack! Dealer wins!"
    elif player == 0:
        return "Blackjack! You win!"
    elif player > 21:
        return "Bust! You lose!"
    elif dealer > 21:
        return "Bust! Dealer loses!"
    elif player > dealer:
        return "You win!"
    else:
        return "Dealer wins!"

def deal_card(hand):
    index = random.randint(0, 12)
    hand.append(cards[index])

def blackjack():
    player_hand = []
    dealer_hand = []
    player_total = 0
    dealer_total = 0
    again = "n"
    length = 0
    should_continue = "y"
    again = "n"

    dealer_score = 0

    print(logo)

    deal_card(player_hand)
    deal_card(player_hand)
    deal_card(dealer_hand)
    deal_card(dealer_hand)

    while should_continue == "y":
        draw = "n"

        player_total = calculate_score(player_hand)
        dealer_total = calculate_score(dealer_hand)
        dealer_score = dealer_total

        if player_total == 0:
            player_score = 21
        else:
            player_score = player_total

        print(f"You have {player_hand} in your hand totalling {player_score}.")

        if player_total >= 21 or player_total == 0 or dealer_total >= 21 or dealer_total == 0:
            should_continue = "n"
        else:
            draw = input(f"Hit? y/n ")
            if draw == "y":
                deal_card(player_hand)
            else:
                should_continue = "n"

                while dealer_total < 17 and dealer_total != 0:
                    deal_card(dealer_hand)
                    dealer_total = calculate_score(dealer_hand)

                if dealer_total == 0:
                    dealer_score = 21
                else:
                    dealer_score = dealer_total

    length = len(dealer_hand)

    print(f"The dealer has {length} cards totalling {dealer_score}!")

    result = compare_scores(player_total, dealer_total)

    print(f"\nRESULT: {result}")
    again = input("Would you like another game? y/n ")

    if again == "y":
        clearConsole()
        blackjack()
    else:
        print("\nThank you for playing!")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


blackjack()
