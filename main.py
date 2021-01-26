from data import MENU, resources

# welcome message and pricing
print("""
Welcome to the coffee maker!
THe prices are:
espresso: 1.50 $
latte: 2.50 $
cappuccino: 3.00 $
""")

# ingredients list:
espresso_water = MENU["espresso"]["ingredients"]["water"]
espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]

latte_water = MENU["latte"]["ingredients"]["water"]
latte_milk = MENU["latte"]["ingredients"]["milk"]
latte_coffee = MENU["latte"]["ingredients"]["coffee"]

cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]


# main body: input question:

profit = 0
resources["profit"] = 0

machine_works = True
while machine_works:
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

# how to update resources (no need to do that for coffee with such low initial resources):

    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    profit = resources["profit"]

    if drink == "report":
        print(f"""
              water = {resources["water"]} ml
              milk = {resources["milk"]} ml
              coffee = {resources["coffee"]} ml
              money = {resources["profit"]} $
              """)

    elif drink == "off":
        print("Good bye!")
        machine_works = False

    elif water >= espresso_water and cappuccino_water and latte_water:

        if drink == "espresso":
            resources["water"] = water - 50
            resources["milk"] = milk
            resources["coffee"] = coffee - 18
            resources["profit"] = profit + 1.5
        elif drink == "latte":
            resources["water"] = water - 200
            resources["milk"] = milk - 150
            resources["coffee"] = coffee - 24
            resources["profit"] = profit + 2.5
        elif drink == "cappuccino":
            resources["water"] = water - 250
            resources["milk"] = milk - 100
            resources["coffee"] = coffee - 24
            resources["profit"] = profit + 3
        else:
            print("I am sorry, wrong input.")
    else:
        print("I am sorry, not enough resources")
        machine_works = False
    # print(resources)
