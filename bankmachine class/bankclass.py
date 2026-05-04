class ATM:
    def __init__(self):
        self.name = "DuBank"
        self.pincode = "2678"
        self.currency_balances = {
            "RON": 500_000,
            "EUR": 25_000
        }

    def pin(self):
        count = 0

        while count < 3:
            code = input("Enter PIN:\n")

            if len(code) != 4:
                count += 1
                print(f"Wrong PIN! Your PIN must be 4 digits long! Attempt {count}/3")
                continue

            elif code != self.pincode:
                count += 1
                print(f"Wrong PIN! Attempt {count}/3")
                continue

            else:
                print("Welcome!")
                return True

        print("Card blocked, please contact the bank to unblock it.")
        return False

    def account_menu(self, currency):
        while True:
            transaction = input(
                "\nPress:\n"
                "1 for Check balance\n"
                "2 for Deposit\n"
                "3 for Withdraw\n"
                "0 for Exit\n"
            )

            if transaction == "1":
                print(f"Your balance is {self.currency_balances[currency]} {currency}")

            elif transaction == "2":
                deposit = int(input("Please add the value of the deposit:\n"))

                if deposit <= 0:
                    print("Invalid amount!")
                    continue

                self.currency_balances[currency] += deposit
                print("Transaction complete!")

            elif transaction == "3":
                withdraw = int(input("The amount you wish to withdraw:\n"))

                if withdraw <= 0:
                    print("Invalid amount!")
                    continue

                if withdraw > self.currency_balances[currency]:
                    print("Insufficient funds!")
                    continue

                self.currency_balances[currency] -= withdraw
                print("Transaction complete!")

            elif transaction == "0":
                print("Goodbye!")
                break

            else:
                print("Invalid option!")


atm = ATM()

if atm.pin():
    atm.account_menu("RON")