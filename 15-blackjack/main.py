import os
import random
from art import logo


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


def blackjack():
    player_hand = []
    dealer_hand = []
    dealer_card_total = 0

    clearConsole()
    print(logo)

    deal_card(player_hand)
    deal_card(player_hand)
    deal_card(dealer_hand)
    deal_card(dealer_hand)

    dealer_card_total = len(dealer_hand)

    print(
        f"The dealer has {dealer_card_total} cards, and the first is [{dealer_hand[0]}]")

    player_action = "y"

    player_score = calculate_score(player_hand)

    while player_action == "y":
        print(f"Your cards are {player_hand}.")
        print(f"Your hand totals {player_score}.")

        player_action = input("Would you like another card? y/n ")

        if player_action == "y":
            deal_card(player_hand)
        else:
            player_action = "n"

        player_score = calculate_score(player_hand)

        if player_score > 21:
            player_action = "n"

    print(f"You stand. \nYou hold {player_hand} worth {player_score}.")

    dealer_score = calculate_score(dealer_hand)

    while dealer_score < 17 and not player_score > 21:
        deal_card(dealer_hand)
        dealer_score = calculate_score(dealer_hand)
        print("The dealer draws a card.")

    print(f"The dealer holds {dealer_hand} worth {dealer_score}.")

    result = compare_scores(player_score, dealer_score)

    print(result)

    should_continue = input("Would you like to play again? y/n ")

    if should_continue == "y":
        blackjack()
    else:
        clearConsole()
        print(logo)
        print("Thank you for playing!")


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


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

blackjack()
