from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

mm = MoneyMachine()
cm = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    drink_choice = input(f"What would you like? ({menu.get_items()}): ")

    match drink_choice:
        case "report":
            cm.report()
            mm.report()
        case "off":
            exit(0)
        case _:
            drink = menu.find_drink(drink_choice)
            if cm.is_resource_sufficient(drink) and mm.make_payment(drink.cost):
               cm.make_coffee(drink)
