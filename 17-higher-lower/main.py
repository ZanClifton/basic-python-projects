import os
from random import choice
from game_data import data
from art import logo, vs


def clearConsole():
    return os.system(
        'cls' if os.name in ('nt', 'dos') else 'clear')


def increase_count(n):
    return count + n


def select_subject():
    return choice(data)


a = (select_subject())
b = (select_subject())

should_continue = "y"
count = 0

while should_continue == "y":
    clearConsole()
    print(logo)
    if count > 0:
        print(f"That's right! Your current score is {count}!")

    while a == b:
        b = select_subject()

    print("Which of the following has the greatest number of Instagram followers?\n")
    print(
        f"Compare A: {a['name']}, a {a['description'].lower()} from {a['country']}")
    print(vs)
    print(
        f"Against B: {b['name']}, a {b['description'].lower()} from {b['country']}")

    guess = input("A or B? a/b ").lower()

    if guess == "a" and a["follower_count"] > b["follower_count"] or guess == "b" and a["follower_count"] < b["follower_count"]:
        should_continue = "y"
    # elif guess == "a" and a["follower_count"] < b["follower_count"] or guess == "b" and a["follower_count"] > b["follower_count"]:
    #   should_continue = "n"
    else:
        clearConsole()
        print(logo)
        should_continue = "n"

    if should_continue != "y":
        print(f"Sorry, that's wrong. You scored {count}!")
    else:
        count = increase_count(1)
        a = b
        b = select_subject()
