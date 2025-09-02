from transactions.deposit import Deposit
from transactions.withdraw import Withdraw
from transactions.transfer import Transfer

class Management:
    @staticmethod

#so that it can be called without creating an obj m=Managment().. m.transaction_type(..) 
#it doesnt care about instance (self) only if the user is inputing the correct action 
# in other words it doesnt need an instance (makes code cleaner in main)


    def transaction_type(user_account, method, amount=None, recipient=None):
        if method.lower() == "deposit":
            return Deposit(user_account).Deposit(amount)
        elif method.lower() == "withdraw":
            return Withdraw(user_account).Withdraw(amount)
        elif method.lower() == "transfer":
            return Transfer(user_account).Transfer(amount, recipient)
        else:
            return "Unknown Method"
        
 