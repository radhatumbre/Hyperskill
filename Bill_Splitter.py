import random

try:
    guests = dict()
    amount = int(input("Enter the number of friends joining (including you): \n"))
    if amount <= 0:
        print("No one is joining for the party")
    else:
        print("\nEnter the name of every friend (including you), each on a new line:")
        for i in range(0, amount):
            guests[input()] = 0

        print("\nEnter the total bill value:")
        bill = int(input())

        print("\nDo you want to use the \"Who is lucky?\" feature? Write Yes/No:")
        ans = input()
        if ans == "Yes":
            name = random.choice(list(guests))
            print(f'\n{name} is the lucky one!')
            lucky = guests.pop(name)
            for i in guests:
                guests[i] = round(bill / len(guests), 2)
            guests[name] = 0
            print("")
            print(guests)

        elif ans == "No":
            print("No one is going to be lucky")
            for i in guests:
                guests[i] = round(bill / len(guests), 2)
            print("")
            print(guests)
        else:
            print("Invalid answer")

except:
    print("No one is joining for the party")