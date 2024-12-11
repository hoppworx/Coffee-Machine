MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def process_coins():
    """Prompts user to enter coins and returns the total"""
    print("Please insert coins:")
    total = int(input("How many quarters? ")) * .25
    total += int(input("How many dimes? ")) * .10
    total += int(input("How many nickels? ")) * .05
    total += int(input("How many pennies? ")) * .01
    return total

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print("You don't have enough {item}.")
            return False
    return True

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True

    else:
        print("You don't have enough money.  Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deducts resources needed and completes order"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name} ☕️. Enjoy!")



is_on = True  #Verifies if coffee machine is on or off

while is_on == True:
    choice = input("What would you like? (espresso, latte, capuccino, report, off/on): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']): # Passes ingredients required for selected drink
            payment = process_coins()  # Gets total of coins prompted for entry
            if is_transaction_successful(payment, drink["cost"]): # Passes payment and cost of selected drink
                make_coffee(choice, drink["ingredients"])
