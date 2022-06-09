import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Ahh! You have come to challenge me to a game of 'Rock, Paper, Scissors'? Very well.")
player_guess = int(
    input("Choose your weapon! Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

guess = [f"Rock\n{rock}", f"Paper\n{paper}", f"Scissors\n{scissors}"]

print(f"You have chosen... {guess[player_guess]}")

my_guess = random.randint(0, 2)

print(f"I chose... {guess[my_guess]}")

if player_guess == 0:
    if my_guess == 0:
        print("A draw! We are evenly matched!")
    elif my_guess == 1:
        print("Ha! I am victorious! You lose!")
    else:
        print("Curses! You won!")
elif player_guess == 1:
    if my_guess == 0:
        print("Curses! You won!")
    elif my_guess == 1:
        print("A draw! We are evenly matched!")
    else:
        print("Ha! I am victorious! You lose!")
else:
    if my_guess == 0:
        print("Ha! I am victorious! You lose!")
    elif my_guess == 1:
        print("Curses! You won!")
    else:
        print("A draw! We are evenly matched!")
