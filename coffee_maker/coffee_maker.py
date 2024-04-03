# Welcome to the Coffee Machine!
#Users of this machine will select what coffee they would like and receive it
#Admistrators of the machine can type "off" or "report" to shut down or view resources

#Importing MENU and RESOURCES from a data module
from data import MENU, RESOURCES

# Creating aliases for MENU and RESOURCES
menu = MENU
resources_copy = RESOURCES

# Updating the 'money' key in the resources_copy dictionary to 0
resources_copy["money"] = 0


# Define function to get the ingredients for the corresponding type of coffee
def get_ingredients(type):
  """
    Returns the ingredients required for a specific type of coffee.

    Args:
        type (str): Type of coffee (espresso, latte, or cappuccino).

    Returns:
        dict: Ingredients required for the specified type of coffee.
    """
  switcher = {
      "espresso": menu["espresso"]["ingredients"],
      "latte": menu["latte"]["ingredients"],
      "cappuccino": menu["cappuccino"]["ingredients"]
  }
  return switcher.get(type, "invalid type")


# Define function to get the cost of a specific type of coffee
def coffee_cost(type):
  """
    Returns the cost of a specific type of coffee.

    Args:
        type (str): Type of coffee (espresso, latte, or cappuccino).

    Returns:
        float: Cost of the specified type of coffee.
    """
  switcher = {
      "espresso": menu["espresso"]['cost'],
      "latte": menu["latte"]['cost'],
      "cappuccino": menu["cappuccino"]['cost']
  }
  return switcher.get(type, "invalid type")


# Define function to check if there are enough resources for the coffee
def check_resources():
  """
    Checks if there are enough resources to make the selected coffee.

    Returns:
        bool: True if there are not enough resources, False otherwise.
    """
  is_enough_resources = True
  ingredients = get_ingredients(coffee_choice)
  # Loop over ingredients for the chosen coffee and check if there is enough resources
  for ingredient in ingredients:
    if resources_copy[ingredient] < ingredients[ingredient]:
      print(f"not enough {ingredient}")
      is_enough_resources = False
  return is_enough_resources


# Define function to calculate the total amount of money inserted
def calculate_inserted_money(array_numbers):
  """
    Calculates the total amount of money inserted based on the number of each coin.

    Args:
        array_numbers (list): List containing the number of each coin inserted.

    Returns:
        float: Total amount of money inserted.
    """
  coin_values = [.25, .1, .05, .01]
  total = 0
  for i in range(len(coin_values)):
    total += coin_values[i] * array_numbers[i]
  return round(total, 2)


# Define function to deduct the resources used to make the coffee
def deduct_resources(coffee_ingredients):
  """
    Deducts the resources used to make the coffee from the available resources.

    Args:
        coffee_ingredients (dict): Ingredients required for the coffee.
    """
  for ingredient in coffee_ingredients:
    resources_copy[ingredient] -= coffee_ingredients[ingredient]


# Main program loop
while True:
  # Prompt user to choose their coffee after each transaction completes
  coffee_choice = input('What would you like? (espresso/latte/cappuccino): ')
  #statement to check if input is valid, if not then restart loop
  if coffee_choice not in ["espresso", "latte", "cappuccino", "off", "report"]:
    continue
  #further check if input is a admin prompt
  if coffee_choice not in ["off", "report"]:
    print(f'An {coffee_choice} will cost you {coffee_cost(coffee_choice)}')
  # check for a requested shutdown
  if coffee_choice == "off":
    print('shutting down')
    break
  #check for a resources report of the machine
  elif coffee_choice == "report":
    print(resources_copy)
  else:
    # Check for sufficient ingredients
    enough_resources = check_resources()
    # Process coins
    if enough_resources == True:
      amounts = []
      coins = ["quarters", "dimes", "nickles", "pennies"]
      for coin in coins:
        while True:
          try:
            amount = int(input(f"how many {coin}?"))
            amounts.append(amount)
            break
          except ValueError as e:
            print("Please input a number.")

      total_inserted = calculate_inserted_money(amounts)
      coffee_amount = coffee_cost(coffee_choice)
      if total_inserted < coffee_amount:
        print(
            f"Sorry, you didn't insert enough money, you inserted {total_inserted} and the {coffee_choice} cost {coffee_amount}"
        )
      elif total_inserted >= coffee_amount:
        print(
            f"Your change is ${round(total_inserted - coffee_amount, 2)}\ntotal inserted is {total_inserted}"
        )
        resources_copy["money"] += coffee_amount
        deduct_resources(get_ingredients(coffee_choice))
        print(f"here is your {coffee_choice}")
