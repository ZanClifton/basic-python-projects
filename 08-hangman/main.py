import random
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
display = []
end_of_game = False

print(logo)
# print(f"\nPssst, the chosen word is \"{chosen_word}\"!")
print(f"\nYou have {lives} lives! Good luck!")
print(stages[lives])

for index in range(word_length):
    display.append("_")
print(" ".join(display))

while not end_of_game:
    letter_exists = False

    guess = input("\nPick a letter: ").lower()

    print(f"You chose: \"{guess.upper()}\"")

    guessed_letter = []
    letter_guessed = False

    for letter in display:
        if guess == letter:
            letter_guessed = True
            guessed_letter.append(letter)
    if letter_guessed:
        letter_guessed = False
        print(f"\nYou already guessed {guessed_letter[0]}!")

    for index in range(word_length):
        letter = chosen_word[index]
        if letter == guess:
            display[index] = letter
            letter_exists = True

    if not letter_exists:
        print(f"\nOh no! \"{guess.upper()}\" isn't in the chosen word!")
        lives -= 1

    if lives == 1:
        print("\nYou have 1 life remaining!")
    else:
        print(f"\nYou have {lives} lives remaining!")

    print(stages[lives])

    print(" ".join(display))

    if lives == 0:
        end_of_game = True
        print(
            f"\nThe word was \"{chosen_word.upper()}\". \nYou lost. Bad luck!")

    if "_" not in display:
        end_of_game = True
        print(f"\nYou guessed \"{chosen_word.upper()}\"!")
        print("YOU WON! HOORAY!")
