# TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
# TODO: 3.print report of the resources of the Coffee machine.
# TODO: 2. Turn off the coffee machine by entering "off" to the prompt.
# TODO: 4. Check resources sufficient?
# TODO: 5. Process coins.
# TODO: 6. Check transaction successful?
# TODO: 7. make coffee.


import main

off_machine = False
cost = 0


def transaction(money, drink_cost):
    """Returns true if the payment is successful, false if the money is insufficient"""
    if money >= drink_cost:
        change = round(money - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global cost
        cost += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def is_resources_sufficient(ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    for item in ingredients:
        if ingredients[item] >= main.resources[item]:
            print("Sorry there is not enough {item}.")
            return False
        return True


def coins():
    """Returns the total calculated from the coins inserted"""
    print("Please insert coins")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.10
    total += int(input("How many nickles?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        main.resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


while not off_machine:

    prompt = input("What would you like? (espresso/latte/cappuccino: ").lower()
    if prompt == 'report':
        print(f"water: {main.resources['water']}")
        print(f"Milk: {main.resources['milk']}")
        print(f"coffee: {main.resources['coffee']}")
        print(f"Price: ${cost}")
    elif prompt == 'off':
        off_machine = True
    else:
        drink = main.MENU[prompt]
        if is_resources_sufficient(drink["ingredients"]):
            payment = coins()
            if transaction(payment, drink["cost"]):
                make_coffee(prompt, drink["ingredients"])

#This Type of programming is called Procedural Programming.