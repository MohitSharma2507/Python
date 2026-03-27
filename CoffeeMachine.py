Menu = {
    'latte': {
        'ingredients': {'water':200, 'milk':150, 'coffee':24},
        'cost':150
    },
    'espresso': {
        'ingredients': {'water':50, 'coffee':18},
        'cost':100
    },
    'cappuccino': {
        'ingredients': {'water':250, 'milk':100, 'coffee':24},
        'cost':200
    }
}

profit=0

resources = {
    'water':1500,
    'milk':1200,
    'coffee':500
}

def check_resources(coffee_type):
    for item in coffee_type:
        if coffee_type[item] > resources.get(item, 0):
            print(f"❌ Not enough {item}. Required: {coffee_type[item]}, Available: {resources.get(item, 0)}")
            return False
    return True


              
def insert_coin():
    print("Please insert coins")
    rs_5 = int(input("How many 5Rs. Coin: "))
    rs_10 = int(input("How many 10Rs. Coin: "))
    rs_20 = int(input("How many 20Rs. Coin: "))

    total = (rs_5*5) + (rs_10*10) + (rs_20*20)
    return total
  
def is_payment_successful(payment, coffee_cost):
    global profit
    if payment >= coffee_cost:
        profit += coffee_cost
        change = payment - coffee_cost
        print(f"Here is your Rs.{change} in change")
        return True
    else:
        print("❌ Sorry that's not enough. Money refunded")
        return False


def make_coffee(coffee_name, coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"☕ Here is your {coffee_name}")


is_On=True

while is_On:
    choice=input("What would you like to have? (latte/espresso/cappuccino): ").lower()

    if choice == "off":
        print("Thank you! Bye 👋")
        is_On=False

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Money: Rs.{profit}")
   
    elif choice not in Menu:
        print("❌ Invalid choice")

    else:
        coffee_type = Menu[choice]

        if check_resources(coffee_type['ingredients']):
            payment = insert_coin()

            if is_payment_successful(payment, coffee_type['cost']):
                make_coffee(choice, coffee_type['ingredients'])
              


