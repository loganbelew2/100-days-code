from data import MENU, resources
menu = MENU
resources_copy = resources
resources_copy["money"] = 0

#define function to get the ingredients for the corresponding type of coffee
def coffee_type(type):
    switcher = {
        "espresso": menu["espresso"]["ingredients"],
        "latte": menu["latte"]["ingredients"],
        "cappuccino": menu["cappuccino"]["ingredients"]
    }
    return switcher.get(type, "invalid type")

def coffee_cost(type):
    switcher = {
        "espresso": menu["espresso"]['cost'],
        "latte": menu["latte"]['cost'],
        "cappuccino": menu["cappuccino"]['cost']
    }
    return switcher.get(type, "invalid type")

#define function to check if there is enough resources for the coffee
def check_resources():
    not_enough_ingredients = False
    ingredients = coffee_type(coffee_choice)
    #loop over ingredients for the chosen coffee and check if there is enough of each resource for each ingredient
    for ingredient in ingredients:
        if resources_copy[ingredient] < ingredients[ingredient]:
            print(f"not enough {ingredient}")
            not_enough_ingredients = True
    return not_enough_ingredients

def calculate_inserted_money(array_numbers):
    coin_values =[.25, .1, .05, .01]
    total = 0
    for i in range(4):
        total += coin_values[i] * array_numbers[i]
    return round(total, 2)

def deduct_resources(coffee_ingredients):
    for ingredient in coffee_ingredients:
        resources_copy[ingredient] -= coffee_ingredients[ingredient]

while True:
    #Prompt user to choose their coffee after each transaction completes
    coffee_choice = input('What would you like? (espresso/latte/cappuccino): ')
    if coffee_choice not in ["espresso", "latte", "cappuccino", "off", "report"]:
        break
    if coffee_choice not in ["off", "report"]:
        print(f'An {coffee_choice} will cost you {coffee_cost(coffee_choice)}')
    #check for a requested report of turn off 
    if coffee_choice == "off":
        print('shutting down')
        break
    elif coffee_choice == "report":
        print(resources_copy)
    #check for sufficient ingredients
    else:
        not_enough_resources = check_resources()
        #process coins
        if not_enough_resources == False: 
            amounts = []          
            coins = ["quarters", "dimes", "nickles", "pennies"]
            for coin in coins:
                amount = int(input(f"how many {coin}?"))
                amounts.append(amount)
            total_inserted = calculate_inserted_money(amounts)
            coffee_amount = coffee_cost(coffee_choice)
            if total_inserted < coffee_amount:
                print(f"Sorry, you didn't insert enough money, you inserted {total_inserted} and the {coffee_choice} cost {coffee_amount}")
            elif total_inserted >= coffee_amount:
                print(f"Your change is {round(total_inserted - coffee_amount, 2)} total inserted is {total_inserted}")
                resources_copy["money"] += coffee_amount
                deduct_resources(coffee_type(coffee_choice))
                print(f"here is your {coffee_choice}")