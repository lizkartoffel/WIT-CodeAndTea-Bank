class deposit:
    def __init__(self, bankobj):
        self.user=bankobj.user
        
    def Deposit(self, amount):


        if amount<250:
            return "Message: Failed Attempt.. Minimum deposit amount (250).."
       
        self.user["Balance"]+=amount
        return f"Name: {self.user["Name"]} | New Balanace: {self.user["Balance"]} | Deposited ({amount}).."
