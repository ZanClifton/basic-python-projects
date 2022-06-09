from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(message, moves, direction):
    new_text = ""
    if direction == "decode":
        moves *= -1
    for letter in message:
        if letter not in alphabet:
            new_text += letter
        else:
            index = alphabet.index(letter)
            new_index = index + moves
            while new_index >= 26:
                new_index -= 26
            while new_index < 0:
                new_index += 26
            new_text += alphabet[new_index]
    print(f"The {direction}d text is: {new_text}")


repeat = True
while repeat:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(message=text, moves=shift, direction=direction)

    restart = input(
        "Would you like to encode or decode something else? y/n? ").lower()

    if restart == "n":
        repeat = False
        print("Goodbye!")
