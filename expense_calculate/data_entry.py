from datetime import datetime

date_fromat = "%d-%m-%Y"
CATAGORIES = {"I" : "Income" , "E" : "Expense"}

def get_date(prompt ,allow_default= False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_fromat)
    try:
        valid_date = datetime.strptime(date_str , date_fromat)
        return valid_date.strftime(date_fromat)
    except ValueError:
        print("invalid date fromat. please enter the correct date fromat  i.e (dd-mm-yyyy) : ")
        return get_date(prompt, allow_default)
    


def get_amount():
    try:
        amount= float(input("Enter the amount: "))
        if  amount <= 0:
            raise ValueError("please enter the non-negative and amount greater than 0")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()


def get_category():
    category = input("Enter the category ('I' for Income and 'E' for Expense) : ").upper()
    if  category in CATAGORIES:
        return CATAGORIES[category]
    print("Invalid catagory. please enter Either 'I' or 'E'")
    return get_category()

def get_description():
    return input("Enter Discription ('Optional') : ")
