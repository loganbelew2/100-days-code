from data import (MENU, resources)
menu = MENU
latte = menu["latte"]
cappuccino = menu["cappuccino"]
espresso = menu["espresso"]
class Latte:
    def __init__(self, menu) -> None:
        self.menu = menu

class Drink:
    def make_drink(type):
        if type == "latte":
            global latte
            return latte
        if type == "cappuccino":
            global cappuccino
            return cappuccino
        if type == "espresso":
            global espresso
            return espresso
new_drink = Drink.make_drink("latte")
newer = Drink.make_drink("espresso")
newest = Drink.make_drink("cappuccino")
print(new_drink)
print(newer)
print(newest)