class Deposit:
    def __init__(self, account):
        self.account = account

    def Deposit(self, amount):
       
        self.account.Balance += amount
        return f"Deposit successful! New Balance: {self.account.Balance} IQD"
                