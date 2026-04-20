from bank_functions import pin, account_menu


print("wellcome to DuBank")
pin_ok=pin()

if not pin_ok():
    exit()


balances={"RON":500_000, "EUR":25000}
while True:
    currency_menu=input("press:\n 1 for Ron Account\n 2 for Euro Account\n 3 for Exchange\n 4 for Exit:\n")
    if currency_menu == "1":
        account_menu("RON", balances)
    elif currency_menu == "2":
        account_menu("EUR", balances)

    elif currency_menu == "3":
        currency_exchange=input("Press:\n 1 for RON/EURO exchange\n 2 for EURO/RON exchange:\n")
        if currency_exchange=="1":
            exchange1=float(input("The Amount of RON you wish to exchange in EURO:\n"))
            if exchange1 > balances["RON"]:
                print("Insufficient Founds!")
                continue
            else:
                balances["RON"]-=exchange1
                rate=5.09
                eur_conversion=exchange1/rate
                balances["EUR"]+=eur_conversion
                print(f"An amount of {exchange1} RON was converted into {eur_conversion} EUR at an exchange rate of {rate}RON/EUR.")

        elif currency_exchange == "2":
            exchange1=float(input("The Amount of EURO you wish to exchange in RON:\n"))
            if exchange1 > balances["EUR"]:
                print("Insufficient Founds!")
                continue
            else:
                balances["EUR"]-=exchange1
                rate=5.09
                ron_conversion=exchange1*rate
                balances["RON"]+=ron_conversion
                print(f"An amount of {exchange1} EUR was converted into {ron_conversion} RON at an exchange rate of {rate}RON/EUR.")
    elif currency_menu=="4":
        print("Thank you for choosing DuBank! Good Day!")
        break
    else:
        print("Invalid Option!")
        continue




    





