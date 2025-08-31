from transactions.transfer import transfer
from transactions.withdraw import withdraw
from transactions.deposit import deposit

class Management:
    def transaction_type(bankobj, method, amount=None, receiver_email=None):
        if method.lower() == "deposit":
            return deposit(bankobj).Deposit(amount)
        elif method.lower() == "withdraw":
            return withdraw(bankobj).Withdraw(amount)
        elif method.lower() == "transfer":
            return transfer(bankobj).Transfer(amount, receiver_email)
        else:
            return 
        
 