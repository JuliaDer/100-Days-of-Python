from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
money = MoneyMachine()
drinks = Menu()

is_on = True
while is_on:
    options = drinks.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee.report()
        money.report()
    else:
        drink = drinks.find_drink(choice)
        is_enough_ingredients = coffee.is_resource_sufficient(drink)
        is_payment_successful = money.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffee.make_coffee(drink)
