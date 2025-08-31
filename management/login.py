from Bank.Bank import Bank 

def login(email, password):

    email=email.lower()
    for user in Bank.Users:
        if user["Email"].lower()==email.lower():
            if  user ["password"]==password:
                return Bank(user)
            else:  print ("-- Wrong Password! --")
            return None
    print("Login Failed.. No such email registered.")
    return None








