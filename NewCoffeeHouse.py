
def greet_customer():
    print("\n\n\nHello!\n")


greet_customer()


def get_name():
    print("Welcome to Ben's Coffee House. Can I get a name for the order?")


get_name()

name = input('\n\n')


def respond_name():
    print('Hello, ' + name + '. Would you like to see our menu?\n')


respond_name()


menu = '\n- Dark Roast' '\n- Light Roast' '\n- Medium Roast'
see_menu = input('\n')


def menu_items():
    if see_menu == 'yes' or 'Yes':
        print('Okay, here is our menu:' + menu)
        print('\nWhich roast would you like?')
    elif see_menu == 'no' or 'No':
        print('Okay. So you already know what you want?')


menu_items()


chosen_roast = input('\n')


def chosen_menu_item():
    print(chosen_roast + ', got it!\n')


chosen_menu_item()


def amount_of_coffees():
    print('How many ' + chosen_roast + ' coffees would you like?')


amount_of_coffees()


amount = input()


def specified_amount():
    if amount == 1:
        print('Okay. ' + amount + ' ' + chosen_roast + ' coffee. Would you like anything else?')
    elif amount != 1:
        print('Okay, ' + amount + ' ' + chosen_roast + " coffee's. Would you like anything else?")


specified_amount()