import os
from art import logo


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')

# calculator functions


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# function dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    print("Thank you for using the calculator.")
    running = "y"

    num1 = float(input("What is the first number? "))

    while running == "y":
        for key in operations:
            print(key)

        operation = input("Pick one of the above operations: ")

        num2 = float(input("What is the next number? "))

        function = operations[operation]

        result = function(num1, num2)

        print(f"{num1} {operation} {num2} = {result}")

        num1 = result

        running = input(f"Continue calculating with {result}? y/n ")

    if running == "n":
        clearConsole()
        calculator()


clearConsole()
calculator()
