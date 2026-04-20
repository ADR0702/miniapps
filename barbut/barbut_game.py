from dice import roll
from vfg import client, ready

print("""Welcome to BARBUT

Step up to the table.
Roll the dice against the house.
Highest total takes the hand — €100 on the line.
We play 10 hands.
Win more hands than the house...
And you take it all.
Place your bet.
Roll the dice. 
Good luck!""")

computer_amount = 10_000
user_amount = client()

print(f"The computer's balance is {computer_amount}")

tries = 0
user_won = 0
computer_won = 0
cashout = False

while tries < 10:
    print("Are you ready?")
    if not ready():
        cashout = True
        break

    print("Roll the dice!")
    user_d1, user_d2 = roll()
    print(f"Your dice are {user_d1} and {user_d2}")
    user_total = user_d1 + user_d2

    comp_d1, comp_d2 = roll()
    print(f"My dice are {comp_d1} and {comp_d2}")
    comp_total = comp_d1 + comp_d2

    if user_total > comp_total:
        user_amount += 100
        computer_amount -= 100
        tries += 1
        user_won += 1
        print(f"You won!\nYour new balance is: {user_amount}")
        print(f"My balance is: {computer_amount}")
        print(f"Hand no: {tries}")

    elif comp_total > user_total:
        computer_amount += 100
        user_amount -= 100
        tries += 1
        computer_won += 1
        print(f"I won!\nMy new balance is: {computer_amount}")
        print(f"Your new balance is: {user_amount}")
        print(f"Hand no: {tries}")

    else:
        tries += 1
        print("Even!")
        print(f"Hand no: {tries}")

    if user_amount == 0:
        break

if cashout:
    print("You cashed out.")
    print(f"Your final balance is {user_amount}")

elif user_won > computer_won:
    user_amount += computer_amount
    computer_amount = 0
    print("Congrats! You won everything!")
    print(f"Your new balance is {user_amount}")

elif computer_won > user_won:
    computer_amount += user_amount
    user_amount = 0
    print("Game Over!")
    print(f"Your new balance is {user_amount}")

else:
    print("It's a draw!")
    print(f"Your balance remains {user_amount}")