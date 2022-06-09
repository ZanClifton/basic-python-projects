import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for letter in range(1, nr_letters+1):
    gen_letter = random.randint(0, 51)
    password_list.append(letters[gen_letter])

for symbol in range(1, nr_symbols+1):
    gen_symbol = random.randint(0, 8)
    password_list.append(symbols[gen_symbol])

for number in range(1, nr_numbers+1):
    gen_number = random.randint(0, 10)
    password_list.append(numbers[gen_number])

random.shuffle(password_list)

print("".join(password_list))
