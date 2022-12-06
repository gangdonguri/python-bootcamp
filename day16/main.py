from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True
coffee_resources = CoffeeMaker()
coins = MoneyMachine()

while is_on:
    # TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino/):”
    choice = input("“What would you like? (espresso/latte/cappuccino/): ")

    # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
    # TODO 3. Print report.
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_resources.report()
        coins.report()
    else:
        # TODO 4. Check resources sufficient?
        drink_menu = Menu()
        drink_object = drink_menu.find_drink(choice)

        is_sufficient = coffee_resources.is_resource_sufficient(drink_object)
        if is_sufficient == True:
            # TODO 5. Process coins.
            # TODO 6. Check transaction successful?
            can_make = coins.make_payment(drink_object.cost)

            # TODO 7. Make Coffee
            if can_make == True:
                coffee_resources.make_coffee(drink_object)







