def get_valid_amount(prompt): #prompt is our parameter (message) in main 
   
    """
    Prompt the user for an amount.
    Ensures it's an integer >= 250 and divisible by 250.
    Keeps asking until a valid amount is entered.
    The user can enter 'R' to cancel, which returns None.
    """
    while True:
        amount_str = input(prompt)
        
        if amount_str.lower() == "r":
            return None  # user chose to cancel/retry
        
        if not amount_str.isdigit():
            print("Enter numbers only!")
            continue
        
        amount = int(amount_str)
        if amount < 250:   #make sure user is correctly inserting IQD currencey
            print("Amount must be at least 250 IQD.")
            continue
        if amount % 250 != 0:
            print("Enter valid IQD currencey.")
            continue
        
        return amount