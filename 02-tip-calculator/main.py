print("Welcome to the Tip Calculator!")

bill = float(input("How much is the bill?\n£"))

tip = float(input("What percentage tip would you like to give? 0, 5, 10, 12 or 15?\n"))

people = int(input("How many people are you splitting the cost between?\n"))

percent_calc = tip / 100 + 1

total = round(bill * percent_calc / people, 2)
per_person = "{:.2f}".format(total)
print(f"Each person should pay: £{per_person}")
