from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()

dispenser = CoffeeMaker()
cash_machine = MoneyMachine()

should_continue = "y"

while should_continue == "y":
    selection = input(
        f"What would you like? ({coffee_menu.get_items()}): ").lower()

    if selection == "off":
        print("The coffee machine is off.")
        should_continue = "n"
    elif selection == "report":
        dispenser.report()
        cash_machine.report()
    else:
        drink_object = coffee_menu.find_drink(selection)
        if drink_object:
            enough = dispenser.is_resource_sufficient(drink_object)
            if enough:
                money_good = cash_machine.make_payment(drink_object.cost)
                if money_good:
                    dispenser.make_coffee(drink_object)
