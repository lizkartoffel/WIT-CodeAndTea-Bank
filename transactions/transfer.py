from management.Account import Customer_Accounts

class Transfer:
    def __init__(self, account):
        self.account = account

    def Transfer(self, amount, recipient_acc_num):
        while True:
            #check cancel first
            if recipient_acc_num.lower() == "r":
                return "Action cancelled. Returning to menu..."

            if not recipient_acc_num.isdigit():
                return "Enter numbers only!"

            recipient = Customer_Accounts.get(recipient_acc_num)  #find recipient only after validation
            if not recipient:
                return "Recipient Not Found. Please try again."

            if self.account.Account_Number == recipient.Account_Number:
                return "Cannot transfer to the same account."

            if self.account.Balance < amount:
                return "Insufficient funds!"

            self.account.Balance -= amount
            recipient.Balance += amount
            return f"Transfer Done! From {self.account.Name} (New Balance: {self.account.Balance}) " \
                   f"To {recipient.Name} (New Balance: {recipient.Balance})"
        
