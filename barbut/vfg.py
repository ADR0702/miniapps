
def client ():
    while True:
        try:
            user_money=int(input("Please add money in your balance:\n"))
            if user_money < 100:
                print("Minimum requiered to start the game is 100 EUR")
                continue
            else:
                return user_money
        except ValueError:
            print("Please add only digits")
            continue


def ready():
    while True:
        roll_question=input("type yes to roll the dices, or Cash Out\n").lower()
        if roll_question == "yes":
            print("Let's go!")
            return True
        elif roll_question== "cash out":
            print("You're a coward! Go to mommy!")
            return False
        else:
            print("Only Yes or Cash Out answers!!")
            continue

