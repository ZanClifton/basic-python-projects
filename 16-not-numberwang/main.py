from art import logo
import random


def compare_numbers(num, guess):
    if guess > num:
        return "Too high!"
    elif guess < num:
        return "Too low!"
    else:
        return "You win!"


def decrease_guesses():
    return guesses - 1


print(logo)
print("Welcome to the Number Guessing Game, \"Not#Wang\"!")
print("\nHmm... I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type \"easy\" or \"hard\": ")
if difficulty == "easy":
    guesses = 10
else:
    guesses = 5


number = random.randint(1, 100)

player_guess = 0

while player_guess != number and guesses > 0:
    print(f"You have {guesses} attempts remaining to guess the number.")
    player_guess = int(input("Make a guess: "))
    guesses = decrease_guesses()
    result = compare_numbers(number, player_guess)
    print(result)

if guesses == 0 and player_guess != number:
    print("You ran out of guesses!")
elif player_guess == number:
    print("Thank you for playing!")
