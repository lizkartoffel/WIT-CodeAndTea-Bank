class withdraw:
    def __init__(self, bankobj):
        self.user=bankobj.user

    def Withdraw(self, amount):

            if self.user["Balance"]<amount:
                return "Message: Insufficient Funds! Unable To Withdraw"
        
            if amount<250:
                return "Message: Failed Attempt.. Minimum withdraw amount (250).."
        
            self.user["Balance"]-=amount
            return f"Name: {self.user["Name"]} | New Balanace: {self.user["Balance"]} | Withdrew ({amount}).."