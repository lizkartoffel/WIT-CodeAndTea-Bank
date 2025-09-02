class Withdraw:
    def __init__(self, account):
        self.account = account

    def Withdraw(self, amount):
  
        self.account.Balance -= amount
        return f"Withdraw successful! New Balance: {self.account.Balance} IQD"