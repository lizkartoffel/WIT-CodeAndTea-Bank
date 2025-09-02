from management.Account import Login,Customer_Accounts
from management.manage import Management
from management.utils import get_valid_amount
from management.Account import History

def main():
    while True:  # Outer loop to allow signing out and re-login
        print("Would you like to login?.. Y/N")
        choice = input().upper()
        if  choice == "N":
            print ("Goodbye!")
            return
        elif choice != "Y":
            print("Unknown Action!")
            continue

        account_number = input("Enter Account Number: ")
        account = Customer_Accounts.get(account_number)

        if not account:
            print("No such account registered.")  # Exit immediately if account doesn't exist
            continue
        else:
            while True:  # retry loop only for PIN

                pin_str = input("Enter PIN  (or R to return): ")
                if pin_str.lower() == "r":
                    print ("Returning to menu...")

                    user_account = None
                    break

                if not pin_str.isdigit():
                    print("PIN must be numbers only!")
                    continue

                pin = int(pin_str)
                user_account, message = Login(account_number, pin) #retruns (account obj, message of success) [tuple unpacking]
                print(message)

                if user_account is not None:  # success
                    break   # exit loop and continue program

            if user_account is None: #if we returned in the pin section exit while loop and go back to main menu
                continue


        print(f"\n-- Welcome {user_account.Name}! --")

        print(account.getinfo())  #From Account class

        while True:  # Inner loop for actions after login
            print("\nWhat action would you like to perform?")
            print("(D) Deposit | (W) Withdraw | (T) Transfer | (E) Exit | (S) Sign Out | (H) Bank History ")
            action = input().lower()

            if action == "d":
                amount = get_valid_amount(">>> Enter deposit amount (multiples of 250 IQD)   ||   Press (R) to Return: ")
                if amount is None:
                    print("Action cancelled. Returning to menu...")
                    continue                 
                print(Management.transaction_type(user_account, "deposit", amount))
                History(user_account, amount=amount, transaction_type="deposit") #Calls history to add after the action

            elif action == "w":
                amount = get_valid_amount(">>> Enter withdraw amount (multiples of 250 IQD)   ||   Press (R) to Return: ")
                if amount is None:
                    print("Action cancelled. Returning to menu...")
                    continue
                print(Management.transaction_type(user_account, "withdraw", amount))
                History(user_account, amount=amount, transaction_type="withdraw") #Calls history to add after the action


            elif action == "t":
                amount = get_valid_amount(">>> Enter transfer amount (multiples of 250 IQD)   ||   Press (R) to Return: ")
                if amount is None:
                    print("Action cancelled. Returning to menu...")
                    continue
                recipient_acc_num = input(">>> Enter recipient account number   ||   Press (R) to Return: ") 
                recipient_account = Customer_Accounts.get(recipient_acc_num)

                if recipient_account is None or recipient_acc_num.lower() == "r":
                    print("Action cancelled or recipient not found. Returning to menu...")
                    continue

                result = Management.transaction_type(user_account, "transfer", amount, recipient_acc_num)
                if result is not None:
                    print(result)
                    History(user_account, recipient_account, amount, transaction_type="transfer") #Calls history to add after the action


            elif action == "h":
                if user_account.History:  # check if there are any transactions
                        print("\n-- Transaction History --")
                        for i in user_account.History:
                            print(i)
                else:
                    print("No transactions yet.")

            elif action == "e":
                print("Exiting program...")
                return

            elif action == "s":
                print("Signing out...\n")
                break  # Break inner loop to return to login

            else:
                print("Unknown Action!")
if __name__ == "__main__":
    main()


    """            elif action == "t":
                amount = get_valid_amount(">>> Enter transfer amount (multiples of 250 IQD)   ||   Press (R) to Return: ")
                if amount is None:
                    print("Action cancelled. Returning to menu...")
                    continue
                recipient = input(">>> Enter recipient account number   ||   Press (R) to Return: ") 
                if amount is None:
                    print("Action cancelled. Returning to menu...")
                    continue
                result = Management.transaction_type(user_account, "transfer", amount, recipient) #store value in a new var
                if result is not None:   #to ONLY print if transfer was successful
                    print(result)
                    History(user_account, recipient_account, amount=amount, transaction_type="transfer") #Calls history to add after the action
"""