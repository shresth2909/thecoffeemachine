import RESOURCE
import MENU

def resource_utilisation(user_choice):
    RESOURCE.resources["water"] -= MENU.OUR_MENU[user_choice]["ingredients"].get("water", 0)
    RESOURCE.resources["milk"] -= MENU.OUR_MENU[user_choice]["ingredients"].get("milk", 0)
    RESOURCE.resources["coffee"] -= MENU.OUR_MENU[user_choice]["ingredients"].get("coffee", 0)

def ask_about_the_coins():
    print('Please insert the number of coins:')
    quarters = input("How many quarters?: ")
    dimes = input("How many dimes?: ")
    nickles = input("How many nickles?: ")
    pennies = input("How many pennies?: ")
    amount = int(quarters)* 0.25 + int(dimes)* 0.10 + int(nickles)* 0.05 + int(pennies)* 0.01
    return amount

def coffee_processing(user_choice):
        amount_received = ask_about_the_coins()
        if amount_received > MENU.OUR_MENU[user_choice]["cost"]:
            change = amount_received - MENU.OUR_MENU[user_choice]["cost"]
            print(f'Here is the change {change}')
            print(f'Here is your {user_choice} . enjoy!!')
            resource_utilisation(user_choice)
        elif amount_received < MENU.OUR_MENU[user_choice]["cost"]:
            print('Sorry, you dont have enough money, you are refunded, thanks!')
        else:
            print(f'Here is your {user_choice} . enjoy!!')
            resource_utilisation(user_choice)

def print_report():
    print('The report of all the resources are as follows:')
    print(f'The amount of water is {RESOURCE.resources["water"]}')
    print(f'The amount of milk is {RESOURCE.resources["milk"]}')
    print(f'The amount of coffee is {RESOURCE.resources["coffee"]}')
    print(f'And the amount of water you need for your choice is:{MENU.OUR_MENU[user_choice]["ingredients"]["water"]}')
    if user_choice != "espresso":
        print(f'And the amount of milk you need for your choice is:{MENU.OUR_MENU[user_choice]["ingredients"]["milk"]}')
    print(f'And the amount of coffee you need for your choice is:{MENU.OUR_MENU[user_choice]["ingredients"]["coffee"]}')

def check_resource_sufficiency(user_choice):
    if (MENU.OUR_MENU[user_choice]["ingredients"].get("water", 0) <= RESOURCE.resources.get("water", 0) and
            MENU.OUR_MENU[user_choice]["ingredients"].get("milk", 0) <= RESOURCE.resources.get("milk", 0) and
            MENU.OUR_MENU[user_choice]["ingredients"].get("coffee", 0) <= RESOURCE.resources.get("coffee", 0)):
        return True

machine_is_on = True

while machine_is_on:
    wanna_coffee = input('wanna coffee (y/n)? ')
    if wanna_coffee == 'y':
        machine_is_on = True
    else:
        machine_is_on = False
        print('Okkay, cool!! have a good day!')
        break
    user_choice = input('What would you like to have (espresso/latte/cappuccino)? ')
    if user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
        print(f'It will take water upto:{MENU.OUR_MENU[user_choice]["ingredients"].get("water", 0)}')
        print(f'It will take milk upto:{MENU.OUR_MENU[user_choice]["ingredients"].get("milk", 0)}')
        print(f'It will take coffe upto:{MENU.OUR_MENU[user_choice]["ingredients"].get("coffee", 0)}')
        print(f'It will costs: {MENU.OUR_MENU[user_choice]["cost"]}')
        resources_sufficient = check_resource_sufficiency(user_choice) # Store the boolean result in a new variable
        if resources_sufficient:
            coffee_processing(user_choice)
        else:
            print('Sorry, you dont have enough resources, please check your request')
            print_report()
    else:
        print('Sorry but we dont have this coffe in our menu, please select the correct choice')
