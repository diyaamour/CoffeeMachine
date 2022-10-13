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


def sufficient_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry. There isn't enough {item}. ")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def transaction_status(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here's ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Your coins were refunded. ")
        return False


def make_coffee(drink_choice, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your drink {drink_choice}☕️. Enjoy! ")


is_on = True

while is_on:
    customer_order = input("What would you like? (espresso/latte/cappuccino): ")
    if customer_order == "off":
        is_on = False
    elif customer_order == "report":
        print(f"Water: {resources['water']}mL")
        print(f"Milk: {resources['milk']}mL")
        print(f"Coffee: {resources['coffee']}mL")
        print(f"Money: ${profit}")
    else:
        drink = MENU[customer_order]
        if sufficient_resources(drink["ingredients"]):
            payment = process_coins()
            if transaction_status(payment, drink["cost"]):
                make_coffee(customer_order, drink["ingredients"])


# TODO 1. Print report
# TODO 2. Check resources sufficient?
# TODO 3. Process coins
# TODO 4. Check transaction successful?
# TODO 5. Make coffee
