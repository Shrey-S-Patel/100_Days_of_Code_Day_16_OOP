from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()

espresso = MenuItem("Espresso",50,0,18,1.5)
latte = MenuItem("Latte", 200, 150, 24, 2.5)
cappuccino = MenuItem("Cappuccino", 250, 100, 24, 3.0)

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# print(coffee_menu.find_drink("capp"))

is_on = True

while is_on:
    choice = input(f"What would you like? ({coffee_menu.get_items()})\n").lower()

    if choice == "off":
        is_on = False
        print("Goodbye!")
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order = coffee_menu.find_drink(choice)
        if order is not None:
            if coffee_maker.is_resource_sufficient(order):
                if money_machine.make_payment(order.cost):
                    coffee_maker.make_coffee(order)