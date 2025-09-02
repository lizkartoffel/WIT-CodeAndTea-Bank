class Withdraw:
    def __init__(self, account):
        self.account = account

    def Withdraw(self, amount):

        if self.account.Balance < amount:
                return None, "Insufficient funds! " #return none to not be added to history

        self.account.Balance -= amount
        return self.account.Balance ,f"Withdraw successful! New Balance: {self.account.Balance} IQD"