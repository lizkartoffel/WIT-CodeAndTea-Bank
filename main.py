import os
from Bank.Bank import Bank
from management.manage import Management
from management.login import login

def main():

    print("would you like to login?.. Y/N")
    choice=input().upper()
    if choice=="Y":
        email=input("Enter Email : ").capitalize()
        password=input("Enter Password : ")

        bankobj=login(email,password)

        if bankobj==None:
            return
        else:
            print()
            print (f"              -- Welcome {bankobj.user["Name"]}! --")

            while True:
                print()
                print("      What action would you like to perform?  ")
                print("         -------------------------------      ")
                print("(D) Deposit | (W) Withdraw | (T) Transfer | (E) Exit")
                action=input().lower()
                if action =="d":
                    amount_str=(input("Enter deposit amount: "))
                    if not amount_str.isdigit():
                        print ("Enter numbers only please!")
                    else:
                        amount=int(amount_str)
                        print (Management.transaction_type(bankobj, "deposit", amount))

                elif action == "w":
                    amount_str=(input("Enter withdraw amount: "))
                    if not amount_str.isdigit():
                        print ("Enter numbers only please") 
                    else:
                        amount=int(amount_str)                   
                        print (Management.transaction_type(bankobj, "withdraw", amount))

                elif action == "t":
                    amount_str=(input("Enter transfer amount: "))
                    if not amount_str.isdigit():
                        print ("Enter numbers only please!") 
                        continue
                    else:
                        amount=int(amount_str)
                    receiver=input("Input receiver email address: ")                    
                    print (Management.transaction_type(bankobj, "transfer", amount, receiver))

                elif action == "e":
                    print ("Exiting..")                    
                    return 

                else:  
                    print ("Unknown Action!")
    
    else: return 

if __name__ == "__main__":
    main()