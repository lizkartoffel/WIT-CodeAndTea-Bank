from management.Account import Customer_Accounts

class Transfer:
    def __init__(self, account):
        self.account = account

    def Transfer(self, amount, recipient_acc_num):
        while True:
            recipient = Customer_Accounts.get(recipient_acc_num)

            if recipient_acc_num.lower() == "r":
                print("Action cancelled. Returning to menu...")
                return None
            elif not recipient:
                print("Recipient Not Found. Please try again.")
                recipient_acc_num = input("Enter recipient account number (or R to return): ")
                continue

            if self.account.Account_Number == recipient.Account_Number:
                print("Cannot transfer to the same account. Try a different recipient.")
                recipient_acc_num = input("Enter recipient account number: ")
                continue

            if self.account.Balance < amount:
                print("Insufficient funds! Try a smaller amount.")
                amount_str = input("Enter transfer amount: ")
                if not amount_str.isdigit():
                    print("Numbers only please!")
                    continue
                amount = int(amount_str)
                continue

            # Valid transfer
            self.account.Balance -= amount
            recipient.Balance += amount
            return f"Transfer Done! From {self.account.Name} (New Balance: {self.account.Balance}) " \
                   f"To {recipient.Name} (New Balance: {recipient.Balance})"
