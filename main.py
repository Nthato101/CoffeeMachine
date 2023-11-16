from menu import MENU, resources


# Money Inserted Function
def money_inserted():

    penny =float(input("How many pennies: ")) * 0.01
    nickle = float(input("How many nickles: ")) * 0.05
    dime = float(input("How many dimes: ")) * 0.10
    quarter = float(input("How many quarters: ")) * 0.25
    total = float(nickle + penny + dime + quarter)
    print(f"You have ${total}")
    return total


# Item Selection Function
def items_selected():

    item_attr = {}
    incomplete = True

    while incomplete:
        key = input("What would you like [C]cappuccino/[E]espresso/[L]Latte ?\n").upper()
        if key == "C":
            item = "cappuccino"
        elif key == "E":
            item = "espresso"
        elif key == "L":
            item = "latte"
        else:
            print("Error : Invalid Selection")
            continue
        item_attr[item] = MENU[item]
        complete = input("Are you done adding items [Y] or [N] : ").upper()
        if complete == "N":
            continue
        elif complete == "Y":
            incomplete = False
        return item_attr


# total cost
def cost_of_items(items_chosen):
    cost_for_items = items_chosen
    total_cost = 0
    for item in cost_for_items:
        total_cost += cost_for_items[item]["cost"]
    print(f"Order total is ${total_cost}")
    return total_cost


# Check if funds are sufficient
def transaction_money(money_given, money_required):
    outcome_m = 0
    if money_given >= money_required:
        change = round(money_given - money_required, 2)
        print(f"Transaction Successful\nYour change is ${change}")
        outcome_m = True
    elif money_given < money_required:
        shortfall = round(money_required - money_given, 2)
        print(f"Transaction Unsuccessful\nYou are short ${shortfall}")
        outcome_m = False
    return outcome_m


# Check the ingredients
def ingredients(items_chosen, item_chosen):

    status_update = True
    if item_chosen == "water":
        required_water = items_chosen[item_chosen]["ingredients"]["water"]
        if required_water > resources["water"]:
            print("Sorry, there's not enough water to complete your order.")
            status_update = False
    elif item_chosen == "milk":
        required_milk = items_chosen[item_chosen]["ingredients"]["milk"]
        if required_milk > resources["milk"]:
            print("Sorry, there's not enough milk to complete your order.")
            status_update = False
    elif item_chosen == "coffee":
        required_coffee = items_chosen[item_chosen]["ingredients"]["coffee"]
        if required_coffee <= resources["coffee"]:
            print("Sorry, there's not enough coffee to complete your order.")
            status_update = False
    return status_update


# Update resources
def resource_update(items_list, item):
    for resource in items_list[item]["ingredients"]:
        resources[resource] = resources[resource] - items_list[item]["ingredients"][resource]

    return resources


money_status = 0
ingr_status = 0
order = items_selected()
for item in order:
    key = str(item)
    print(item)
cost = cost_of_items(order)
coins_inserted = money_inserted()
money_status = transaction_money(coins_inserted, cost)

ingr_status = ingredients(order, key)


if ingr_status and money_status:
    new_resources = resource_update(order, key)
    print("Thank you Enjoy!!")

report_request = input("Would you like a report on ingredients in the machine? [Y] or any other key to exit").upper()

if report_request == "Y":
    print(f"Water Level = {new_resources['water']}ml ")
    print(f"Milk Level = {new_resources['milk']}ml ")
    print(f"Coffee Level = {new_resources['coffee']}g ")
else:
    print("Goodbye!")
    quit()
