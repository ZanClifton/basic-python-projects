def amend_resource(resource, drink):
    if resource == "money":
        resources[resource] = resources[resource] + drinks_menu[drink][resource]
    else:
        resources[resource] = resources[resource] - drinks_menu[drink][resource]


def check_resources(drink):
    check = ""
    water = compare_resource(resources["water"], drinks_menu[drink]["water"])
    coffee = compare_resource(resources["coffee"], drinks_menu[drink]["coffee"])
    if drink != "espresso":
        milk = compare_resource(resources["milk"], drinks_menu[drink]["milk"])
    else:
        milk = True
    money = drinks_menu[drink]["money"]

    if water and milk and coffee:
        check = f"A {drink} costs ${money}0."
    elif not milk:
        check = "milk"
    elif not coffee:
        check = "coffee"
    elif not water:
        check = "water"

    return check


def compare_resource(resource, drink_resource):
    """Checks there are sufficient resources and returns True if there are"""
    if resource >= drink_resource:
        return True


def make_report():
    """Returns an f-string report of the current resources available in the machine"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}"


def turn_off_machine():
    """Turns off the coffee machine and exits the program"""
    return "off"


resources = {
    "water": 500,
    "milk": 500,
    "coffee": 76,
    "money": 2.5
}

drinks_menu = {"espresso": {"water": 50, "coffee": 18, "money": 1.5},
               "latte": {"water": 200, "milk": 150, "coffee": 24, "money": 2.5},
               "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "money": 3.0}}

machine = "on"

while machine != "off":
    program = input("\nWhat would you like? (espresso/latte/cappuccino): ")

    can_brew = False

    if program == "off":
        machine = turn_off_machine()
    elif program == "report":
        print("The coffee machine has the following resources:")
        print(make_report())
    elif program == "espresso" or program == "cappuccino" or program == "latte":
        can_brew = check_resources(program)
    else:
        print(f"'{program}' is not a valid selection. Please try again.")

    if can_brew == "water" or can_brew == "milk" or can_brew == "coffee":
        print(f"\nThere is not enough {can_brew} to make your drink.")
    elif not can_brew:
        print("Thank you.")
    else:
        print(f"\n{can_brew} Please insert enough money to pay for your drink.")

        quarters = int(input("Insert quarters ($0.25 each): "))
        total_quarters = quarters * 0.25
        string_quarters = "{0:.2f}".format(total_quarters)
        print(f"You have inserted ${string_quarters}")

        dimes = int(input("Insert dimes ($0.10 each): "))
        total_dimes = dimes * 0.1
        total_cash = total_quarters + total_dimes
        string_cash = "{0:.2f}".format(total_cash)
        print(f"You have inserted ${string_cash}")

        nickels = int(input("Insert nickels ($0.05 each): "))
        total_nickels = nickels * 0.05
        total_cash = total_quarters + total_dimes + total_nickels
        string_cash = "{0:.2f}".format(total_cash)
        print(f"You have inserted ${string_cash}")

        pennies = int(input("Insert pennies ($0.01 each): "))
        total_pennies = pennies * 0.01
        total_cash = total_quarters + total_dimes + total_nickels + total_pennies
        string_cash = "{0:.2f}".format(total_cash)
        print(f"You have inserted ${string_cash}.")

        if total_cash >= drinks_menu[program]["money"]:
            print(f"\nBrewing your {program}...")
            print(f"Collect your {program}! Careful! It's hot!")
            amend_resource("water", program)
            amend_resource("coffee", program)
            if program != "espresso":
                amend_resource("milk", program)
            amend_resource("money", program)
        else:
            print("Sorry, that's not enough money. Money refunded.")

        if total_cash > drinks_menu[program]["money"]:
            change = total_cash - drinks_menu[program]["money"]
            string_change = "{0:.2f}".format(change)
            print(f"Here's your change: ${string_change}")
