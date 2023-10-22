from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_dispenser = MoneyMachine()

power_switch = True
correct_input = False

while power_switch:

    user_choice = input("What would you like (espresso/latte/cappuccino): ")
    if menu.find_drink(user_choice):
        if coffee_machine.is_resource_sufficient(menu.find_drink(user_choice)):
            money_dispenser.make_payment(menu.find_drink(user_choice).cost)
            coffee_machine.make_coffee(menu.find_drink(user_choice))
        else:
            pass
    elif user_choice == "report":
        coffee_machine.report()
    elif user_choice == "off":
        power_switch = False
