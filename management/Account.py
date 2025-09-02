class Account:
    def __init__(self, Account_Number: str, Balance: float, PIN_Password: int , Name:str, History):
        self.Account_Number = Account_Number
        self.Balance = Balance
        self.PIN_Password = PIN_Password
        self.Name = Name
        self.History = History

    def getinfo(self):  #return account details 
        return f"\nAccount Number: {self.Account_Number} | Balance: {self.Balance} | Name: {self.Name}"

"""
later retrieve values quickly by that key, instead of relying on position like in a list.
to not relay on index for ex.. account = Customer_Accounts.get(Account_Number)
w/o index | for account in Customer_Accounts:  if account.Account_Number == account_number:...
.get() method is specific to dictionaries
"""

Customer_Accounts = {           #dict is keyed by account number  key(label) : values (data to store) 
    "224488": Account("224488", 700000, 1234, "Sara Safaa", History=[]),  
    "335577": Account("335577", 500000, 2345, "Rawan Amel", History=[]),
    "884400": Account("884400", 300000, 3456, "Maryam Raad", History=[])
}   

def Login(Account_Number, PIN):
    while True:
        account = Customer_Accounts.get(Account_Number) #access values by the key (direct lookup) | prevents crashes
        if not account:    #If false
            return None, "No such account registered."
        if account.PIN_Password != PIN:
            return None, "Wrong PIN." 
        
        return account, "Login successful!"
    """
    1. returns account obj continue with program 
    2. a message to indicate success with login
    3. account details for user to see before preforming any actions
    """
def History(sender, recipient = None,  amount=0, transaction_type="deposit"):  #default value to transaction type can be any operation

    if transaction_type == "deposit":
        sender.History.append(f"Deposited {amount} IQD. New balance: {sender.Balance} IQD")
    elif transaction_type == "withdraw":
        sender.History.append(f"Withdrew {amount} IQD. Remaining balance: {sender.Balance} IQD")
    elif transaction_type == "transfer" and recipient:
        sender.History.append(f"Transferred {amount} IQD to {recipient.Name}. Remaining balance: {sender.Balance} IQD")
        recipient.History.append(f"Received {amount} IQD from {sender.Name}. New balance: {recipient.Balance} IQD")