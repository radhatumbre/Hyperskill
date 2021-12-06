water = 400
milk = 540
beans = 120
discups = 9
money = 550

class ResourceError(Exception):
    pass

def select_flavor() -> int:
    print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    response = input()
    if response == 'back':
        return 0
    return int(response)

def is_enough(need_water=0, need_milk=0, need_beans=0):
    global water, milk, beans, discups, money
    if water > need_water and milk > need_milk and beans > need_beans and discups >= 1:
        print('I have enough resources, making you a coffee!\n')
    else:
        if water < need_water:
            print('Sorry, not enough water!\n')
            raise ResourceError
        if milk < need_milk:
            print('Sorry, not enough milk!\n')
            raise ResourceError
        if beans < need_beans:
            print('Sorry, not enough beans!\n')
            raise ResourceError
        if discups < 1:
            print('Sorry, not enough cups\n')
            raise ResourceError

# function for buy action
def buy():
    global water, milk, beans, discups, money

    flavor = select_flavor()
    try:
        if flavor == 0:
            pass
        elif flavor == 1:  # espresso
            is_enough(need_water=250, need_beans=16)
            money += 4
            water -= 250
            beans -= 16
            discups -= 1

        elif flavor == 2:  # latte
            is_enough(need_water=350, need_milk=75, need_beans=20)
            money += 7
            water -= 350
            milk -= 75
            beans -= 20
            discups -= 1

        elif flavor == 3:  # cappuccino
            is_enough(need_water=200, need_milk=100, need_beans=12)
            money += 6
            water -= 200
            milk -= 100
            beans -= 12
            discups -= 1

        else:
            raise ValueError(f'Unknown flavor {flavor}')

    except ResourceError:
        pass


# function for fill action
def fill():
    global water, milk, beans, discups, money
    print("\nWrite how many ml of water you want to add:")
    add_water = int(input())
    water += add_water
    print("Write how many ml of milk you want to add:")
    add_milk = int(input())
    milk += add_milk
    print("Write how many grams of coffee beans you want to add:")
    add_beans = int(input())
    beans += add_beans
    print("Write how many disposable coffee cups you want to add:")
    add_cups = int(input())
    discups += add_cups
    print()


# function for take action
def take():
    global water, milk, beans, discups, money
    print(f"I gave you ${money}")
    money = 0

# function for remaining action
def remaining():
    global water, milk, beans, discups, money
    print(f"""
The coffee machine has:
{water} of water
{milk} of milk
{beans} of coffee beans
{discups} of disposable cups
${money} of money
    """)

while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()

    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        remaining()
    elif action == "exit":
        break
    else:
        print(f"Incorrect Action {action}")



