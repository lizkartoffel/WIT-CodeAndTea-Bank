from Bank import Bank
class transfer:
    def __init__(self, bankobj):
        self.user=bankobj.user
        self.Users=bankobj.Users


    def Transfer(self, amount, receiver_email):

        receiver= None
        for i in self.Users:
            if i["Email"].lower()==receiver_email.lower():
                receiver=i
                break

        if receiver==None:
                return "Message: Receiver Not Found.."
            

        if self.user["Email"].lower()==receiver_email.lower():
            return "Message: Failed.. Cannot transfer to the same email address.."

        if self.user["Balance"]<amount:
            return "Message: Insufficient Funds! Unable To Transfer"
        
        self.user["Balance"]-=amount
        receiver["Balance"]+=amount

        return f"Transfer Done! From User {self.user["Name"]} (New Balance : {self.user["Balance"]}) To {receiver["Name"]} (New Balance : {receiver["Balance"]})" 