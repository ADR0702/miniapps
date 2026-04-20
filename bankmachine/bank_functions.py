
def pin():
    count=0
    pin="2678"
    while count < 3:
        code=input("Please type 4 digits pin code of your card\n")
        if len(code) !=4 :
            count+=1
            print(f"Wrong Pin! Your pin must be 4 digits long! Attempt no {count}/3 ")
            continue
        elif code != pin:
            count+=1
            print(f"Wrong Pin! Attempt no {count}/3 ")
            continue
        else:
            print("Wellcome!")
            return True
    else:
        print("Card Blocked, please contact the bank to unblock it")
        return False
        

def account_menu(currency, balances):
    while True:
        transaction=input("Press:\n 1 for Check balance\n 2 for Deposit\n 3 for Withdraw\n \n")
        if transaction == "1":
            print(f"Your balance is {balances[currency]}")

        elif transaction == "2":
            deposit=int(input("Pleasee add the value of the deposit:\n"))
            if deposit <=0:
                print("Invalid Amount!")
                continue
            balances[currency]+=deposit
            print("Transacton Complete!")

        elif transaction == "3":
            withdraw=int(input("The amount you wish to withdraw:\n"))
            if withdraw > balances[currency]:
                print("Insufficient Founds!")
                continue
            else:
                balances[currency]-=withdraw
                print("Transacton Complete!")

       
    

    

        


        
