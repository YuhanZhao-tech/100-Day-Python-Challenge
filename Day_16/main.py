from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def start():
    coffee_maker = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()
    while True:
        order_name = input(
            "What would you like? (espresso/latte/cappuccino): ")
        if order_name == 'off':
            return

        elif order_name == 'report':
            coffee_maker.report()
            continue

        else:
            order = menu.find_drink(order_name)

        if not coffee_maker.is_resource_sufficient(order):
            print("Sorry, not enough resources")
            continue

        print(f"The cost of your drink is {str(order.cost)}")

        if money_machine.make_payment(money_machine.make_payment(order.cost)):
            coffee_maker.make_coffee(order)

        else:
            print("Payment failed! try again.")
            continue


start()
